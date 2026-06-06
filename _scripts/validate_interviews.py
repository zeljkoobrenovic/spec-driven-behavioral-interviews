#!/usr/bin/env python3
"""Validate behavioral interview manifests and specs."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TEMPLATES = ROOT / "_templates"

REQUIRED_TOP_LEVEL = (
    "title",
    "description",
    "competency",
    "prompt",
    "storyAnatomy",
    "exampleStories",
    "strongAnswerPattern",
    "weakAnswerPattern",
    "followUps",
    "evaluation",
    "visualizations",
    "practiceTemplate",
)

REQUIRED_STORY_FIELDS = {
    "situation",
    "task",
    "action",
    "result",
    "reflection",
    "systemChange",
}

ROLE_LEVELS: set[str] = set()
KNOWN_SIGNAL_TESTS: set[str] = set()
COMPETENCY_FAMILIES: set[str] = set()


class ValidationError(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"{path}: invalid JSON: {exc}") from exc


def load_metadata_names(path: Path, key: str) -> set[str]:
    data = load_json(path)
    require(isinstance(data, dict), f"{path}: expected object")
    values = data.get(key)
    require(isinstance(values, list), f"{path}: {key} must be a list")

    names: set[str] = set()
    for index, item in enumerate(values):
        require(isinstance(item, dict), f"{path}: {key}[{index}] must be object")
        name = item.get("name")
        require(isinstance(name, str) and name, f"{path}: {key}[{index}].name is required")
        require(name not in names, f"{path}: duplicate {key} name {name!r}")
        names.add(name)
    return names


def load_metadata() -> None:
    global ROLE_LEVELS, KNOWN_SIGNAL_TESTS, COMPETENCY_FAMILIES
    ROLE_LEVELS = load_metadata_names(TEMPLATES / "role-levels.json", "levels")
    KNOWN_SIGNAL_TESTS = load_metadata_names(TEMPLATES / "signal-types.json", "tests")
    COMPETENCY_FAMILIES = load_metadata_names(TEMPLATES / "competency-types.json", "families")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def ensure_list(value: Any, path: str) -> list[Any]:
    require(isinstance(value, list), f"{path}: expected list")
    return value


def probe_further_links(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, dict):
        return ensure_list(value.get("links", []), "toProbeFurther.links")
    if isinstance(value, list):
        links: list[Any] = []
        for group in value:
            if isinstance(group, dict):
                links.extend(ensure_list(group.get("links", []), "toProbeFurther[].links"))
        return links
    return []


def reject_local_probe_links(value: Any, field_path: str) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{field_path}.{key}" if field_path else key
            require(
                key != "probeLinks",
                f"{child_path}: probeLinks is no longer supported; keep external resources only in toProbeFurther.links",
            )
            reject_local_probe_links(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_local_probe_links(child, f"{field_path}[{index}]")


def validate_inline_markup(value: Any, field_path: str) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            validate_inline_markup(child, f"{field_path}.{key}" if field_path else str(key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_inline_markup(child, f"{field_path}[{index}]")
    elif isinstance(value, str):
        require(value.count("**") % 2 == 0, f"{field_path}: unbalanced ** bold marker")
        require("****" not in value, f"{field_path}: empty ** bold marker")


def validate_to_probe_further(spec: dict[str, Any], path: Path) -> None:
    payload = spec.get("toProbeFurther")
    if payload is None:
        return
    require(isinstance(payload, (dict, list)), f"{path}: toProbeFurther must be object or list")
    known_ids: set[str] = set()
    known_titles: set[str] = set()
    known_urls: set[str] = set()
    for index, link in enumerate(probe_further_links(payload)):
        require(isinstance(link, dict), f"{path}: toProbeFurther link {index} must be object")
        link_id = link.get("id")
        require(isinstance(link_id, str) and link_id, f"{path}: toProbeFurther link {index}.id is required")
        require(link_id not in known_ids, f"{path}: duplicate toProbeFurther link id {link_id!r}")
        require(
            not link_id.startswith("bookshelf"),
            f"{path}: toProbeFurther link {link_id}: use canonical resource ids, not bookshelf-derived ids",
        )
        known_ids.add(link_id)
        require(isinstance(link.get("title"), str) and link["title"], f"{path}: toProbeFurther link {link_id}.title is required")
        normalized_title = " ".join(link["title"].casefold().split())
        require(
            normalized_title not in known_titles,
            f"{path}: duplicate toProbeFurther title {link['title']!r}",
        )
        known_titles.add(normalized_title)
        url = link.get("url")
        require(
            isinstance(url, str) and url.startswith(("http://", "https://")),
            f"{path}: toProbeFurther link {link_id}.url must be http(s)",
        )
        normalized_url = url.rstrip("/")
        require(normalized_url not in known_urls, f"{path}: duplicate toProbeFurther url {url!r}")
        require(
            "obren.io" not in url.lower(),
            f"{path}: toProbeFurther link {link_id}.url must use a canonical non-Obren resource",
        )
        known_urls.add(normalized_url)
        require(
            isinstance(link.get("why"), str) and link["why"],
            f"{path}: toProbeFurther link {link_id}.why is required",
        )
        for field in ("group", "source", "type"):
            if field in link:
                require(isinstance(link[field], str) and link[field], f"{path}: toProbeFurther link {link_id}.{field} must be non-empty string")
        require(
            "Obren.io Bookshelf" not in link.get("group", ""),
            f"{path}: toProbeFurther link {link_id}.group must use a topic group, not Obren.io Bookshelf Picks",
        )
        require(
            "Obren.io Bookshelf" not in link.get("source", ""),
            f"{path}: toProbeFurther link {link_id}.source must name the canonical source",
        )


def validate_dataset_asset_path(dataset_dir: Path, value: Any, field_path: str) -> None:
    require(isinstance(value, str) and value, f"{field_path}: expected non-empty string path")
    require(
        not value.startswith(("/", "http://", "https://", "data:")),
        f"{field_path}: expected dataset-relative path, got {value!r}",
    )
    target = (dataset_dir / value).resolve()
    require(
        dataset_dir.resolve() in target.parents or target == dataset_dir.resolve(),
        f"{field_path}: path escapes dataset directory: {value!r}",
    )
    require(target.is_file(), f"{field_path}: referenced file does not exist: {value!r}")


def validate_spec(path: Path, expected_id: str) -> None:
    spec = load_json(path)
    require(isinstance(spec, dict), f"{path}: expected object")
    validate_inline_markup(spec, str(path))
    dataset_dir = path.parent

    for field in REQUIRED_TOP_LEVEL:
        require(field in spec, f"{path}: missing required field {field}")

    if "id" in spec:
        require(spec["id"] == expected_id, f"{path}: id must match manifest id {expected_id}")

    assets = spec.get("assets")
    if assets is not None:
        require(isinstance(assets, dict), f"{path}: assets must be object")
        if assets.get("icon"):
            validate_dataset_asset_path(dataset_dir, assets["icon"], f"{path}: assets.icon")
    if spec.get("explainerComic"):
        validate_dataset_asset_path(dataset_dir, spec["explainerComic"], f"{path}: explainerComic")

    reject_local_probe_links(spec, str(path))
    validate_to_probe_further(spec, path)

    roles = ensure_list(spec.get("roleFocus"), f"{path}: roleFocus")
    require(roles, f"{path}: roleFocus must include at least one role")
    for role in roles:
        require(role in ROLE_LEVELS, f"{path}: unknown roleFocus level {role!r}")

    competency = spec["competency"]
    require(isinstance(competency, dict), f"{path}: competency must be object")
    for field in ("id", "name", "family", "definition", "whyItMatters"):
        require(competency.get(field), f"{path}: competency.{field} is required")
    require(
        competency["family"] in COMPETENCY_FAMILIES,
        f"{path}: unknown competency family {competency['family']!r}",
    )
    prompt = spec["prompt"]
    require(isinstance(prompt, dict), f"{path}: prompt must be object")
    require(prompt.get("primary"), f"{path}: prompt.primary is required")

    scenario = spec.get("scenario")
    if scenario is not None:
        require(isinstance(scenario, dict), f"{path}: scenario must be object")

    story = spec["storyAnatomy"]
    require(isinstance(story, dict), f"{path}: storyAnatomy must be object")
    missing_story = REQUIRED_STORY_FIELDS - set(story)
    require(not missing_story, f"{path}: missing storyAnatomy fields: {', '.join(sorted(missing_story))}")

    for pattern_name in ("strongAnswerPattern", "weakAnswerPattern"):
        pattern = spec[pattern_name]
        require(isinstance(pattern, dict), f"{path}: {pattern_name} must be object")
        if pattern.get("aiVisual"):
            validate_dataset_asset_path(
                dataset_dir,
                pattern["aiVisual"],
                f"{path}: {pattern_name}.aiVisual",
            )

    examples = ensure_list(spec["exampleStories"], f"{path}: exampleStories")
    require(examples, f"{path}: exampleStories must include at least one concrete example")
    example_ids: set[str] = set()
    for index, example in enumerate(examples):
        require(isinstance(example, dict), f"{path}: exampleStories[{index}] must be object")
        for field in ("id", "title", "level", "promptVariant", "situation", "weakVersion"):
            require(example.get(field), f"{path}: exampleStories[{index}].{field} is required")
        require(example["id"] not in example_ids, f"{path}: duplicate exampleStories id {example['id']}")
        example_ids.add(example["id"])
        require(example["level"] in ROLE_LEVELS, f"{path}: exampleStories[{index}] unknown level {example['level']!r}")
        for field in ("strongAnswerSketch", "whyItWorks", "followUpAngles"):
            values = ensure_list(example.get(field), f"{path}: exampleStories[{index}].{field}")
            require(values, f"{path}: exampleStories[{index}].{field} must not be empty")
            for item_index, item in enumerate(values):
                require(
                    isinstance(item, str) and item,
                    f"{path}: exampleStories[{index}].{field}[{item_index}] must be non-empty string",
                )
        if example.get("aiVisual"):
            validate_dataset_asset_path(
                dataset_dir,
                example["aiVisual"],
                f"{path}: exampleStories[{index}].aiVisual",
            )

    follow_ups = ensure_list(spec["followUps"], f"{path}: followUps")
    follow_up_ids: set[str] = set()
    for index, probe in enumerate(follow_ups):
        require(isinstance(probe, dict), f"{path}: followUps[{index}] must be object")
        require(probe.get("id"), f"{path}: followUps[{index}].id is required")
        require(probe["id"] not in follow_up_ids, f"{path}: duplicate follow-up id {probe['id']}")
        follow_up_ids.add(probe["id"])
        require(probe.get("question"), f"{path}: followUps[{index}].question is required")
        tests = ensure_list(probe.get("tests"), f"{path}: followUps[{index}].tests")
        for test in tests:
            require(
                isinstance(test, str) and test in KNOWN_SIGNAL_TESTS,
                f"{path}: followUps[{index}].tests has unknown signal test {test!r}",
            )
        example_answers = probe.get("exampleAnswers")
        if example_answers is not None:
            require(isinstance(example_answers, dict), f"{path}: followUps[{index}].exampleAnswers must be object")
            for answer_kind in ("strong", "weak"):
                answers = ensure_list(
                    example_answers.get(answer_kind),
                    f"{path}: followUps[{index}].exampleAnswers.{answer_kind}",
                )
                require(
                    answers,
                    f"{path}: followUps[{index}].exampleAnswers.{answer_kind} must not be empty",
                )
                for answer_index, answer in enumerate(answers):
                    require(
                        isinstance(answer, str) and answer,
                        f"{path}: followUps[{index}].exampleAnswers.{answer_kind}[{answer_index}] must be non-empty string",
                    )

    evaluation = spec["evaluation"]
    require(isinstance(evaluation, dict), f"{path}: evaluation must be object")
    signals = ensure_list(evaluation.get("signals"), f"{path}: evaluation.signals")
    signal_ids: set[str] = set()
    for index, signal in enumerate(signals):
        require(isinstance(signal, dict), f"{path}: evaluation.signals[{index}] must be object")
        for field in ("id", "name", "strong", "weak"):
            require(signal.get(field), f"{path}: evaluation.signals[{index}].{field} is required")
        require(signal["id"] not in signal_ids, f"{path}: duplicate evaluation signal id {signal['id']}")
        signal_ids.add(signal["id"])
        for visual_field in ("strongAiVisual", "weakAiVisual"):
            if signal.get(visual_field):
                validate_dataset_asset_path(
                    dataset_dir,
                    signal[visual_field],
                    f"{path}: evaluation.signals[{index}].{visual_field}",
                )

    rubrics = ensure_list(evaluation.get("rubric"), f"{path}: evaluation.rubric")
    for index, row in enumerate(rubrics):
        require(isinstance(row, dict), f"{path}: evaluation.rubric[{index}] must be object")
        require(row.get("level") in ROLE_LEVELS, f"{path}: unknown role level {row.get('level')!r}")
        require(row.get("expected"), f"{path}: evaluation.rubric[{index}].expected is required")

    visualizations = spec["visualizations"]
    require(isinstance(visualizations, dict), f"{path}: visualizations must be object")
    for field in visualizations.get("timeline", []):
        require(field in REQUIRED_STORY_FIELDS, f"{path}: visualizations.timeline unknown story field {field!r}")
    for signal_id in visualizations.get("signalMap", []):
        require(signal_id in signal_ids, f"{path}: visualizations.signalMap unknown signal id {signal_id}")
    for probe_id in visualizations.get("followUpTree", []):
        require(probe_id in follow_up_ids, f"{path}: visualizations.followUpTree unknown follow-up id {probe_id}")

    practice = spec["practiceTemplate"]
    require(isinstance(practice, dict), f"{path}: practiceTemplate must be object")
    prompts = ensure_list(practice.get("prompts"), f"{path}: practiceTemplate.prompts")
    for index, prompt_item in enumerate(prompts):
        require(isinstance(prompt_item, dict), f"{path}: practiceTemplate.prompts[{index}] must be object")
        field = prompt_item.get("field")
        require(field in REQUIRED_STORY_FIELDS, f"{path}: unknown practice field {field!r}")
        require(prompt_item.get("label"), f"{path}: practiceTemplate.prompts[{index}].label is required")


def validate_group(group_dir: Path) -> int:
    manifest_path = group_dir / "index.json"
    manifest = load_json(manifest_path)
    require(isinstance(manifest, dict), f"{manifest_path}: expected object")
    categories = ensure_list(manifest.get("groups"), f"{manifest_path}: groups")

    count = 0
    ids: set[str] = set()
    for category_index, category in enumerate(categories):
        require(isinstance(category, dict), f"{manifest_path}: groups[{category_index}] must be object")
        require(category.get("id"), f"{manifest_path}: groups[{category_index}].id is required")
        require(category.get("name"), f"{manifest_path}: groups[{category_index}].name is required")
        datasets = ensure_list(category.get("datasets"), f"{manifest_path}: groups[{category_index}].datasets")
        for dataset_index, dataset in enumerate(datasets):
            require(isinstance(dataset, dict), f"{manifest_path}: dataset entry must be object")
            dataset_id = dataset.get("id")
            require(dataset_id, f"{manifest_path}: dataset[{dataset_index}].id is required")
            require(dataset_id not in ids, f"{manifest_path}: duplicate dataset id {dataset_id}")
            ids.add(dataset_id)
            require(dataset.get("name"), f"{manifest_path}: dataset {dataset_id} missing name")
            rel_path = dataset.get("path")
            require(rel_path, f"{manifest_path}: dataset {dataset_id} missing path")
            spec_path = group_dir / rel_path.removeprefix("data/")
            require(spec_path.is_file(), f"{manifest_path}: dataset {dataset_id} path not found: {rel_path}")
            validate_spec(spec_path, dataset_id)
            count += 1

    return count


def main() -> int:
    if not DATA.is_dir():
        print("error: missing data directory", file=sys.stderr)
        return 1

    try:
        load_metadata()
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    total = 0
    errors: list[str] = []
    groups = [path for path in sorted(DATA.iterdir()) if path.is_dir() and (path / "index.json").is_file()]
    for group_dir in groups:
        try:
            count = validate_group(group_dir)
            total += count
            print(f"ok: {group_dir.relative_to(ROOT)} ({count} dataset(s))")
        except ValidationError as exc:
            errors.append(str(exc))

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Validated {total} dataset(s) across {len(groups)} group(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

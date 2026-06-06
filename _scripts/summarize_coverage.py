#!/usr/bin/env python3
"""Summarize behavioral interview dataset coverage."""

from __future__ import annotations

import collections
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def iter_specs():
    for group_dir in sorted(DATA.iterdir()):
        manifest_path = group_dir / "index.json"
        if not group_dir.is_dir() or not manifest_path.is_file():
            continue
        manifest = load_json(manifest_path)
        for category in manifest.get("groups", []):
            for dataset in category.get("datasets", []):
                rel_path = dataset["path"].removeprefix("data/")
                spec_path = group_dir / rel_path
                yield group_dir.name, category, dataset, load_json(spec_path)


def print_counter(title: str, counter: collections.Counter[str]) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    if not counter:
        print("(none)")
        return
    for key, count in counter.most_common():
        print(f"{key}: {count}")


def main() -> int:
    groups = collections.Counter()
    categories = collections.Counter()
    families = collections.Counter()
    roles = collections.Counter()
    difficulties = collections.Counter()
    signals = collections.Counter()
    follow_up_tests = collections.Counter()
    example_counts = collections.Counter()
    datasets = []

    for group_name, category, dataset, spec in iter_specs():
        datasets.append((group_name, dataset["id"], spec.get("title", dataset["name"])))
        groups[group_name] += 1
        categories[f"{group_name}/{category.get('name', category.get('id'))}"] += 1
        competency = spec.get("competency", {})
        families[competency.get("family", "(missing)")] += 1
        difficulties[spec.get("difficulty", "(missing)")] += 1
        for role in spec.get("roleFocus", []):
            roles[role] += 1
        for signal in spec.get("evaluation", {}).get("signals", []):
            signals[signal.get("name", signal.get("id", "(missing)"))] += 1
        for probe in spec.get("followUps", []):
            for test in probe.get("tests", []):
                follow_up_tests[test] += 1
        example_counts[len(spec.get("exampleStories", []))] += 1

    print(f"Datasets: {len(datasets)}")
    for group_name, dataset_id, title in datasets:
        print(f"- {group_name}/{dataset_id}: {title}")

    print_counter("Groups", groups)
    print_counter("Categories", categories)
    print_counter("Competency Families", families)
    print_counter("Role Focus", roles)
    print_counter("Difficulty", difficulties)
    print_counter("Evaluation Signals", signals)
    print_counter("Follow-Up Test Tags", follow_up_tests)
    print_counter("Concrete Examples Per Dataset", example_counts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

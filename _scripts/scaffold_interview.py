#!/usr/bin/env python3
"""Create and register a new behavioral interview spec skeleton."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TEMPLATES = ROOT / "_templates"
STORY_FIELDS = ("situation", "task", "action", "result", "reflection", "systemChange")


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def title_from_id(identifier: str) -> str:
    return " ".join(part.capitalize() for part in identifier.split("-"))


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "interview"


def metadata_names(path: Path, key: str) -> list[str]:
    data = load_json(path)
    return [item["name"] for item in data[key]]


def parse_roles(raw: str) -> list[str]:
    return [role.strip() for role in raw.split(",") if role.strip()]


def build_spec(args: argparse.Namespace) -> dict[str, Any]:
    roles = parse_roles(args.roles)
    return {
        "id": args.id,
        "title": args.title,
        "description": args.description,
        "roleFocus": roles,
        "difficulty": args.difficulty,
        "competency": {
            "id": slugify(args.competency_name),
            "name": args.competency_name,
            "family": args.family,
            "definition": "TODO: Define the leadership competency this interview tests.",
            "whyItMatters": "TODO: Explain why this competency matters for senior technology leadership.",
        },
        "prompt": {
            "primary": f"Tell me about a time you demonstrated {args.competency_name.lower()}.",
            "variants": [
                "TODO: Add an alternate prompt.",
                "TODO: Add another variant that probes the same competency.",
            ],
            "interviewerIntent": [
                "TODO: State what the interviewer is trying to learn.",
                "TODO: State which senior-level signal this prompt reveals.",
            ],
        },
        "scenario": {
            "signatureExample": "TODO: Summarize the senior leadership situation in one concrete sentence.",
            "context": [
                "TODO: Add context that makes the situation realistic.",
                "TODO: Add a second context detail.",
            ],
            "constraints": [
                "TODO: Add a constraint or trade-off.",
                "TODO: Add another constraint.",
            ],
        },
        "storyAnatomy": {
            "situation": "TODO: What was happening, and why did it matter?",
            "task": "TODO: What were you personally accountable for?",
            "action": [
                "TODO: Describe a concrete action, mechanism, or decision.",
                "TODO: Describe another action that shows senior-level ownership.",
            ],
            "result": [
                "TODO: Describe measurable or observable impact.",
                "TODO: Describe customer, business, team, or operating impact.",
            ],
            "reflection": "TODO: What did you learn or revise in your leadership model?",
            "systemChange": [
                "TODO: What mechanism changed after the story?",
                "TODO: What became more repeatable or resilient?",
            ],
        },
        "exampleStories": [
            {
                "id": "primary-example",
                "title": f"Concrete {args.title} Example",
                "level": roles[-1],
                "promptVariant": f"Tell me about a time you demonstrated {args.competency_name.lower()}.",
                "situation": "TODO: Describe a concrete leadership situation with real stakes.",
                "strongAnswerSketch": [
                    "TODO: Name the context and uncertainty clearly.",
                    "TODO: Describe the personal decisions and mechanisms you drove.",
                    "TODO: Show measurable outcome and durable system change.",
                ],
                "whyItWorks": [
                    "TODO: Explain the senior-level judgment signal.",
                    "TODO: Explain why the answer is concrete and measurable.",
                ],
                "weakVersion": "TODO: Describe a realistic but weak version of the answer.",
                "followUpAngles": [
                    "TODO: Add a follow-up that probes ownership.",
                    "TODO: Add a follow-up that probes trade-offs.",
                    "TODO: Add a follow-up that probes measurable impact.",
                ],
            }
        ],
        "strongAnswerPattern": {
            "summary": "TODO: Explain what a strong answer demonstrates.",
            "moves": [
                "TODO: Strong move 1.",
                "TODO: Strong move 2.",
                "TODO: Strong move 3.",
            ],
        },
        "weakAnswerPattern": {
            "summary": "TODO: Explain what a weak answer misses.",
            "redFlags": [
                "TODO: Red flag 1.",
                "TODO: Red flag 2.",
                "TODO: Red flag 3.",
            ],
        },
        "followUps": [
            {
                "id": "ownership",
                "question": "What exactly did you personally own?",
                "tests": [
                    "accountability",
                    "ownership",
                ],
                "exampleAnswers": {
                    "strong": [
                        "TODO: Add a concise strong answer snippet with specific ownership and evidence.",
                    ],
                    "weak": [
                        "TODO: Add a concise weak answer snippet that sounds plausible but lacks evidence.",
                    ],
                },
            },
            {
                "id": "tradeoffs",
                "question": "What alternatives or trade-offs did you consider?",
                "tests": [
                    "decision quality",
                    "trade-off reasoning",
                ],
                "exampleAnswers": {
                    "strong": [
                        "TODO: Add a concise strong answer snippet with rejected alternatives and trade-offs.",
                    ],
                    "weak": [
                        "TODO: Add a concise weak answer snippet that skips alternatives or trade-offs.",
                    ],
                },
            },
            {
                "id": "measurement",
                "question": "How did you know the situation improved?",
                "tests": [
                    "measurement",
                    "learning",
                ],
                "exampleAnswers": {
                    "strong": [
                        "TODO: Add a concise strong answer snippet with outcome and learning evidence.",
                    ],
                    "weak": [
                        "TODO: Add a concise weak answer snippet that relies on vague feelings or activity.",
                    ],
                },
            },
        ],
        "evaluation": {
            "signals": [
                {
                    "id": "ownership",
                    "name": "Ownership",
                    "strong": "TODO: Describe strong evidence for this signal.",
                    "weak": "TODO: Describe weak or missing evidence for this signal.",
                },
                {
                    "id": "tradeoff-reasoning",
                    "name": "Trade-off Reasoning",
                    "strong": "TODO: Describe strong trade-off reasoning.",
                    "weak": "TODO: Describe weak trade-off reasoning.",
                },
                {
                    "id": "system-change",
                    "name": "System Change",
                    "strong": "TODO: Describe durable operating change.",
                    "weak": "TODO: Describe a story that stops at the immediate result.",
                },
            ],
            "rubric": [
                {
                    "level": role,
                    "expected": f"TODO: Expected evidence for {role}.",
                }
                for role in roles
            ],
        },
        "visualizations": {
            "timeline": list(STORY_FIELDS),
            "signalMap": [
                "ownership",
                "tradeoff-reasoning",
                "system-change",
            ],
            "followUpTree": [
                "ownership",
                "tradeoffs",
                "measurement",
            ],
        },
        "practiceTemplate": {
            "prompts": [
                {
                    "field": field,
                    "label": label,
                }
                for field, label in (
                    ("situation", "What was the leadership situation?"),
                    ("task", "What were you personally accountable for?"),
                    ("action", "What decisions, mechanisms, or conversations did you drive?"),
                    ("result", "What changed measurably or observably?"),
                    ("reflection", "What did you learn?"),
                    ("systemChange", "What changed beyond the immediate story?"),
                )
            ],
        },
        "relatedScenarios": [
            "TODO: Add a related scenario.",
            "TODO: Add another related scenario.",
        ],
    }


def load_or_create_manifest(path: Path) -> dict[str, Any]:
    if path.exists():
        data = load_json(path)
        if not isinstance(data, dict) or not isinstance(data.get("groups"), list):
            fail(f"{path}: expected manifest object with groups list")
        return data
    return {"groups": []}


def register_dataset(manifest: dict[str, Any], args: argparse.Namespace) -> bool:
    for category in manifest["groups"]:
        for dataset in category.get("datasets", []):
            if dataset.get("id") == args.id:
                return False

    target_category = None
    for category in manifest["groups"]:
        if category.get("id") == args.category_id:
            target_category = category
            break

    if target_category is None:
        target_category = {
            "id": args.category_id,
            "name": args.category_name,
            "datasets": [],
        }
        manifest["groups"].append(target_category)

    target_category.setdefault("datasets", []).append(
        {
            "id": args.id,
            "name": args.title,
            "path": f"data/{args.id}/interview.json",
        }
    )
    return True


def parse_args(argv: list[str]) -> argparse.Namespace:
    families = metadata_names(TEMPLATES / "competency-types.json", "families")
    role_levels = metadata_names(TEMPLATES / "role-levels.json", "levels")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("group", nargs="?", help="Data group, currently book.")
    parser.add_argument("id", nargs="?", help="Dataset id and directory name, for example crisis-leadership.")
    parser.add_argument("--title", help="Display title. Defaults to title-cased id.")
    parser.add_argument("--description", help="Short overview description.")
    parser.add_argument("--category-id", default="drafts", help="Manifest category id to register under.")
    parser.add_argument("--category-name", default="Drafts", help="Manifest category display name.")
    parser.add_argument("--family", default="Judgment and Strategy", choices=families)
    parser.add_argument("--competency-name", help="Competency display name. Defaults to title.")
    parser.add_argument("--roles", default="Director,VP Engineering,CTO", help="Comma-separated role levels.")
    parser.add_argument("--difficulty", default="advanced", choices=("foundational", "intermediate", "advanced"))
    parser.add_argument("--force", action="store_true", help="Overwrite an existing interview.json.")
    parser.add_argument("--list-families", action="store_true", help="List canonical competency families and exit.")
    parser.add_argument("--list-roles", action="store_true", help="List canonical role levels and exit.")

    args = parser.parse_args(argv)
    if args.list_families:
        print("\n".join(families))
        raise SystemExit(0)
    if args.list_roles:
        print("\n".join(role_levels))
        raise SystemExit(0)
    if not args.group or not args.id:
        parser.error("group and id are required unless using --list-families or --list-roles")

    args.id = slugify(args.id)
    args.title = args.title or title_from_id(args.id)
    args.description = args.description or f"TODO: Describe the {args.title} behavioral interview case."
    args.competency_name = args.competency_name or args.title

    roles = parse_roles(args.roles)
    unknown_roles = [role for role in roles if role not in role_levels]
    if unknown_roles:
        fail(f"unknown role level(s): {', '.join(unknown_roles)}")
    if not roles:
        fail("at least one role is required")

    return args


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    group_dir = DATA / args.group
    dataset_dir = group_dir / args.id
    spec_path = dataset_dir / "interview.json"
    manifest_path = group_dir / "index.json"

    if spec_path.exists() and not args.force:
        fail(f"{spec_path} already exists; use --force to overwrite")

    group_dir.mkdir(parents=True, exist_ok=True)
    dataset_dir.mkdir(parents=True, exist_ok=True)

    spec = build_spec(args)
    write_json(spec_path, spec)

    manifest = load_or_create_manifest(manifest_path)
    registered = register_dataset(manifest, args)
    write_json(manifest_path, manifest)

    print(f"wrote {spec_path.relative_to(ROOT)}")
    if registered:
        print(f"registered {args.id} in {manifest_path.relative_to(ROOT)}")
    else:
        print(f"{args.id} was already registered in {manifest_path.relative_to(ROOT)}")
    print("next: python3 _scripts/validate_interviews.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

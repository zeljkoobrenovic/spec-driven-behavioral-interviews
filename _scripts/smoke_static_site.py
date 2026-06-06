#!/usr/bin/env python3
"""Smoke-test generated static site output under docs/."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"

REQUIRED_GROUP_FILES = (
    "index.html",
    "explorer.html",
    "overview.js",
    "explorer.js",
    "styles.css",
    "competency-types.json",
    "role-levels.json",
    "signal-types.json",
    "rubric-scale.json",
)


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def discover_groups() -> list[str]:
    return [
        path.name
        for path in sorted(DATA.iterdir())
        if path.is_dir() and (path / "index.json").is_file()
    ]


def check_file(errors: list[str], path: Path) -> None:
    if not path.is_file():
        fail(errors, f"missing file: {path.relative_to(ROOT)}")


def http_head(errors: list[str], base_url: str, route: str) -> None:
    url = f"{base_url.rstrip('/')}/{route.lstrip('/')}"
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            if response.status >= 400:
                fail(errors, f"HTTP {response.status}: {url}")
    except (urllib.error.URLError, TimeoutError) as exc:
        fail(errors, f"failed HTTP check {url}: {exc}")


def check_group(group: str, errors: list[str], base_url: str | None) -> int:
    source_manifest = DATA / group / "index.json"
    built_group = DOCS / group
    built_manifest = built_group / "data" / "index.json"

    for name in REQUIRED_GROUP_FILES:
        check_file(errors, built_group / name)
    check_file(errors, built_manifest)

    if base_url:
        http_head(errors, base_url, f"{group}/")
        http_head(errors, base_url, f"{group}/explorer.html")
        http_head(errors, base_url, f"{group}/data/index.json")

    if not source_manifest.is_file() or not built_manifest.is_file():
        return 0

    source = load_json(source_manifest)
    built = load_json(built_manifest)
    source_count = sum(len(category.get("datasets", [])) for category in source.get("groups", []))
    built_count = sum(len(category.get("datasets", [])) for category in built.get("groups", []))
    if source_count != built_count:
        fail(errors, f"{group}: source dataset count {source_count} != built count {built_count}")

    seen: set[str] = set()
    for category in built.get("groups", []):
        for dataset in category.get("datasets", []):
            dataset_id = dataset.get("id")
            if dataset_id in seen:
                fail(errors, f"{group}: duplicate built dataset id {dataset_id}")
            seen.add(dataset_id)

            rel_path = dataset.get("path", "")
            if not rel_path:
                fail(errors, f"{group}: dataset {dataset_id} has empty path")
                continue
            spec_path = built_group / rel_path
            check_file(errors, spec_path)
            if base_url:
                http_head(errors, base_url, f"{group}/{rel_path}")

    return built_count


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", help="Optional local server URL, for example http://localhost:8000.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    errors: list[str] = []

    check_file(errors, DOCS / "index.html")
    if args.base_url:
        http_head(errors, args.base_url, "/")

    total = 0
    groups = discover_groups()
    for group in groups:
        total += check_group(group, errors, args.base_url)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Smoke-tested {total} generated dataset route(s) across {len(groups)} group(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

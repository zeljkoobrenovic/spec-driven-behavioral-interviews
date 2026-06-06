#!/usr/bin/env python3
"""Generate only missing behavioral interview overview icons."""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path
from typing import Any

import generate_interview_assets as assets


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA = REPO_ROOT / "data"


def find_interview_files(groups: list[str]) -> list[Path]:
    if groups:
        files: list[Path] = []
        for group in groups:
            group_dir = DATA / group
            if not group_dir.is_dir():
                raise SystemExit(f"error: no data group at {assets.rel(group_dir)}")
            files.extend(sorted(group_dir.glob("*/interview.json")))
        return sorted(files)
    return sorted(DATA.glob("*/*/interview.json"))


def has_icon(interview_file: Path) -> bool:
    data = assets.load_dataset(interview_file)
    icon = data.get("assets", {}).get("icon") if isinstance(data.get("assets"), dict) else None
    if icon and (interview_file.parent / icon).is_file():
        return True
    return assets.existing_for_stem(interview_file.parent / "icon.png") is not None


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("groups", nargs="*", help="Optional data groups to scan. Defaults to all groups.")
    parser.add_argument("--dry-run", action="store_true", help="Print targets and prompt summaries without API calls or writes.")
    parser.add_argument("--force", action="store_true", help="Regenerate icons even if they already exist.")
    parser.add_argument("--no-write-json", action="store_true", help="Do not write assets.icon into interview.json.")
    parser.add_argument("--model", default=assets.DEFAULT_MODEL, help=f"Gemini image model (default: {assets.DEFAULT_MODEL}).")
    parser.add_argument("--icon-size", default=assets.DEFAULT_ICON_SIZE, help=f"Gemini image size for icons (default: {assets.DEFAULT_ICON_SIZE}).")
    parser.add_argument("--sleep", type=float, default=2.0, help="Seconds between generated images (default: 2).")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    files = find_interview_files(args.groups)
    targets = files if args.force else [path for path in files if not has_icon(path)]
    print(f"Scanned interviews: {len(files)}")
    print(f"Icon targets: {len(targets)}")
    if not targets:
        return 0

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key and not args.dry_run:
        print("error: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        return 2

    errors = 0
    for index, interview_file in enumerate(targets, start=1):
        data = assets.load_dataset(interview_file)
        spec = assets.collect_specs(
            interview_file=interview_file,
            data=data,
            only={"icon"},
            model=args.model,
            icon_size=args.icon_size,
            image_size=assets.DEFAULT_IMAGE_SIZE,
        )[0]
        print(f"[{index}/{len(targets)}] {assets.rel(interview_file)}")
        try:
            status, path = assets.process_spec(spec, api_key=api_key, force=args.force, dry_run=args.dry_run)
            print(f"    {status}")
            if path and not args.no_write_json and not args.dry_run:
                changes = assets.apply_json_updates(interview_file, data, {("assets", "icon"): path})
                for change in changes:
                    print(f"    {change}")
            if path and args.sleep and index < len(targets):
                time.sleep(args.sleep)
        except Exception as exc:  # noqa: BLE001
            errors += 1
            print(f"    ERROR: {exc}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

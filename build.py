#!/usr/bin/env python3
"""Build static site groups from templates and data into docs/."""

from __future__ import annotations

import html
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "_templates"
DATA = ROOT / "data"
DOCS = ROOT / "docs"

REQUIRED_TEMPLATE_FILES = (
    "index.html",
    "explorer.html",
    "styles.css",
    "overview.js",
    "explorer.js",
)

NON_DATA_SUFFIXES = (".md", ".markdown", ".py", ".mjs")
NON_TEMPLATE_SUFFIXES = (".md", ".markdown")


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def ignore_suffixes(suffixes: tuple[str, ...]):
    def _ignore(_dirpath: str, names: list[str]) -> list[str]:
        return [name for name in names if name.lower().endswith(suffixes)]

    return _ignore


def discover_groups() -> list[str]:
    if not DATA.is_dir():
        fail(f"missing data directory: {DATA}")

    groups: list[str] = []
    for child in sorted(DATA.iterdir()):
        if child.is_dir() and (child / "index.json").is_file():
            groups.append(child.name)
    return groups


def build_group(group: str) -> None:
    source_data = DATA / group
    output = DOCS / group
    output_data = output / "data"

    if output.exists():
        shutil.rmtree(output)

    shutil.copytree(TEMPLATES, output, ignore=ignore_suffixes(NON_TEMPLATE_SUFFIXES))
    output_data.mkdir(parents=True)
    shutil.copy2(source_data / "index.json", output_data / "index.json")

    for entry in sorted(source_data.iterdir()):
        if entry.is_dir():
            shutil.copytree(entry, output_data / entry.name, ignore=ignore_suffixes(NON_DATA_SUFFIXES))

    dataset_count = sum(1 for entry in output_data.iterdir() if entry.is_dir())
    print(f"  built docs/{group}/ ({dataset_count} dataset(s))")


def write_root_index(groups: list[str]) -> None:
    DOCS.mkdir(exist_ok=True)
    if len(groups) == 1:
        target = html.escape(groups[0])
        content = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="0; url={target}/">
    <title>Behavioral Interview Explorer</title>
    <link rel="canonical" href="{target}/">
  </head>
  <body>
    <p><a href="{target}/">Open Behavioral Interview Explorer</a></p>
  </body>
</html>
"""
        (DOCS / "index.html").write_text(content, encoding="utf-8")
        return

    links = "\n".join(
        f'        <li><a href="{html.escape(group)}/">{html.escape(group.title())}</a></li>'
        for group in groups
    )
    content = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Behavioral Interview Explorer</title>
    <style>
      body {{
        margin: 0;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: #f6f3ee;
        color: #202124;
      }}
      main {{
        max-width: 760px;
        margin: 0 auto;
        padding: 56px 24px;
      }}
      a {{
        color: #0f6b68;
        font-weight: 700;
      }}
    </style>
  </head>
  <body>
    <main>
      <h1>Behavioral Interview Explorer</h1>
      <p>Generated static sites:</p>
      <ul>
{links}
      </ul>
    </main>
  </body>
</html>
"""
    (DOCS / "index.html").write_text(content, encoding="utf-8")


def main(argv: list[str]) -> int:
    if not TEMPLATES.is_dir():
        fail(f"missing templates directory: {TEMPLATES}")
    for name in REQUIRED_TEMPLATE_FILES:
        if not (TEMPLATES / name).is_file():
            fail(f"missing required template file: {TEMPLATES / name}")

    available = discover_groups()
    if not available:
        fail("no publishable groups found under data/ (need index.json)")

    requested = argv[1:]
    unknown = [group for group in requested if group not in available]
    if unknown:
        fail(f"unknown group(s): {', '.join(unknown)}; available: {', '.join(available)}")

    groups = requested or available
    print(f"Building {len(groups)} group(s): {', '.join(groups)}")
    for group in groups:
        build_group(group)
    write_root_index(available)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

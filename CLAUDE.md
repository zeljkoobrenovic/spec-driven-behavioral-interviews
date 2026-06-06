# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A static, framework-free explorer for senior technology leadership behavioral interviews. Interview content is authored as structured JSON specs; shared HTML/CSS/JS templates render those specs into interactive walkthroughs at build time. There is no backend, no bundler, and no package manager — just Python build/validation scripts and vanilla browser JS.

`AGENTS.md` is the canonical, detailed contributor guide (data model, manifest, content quality, link/visual conventions). Read it before authoring or editing interview content. This file is the orientation layer.

## Architecture

The pipeline is **specs → build → static site**, with four clearly separated layers. Do not blur them:

- `_templates/` — the shared app shell (DOM + browser logic + canonical metadata JSON). `index.html`/`overview.js` render the catalog; `explorer.html`/`explorer.js` render a single interview (JSON loading, section rendering, hash routing, worksheet persistence). The `*-types.json`, `role-levels.json`, `rubric-scale.json` files are canonical vocabularies shared by the app, validation, and coverage.
- `data/<group>/` — authored content. A group is **publishable** only when `data/<group>/index.json` (the manifest) exists. Each interview lives at `data/<group>/<id>/interview.json`. Currently the only group is `book/`.
- `build.py` — copies `_templates/` into `docs/<group>/`, then copies that group's data beside it as `docs/<group>/data/`. The app fetches that JSON at runtime, which is why a static server is required (`file://` does not work).
- `docs/` — **generated output**, committed for GitHub Pages. Never hand-edit it; always regenerate with `python3 build.py`.

Key consequence: editing app behavior means editing `_templates/` (not `docs/`), and editing content means editing `data/` then rebuilding. The build wipes and recreates each `docs/<group>/` on every run.

## Required Checks After Editing Source

Run the full sequence after changing `_templates/` or `data/`:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
node --check _templates/overview.js
node --check _templates/explorer.js
python3 build.py
python3 _scripts/smoke_static_site.py
```

Prose-only changes to `README.md`, `PLAN.md`, or `AGENTS.md` do not need a build.

`validate_interviews.py` enforces the spec schema (required top-level fields, the Situation→Task→Action→Result→Reflection→System Change story shape, known signal tests / role levels / competency families from the canonical `_templates/*.json` vocabularies, and that referenced visual asset files actually exist). Treat it as the schema authority alongside `PLAN.md`.

## Run Locally

```bash
python3 -m http.server 8000 -d docs
# open http://localhost:8000/book/
```

## Adding / Editing an Interview

Scaffold and register a new dataset (this updates the manifest):

```bash
python3 _scripts/scaffold_interview.py --list-families
python3 _scripts/scaffold_interview.py --list-roles
python3 _scripts/scaffold_interview.py book new-case \
  --title "New Case" --category-id judgment-strategy \
  --category-name "Judgment and Strategy"
```

Then edit `data/book/<id>/interview.json` and run the required checks above. A dataset `id` must match the `id` inside its `interview.json`. See `AGENTS.md` for the full data-model and content-quality conventions.

## Visual Assets (optional)

Generators live in `_scripts/generate_*.py`. **Always pass `--dry-run` first.** Real generation requires `GEMINI_API_KEY`, writes image files under the dataset directory, writes the corresponding JSON path, and requires a rebuild of `docs/` afterward.

## Project Skills

Authoring workflows are encoded as Codex skills under `.codex/skills/` (e.g. `behavioral-interview-author`, `behavioral-interview-improver`, `behavioral-interview-reviewer`, `interview-examples-variants`, `interview-visual-assets`, `research-external-links`). Consult the relevant `SKILL.md` when doing that kind of work.

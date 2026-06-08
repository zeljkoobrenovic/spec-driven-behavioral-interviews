# Spec-Driven Behavioral Interview Explorer

A static, framework-free explorer for senior technology leadership behavioral
interviews. Interview content is authored as structured JSON specs; shared
templates turn those specs into interactive walkthroughs, visual timelines,
concrete story examples, follow-up probes, rubrics, practice worksheets, and
curated external resources for deeper learning.

See generated site: [zeljkoobrenovic.github.io/spec-driven-behavioral-interviews/](https://zeljkoobrenovic.github.io/spec-driven-behavioral-interviews/)

## Repository Layout

| Path | Purpose |
|------|---------|
| `PLAN.md` | Product and implementation plan. |
| `_templates/` | Shared HTML, CSS, and JS used by every generated site. |
| `data/` | Authored behavioral interview specs. |
| `_scripts/` | Validation and maintenance scripts. |
| `build.py` | Copies templates and data into `docs/`. |
| `docs/` | Generated static site output. Commit this for GitHub Pages. |

Current site:

- `book/`: canonical book content, with the reusable method and the initial
  chapter catalog from `IDEA.md`.

## Build And Run

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
python3 -m http.server 8000 -d docs
```

Then open:

```text
http://localhost:8000/book/
```

The app fetches JSON at runtime, so use a static server rather than opening the
HTML files directly with `file://`.

## Adding An Interview

Scaffold and register a new dataset:

```bash
python3 _scripts/scaffold_interview.py --list-families
python3 _scripts/scaffold_interview.py --list-roles
python3 _scripts/scaffold_interview.py book new-case \
  --title "New Case" \
  --category-id judgment-strategy \
  --category-name "Judgment and Strategy"
```

Then:

1. Edit `data/book/<id>/interview.json`.
2. Run `python3 _scripts/validate_interviews.py`.
3. Run `python3 _scripts/summarize_coverage.py` when you want a coverage check.
4. Run `python3 build.py`.
5. Run `python3 _scripts/smoke_static_site.py`.
6. Inspect the generated site under `docs/book/`.

The current schema is documented in `PLAN.md` and enforced by
`_scripts/validate_interviews.py`.

## External Resources

Each interview can include a canonical `toProbeFurther.links[]` list of books,
articles, interviews, podcasts, official guides, and standards. These links are
rendered only in the final **To Probe Further** section.

Use the project-local `$research-external-links` Codex skill when adding or
refreshing these links. For leadership-related topics, the skill should also
check `https://obren.io/bookshelf/docs/leadership.html` and include a short
context-specific `why` note for every resource.

## Visual Assets

Visuals are optional and live beside each dataset. Generate them with dry-run
first:

```bash
python3 _scripts/generate_interview_assets.py data/book/crisis-leadership/interview.json --dry-run
python3 _scripts/generate_example_story_pictures.py data/book/crisis-leadership/interview.json --dry-run
python3 _scripts/generate_answer_pattern_pictures.py data/book/crisis-leadership/interview.json --dry-run
python3 _scripts/generate_signal_pictures.py data/book/crisis-leadership/interview.json --dry-run
python3 _scripts/generate_interview_comic.py data/book/crisis-leadership/interview.json --dry-run
python3 _scripts/generate_missing_interview_icons.py book --dry-run
```

Real generation requires `GEMINI_API_KEY`. After generating images, run
validation and rebuild `docs/`.

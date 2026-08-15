# Agent Guide

This repository is an explorer for senior technology
leadership behavioral interviews. Keep the source data, templates, scripts, and
generated output clearly separated.

## Source Of Truth

- Edit interview content under `data/book/<id>/interview.json`.
- Edit the book manifest under `data/book/index.json`.
- Edit shared app behavior and styling under `_templates/`.
- Edit build and validation behavior under `build.py` and `_scripts/`.
- Treat `docs/` as generated output. Rebuild it with `python3 build.py` after
  changing `_templates/` or `data/`; do not hand-edit generated copies.

Current publishable site:

- `book/`: the canonical book-oriented catalog from `IDEA.md`.

## Required Checks

Run these after changing source files:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
node --check _templates/overview.js
node --check _templates/explorer.js
python3 -m py_compile build.py _scripts/validate_interviews.py _scripts/summarize_coverage.py _scripts/scaffold_interview.py _scripts/smoke_static_site.py _scripts/generate_interview_assets.py _scripts/generate_example_story_pictures.py _scripts/generate_answer_pattern_pictures.py _scripts/generate_signal_pictures.py _scripts/generate_interview_comic.py _scripts/generate_missing_interview_icons.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

If you change only prose in `README.md`, `PLAN.md`, or `AGENTS.md`, the full
build is not required.

## Running Locally

Serve the generated `docs/` directory:

```bash
python3 -m http.server 8000 -d docs
```

Then inspect:

```text
http://localhost:8000/book/
```

The app fetches JSON at runtime, so `file://` will not work reliably.

## Project Skills

Project-local Codex skills live under `.codex/skills/`:

- `behavioral-interview-author`: create a new interview dataset.
- `behavioral-interview-improver`: strengthen an existing interview spec.
- `interview-examples-variants`: add concrete examples and prompt variants.
- `interview-visual-assets`: plan or generate interview visuals.
- `behavioral-interview-reviewer`: review realism, balance, educative value, and write `REVIEW.md`.
- `research-external-links`: find credible external resources for the final `toProbeFurther.links[]` list.

## Data Model Conventions

Every dataset should model a senior behavioral interview structurally:

- `competency`
- `prompt`
- `scenario`
- `storyAnatomy`
- `exampleStories`
- `strongAnswerPattern`
- `weakAnswerPattern`
- `followUps`
- `evaluation`
- `visualizations`
- `practiceTemplate`

The expected senior answer shape is:

```text
Situation -> Task -> Action -> Result -> Reflection -> System Change
```

Make senior-level judgment visible. Strong examples should include trade-offs,
personal ownership, stakeholder alignment, measurable outcomes, reflection, and
a durable mechanism that changed after the story.

Use `exampleStories` for concrete story variants. Each example should include a
specific situation, a strong answer sketch, why it works, a weak version, and
follow-up angles. These examples should be adaptable story shapes, not scripts
to memorize.

Use `followUps[].exampleAnswers` when a probe benefits from calibration
examples. Keep snippets short. Strong examples should include specific evidence,
ownership, trade-offs, measurement, or learning. Weak examples should be
realistic but expose missing specificity, ownership, or evidence.

Use `**key phrase**` sparingly in natural-language text fields to make pages
skimmable. Prefer one short phrase per sentence or list item. Do not add HTML,
and do not add bold markers to IDs, URLs, asset paths, tags, or other machine
fields.

Visual fields are optional and dataset-relative:

- `assets.icon`
- `explainerComic`
- `strongAnswerPattern.aiVisual`
- `weakAnswerPattern.aiVisual`
- `evaluation.signals[].strongAiVisual`
- `evaluation.signals[].weakAiVisual`
- `exampleStories[].aiVisual`

Use `--dry-run` before any image generation. Real image generation requires
`GEMINI_API_KEY`, writes image files under the dataset directory, and then
writes the corresponding JSON path. Always rebuild `docs/` afterward.

External resources are optional but recommended:

- `toProbeFurther.links[]`: canonical per-interview reading/listening list rendered only in the final To Probe Further section.

Use researched, high-quality sources such as official book pages, engineering
blogs, SRE guides, responsible-tech standards, interviews, and podcasts. Avoid
generic SEO summaries.

For leadership, management, communication, strategy, and technology-leadership
topics, also check the curated bookshelf at
`https://obren.io/bookshelf/docs/leadership.html` as a discovery source. Do not
add `obren.io` bookshelf notes or PDFs to `toProbeFurther.links[]`; link to the
canonical author, publisher, book, article, podcast, or framework page instead.
Avoid duplicate entries for the same resource, such as both a book page and a
bookshelf note for that book.

## Manifest Conventions

A group is publishable when `data/<group>/index.json` exists. The manifest uses
`groups` for overview categories:

```json
{
  "groups": [
    {
      "id": "judgment-strategy",
      "name": "Judgment and Strategy",
      "datasets": [
        {
          "id": "leading-through-ambiguity",
          "name": "Leading Through Ambiguity",
          "path": "data/leading-through-ambiguity/interview.json"
        }
      ]
    }
  ]
}
```

Dataset ids must match their `interview.json` `id` fields when present.

Use the scaffold script for new datasets:

```bash
python3 _scripts/scaffold_interview.py --list-families
python3 _scripts/scaffold_interview.py --list-roles
python3 _scripts/scaffold_interview.py book new-case \
  --title "New Case" \
  --category-id judgment-strategy \
  --category-name "Judgment and Strategy"
```

## Template Conventions

- Keep the app framework-free unless the project explicitly changes direction.
- Keep browser code in `_templates/overview.js` and `_templates/explorer.js`.
- Keep shared visual styling in `_templates/styles.css`.
- Generated sites load data relative to each built group, for example
  `docs/book/data/index.json`.
- Keep `overview.js` and `explorer.js` syntax-checkable with `node --check`.

## Content Quality

Avoid generic behavioral-interview filler. Each case should answer:

- What senior leadership situation is being tested?
- What does a strong answer do that a weak answer does not?
- What follow-ups reveal real ownership or weak claims?
- What signals should an interviewer evaluate?
- How does the expected answer change by level?

Prefer concrete operating mechanisms over vague claims such as "aligned
stakeholders", "raised the bar", or "improved communication" unless the spec
explains exactly how.

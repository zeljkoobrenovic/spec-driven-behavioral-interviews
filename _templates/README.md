# `_templates/`

Shared static shell for every generated behavioral interview site.

`build.py` copies this directory into each `docs/<group>/`, then copies the
group's data beside it. Edit these files, not generated copies under `docs/`.

| File | Purpose |
|------|---------|
| `index.html` | Overview page DOM shell. |
| `overview.js` | Manifest loading, filters, and catalog rendering. |
| `explorer.html` | Per-interview explorer DOM shell. |
| `explorer.js` | JSON loading, section rendering, hash routing, worksheet persistence. |
| `styles.css` | Shared visual system and responsive layout. |
| `competency-types.json` | Canonical competency family metadata. |
| `rubric-scale.json` | Shared answer-quality scale. |
| `role-levels.json` | Canonical seniority levels used by rubrics. |
| `signal-types.json` | Canonical follow-up probe tags used by validation and coverage. |

The explorer renders optional dataset-relative visuals:

- `assets.icon` on overview cards.
- `explainerComic` in the Visual Summary section.
- `strongAnswerPattern.aiVisual` and `weakAnswerPattern.aiVisual` inside Answer Contrast.
- `evaluation.signals[].strongAiVisual` and `evaluation.signals[].weakAiVisual` inside Answer Contrast and Evaluation Rubric.
- `exampleStories[].aiVisual` inside Concrete Examples.

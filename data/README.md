# `data/`

Behavioral interview specs live here. The publishable book catalog is under
`data/book/`.

```text
data/
  book/
    index.json
    interview-method/
      interview.json
```

The manifest uses a `groups` array for category sections:

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

Run validation after edits:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
```

Each `interview.json` includes `exampleStories` for concrete variants. Keep
them specific: a realistic situation, strong answer sketch, why it works, weak
version, and likely follow-up angles.

External resources use one canonical list plus local references:

- `toProbeFurther.links[]` stores researched books, articles, interviews,
  podcasts, standards, or official guides.

External links are rendered only in the final To Probe Further section. Do not
add `probeLinks` to local structures such as `competency`, `prompt`,
`exampleStories[]`, `followUps[]`, or `evaluation.signals[]`.

Use high-quality sources with direct URLs and short `why` notes. Prefer official
book pages, author pages, company engineering blogs, SRE guides, standards
bodies, and named operator interviews over generic summaries.

For leadership-related topics, also use the curated bookshelf at
`https://obren.io/bookshelf/docs/leadership.html` as inspiration for resource
selection. Do not link directly to `obren.io` bookshelf notes or PDFs from
`toProbeFurther.links[]`; use canonical author, publisher, book, article,
podcast, or framework pages instead. Avoid duplicate entries for the same
resource.

Optional visual fields are dataset-relative paths:

- `assets.icon`
- `explainerComic`
- `strongAnswerPattern.aiVisual`
- `weakAnswerPattern.aiVisual`
- `evaluation.signals[].strongAiVisual`
- `evaluation.signals[].weakAiVisual`
- `exampleStories[].aiVisual`

If present, validation requires the referenced file to exist.

Inline emphasis uses lightweight bold markers:

- Use `**key phrase**` inside natural-language strings to help skimmers.
- Highlight one short phrase per sentence or list item.
- Do not use HTML in JSON text fields.
- Do not add bold markers to IDs, URLs, paths, tags, or asset fields.

Follow-up probes may include optional example answer snippets:

- `followUps[].exampleAnswers.strong[]`
- `followUps[].exampleAnswers.weak[]`

Use these as calibration examples, not scripts. Strong snippets should show
specific evidence, trade-offs, ownership, and measurement. Weak snippets should
sound plausible but reveal missing specificity, ownership, or learning.

To create and register a new skeleton:

```bash
python3 _scripts/scaffold_interview.py --list-families
python3 _scripts/scaffold_interview.py --list-roles
python3 _scripts/scaffold_interview.py book new-case \
  --title "New Case" \
  --category-id judgment-strategy \
  --category-name "Judgment and Strategy"
```

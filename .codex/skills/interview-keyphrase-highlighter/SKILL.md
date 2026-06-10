---
name: interview-keyphrase-highlighter
description: "Add or improve Markdown bold emphasis for key phrases in behavioral interview JSON text. Use when highlighting competency briefs, prompts, prompt variants, interviewer intent, evidence, decision criteria, trade-offs, operating mechanisms, red flags, follow-up probes, or rubric signals with **key phrase** markers while preserving valid project data."
---

# Interview Keyphrase Highlighter

## Purpose

Add `**key phrase**` emphasis to natural-language text in `data/<group>/<id>/interview.json` so generated interview pages are easier to scan. This is an editorial pass: highlight the phrases that carry meaning, not every important-sounding word.

## Workflow

1. Read `AGENTS.md`, the target `interview.json`, and one nearby interview if useful for local emphasis density.
2. Start with the default first-pass fields: competency brief, prompt, prompt variants, and interviewer intent.
3. Identify the interview's main leadership behaviors, evaluation signals, operating mechanisms, follow-up probes, and weak-answer red flags.
4. Add or adjust `**...**` only in human-readable text fields.
5. Preserve existing wording unless a tiny edit is needed to make the emphasized phrase grammatical.
6. Keep JSON valid and rebuild generated output after changing source interview data.

## Default First Pass

When the user asks to highlight an interview without naming a narrower scope, cover these fields first:

- Competency brief:
  - `description`
  - `competency.definition`
  - `competency.whyItMatters`
- Prompt block:
  - `prompt.primary`
  - every `prompt.variants[]` entry
  - every `prompt.interviewerIntent[]` entry

For prompt text, highlight the behavior being requested, not the generic lead-in. For interviewer intent, highlight the evaluation distinction the interviewer should notice.

Examples:

- Better: `influenced a **technical decision without formal authority**`
- Weaker: `**Tell me about a time** you influenced...`
- Better: `turn discussion into an **explicit decision mechanism**`
- Weaker: `Can they **turn discussion**...`

## Good Phrases To Highlight

Prefer short phrases that help a reader skim senior leadership judgment:

- Competency concepts: `**decision criteria**`, `**customer impact**`, `**ownership model**`.
- Situation constraints: `**incomplete data**`, `**executive ambiguity**`, `**roadmap pressure**`.
- Evidence and mechanisms: `**service-level objectives**`, `**incident taxonomy**`, `**recurring review**`.
- Strong-answer moves: `**personal actions**`, `**measurable results**`, `**durable operating change**`.
- Weak-answer gaps: `**no clear baseline**`, `**generic alignment**`, `**missing ownership**`.
- Rubric signals: `**cross-functional alignment**`, `**portfolio trade-offs**`, `**decision rights**`.

## Density Rules

- Use emphasis sparingly: usually one short phrase per sentence or list item.
- Prefer 2-5 word phrases over single generic words or long clauses.
- Do not bold full sentences, whole bullets, headings, or repeated boilerplate.
- Do not bold every occurrence of the same phrase; emphasize where it teaches the reader what to notice.
- If a section is already dense with bold markers, improve the weakest markers instead of adding more.
- Keep `**` markers balanced and inside the string value.

## Fields To Consider

Natural-language fields commonly worth highlighting:

- `description`
- `competency.definition`
- `competency.whyItMatters`
- `prompt.primary`, `prompt.variants[]`, `prompt.interviewerIntent[]`
- `scenario.signatureExample`, `scenario.context[]`, `scenario.constraints[]`
- `storyAnatomy.situation`, `task`, `action[]`, `result[]`, `reflection`, `systemChange[]`
- `exampleStories[].situation`, `strongAnswerSketch[]`, `whyItWorks[]`, `weakVersion`, `followUpAngles[]`
- `strongAnswerPattern.summary`, `strongAnswerPattern.moves[]`
- `weakAnswerPattern.summary`, `weakAnswerPattern.redFlags[]`
- `followUps[].question`, `followUps[].exampleAnswers.strong[]`, `followUps[].exampleAnswers.weak[]`
- `evaluation.signals[].strong`, `evaluation.signals[].weak`
- `evaluation.rubric[].expected`
- `practiceTemplate.prompts[].label`
- `relatedScenarios[]`
- `toProbeFurther.links[].why`

## Fields To Avoid

Do not add bold markers to machine-readable or path-like fields:

- `id`, `name`, `title`, `family`, `roleFocus`, `difficulty`, `level`, `source`, `type`, `year`, `url`
- asset paths such as `assets.icon`, `explainerComic`, `aiVisual`, `strongAiVisual`, `weakAiVisual`
- visualization ids such as `visualizations.timeline[]`, `signalMap[]`, `followUpTree[]`
- `toProbeFurther.links[].id`, `group`, `groupDescription`, `title`, `url`

When unsure, leave the field unmodified.

## Editing Guidance

Keep the interview's seniority signal intact. A good highlight points to a real behavior or evaluation distinction:

- Better: `created **decision criteria** before execution`
- Weaker: `created **clarity**`
- Better: `left behind **ownership and escalation paths**`
- Weaker: `left behind **important changes**`

If highlighting exposes vague prose, make the smallest useful wording improvement and treat the task like a content edit. Coordinate with `behavioral-interview-improver` when the user asks for broader improvement beyond emphasis.

## Verification

After editing interview JSON, run:

```bash
python3 -m json.tool data/<group>/<id>/interview.json >/dev/null
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

For skill-only edits, `git diff --check` is enough.

---
name: interview-examples-variants
description: "Add or improve concrete example stories, prompt variants, weak and strong answer variants, and follow-up angles for behavioral interview specs in this repository. Use when a user asks for more concrete examples inside each interview, more variants by role or level, or better example coverage."
---

# Interview Examples Variants

## Workflow

1. Read the target `interview.json`, especially `prompt`, `scenario`, `storyAnatomy`, `exampleStories`, `followUps`, and `evaluation`.
2. Add examples that expand coverage rather than repeat the same story with different nouns.
3. Keep each example compatible with the interview's competency and role focus.
4. Update related prompts, follow-up probes, or rubric language when a new example reveals a missing signal.
5. Validate and rebuild after editing source data.

## Example Story Shape

Each `exampleStories` item should include:

- `id`: stable hyphen-case id.
- `title`: concrete situation title.
- `level`: expected role or level, such as Director, VP Engineering, or CTO.
- `promptVariant`: the prompt wording this story answers.
- `situation`: specific context, stakes, constraints, and disagreement.
- `strongAnswerSketch`: 3-5 action bullets with decisions, mechanisms, and trade-offs.
- `whyItWorks`: 2-4 bullets tied to the competency and evaluation signals.
- `weakVersion`: a plausible but insufficient answer pattern.
- `followUpAngles`: questions that test ownership, judgment, metrics, disagreement, and learning.

## Variant Strategy

Prefer examples that differ by operating context:

- Ambiguous executive mandate.
- Cross-functional conflict.
- Technical risk under business pressure.
- Organizational scaling or re-org tension.
- Ethical, customer, reliability, security, or cost constraint.
- Different level expectations for Director, VP Engineering, and CTO.

Avoid creating variants that only rename the same problem. If two examples test the same behavior, make one reveal a different failure mode or stakeholder tension.

## Verification

Run:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
```

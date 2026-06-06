---
name: behavioral-interview-author
description: "Create new behavioral interview specs for the spec-driven-behavioral-interviews repository. Use when adding a new interview dataset, choosing category placement, scaffolding data/book or data/examples entries, filling the JSON schema, or preparing a new interview for the static explorer."
---

# Behavioral Interview Author

## Workflow

1. Read `AGENTS.md`, `data/README.md`, the target group manifest such as `data/book/index.json`, and one or two nearby `interview.json` files in the same competency family.
2. Choose the publishable group and category. Use `book` for canonical catalog content and `examples` only for small renderer examples.
3. Scaffold the dataset before hand-authoring JSON:

```bash
python3 _scripts/scaffold_interview.py --list-families
python3 _scripts/scaffold_interview.py --list-roles
python3 _scripts/scaffold_interview.py book new-interview-id \
  --title "New Interview Title" \
  --category-id judgment-strategy \
  --category-name "Judgment and Strategy"
```

4. Fill the source file at `data/<group>/<id>/interview.json`. Do not edit generated files under `docs/`.
5. Preserve the structural answer shape: `Situation -> Task -> Action -> Result -> Reflection -> System Change`.
6. Rebuild and verify after content changes.

## Content Requirements

Include these fields with concrete senior-leadership content:

- `roleFocus`, `difficulty`, and `competency` with a clear family and definition.
- `prompt.primary`, at least two `prompt.variants`, and interviewer intent.
- `scenario` with a signature example, context, and constraints.
- `storyAnatomy` with personal accountability, trade-offs, measurable results, reflection, and durable operating change.
- At least two `exampleStories` with distinct level, situation, strong answer sketch, why it works, weak version, and follow-up angles.
- `strongAnswerPattern`, `weakAnswerPattern`, `followUps`, `evaluation.signals`, `evaluation.rubric`, `visualizations`, `practiceTemplate`, and `relatedScenarios`.

## Quality Bar

Make the interview test a real senior operating judgment, not a generic behavioral prompt. Strong content names the ambiguity, conflict, constraints, personal decisions, rejected alternatives, measurable outcomes, and mechanisms left behind. Avoid vague claims such as "aligned stakeholders" unless the spec explains the actual forum, decision rule, metric, or ownership model.

## Verification

Run the focused checks before finishing:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

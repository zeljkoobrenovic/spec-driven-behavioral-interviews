---
name: behavioral-interview-improver
description: "Improve existing behavioral interview specs in this repository. Use when upgrading an interview JSON file, making generic examples more concrete, strengthening strong and weak answer patterns, deepening follow-up probes, improving evaluation rubrics, or aligning an existing interview with the project schema and quality bar."
---

# Behavioral Interview Improver

## Workflow

1. Read the target `data/<group>/<id>/interview.json`, its group manifest, `AGENTS.md`, and adjacent interviews in the same competency family.
2. Run or inspect coverage before editing:

```bash
python3 _scripts/summarize_coverage.py
python3 _scripts/validate_interviews.py
```

3. Identify the weakest part of the spec: prompt specificity, scenario constraints, story anatomy, example diversity, answer contrast, follow-up probes, rubric expectations, visual configuration, or role-level differentiation.
4. Edit only the source JSON under `data/`. Preserve ids and manifest paths unless the user explicitly asks to rename.
5. Rebuild generated output with `python3 build.py` after source changes.

## Improvement Checklist

Strengthen the spec until it answers these questions:

- What senior leadership situation is being tested?
- What makes the situation high-stakes, ambiguous, or politically difficult?
- What did the candidate personally decide or change?
- Which alternatives, trade-offs, or stakeholder conflicts were handled?
- What measurable outcome resulted?
- What durable mechanism changed after the story?
- How would a weak answer sound credible at first but fail under follow-up?
- What evidence should the interviewer score at Senior Manager, Director, VP Engineering, and CTO levels?

## Editing Rules

Prefer concrete operating mechanisms over adjectives. Replace "improved communication" with a forum, cadence, decision rights, escalation rule, dashboard, ownership model, or planning change. Replace "drove alignment" with who disagreed, what criteria resolved the disagreement, and what decision became easier afterward.

Keep example stories adaptable. They should be story shapes a candidate can map to their experience, not scripts to memorize.

## Verification

Run the checks relevant to the edit:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

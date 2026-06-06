# Review

## Purpose

This document defines how to review the behavioral interview catalog for realism, balance, educative value, interviewer usability, and spec quality. It should be updated after substantial additions to `data/book/` or major changes to the shared templates.

## Rating Scale

- `5 - Excellent`: realistic, fair, concrete, educative, and ready to publish.
- `4 - Strong`: publishable with minor improvements.
- `3 - Useful but uneven`: structurally sound, but needs more concrete examples, sharper rubrics, or better balance.
- `2 - Weak`: plausible topic, but too generic or hard to use in a real interview.
- `1 - Rewrite`: unrealistic, misleading, or not educational enough to keep.

## Current Snapshot

The catalog currently has 16 canonical datasets in `book`. Every dataset validates structurally and has two concrete example stories.

Coverage is strongest for Director, VP Engineering, and CTO audiences. Senior Manager appears in fewer datasets, which is reasonable for a senior-leadership book but should be deliberate when adding foundational or transition-level material.

## Overall Assessment

Current rating: `4 - Strong`.

The catalog has a solid spec structure and a useful educational model. The strongest pattern is that each interview separates prompt, scenario, story anatomy, strong answer, weak answer, follow-ups, evaluation signals, rubric, and practice template. That makes the system more teachable than a conventional list of behavioral questions.

The main improvement opportunity is realism breadth. Many examples are credible senior-engineering situations, but the catalog would become more robust with more variation by company stage, industry, failure mode, team size, geography, regulatory pressure, business model, and organizational maturity.

## Strengths

- The structured data model is clear and consistent across interviews.
- Strong answers emphasize trade-offs, ownership, measurable outcomes, reflection, and durable operating mechanisms.
- Weak answer patterns are useful because they describe plausible but insufficient answers, not obviously bad caricatures.
- Follow-up probes generally test evidence instead of inviting generic narration.
- The STAR-plus-system-change structure makes the material educative for candidates and interviewers.
- The generated explorer supports scanning, practice, comparison, and visual learning.

## Gaps And Risks

- Two concrete examples per interview is a good baseline, but not enough to show the full range of realistic senior-leadership contexts.
- Most canonical interviews are marked `advanced`; the catalog may under-serve candidates transitioning from Senior Manager to Director.
- Some examples risk over-rewarding process creation. Add cases where the right answer is escalation, simplification, stopping work, technical deep dive, principled refusal, or rapid containment.
- Rubrics should keep separating Director, VP Engineering, and CTO expectations. If level language becomes too similar, interviewers will score on polish instead of evidence.
- Add more explicit negative space: what a strong candidate chose not to do, which stakeholder view they did not accept, or what trade-off they knowingly left unresolved.
- Ensure examples do not imply that every senior problem ends with a new ritual, dashboard, or governance forum.

## Review Dimensions

### Realism

Look for messy context: incomplete data, disagreeing stakeholders, unclear ownership, time pressure, customer or business impact, and credible constraints. A realistic interview should sound like something a Director, VP Engineering, or CTO could have actually faced.

### Balance

Look for balanced signals across technical judgment, business judgment, people leadership, execution, influence, ethics, and communication. The catalog should not teach one universal leadership style. Strong answers should vary by context.

### Educative Value

Look for clear teaching value. The spec should help a reader understand what evidence matters, why weak answers fail, and how follow-up questions reveal real ownership or inflated claims.

### Interview Usability

Look for prompts an interviewer can ask naturally, variants that gather different evidence, follow-ups that expose judgment, and rubrics that support fair level calibration.

### Spec Quality

Look for consistent ids, complete required fields, valid manifest paths, clear visualization settings, and source changes made under `data/` rather than `docs/`.

## Priority Recommendations

1. Add one or two more example stories to the highest-value canonical interviews, starting with ambiguity, technical judgment, executive conflict, underperformance, and ethics.
2. Add variant examples by company context: startup, scale-up, enterprise, regulated industry, marketplace, infrastructure platform, and AI/data-heavy product.
3. Strengthen level calibration by making each rubric explain what changes from Director to VP Engineering to CTO.
4. Add more counterexamples where the strong answer is not "create a process", but "make a hard call", "stop a harmful initiative", "narrow scope", "escalate clearly", or "absorb short-term pain for long-term trust".
5. Review all `weakVersion` fields for plausibility. The weak version should be tempting and common, not obviously incompetent.

## Per-Interview Review

Initial review of the canonical `book` catalog:

| Interview | Rating | Review Notes | Next Improvement |
| --- | --- | --- | --- |
| `interview-method` | 4 | Educative framing is strong and helps users understand how to shape senior stories. | Add more interviewer-side calibration examples and common scoring mistakes. |
| `leading-through-ambiguity` | 4 | Realistic senior ambiguity with useful operating mechanisms and AI/reliability variants. | Add a non-platform example where the right move is narrowing scope or rejecting an unclear mandate. |
| `strategy-vs-execution` | 4 | Good business-context balance and useful strategy/execution tension. | Add an example where execution discipline beats a more attractive strategic narrative. |
| `technical-judgment` | 4 | Strong balance between technical depth and executive-scale decision making. | Add variants for data, security, or reliability trade-offs beyond architecture and build-versus-buy. |
| `technical-debt-modernization` | 4 | Economic framing makes the topic realistic and educative. | Add more stakeholder tension with Product, Finance, or Sales commitments. |
| `failure-accountability` | 4 | Strong realism because it tests ownership without simple blame. | Add an example with shared ownership across vendor, platform, and product boundaries. |
| `crisis-leadership` | 4 | Practical crisis signals and follow-ups make the interview usable. | Add more long-tail recovery detail: customer remediation, trust repair, and post-crisis sequencing. |
| `building-leadership-teams` | 4 | Well balanced between talent judgment, development, and calibration. | Add a case where the obvious promotion is politically popular but wrong for the future org. |
| `handling-underperformance` | 4 | Realistic and fair, with useful distinction between clarity, fairness, and decisiveness. | Add more constraints around role mismatch, HR process, and team morale. |
| `culture-change` | 4 | Educative because it ties culture to incentives and operating systems. | Add a case where the desired culture change conflicts with urgent delivery pressure. |
| `scaling-organization` | 4 | Realistic scaling diagnosis with useful operating-design focus, now strengthened with measured outcomes and a simplification-focused variant. | Add future variants for global teams or regulated operational complexity. |
| `executive-conflict` | 4 | High-value topic with realistic peer and founder conflict patterns. | Add an example where the strong answer includes adapting or conceding after new evidence. |
| `cross-functional-influence` | 4 | Good balance between empathy, framing, and durable shared mechanisms. | Add examples involving Sales, Customer Success, or Support to broaden business realism. |
| `executive-communication` | 4 | Strong educative value for board and executive communication. | Add more explicit examples of concise metrics, decision asks, and uncertainty framing. |
| `ethics-responsible-technology` | 4 | Realistic modern senior-leadership topic with strong trust-risk signals. | Add variants involving international regulation, data retention, or model governance. |
| `innovation-emerging-technology` | 4 | Balanced treatment of innovation, adoption risk, and measurable learning. | Add a failed experiment example with clear kill criteria and learning reuse. |

Use this template when reviewing individual specs:

```text
Path:
Rating:
Realism:
Balance:
Educative Value:
Interview Usability:
Spec Quality:
Strengths:
Risks:
Recommended Edits:
```

## Ongoing Review Checklist

- Run `python3 _scripts/validate_interviews.py`.
- Run `python3 _scripts/summarize_coverage.py`.
- Inspect the target `data/<group>/<id>/interview.json`.
- Compare against at least one adjacent interview in the same competency family.
- Check whether prompt variants create different evidence, not just different wording.
- Check whether example stories are specific enough to be memorable but general enough to adapt.
- Check whether strong and weak answer patterns are realistic opposites.
- Check whether follow-ups test the claims made in the strong answer pattern.
- Check whether rubrics differentiate levels with real scope, accountability, and judgment differences.
- Rebuild with `python3 build.py` after source data changes.

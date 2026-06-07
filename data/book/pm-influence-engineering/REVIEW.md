# Review: Influencing Engineering and Stakeholders

File: `data/book/pm-influence-engineering/interview.json`

## Purpose

Per-interview review of the PM "Influencing Engineering and Stakeholders" spec
against the project review dimensions: realism, balance, educative value,
interview usability, spec quality, and external resources.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- Validation: passes (`validate_interviews.py` — 28 datasets ok).
- Coverage: registered in `data/book/index.json` under the Product Managers
  group; competency family Influence and Communication.
- Structure: all expected fields present (competency, prompt, scenario,
  storyAnatomy, exampleStories, strong/weak patterns, followUps, evaluation,
  visualizations, practiceTemplate, relatedScenarios, toProbeFurther).
- Example stories: **five**, spanning Product Manager → Senior PM → Group PM and
  three modes — rescope, principled refusal, and concede-when-right.
- Follow-ups: five (`stakeholder-empathy`, `decision-options`, `mechanism`,
  `escalation-boundary`, `concede-when-right`); four evaluation signals.
- Visual assets: none referenced (no icon, comic, or signal/story visuals).
- External resources: **10 curated `toProbeFurther.links[]`**, grouped into five
  themes, each with a relevance note and no duplication against sibling PM
  interviews.

## What Changed Since The Previous Review

The spec has been substantially expanded, and every priority recommendation from
the prior review has been addressed:

1. **External resources added.** A 10-link `toProbeFurther.links[]` now exists
   (was the highest-priority gap, previously scored 1). Links are grouped by
   theme — influence/stakeholders (SVPG stakeholder management, Cialdini),
   product-engineering risk (SVPG Four Big Risks, PM Introduction), decision
   mechanisms (Intercom decision framework, Google Cloud ADRs), customer
   commitments/roadmaps (Intercom feature-request + sales-input, O'Reilly
   *Product Roadmaps Relaunched*), and launch readiness (Google SRE launch
   planning). Spot-checked URLs return 200; no obren.io links; no duplicate
   book/article shared with `pm-customer-discovery` or `cross-functional-influence`.
2. **GPM-level example story added.** `portfolio-api-launch-phasing` is set at
   Group Product Manager level (a partner-API launch across three product
   areas), giving the top rubric band a concrete calibration anchor it previously
   lacked.
3. **Concede-when-right counter-case added.** New story
   `strategic-sso-commitment-accepted`, a new `concede-when-right` follow-up, a
   matching prompt variant, an `interviewerIntent` line, and a
   `strongAnswerPattern` move ("Concedes when stakeholder evidence reveals a
   strategic product bet worth the cost"). This directly fixes the prior
   "over-rewards principled refusal" balance risk.
4. **Escalation/refusal case added.** New story
   `regulated-data-commitment-refusal`, a new `escalation-boundary` follow-up, and
   a fourth signal `boundary-escalation`, distinguishing healthy escalation from
   appealing upward to win an argument.

## Overall Assessment

A strong, well-rounded spec — clearly improved from the prior pass. It tests
influence-without-authority for PMs across the full judgment range: rescoping a
bespoke ask, refusing an unsafe commitment, and conceding when evidence proves a
stakeholder right. The strong/weak calibration is consistently concrete, the
durable-mechanism move is reinforced throughout, and the resource list is now at
or above catalog norm. The chief remaining items are minor: residual catalog
overlap with two adjacent influence interviews and the absence of optional visual
assets.

## Strengths

- **Realism (5).** All five stories carry genuine conflict, rejected
  alternatives, and measurable boundaries — "only two of the requested
  capabilities were tied to renewal risk," "the data model would support only
  three of the five promised metrics," Legal refusing a side letter for regulated
  EU employee data, and an all-seven-partner API launch narrowed to a five-partner
  first wave. Recognizable, messy PM situations rather than polished hindsight.
- **Balance (4).** The spec now models three distinct strong moves — rescope,
  refuse, and concede — rather than uniformly rewarding "say no well." The
  `concede-when-right` follow-up and the SSO story explicitly reward changing
  one's mind on evidence, and the weak-answer red flags penalize both reflexive
  refusal and reflexive acceptance.
- **Educative value (5).** Weak follow-up answers ("They had valid concerns, but
  we needed to move forward") are deliberately realistic and expose missing
  evidence/ownership, giving interviewers a clear calibration anchor.
- **Mechanism discipline (5).** `systemChange`, the `decision-mechanism` signal,
  and the `mechanism` follow-up push past one-time alignment toward reusable
  artifacts (customer-commitment review with exception expiration, launch-readiness
  checklist, partner-launch gate, segment-fit review). Still the spec's best
  teaching point.
- **Level calibration (4).** Stories span PM, Senior PM, and Group PM, so each
  rubric band has at least one anchored example.
- **External resources (4).** Themed grouping, one-sentence relevance notes,
  canonical non-Obren sources, and no duplication with sibling PM interviews.

## Gaps And Risks

1. **Catalog overlap / balance (medium).** Three catalog interviews still cover
   adjacent influence terrain: this one, `tech-lead-influence` (Influence Without
   Authority), and `cross-functional-influence`. The PM framing here is genuinely
   distinct (Sales/renewal/launch-promise/segment-fit lens), and the SSO and
   regulated-data stories sharpen that distinctiveness, but the scenario does not
   yet *name* the PM-unique ownership (customer commitments, GTM/launch promises)
   as an explicit differentiator. Low-cost to add a one-line note.
2. **Rubric still scaled rather than re-shaped (low).** The Group PM band reads as
   the Senior PM band plus "across product areas / institutionalizing." The new
   GPM story now anchors it concretely, so this is no longer a calibration gap —
   but the band could test a more distinct behavior (portfolio decision quality,
   coaching other PMs, changing org commitment norms) rather than a scaled
   restatement.
3. **No visual assets (low / optional).** No icon or signal visuals. Optional, not
   required.

## Review Dimensions

| Dimension            | Score | Notes |
|----------------------|-------|-------|
| Realism              | 5     | Five stories with concrete conflict, rejected alternatives, measurable boundaries. |
| Balance              | 4     | Now models rescope, refuse, and concede; minor residual overlap with two influence interviews. |
| Educative value      | 5     | Strong/weak calibration teaches observable behavior, not slogans. |
| Interview usability  | 5     | Tight prompts, five evidence-exposing follow-ups, level-anchored rubric. |
| Spec quality         | 5     | Complete, internally consistent, ids/paths stable, passes validation. |
| External resources   | 4     | 10 themed, deduplicated, canonical links with relevance notes. |

## Priority Recommendations

The four previous priority recommendations have all been implemented. Remaining
items are optional polish:

1. **Make the PM-specific lens explicit (optional, improves balance).** A short
   scenario note distinguishing this from `tech-lead-influence` and
   `cross-functional-influence` — the PM uniquely owns the customer commitment and
   the launch promise — would reduce perceived catalog redundancy.
2. **Re-shape, don't just scale, the GPM rubric band (optional).** Rewrite the
   GPM `expected` row to test portfolio-level decision quality or coaching of
   other PMs rather than a scaled restatement of the Senior PM row. The
   `portfolio-api-launch-phasing` story already supports this re-shaping.
3. **Consider optional visual assets (low).** An icon or signal-map visual would
   match richer catalog entries; not required.

## Verification

After data edits, run:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

REVIEW.md-only changes need no build.

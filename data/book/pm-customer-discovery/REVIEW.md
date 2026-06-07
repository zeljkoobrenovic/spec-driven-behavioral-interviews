# Review

## Purpose

Single-interview review of `data/book/pm-customer-discovery/interview.json`
("Customer Discovery and Product Direction") against the repository's realism,
balance, educative value, interviewer usability, spec quality, and external
resource dimensions. This revision reflects the expanded spec (third example,
Group Product Manager level, fourth follow-up, sharper scenario constraints).

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- Group: `product-managers` (Product Managers).
- Competency: Customer Discovery and Product Direction (family: Judgment and Strategy).
- Role focus: Product Manager, Senior Product Manager, Group Product Manager. Difficulty: intermediate.
- Three example stories, three signals, four follow-ups, three rubric levels.
- `python3 _scripts/validate_interviews.py`: passes (28 datasets ok).
- `python3 _scripts/summarize_coverage.py`: passes; this dataset is one of 3 in
  Product Managers.
- Signal tests and role levels used are all canonical per `_templates/*.json`.

## What Changed Since The Last Review

The previous review (two examples, two rubric levels, three follow-ups) is
superseded. The spec has grown materially:

- **Added a Group Product Manager example** (`admin-dashboard-to-team-templates`):
  an inherited executive-dashboard roadmap that discovery reframes as a
  post-purchase setup problem. It admits the first hypothesis was buyer-centered
  and was wrong — directly addressing the old "always-pivot / hindsight-polished"
  concern.
- **Added a third role and a Group Product Manager rubric row** — resolves the old
  Gap #3 (two-level rubric blurred the top end).
- **Added a fourth follow-up** (`partial-learning`: "What did your first
  hypothesis or revised direction still get wrong?") with calibrated strong/weak
  answers — strengthens the accountability/learning dimension.
- **Sharpened the scenario**: a context line about conflicting-segment evidence
  and a constraint requiring the PM to name the rejected path, its residual risk,
  and a revisit trigger.
- **Added weak-pattern red flag**: "presents the change as a clean win and cannot
  name who lost," reinforcing the new partial-learning probe.

## Overall Assessment

A strong, well-constructed PM interview that is now noticeably more complete than
at the last review. The core idea — separating the *request* from the *job behind
it* — is the right thing to test, and the spec teaches it concretely through the
bulk-export-to-reconciliation signature example. The new GPM example raises the
ceiling: it models discovery across personas and an explicit, owned admission
that the first hypothesis was wrong. Strong and weak patterns remain crisp and
genuinely distinguishable. The single material remaining gap is the missing
`toProbeFurther.links[]` section, which is a cluster-wide PM gap rather than
unique to this file.

Composite: **4.4 / 5** (up from 4.2 — the third level, fourth follow-up, and
GPM example closed two of the prior gaps).

## Strengths

- The signature example (bulk export request hiding a billing-reconciliation job)
  is realistic and memorable, and the weak version ("customers asked for export,
  so I gathered requirements, aligned the team, and shipped") is an accurate
  picture of how the failure mode actually sounds.
- The second example (onboarding drop-off framed as a *trust* problem, not a
  *confusion* problem) adds a genuinely different shape — competing hypotheses
  and funnel-plus-qualitative reasoning — rather than restating example one.
- The new third example (executive-dashboard request reframed as a setup problem)
  adds a distinct GPM-altitude shape: discovery across buyers/admins/team
  leads/churned accounts, an explicit "the first hypothesis was too buyer-centered"
  admission, and a residual-risk mitigation (manual reporting packet for two
  account teams). This is the strongest realism/accountability lift in the file.
- Follow-up example answers are well calibrated across all four probes. The
  strong/weak pairs draw a clean line between specific evidence and generic
  alignment talk, and the new `partial-learning` probe forces a candidate off the
  "clean win" narrative.
- The scenario carries real tension: a visible, validated-looking request the PM
  "must not ignore", limited capacity for one release, conflicting-segment
  evidence, and a planning deadline.
- Signals, rubric, answer patterns, and the new red flag are internally consistent
  (the `learning-loop` signal, the systemChange items, the "no post-launch
  checkpoint" and "clean win / cannot name who lost" red flags all reinforce each
  other).
- The rubric now spans all three canonical levels and differentiates them
  meaningfully: scope-a-focused-solution (PM) → change-direction-across-segments
  (Senior) → own-the-discovery-mechanism-across-areas (GPM).

## Gaps And Risks

1. **No `toProbeFurther.links[]` (highest priority).** This file — like all three
   Product Manager interviews — has no external reading list, while most
   leadership interviews carry 13–16 curated links. This is the one concrete data
   deficiency remaining. (Cluster-wide, not file-unique.)
2. **No visual assets.** No `assets.icon`, no `explainerComic`, no `aiVisual`
   fields on patterns/signals/examples. Optional per the spec, but the leadership
   interviews set a higher bar; consider at least an `icon`.
3. **Residual balance tilt toward "change direction."** All three examples reward
   pivoting away from (or reframing) the requested feature. The new GPM example
   softens this by admitting a wrong first hypothesis, but discovery sometimes
   *confirms* the request, and the strong move is then shipping with conviction
   plus a tighter metric and a kill criterion. A short note or fourth example
   where evidence validates the original idea would prevent candidates from
   learning "the right answer is always to pivot." (Reduced from prior review but
   not eliminated.)
4. **`relatedScenarios` are not cross-links.** They are prose restatements of the
   scenario rather than pointers to sibling PM interviews
   (`pm-prioritization-tradeoffs`, `product-data-decisions`), which overlap
   heavily. Not a defect, but a missed navigation opportunity.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 5 | Credible request-hides-a-job scenarios across three altitudes; the GPM example's "admit the first hypothesis was wrong" plus residual-risk mitigation removes the prior hindsight-polish concern. |
| Balance | 4 | Strong qual/quant, segment trade-off, and persona coverage; mild residual tilt toward "pivot/reframe the request" as the rewarded behavior. |
| Educative Value | 5 | Strong/weak patterns and calibrated four-probe follow-up answers make the evaluation logic explicit and teachable. |
| Interview Usability | 5 | Prompt and variants are easy to ask; follow-ups expose evidence vs. opinion; the three-level rubric no longer blurs at the top. |
| Spec Quality | 5 | Validates clean; ids, paths, signal tests, and role levels are all canonical and internally consistent. |
| External Resources | 1 | No `toProbeFurther.links[]` at all. |

## Priority Recommendations

1. **Add `toProbeFurther.links[]`.** Target 6–10 canonical, non-Obren resources on
   customer discovery and continuous discovery. Strong candidates to research:
   Teresa Torres *Continuous Discovery Habits* (publisher/author page), Marty
   Cagan / SVPG essays on product discovery, the Intercom "Jobs To Be Done"
   material, the original Christensen JTBD HBR article, and Steve Blank's customer
   development writing. Each link needs a one-sentence `why`. Consider doing the
   whole PM cluster together for shared groups.
2. **Add a counter-example or note where discovery *confirms* the request** so the
   spec does not teach "pivoting is the correct answer." The strong move there is
   shipping with a sharper success metric and a kill criterion.
3. **(Optional) Add at least an `assets.icon`** to match the visual bar set by the
   leadership interviews.
4. **(Optional) Turn `relatedScenarios` into cross-links** to sibling PM
   interviews as the cluster matures.

## Per-Interview Review

- **File:** `data/book/pm-customer-discovery/interview.json`
- **Rating:** 4.4 / 5 — strong, now three-level content; one real data gap (no
  external links).
- **Main strengths:** memorable request-vs-job signature example; three
  genuinely distinct example shapes (reconciliation, trust-vs-confusion, GPM
  persona discovery with an owned wrong hypothesis); well-calibrated four-probe
  follow-up answers; clean, consistent, three-level spec.
- **Main risks:** missing external resources; residual "change direction" balance
  tilt; no visual assets.
- **Recommended next edits (in order):** (1) add `toProbeFurther.links[]`;
  (2) add a discovery-confirms-the-request example or note; (3) add an icon.

## Ongoing Review Checklist

- [ ] After any content edit, run `validate_interviews.py` and
      `summarize_coverage.py`, then `build.py` and `smoke_static_site.py`.
- [ ] Keep signal `tests`, role levels, and competency `family` aligned with the
      canonical `_templates/*.json` vocabularies.
- [ ] When adding `toProbeFurther.links[]`, verify links are canonical non-Obren
      pages with a one-sentence `why`, and avoid duplicate book/article entries.
- [ ] Re-check balance: ensure strong answers are not all "pivot away from / reframe
      the requested feature"; add a discovery-confirms case.
- [ ] Keep `relatedScenarios` / cross-links consistent with sibling PM interviews
      as the cluster grows.

# Review

## Purpose

A focused review of `data/book/scaling-organization/interview.json` against the project review dimensions: realism, balance, educative value, interview usability, spec quality, and external resources. Findings separate fixable data issues from subjective content recommendations.

This revision updates the prior review to reflect recent changes to the spec. Most of the earlier recommendations have been implemented (see *Changes Since Last Review*).

## Rating Scale

1 = weak, 2 = below bar, 3 = solid, 4 = strong, 5 = exemplary.

## Current Snapshot

- Competency: Scaling An Organization (`organizational-scale`), family Organizational Scale.
- Role focus: **Senior Manager, Director, VP Engineering, CTO**. Difficulty: advanced.
- **4 example stories** (Senior Manager, Director, VP, CTO), **5 follow-ups** with strong/weak calibration answers, **4 evaluation signals**, 4-level rubric.
- No visual assets referenced (no `assets`, `aiVisual`, `explainerComic`). Clean and consistent — nothing to validate.
- 7 external links across interviewing, org design, and people leadership.
- `python3 _scripts/validate_interviews.py` → ok (16 datasets). `summarize_coverage.py` → all signals and follow-up test tags align with the canonical vocabularies (`Manager and Cost Judgment` signal and the new follow-up test tags appear in coverage).

## Changes Since Last Review

The recent edit closed four of the five gaps the prior review raised:

- **Senior Manager role added and reconciled.** `roleFocus` now includes Senior Manager, and a new Senior Manager example (`manager-bench-under-hiring-pressure`) plus the existing rubric rung now align. The rubric/role-focus inconsistency is resolved.
- **People/talent dimension added.** `manager-bench-under-hiring-pressure` centers a *leadership-layer* failure (manager span of 11–13 reports, onboarding lag, senior ICs becoming default coordinators) rather than a process failure — exactly the people-centered example the prior review asked for.
- **Cost / efficiency trade-off added.** A new `structure-cost` follow-up ("What did the added structure cost, and how did you decide it was worth it?") and a new `manager-cost-judgment` signal now probe whether the candidate reasons about the *cost* of structure, not only its coordination payoff.
- **`relatedScenarios` diversified.** Now includes scaling via acquisition/merge and reducing layers/approval gates under cost pressure, instead of restating the example stories.

Remaining open item: the Team Topologies edition/year claim still needs external verification (see Gaps).

## Overall Assessment

A strong, well-constructed interview, now meaningfully more balanced than at the prior review. The central thesis — add structure at points of coordination failure, sometimes remove it — is reinforced consistently across the prompt, examples, signals, and rubric, and it is now complemented by an explicit people-and-cost lens. The CTO example that scales by *removing* a bottleneck remains a genuine differentiator, and the new Senior Manager example adds a leadership-capacity failure mode that most scaling prompts miss. The mechanism-that-backfired-and-was-rolled-back detail (the weekly review that became status theater) now appears in both `storyAnatomy.action` and the Senior Manager example, modeling evidence-based reversal well. The one remaining weakness is a single external-link factual claim that needs verification.

Composite: **4.6 / 5**.

## Strengths

- **Proportional-structure thesis is consistent end to end.** The "add at failure points, not everywhere" idea appears in `storyAnatomy.reflection`, the `strongAnswerPattern.moves` ("Removes or simplifies mechanisms that became bottlenecks"), the `too-much-process` follow-up, and the `proportional-structure` signal. The spec teaches one clear mental model rather than generic "scale = more process."
- **People and cost are now first-class.** The new `manager-cost-judgment` signal, the `structure-cost` follow-up, and the `manager-bench-under-hiring-pressure` example mean the spec now rewards reasoning about manager capacity, onboarding load, and the cost of structure — not just decision-rights mechanics. This was the main balance gap and it is now well covered.
- **The simplification example is still the standout.** `simplifying-platform-bottleneck` (CTO) tests the counter-intuitive move of *retiring* mandatory review and replacing it with guardrails, with concrete metrics (decision lead time, blocked engineering days, platform support load, escaped architecture incidents).
- **Backfired-mechanism modeling.** Both the anatomy and the Senior Manager example show a mechanism that was tried, measured, and rolled back — teaching that reversal on evidence is a strength, not a failure. The `structure-cost` strong answer quantifies the cost ("roughly six manager-hours a week") that justified the reversal.
- **Measurable, credible results.** `storyAnatomy.result` uses hedged, realistic numbers ("roughly 55% to 75%", "dropped by about a third") rather than implausible precision.
- **Follow-up calibration answers are excellent and discriminating.** Each strong/weak pair separates real judgment from generic growth language; the weak answers are realistic failure modes, not strawmen.
- **Variants meaningfully change the evidence gathered**, and each example is tied to a specific variant; the four examples now span all four declared role levels.

## Gaps And Risks

1. **External link factual claim — verify before publishing.** The `team-topologies` entry asserts a "2025 second edition" with `"year": "2025"`. The widely-distributed edition of *Team Topologies* (Skelton & Pais, IT Revolution) is the 2019 first edition. If a 2025 second edition exists, keep the note; if not, correct the year and drop "second edition." Could not verify in this session (web search not available). **Fixable data issue, pending verification.** This is the only carried-over gap from the prior review.
2. **Result/people-example metric symmetry (minor).** The `storyAnatomy.result` is rich with numbers, and the `structure-cost` follow-up quantifies cost, but the Senior Manager example's outcome is framed mostly qualitatively ("accept the cost of slowing two hires and moving one feature by a quarter"). Optionally add one quantified leadership-capacity outcome (e.g., manager span normalized to a target, onboarding ramp time) so the people example matches the measurement bar set by the rest of the spec. Subjective enhancement.
3. **`relatedScenarios` / example overlap is reduced but not eliminated (minor).** "Scaling a product area faster than the manager bench and onboarding system can absorb" now closely mirrors the new Senior Manager example. Acceptable, but could be swapped for a genuinely adjacent scenario if more surface is wanted. Minor.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 5 | Messy constraints (autonomy vs. coordination, hiring vs. onboarding capacity), credible hedged outcomes, a mechanism that backfired and was reversed, real failure modes across four levels. |
| Balance | 5 | Now covers add-vs-remove structure, decentralization, people/talent (manager bench), and cost trade-offs. The prior balance gap is closed. |
| Educative Value | 5 | Clear, consistent thesis; discriminating strong/weak calibration; explicit signals and rubric; teaches evidence-based reversal. |
| Interview Usability | 5 | Variants and follow-ups expose distinct evidence; rubric levels now match the declared `roleFocus`; five follow-ups map cleanly to the four signals plus diagnosis. |
| Spec Quality | 5 | Validates clean; ids, paths, signal/test vocabularies all consistent; new signal and follow-ups appear in coverage; no broken asset references. |
| External Resources | 3 | Credible, well-noted, no duplicates, links only in To Probe Further — but the Team Topologies edition/year claim still needs verification. |

## Priority Recommendations

1. **Verify the Team Topologies edition/year claim** in the `team-topologies` link `why`/`year`. Correct or confirm. (Data fix — the one remaining open item.)
2. **Optionally quantify the Senior Manager example outcome** so the people-centered example matches the measurement standard set elsewhere. (Minor content enhancement.)
3. **Optionally freshen the overlapping `relatedScenarios` entry** that now mirrors the Senior Manager example. (Minor.)

## Per-Interview Review

**File:** `data/book/scaling-organization/interview.json`
**Rating:** 4.6 / 5 — strong, publishable; one link claim to verify.
**Main strengths:** Consistent proportional-structure thesis now balanced by an explicit people-and-cost lens; standout remove-structure CTO example; new Senior Manager leadership-capacity example; backfired-and-reversed mechanism modeling; realistic measurable outcomes; excellent follow-up calibration.
**Main risks:** Unverified Team Topologies edition/year claim.
**Recommended next edits:** (1) verify/correct the Team Topologies link; (2) optionally quantify the Senior Manager example outcome; (3) optionally freshen the overlapping related scenario.

## Ongoing Review Checklist

- [ ] Re-run `validate_interviews.py` and `summarize_coverage.py` after any edit.
- [ ] Confirm external links resolve and edition/year claims are accurate.
- [ ] Keep rubric levels consistent with `roleFocus`.
- [ ] Ensure new signals/test tags reuse canonical vocabularies in `_templates/*.json`.
- [ ] If visual assets are added later, generate with `--dry-run` first and rebuild `docs/`.

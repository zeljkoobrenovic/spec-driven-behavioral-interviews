# Review — Cross-Functional Influence

File: `data/book/cross-functional-influence/interview.json`
Group: `book` / Influence and Communication
Reviewed against: `AGENTS.md`, validation + coverage scripts, sibling `executive-conflict`.
Last updated after the revision that added escalation judgment, a fourth example, and the Cohen & Bradford resource.

## Snapshot

- `validate_interviews.py`: passes (part of 16/16 datasets).
- `summarize_coverage.py`: signals `Stakeholder Empathy`, `Credible Framing`, `Shared Mechanism`, and the newly added `Escalation Judgment` are unique to this dataset; family balance is fine. The dataset now carries 4 concrete example stories (one of only two datasets at that depth).
- `toProbeFurther.links[]` URLs return HTTP 200, except `us.macmillan.com` (Working Backwards), which returns 403 to bots — the page is live in a browser; not a dead link.

## What Changed Since The Previous Review

The revision directly closed most of the prior review's recommendations:

- **Escalation is now a first-class dimension, not a strawman.** A new `Escalation Judgment` signal, a fourth prompt variant, a CTO-level data-residency example, and refined weak/strong language make timely escalation a *senior* move when a customer-trust boundary or irreversible commitment is unresolved. This resolves the old "every strong answer is the same move" balance trap and the "escalation is categorically weak" calibration risk.
- **`whyItMatters` sharpened** from the generic "rarely succeed through reporting lines alone" to a concrete failure mode (engineering risk trapped inside Engineering → unowned customer/commercial/trust decisions).
- **`executive-conflict` is now cross-referenced** in `relatedScenarios` with an explicit boundary statement (peer/CEO disagreement vs. coalition-building).
- **The exact missing resource was added** — *Influence Without Authority* (Cohen & Bradford, Stanford GSB), the influence-specific source the prior review flagged as the clearest gap.
- **A fourth example (Senior Manager) was added**, so the case now ladders cleanly across all four role levels (SM → Director → VP → CTO).

## Rating

| Dimension | Score | Note |
|---|---|---|
| Realism | 5 | Four distinct, well-constrained senior binds (launch delay, QBR scope, infra cost, regulated contract), each with named costs and rejected options. |
| Balance | 4 | Now rewards both coalition-building *and* judicious escalation; the residual tilt is that the "build a durable mechanism" move still closes every example. |
| Educative Value | 5 | Signals name observable behavior; weak/strong contrasts and follow-up example answers make the evaluation logic explicit. |
| Interview Usability | 5 | Four variants gather genuinely different evidence; follow-ups expose costs and ownership; rubric separates levels cleanly. |
| Spec Quality | 5 | Complete, internally consistent, ids/paths stable; validation and coverage clean. |
| External Resources | 4 | Influence-specific gap closed; remaining strategy-tilted links are still loosely on-competency. |

## Strengths

- **The scenarios are genuinely realistic and now varied.** Reliability-vs-committed-launch, a QBR scope promise, an 18% infra cut against reliability margin, and a data-residency clause that can't yet be verified are all real senior binds. Each names a concrete cost (two cohorts slip three weeks; a roadmap theme moves a quarter; a signature slips) rather than a frictionless win.
- **Weak versions are realistic, not strawmen.** "I escalated the reliability risk to executives without options," "I asked Finance for more realistic targets," and "I told Sales and Legal Engineering could not support the language" are things competent people actually do — they expose the gap without being cartoonish.
- **Escalation is taught with nuance.** The spec now distinguishes escalation that *replaces* peer alignment (weak) from escalation that *clarifies an unresolved decision boundary after* alignment (strong), in the signal, the weak-answer red flags, and the `authority` follow-up. This is the hardest thing to calibrate in influence interviews and the spec handles it well.
- **Signals teach observable behavior** — represent other functions' constraints accurately; connect technical risk to customer/business consequence; leave behind criteria/rituals/metrics; escalate transparently at the right boundary — rather than vague "aligned stakeholders."
- **Rubric genuinely ladders by level** — adjacent teams (SM) → multiple functions (Director) → executive peers (VP) → company strategy and external commitments (CTO) — and each level now has a matching example.

## Gaps and Risks

1. **Mild residual balance tilt: the mechanism move still closes every story.** Each of the four examples ends in a durable mechanism (scorecard, commitment review, cost-ownership cadence, regulated-deal review). That is appropriate for this competency, but there is still no context where the right senior call is to accept a launch and own the residual risk *without* building new process, or to hold a principled line when no shared mechanism is reachable in the decision window. Lower priority than before, since escalation now provides the main counter-move.

2. **Resource set is still strategy-heavy relative to the competency.** `EMPOWERED`, `Shape Up`, `Escaping the Build Trap`, and `The Art of Business Value` are good books but sit under "Strategy and Execution" rather than influence-without-authority. With *Influence Without Authority* and *Crucial Conversations* now anchoring the influence group, consider trimming one of the four strategy links or sharpening each `why` to name the specific cross-functional-influence connection. The bookshelf at `obren.io/bookshelf/docs/leadership.html` remains a useful discovery source for a negotiation or stakeholder-mapping pick (linking to the canonical publisher page).

3. **Minor — `infrastructure-cost-alignment.promptVariant` references a variant string that is not in `prompt.variants`.** The example uses `"Describe a time you aligned engineering, product, finance, and customer success around a difficult **trade-off**."`, while the registered variant says `"...engineering, product, design, sales, and customer success..."`. Validation does not enforce this linkage, but the mismatch is worth aligning for consistency.

## Priority Recommendations

1. **(Resources)** Trim or re-justify one strategy-tilted link so each resource's `why` names the influence connection; optionally add one negotiation/stakeholder-mapping source.
2. **(Consistency)** Reconcile the `infrastructure-cost-alignment` `promptVariant` string with a registered `prompt.variants` entry.
3. **(Balance, optional)** Consider a rubric note acknowledging that accepting residual risk or holding a principled line — without building new process — is sometimes the correct senior move.

## No-Build Note

This review changed only `REVIEW.md`; no rebuild required. If the recommendations above are applied to `interview.json`, run:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

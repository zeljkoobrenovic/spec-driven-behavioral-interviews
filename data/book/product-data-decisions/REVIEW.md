# Review — Data-Informed Product Decisions

File: `data/book/product-data-decisions/interview.json`
Group: Senior Product Leaders
Reviewed against: `AGENTS.md` data model, validation schema, and sibling product interviews.
Data checks: `validate_interviews.py` passes (28 datasets ok); `summarize_coverage.py` lists the dataset, which now contributes 5 concrete examples and the signals Metric Literacy / Evidence Integration / Measurement Discipline / Decision Discipline.

_Updated after the interview was revised since the prior review: all three previously flagged gaps — missing external links, reversal-only examples, and a reversal-biased follow-up tree — have been addressed. See "Changes Since Last Review" below._

## Rating Scale
1 weak · 2 below bar · 3 solid · 4 strong · 5 exemplary

## Overall Assessment
A strong, well-constructed interview, now **5/5**. The spec is complete, internally consistent, and validates cleanly. It teaches a genuinely senior idea — being *data-informed, not metric-obedient* — and crucially now teaches **both directions** of that judgment: when to override a favorable metric and when to *hold* a correct decision against anecdotal pressure. Every example carries a named stakeholder, a named short-term cost (or the cost of not overreacting), and a durable measurement-system change. The `toProbeFurther` section is now present, well-grouped, and credible. There is no remaining material gap; only minor polish items remain.

## Changes Since Last Review
The prior review rated this **4/5** with three open items. The revised spec resolves all three:

1. **External resources added (was the only score-1 dimension).** `toProbeFurther.links[]` now contains 10 credible, non-Obren sources across three groups — Experimentation and Guardrails, Data-Informed Product Judgment, and Metric Quality and Product Outcomes — each with a one-sentence `why` and a `groupDescription`. This moves External Resources from **1 → 5**.
2. **Reversal monoculture fixed.** A fifth example, `noisy-feedback-held-decision` ("Noisy Feedback, Correct Metric", GPM), now models the disciplined move of *trusting valid evidence and holding the line* when objections are real for one segment but not representative. The competency definition, story anatomy, strong/weak patterns, signals, and prompts were all updated to include "defend" alongside "reverse/refine." This moves Balance from **4 → 5**.
3. **Follow-up tree no longer presupposes a reversal.** `changed-decision` is re-worded to "changed, narrowed, or held," `tradeoff-pressure` admits a hold-the-line cost, and a new `confirmed-decision` follow-up explicitly probes "when did the data confirm the original direction." A candidate whose true story is "I held against pressure" is now fully served.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 5 | Scenarios are textbook-real: engagement up but task completion down, conversion lift from low-fit churned cohorts, save-rate masking delayed churn, churn model misreading API-heavy enterprise admins, and (new) a self-serve onboarding win contested by a few loud enterprise accounts. Each has messy data, real stakeholders (Growth, Finance, Sales, board, enterprise AMs), and a visible cost. |
| Balance | 5 | Now covers quantitative literacy, qualitative integration, business/margin reality, stakeholder courage, **and** the inverse skill of defending a correct decision against anecdote. The reversal-as-virtue overfitting is resolved. |
| Educative Value | 5 | Strong/weak patterns are concrete and contrastable; weak versions are realistic ("retention was mixed, so we refined onboarding") rather than strawmen. Follow-up exampleAnswers give crisp calibration on both reversing and holding. |
| Interview Usability | 5 | Five prompt variants pull distinct evidence (including the new "hold despite noisy objections"); five follow-ups map to signals and now cover both directions; rubric separates SPM/GPM/Director cleanly. |
| Spec Quality | 5 | All required fields present; ids stable and consistent across `evaluation.signals`, `visualizations.signalMap`, `visualizations.followUpTree`, and `followUps`; the new `confirmed-decision` follow-up is wired into `followUpTree`. Rubric levels match `roleFocus`. No asset paths to break. One cosmetic nit below. |
| External Resources | 5 | 10 credible sources, three coherent groups, one-sentence `why` on each, no Obren bookshelf links, no duplicate book/article, links only in the final section. HBR "Surprising Power of Online Experiments" deliberately counterbalances the reversal bias. (Link liveness not re-verified this pass — WebFetch unavailable in session.) |

## Strengths
- **Both directions of data discipline are taught.** Four examples reverse/narrow a favorable metric; one holds a correct decision against representative-sounding but unrepresentative complaints. The signal `reversal-discipline` (display name "Decision Discipline") explicitly rewards naming the cost of *changing direction or holding the line*.
- **Metric-failure modes are taught explicitly**, not gestured at: repeated opens vs. task completion, segment/denominator effects, delayed churn counted as save, dashboard usage as a non-universal value proxy, and complaints from an excluded segment.
- **System changes are durable and specific** (90-day retained gross margin, reason-coded cancellations, segment-differentiated health scoring, account-size routing rules, pre-registered segment/retention checks) rather than "added more metrics" — and the weak answers explicitly model that filler.
- **Level differentiation is real:** SPM fixes one decision, GPM fixes how multiple funnels read evidence (including the held-decision example), Director moves portfolio investment and measurement governance.
- **External reading is curated, not padded:** experimentation rigor (Kohavi/Cambridge, Airbnb, Spotify, Booking), judgment vs. obedience (HBR, SVPG), and metric quality (Reforge, Mixpanel, Amplitude, Andrew Chen).

## Gaps And Risks
No material gaps remain. Minor polish only:

1. **`year` field inconsistency (cosmetic).** Eight links carry a `year`; `amplitude-product-metrics` and `andrew-chen-consumer-product-metrics` omit it. Add the publication/last-updated year to those two for rendering consistency, or accept that evergreen guide pages legitimately have no fixed year.
2. **Link liveness unverified this pass.** Vendor-blog URLs (Spotify Backstage, Reforge, Mixpanel, Amplitude) drift over time. Re-confirm the four vendor links resolve and that the Reforge/SVPG/HBR years still match the live pages on the next data edit, when WebFetch or a browser is available.
3. **Five examples is now on the larger side** for the catalog. This is a feature, not a problem — the fifth earns its place by covering the inverse skill — but if length ever becomes a concern, it is the natural candidate to keep over trimming, not to cut.

## Priority Recommendations
1. (Optional, cosmetic) Normalize the `year` field across `toProbeFurther.links[]` — add years to the two Amplitude/Andrew Chen entries or confirm they are intentionally omitted.
2. (Optional) On the next edit cycle, re-verify the four vendor-blog links resolve and the stated years match the live pages.
3. After any data edit, run: `validate_interviews.py`, `summarize_coverage.py`, `node --check` on both JS files, `build.py`, `smoke_static_site.py`.

## Snapshot
Realism 5 · Balance 5 · Educative 5 · Usability 5 · Spec 5 · External 5 — **Overall 5/5, ship-ready.** All prior-review gaps closed; remaining items are cosmetic.

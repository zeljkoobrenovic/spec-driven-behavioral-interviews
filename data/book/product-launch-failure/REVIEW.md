# Review

## Purpose

Per-interview review of `data/book/product-launch-failure/interview.json` ("Failed Product Launch") against the project review dimensions: realism, balance, educative value, interview usability, spec quality, and external resources.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- Group: `senior-product-leaders` (Senior Product Leaders).
- Competency: Failed Product Launch — family **Execution and Accountability**.
- Role focus: Senior PM, Group PM, Director of Product. Difficulty: advanced.
- `validate_interviews.py`: passes (28 datasets ok).
- **Four** worked example stories spanning all three levels, **five** follow-ups with strong/weak calibration answers, **four** evaluation signals, three-level rubric.
- `icon.png` exists on disk (11 KB) but is still **not wired** into `assets.icon`.
- No `toProbeFurther.links[]`.

## What Changed Since The Last Review

Recent edits to `interview.json` closed three of the five gaps the previous review flagged:

1. **Group PM level is now exampled.** Added `self-serve-onboarding-quality-drop` (GPM): two PM teams launch self-serve onboarding, signups rise but qualified conversion falls and support doubles because the flow pulls complex enterprise prospects into a simple-team experience. It rewards defining quality/harm/retention guardrails across teams and naming a deliberately-missed trial target — genuine GPM-level cross-team ownership. The rubric-without-example gap at the middle level is closed.
2. **A fourth, sunset-flavored Director story was added.** `partner-marketplace-sunset` (Director): a nine-month marketplace build paused for two quarters because buyer trust and operational readiness (security cert, support ownership, incident escalation) were never proven. It credits a disciplined stop/pause over a clever recovery narrative and exercises the widest stakeholder set (executives, revenue, partners, security, support, platform eng).
3. **The "communicate the miss without blame" thread is now elevated.** A new `communication` follow-up ("What did you communicate to executives, customers, partners, or customer-facing teams?", tests `stakeholder alignment` + `accountability`) carries calibrated strong/weak answers, and a new **Recovery Decision Quality** signal was added (now four signals, registered in coverage). The honesty-without-blame constraint is now tested, not just set up.

Two gaps from the prior review **remain** and are now more conspicuous, because this is the only dataset of 27 still missing each:

- `assets.icon` still not wired.
- No `toProbeFurther.links[]`.

## Overall Assessment

A strong, well-constructed interview that is now noticeably stronger than at the last review. The content teaches a sharp and genuinely senior idea — *shipping the agreed scope is not the same as launching a product customers understand, trust, and use* — and consistently rewards precise failure diagnosis over generic "we needed more education / better alignment" answers. With four stories the level ladder (SPM → GPM → Director) is fully exemplified, and the recovery taxonomy now spans iterate / reposition / narrow / pause / **sunset** with a worked sunset case.

The only remaining weaknesses are two data-completeness gaps that put this file out of step with its 26 sibling datasets: the icon is not wired in, and there is no external-resources list. Both are mechanical fixes that do not touch content.

## Strengths

- **Crisp central lesson.** The reflection and the recurring contrast between "shipped on time / matched requirements" and "adoption missed" make the senior distinction explicit rather than implied.
- **Concrete, multi-axis diagnosis.** Action steps and the Failure Diagnosis signal force separation of discovery, positioning, readiness, execution, and measurement failure modes — the spec teaches the taxonomy, not just the word "diagnose."
- **Strong weak-answer calibration.** "Customers needed more education, so we improved onboarding and iterated" and "the market was not ready yet" are exactly the plausible-sounding non-answers an interviewer hears; pairing them with strong versions is high educative value.
- **Recovery decision discipline — now with a signal and a worked sunset.** The iterate / reposition / narrow / pause / sunset framing with explicit opportunity cost ("accepting lower short-term upsell for lower churn risk") is reinforced by the dedicated Recovery Decision Quality signal and the partner-marketplace pause story.
- **Four genuinely different example stories across all three levels.** Trust/control miss (SPM), commercial-change-without-workflow-validation (Director), growth-quality trade-off across teams (GPM), and operational-readiness sunset (Director) exercise distinct failure modes; the prompt variants now gather meaningfully different evidence at each level.
- **Communication-without-blame is rewarded explicitly.** The new `communication` follow-up calibrates "I told leadership we'd miss the trial target on purpose" against "I shared the learnings and the new plan" — concrete honest-no-blame behavior, not a slogan.
- **Clean level progression, now fully populated.** SPM (own a launch) → GPM (coach multiple PMs, shared mechanisms) → Director (portfolio launch governance) is a real, non-overlapping ladder with at least one story per rung.

## Gaps And Risks

1. **`assets.icon` not wired (data bug).** `icon.png` (11 KB) exists in the folder but no `assets` block references it. This is now the **only** one of 27 content datasets with this gap, so the icon silently fails to render where every sibling shows one. One-line fix.
2. **No `toProbeFurther.links[]`.** The only substantive content gap, and now the **only** dataset of 27 without an external-resources list, so the final "To Probe Further" section is empty. Launch-failure has excellent canonical sources (Marty Cagan / SVPG on launch and outcomes, *Crossing the Chasm* for adoption-chasm framing, *The Lean Startup* for validated learning / pivot-or-persevere, *Escaping the Build Trap*).
3. **No `explainerComic` or per-signal/answer `aiVisual` fields.** Optional, but siblings increasingly carry them; worth noting for visual parity, not a defect.
4. **Slight evaluative tilt remains.** Diagnosis precision is the dominant rewarded behavior across signals and stories. The added sunset story and Recovery Decision Quality signal partly offset this by crediting a clean kill decision, so the balance is better than at the last review; the residual tilt is minor.

## Review Dimensions

| Dimension | Score | Notes |
| --- | --- | --- |
| Realism | 5 | On-time ship + missed adoption + multiple functions with conflicting explanations is the real shape of a launch post-mortem. The four stories (trust miss, pricing/packaging, growth-quality, marketplace sunset) are all credible senior situations with messy trade-offs. |
| Balance | 4 | Good span across discovery, GTM, pricing, growth, readiness, measurement, and now communication. Diagnosis precision is still the most-rewarded behavior, but the sunset story and Recovery Decision Quality signal now also credit a principled stop decision. |
| Educative Value | 5 | Strong/weak contrasts, the taxonomy of failure modes, calibrated follow-ups (including communication), and the systemChange mechanisms make "what good looks like" explicit and teachable. |
| Interview Usability | 5 | Prompt + four variants are easy to ask; five follow-ups expose evidence with calibrated strong/weak answers; rubric levels are distinct and each now has a worked example. Held back only by the empty resources section, which does not affect live use. |
| Spec Quality | 3 | Internally consistent, ids stable, validation passes — but the unwired icon is an actual rendering bug and the missing resources list breaks parity with all 26 siblings. |
| External Resources | 1 | No `toProbeFurther.links[]` at all. |

## Priority Recommendations

1. **Wire the icon.** Add `"assets": { "icon": "icon.png" }` to the top-level spec, then rebuild. One-line fix; clears the last remaining icon gap in the catalog.
2. **Add `toProbeFurther.links[]`.** Use the `research-external-links` skill. Strong canonical candidates, grouped:
   - *Launch & outcomes*: SVPG / Marty Cagan ("Outcomes Are Hard"; launch-readiness writing), *Escaping the Build Trap* (Melissa Perri) book page.
   - *Adoption & the chasm*: *Crossing the Chasm* (Geoffrey Moore) publisher page.
   - *Validated learning & pivot/persevere*: *The Lean Startup* (Eric Ries) canonical page.
   - *Pricing/packaging launch*: a credible monetization/packaging reference (e.g., Reforge or a pricing-strategy canonical page).
   Keep one entry per resource, each with a one-sentence `why`, all pointing to canonical non-Obren pages (the bookshelf may inspire, but do not link `obren.io`). Avoid duplicating any resource already used in `product-data-decisions` (e.g., SVPG "Outcomes Are Hard") unless the relevance note is genuinely distinct.
3. (Optional) Add `explainerComic` / answer-pattern `aiVisual` fields for visual parity, via the visual-assets workflow.

Recommendations 3 (GPM example) and 4 (communication-without-blame) from the previous review are now **done** and have been removed.

## Verification Done

- `python3 _scripts/validate_interviews.py` → ok (28 datasets).
- `python3 _scripts/summarize_coverage.py` → confirms all four signals (Launch Accountability, Failure Diagnosis, Recovery Decision Quality, Launch System Change) register; this dataset reports four concrete examples.
- Cross-checked `assets.icon` and `toProbeFurther` presence across all 27 content datasets: this file is the **only** one missing each.

After applying recommendations 1–2, re-run:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

## Ongoing Review Checklist

- [ ] `assets.icon` wired and rendering.
- [ ] `toProbeFurther.links[]` present, grouped, canonical, de-duplicated against siblings.
- [x] Group PM level has at least one worked example (`self-serve-onboarding-quality-drop`).
- [x] Honest-no-blame communication is rewarded by a signal or calibrated follow-up (`communication` follow-up + Recovery Decision Quality signal).
- [ ] Validation, coverage, build, and smoke test pass after edits.

# Review

## Purpose

Per-interview review of `data/book/executive-conflict/interview.json` ("Conflict With
Executives or Peers") against the project's realism, balance, educative-value,
interviewer-usability, spec-quality, and external-resource dimensions. This revision
re-reviews the spec after a substantial content expansion (two new example stories, a
fourth signal, follow-up `exampleAnswers`, and quantified opportunity-cost detail).

## Rating Scale

1 = poor, 2 = weak, 3 = solid, 4 = strong, 5 = excellent.

## Current Snapshot

- File: `data/book/executive-conflict/interview.json`
- Group: `book` / category `Influence and Communication`
- Family: `Influence and Communication` (3 datasets: this, `cross-functional-influence`, `executive-communication`)
- Difficulty: `advanced`; roleFocus: Senior Manager, Director, VP Engineering, CTO
- `python3 _scripts/validate_interviews.py` → passes (16 datasets, 1 group)
- `python3 _scripts/summarize_coverage.py` → no anomalies for this dataset
- No visual assets referenced (icon/comic/aiVisual all absent) — acceptable but worth noting.

## What Changed Since The Last Review

This update resolved most of the gaps the previous review raised:

- **roleFocus / rubric now consistent.** `Senior Manager` was added to `roleFocus`, so
  `roleFocus`, the four example `level`s, and the four rubric `level`s now agree
  (Senior Manager / Director / VP Engineering / CTO). *(Old gap #1 — fixed.)*
- **Strong-path balance is broadened.** Two new example stories were added: a *principled
  security refusal* (Senior Manager) where no safe alternative exists, and a
  *disagree-and-commit cost reduction* (Director) where the candidate loses the debate and
  still owns execution. The spec no longer rewards only "reframe + propose alternative +
  build process." A new `decision-integrity` signal and a reworked `strongAnswerPattern`
  explicitly reward choosing between compromise, principled refusal, escalation, and
  disagree-and-commit. *(Old gap #3 — addressed.)*
- **Finance conflict is now represented.** The new cost-reduction story is a Finance/CEO
  conflict, honoring the prompt's "finance" framing and `relatedScenarios`. *(Old gap #6 — addressed.)*
- **"Quantify" is now demonstrated, not just asserted.** The VP story names a $2.4M renewal,
  a six-week roadmap slip, support cost, and precedent for three accounts; the `risk`
  follow-up's `exampleAnswers.strong` show eng-weeks, on-call rotations, and error-budget
  framing. *(Old gap #4 — addressed.)*
- **Follow-ups now carry `exampleAnswers`.** All four follow-ups have strong/weak yardsticks.
  *(Old gap #5 — fixed.)*

One previously-flagged defect remains open (see Gaps).

## Overall Assessment

A strong, now notably broader case. The signature scenario (Sales committing engineering
to a bespoke enterprise feature) remains realistic and load-bearing, and the spec now
teaches four genuinely different senior responses across four prompt variants — one example
per variant, one per role level. The conflict-to-mechanism throughline is intact while the
spec also rewards a principled no and active disagree-and-commit, which were the main
balance gaps before. Follow-ups now ship with calibrated strong/weak answers. A single
mechanical data defect (the CTO example's `promptVariant`) still passes validation silently
and should be fixed.

Overall: **4.5 / 5** (would be 5 with the one `promptVariant` fix and optional visual assets).

## Strengths

- **Realistic, high-stakes signature scenario.** Commercially important customer,
  architecture distortion, roadmap already committed, precedent-setting decision, and the
  explicit constraint "cannot simply block revenue." A real VP/CTO bind, not polished hindsight.
- **Four distinct strong responses, one per prompt variant and role level.** Reframe-and-
  alternative (VP/Sales), options-over-positions (CTO/founder), principled refusal with no
  safe alternative (Senior Manager/security), and disagree-and-commit after losing
  (Director/Finance). This is exactly the spread the competency needs and the previous
  review asked for.
- **Strong vs. weak patterns teach concrete behavior.** Each example's `weakVersion` is a
  realistic, plausible-sounding failure that exposes the missing empathy, alternative,
  boundary, or ownership — not a strawman.
- **"Quantify" is shown.** Concrete numbers ($2.4M renewal, six-week slip, on-call
  rotations, error-budget-consuming savings) appear in both the VP story and the `risk`
  follow-up, so the most-repeated instruction is demonstrated.
- **Follow-ups expose evidence with calibration.** All four follow-ups now pair a probe with
  strong/weak `exampleAnswers`, giving interviewers a yardstick, not just a question.
- **Conflict → mechanism throughline preserved.** Deal-review checkpoint, decision criteria,
  exception register with named owners and rollback criteria reward systemic change over heroics.
- **Signals match the broadened content.** The added `decision-integrity` signal distinguishes
  compromise / principled refusal / disagree-and-commit and is wired into `signalMap`.

## Gaps And Risks

- **[Data] promptVariant mismatch (still open).** The CTO example
  (`founder-architecture-preference`) declares `promptVariant`
  "...challenge the CEO **or founder** on a technology decision," but the declared variant in
  `prompt.variants` is "...challenge the CEO, **founder, or board** on a technology decision."
  They do not byte-match, so the explorer cannot reliably tie this example to its variant.
  Make the example's `promptVariant` identical to the declared string. The other three
  examples now match their declared variants exactly.
- **[Coverage] No visual assets.** icon/comic/aiVisual are all absent. Acceptable, but every
  other dimension is now strong enough that assets would be the next quality lift.
- **[Educative, minor] Board-level conflict is named but not exemplified.** The variant and
  CTO rubric reference the *board*, but the four example stories top out at CEO/founder. Not a
  defect — the spread is already excellent — but a board-disagreement example would fully
  honor the declared variant.
- **[Balance, residual] All four examples still resolve into a durable mechanism.** This is
  largely appropriate for this competency and far less dominant than before, but the
  principled-refusal and disagree-and-commit stories both still end in a new policy/register.
  A case where the right senior move is a one-time judgment call with *no* process change
  could add nuance. Low priority.

## Review Dimensions

| Dimension | Score | Notes |
| --- | --- | --- |
| Realism | 5 | Signature scenario and all four example binds are credible senior situations. |
| Balance | 5 | Now rewards reframe, principled refusal, escalation, and disagree-and-commit; Finance and security represented. |
| Educative Value | 5 | Clear strong/weak contrast, quantification demonstrated, follow-ups carry calibrated answers. |
| Interview Usability | 5 | Four useful variants each tied to a distinct example; follow-ups expose evidence with yardsticks. |
| Spec Quality | 4 | Cross-field role consistency fixed; one `promptVariant` byte-mismatch remains. |
| External Resources | 4 | Credible, no duplicates, every link has a relevance note; a few links lean tangential to *conflict*. |

## External Resources Notes

- All seven links carry a one-sentence `why`, are credible canonical pages (no obren.io
  bookshelf links, no duplicate book/article entries), and appear only in `toProbeFurther`. Good.
- **Most on-topic:** Crucial Conversations and Never Split the Difference — directly about
  high-stakes disagreement and surfacing interests over positions.
- **Tangential to executive conflict specifically:** Good Strategy Bad Strategy, High Output
  Management, and Radical Candor are solid leadership reading but lean toward strategy /
  operating-management / feedback rather than peer-and-executive conflict. Consider trimming
  one or two and adding a conflict/negotiation-focused resource (e.g. *Getting to Yes*,
  Harvard's principled-negotiation framework) to tighten relevance.
- GOV.UK structured interviews and Amazon Leadership Principles are reasonable
  calibration/interviewing references shared across the catalog.

## Priority Recommendations

1. **Fix the CTO example `promptVariant`** to exactly match the declared
   "...CEO, **founder, or board**..." variant string. This is the only open mechanical defect.
2. *(Optional)* **Add a board-level disagreement example** to fully honor the declared
   "...CEO, founder, or board..." variant, or broaden the CTO story to reach the board.
3. *(Optional)* **Trim one tangential external link** (strategy/feedback) and add a
   negotiation-specific resource to tighten relevance to conflict.
4. *(Optional)* **Add visual assets** (icon/comic) now that the content quality justifies it.

## Per-Interview Review

- **File:** `data/book/executive-conflict/interview.json`
- **Rating:** 4.5 / 5 — realistic, broad, and highly educative after the expansion; held back
  only by one residual `promptVariant` byte-mismatch.
- **Main strengths:** credible signature scenario; four distinct strong responses (reframe,
  principled refusal, escalation, disagree-and-commit), one per prompt variant and role level;
  quantification demonstrated; follow-ups with calibrated answers; conflict-to-mechanism throughline.
- **Main risks:** CTO `promptVariant` mismatch (slips past validation); board conflict named
  but not exemplified; every example still resolves into a mechanism.
- **Recommended next edits:** item 1 (mechanical, safe) is the only must-fix; items 2–4 are
  optional polish.

## Ongoing Review Checklist

- [ ] Re-run `validate_interviews.py` and `summarize_coverage.py` after any data edit.
- [ ] After editing data, run `build.py` then `smoke_static_site.py`.
- [ ] Keep `roleFocus`, example `level`s, and rubric `level`s mutually consistent
      (validation only checks each is a known role, not cross-field agreement). *(Currently consistent.)*
- [ ] Keep every example `promptVariant` byte-identical to a declared `prompt.variants`
      entry. *(CTO example currently mismatched.)*
- [ ] Keep strong-answer paths rewarding more than one valid senior response — reframe,
      principled refusal, fast escalation, disagree-and-commit. *(Currently satisfied.)*
- [ ] Verify every `toProbeFurther` link is conflict-relevant, canonical, non-duplicate,
      and carries a one-sentence `why`.

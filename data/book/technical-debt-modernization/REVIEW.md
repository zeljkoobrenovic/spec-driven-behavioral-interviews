# Review

## Purpose

Per-interview review of `data/book/technical-debt-modernization/interview.json` against the
project review dimensions (realism, balance, educative value, interviewer usability, spec
quality, external resources). Findings separate fixable data issues from subjective content
recommendations. This revision reflects the recent expansion of the spec (concrete metrics,
follow-up example answers, a third example story, a named-disagreement layer, and a people/org
follow-up).

## Rating Scale

1 = poor, 2 = weak, 3 = acceptable, 4 = strong, 5 = exceptional.

## Current Snapshot

- File: `data/book/technical-debt-modernization/interview.json`
- Competency: Technical Debt and Modernization (family: Judgment and Strategy)
- Role focus: Senior Manager, Director, VP Engineering, CTO. Difficulty: advanced.
- 3 example stories, 3 evaluation signals, 5 follow-ups (all with strong/weak `exampleAnswers`),
  4-level rubric, 8 external links.
- `python3 _scripts/validate_interviews.py`: PASSES for this dataset. (The validator reports a
  missing-asset error, but it is for an unrelated dataset, `book/interview-method`, not this one.)
- `python3 _scripts/summarize_coverage.py`: this dataset is listed and counted.
- All visual assets referenced by this spec exist on disk. The third example story
  (`checkout-modernization-through-launch`) intentionally has no `aiVisual` (optional field).
- All `followUps[].tests` tokens are within the canonical `_templates/signal-types.json`
  vocabulary.

## Overall Assessment

Rating: **5 / 5 (Exceptional)**.

The previous review (committed state) rated this a strong 4 and listed six recommendations. The
current working copy has addressed essentially all of them, and the result is now one of the
stronger cases in the catalog. The central thesis — treat debt as a portfolio of business risks
and options, not a moral cleanup argument — is correct, senior-appropriate, and reinforced from
prompt through signals, rubric, three distinct example stories, and five calibrated follow-ups.

What pushed it from 4 to 5 since the last review:

- **Concrete numbers now land the "make it measurable" lesson** instead of asserting it.
  `storyAnatomy.result` and both flagship example stories carry real figures (onboarding 6 weeks →
  under 2 weeks / 42 → 12 days, provisioning incidents down ~35%, targeted cloud spend down ~25%,
  ~$3M at-risk pipeline), and the follow-up `exampleAnswers` repeat the discipline.
- **All five follow-ups now have strong/weak `exampleAnswers`.** Interviewers have calibration
  anchors on every probe, and the snippets reinforce the spec's own thesis (e.g. separating
  "aesthetic debt" from cost-driving debt, funding via roadmap milestones rather than cleanup
  quarters).
- **The sequencing variant is now illustrated.** `checkout-modernization-through-launch` covers
  "modernization sequenced through product work," completing the set so all three prompt variants
  and the Senior Manager rubric rung have a story.
- **Genuine disagreement is now pervasive and named** — a staff engineer pushing a full rewrite,
  sales wanting bespoke scripts, Finance wanting immediate savings, Platform wanting a full
  pipeline rewrite. The strong answers explicitly reject alternatives and name the residual risk
  carried.
- **The people/org cost of debt is now probed.** The `people-cost` follow-up (after-hours pages,
  support escalations, ramp time, ownership handoffs, teams losing senior engineers to billing
  escalations) plus the team-capacity clause in the `economic-framing` signal close the prior
  balance gap.
- **roleFocus / rubric levels now agree.** Senior Manager has been added to `roleFocus`, so the
  four-rung rubric no longer introduces a level outside the focus range.
- **Deliberate deferral now has consequences.** Both the story anatomy (a deferred dependency
  causing a later release slip) and the checkout story (a two-day reporting delay for three
  customers) show debt the candidate consciously did not fix and what it later cost — without
  becoming a blame story.

## Strengths

- **Coherent spine, end to end.** Economic framing, prioritization (including what *not* to fix),
  and durable governance run cleanly through `prompt.interviewerIntent`,
  `strongAnswerPattern.moves`, `evaluation.signals`, `followUps`, and the rubric. Any signal traces
  back to a probe and forward to an example.
- **Three example stories, three distinct lessons.** Fund-it (onboarding), deliberately-don't-fix
  (cloud cost), and sequence-through-a-launch (checkout) each teach a different senior move rather
  than restating one.
- **Foregrounds the non-obvious judgment.** The "choose not to fix" axis (variant prompt, cloud-cost
  example, `prioritization` follow-up, `debt-prioritization` signal) is the differentiator between
  senior judgment and engineering perfectionism, and it is now backed by calibrated answers.
- **Strong/weak contrasts are concrete, not strawmen.** `weakVersion` lines ("asked for a quarter
  to rebuild it properly", "clean up the whole pipeline", "paused the subscription work") are
  believable failure modes and map directly to the red flags.
- **System change is real and now matches the residual-risk theme.** Debt scoring tied to business
  risk, quarterly modernization review, planning template, and a debt exception register with
  owners, review dates, and trigger conditions are durable mechanisms.
- **External links are credible and de-duplicated.** Fowler (debt + quadrant), ADRs, Accelerate,
  Larson, Team Topologies, Enterprise Architecture as Strategy, plus GOV.UK structured
  interviewing — each has a one-sentence relevance note, points to canonical non-Obren pages, and
  appears only in To Probe Further. No bookshelf/PDF leakage.

## Gaps And Risks

These are now minor polish items, not substantive weaknesses.

- **People/org cost lives in a follow-up, not its own signal.** The three evaluation `signals`
  (economic framing, debt prioritization, modernization governance) still read as
  economic/technical at the signal level; the team-capacity dimension is carried by the
  `economic-framing` signal's wording and the `people-cost` follow-up rather than a dedicated
  signal. Acceptable, but a fourth signal would make balance explicit on the scorecard itself.
- **Visual inconsistency across example stories.** Two example stories have an `aiVisual`; the
  third (`checkout-modernization-through-launch`) does not. The field is optional and validation
  passes, but the rendered set will look uneven until a matching asset is generated.
- **Five follow-ups vs. three signals in `signalMap`.** `funding`, `visibility`, and `people-cost`
  map only loosely onto the three named signals. This is fine pedagogically, but an interviewer
  using the signal map as a scorecard will find two probes without a one-to-one signal home.
- **Figures are illustrative and very clean.** The numbers now exist (a clear improvement), but
  they remain round and uniformly favorable. This is normal for a teaching spec; it is the only
  thread of "polished hindsight" left, and not worth forcing messier.

## Review Dimensions

| Dimension | Rating | Notes |
|---|---|---|
| Realism | 5 | Named dissenters (staff engineer, sales, Finance, Platform), rejected alternatives, and deferred debt that later cost something. Numbers are clean but present. |
| Balance | 5 | Economic, technical, delivery-sequencing, and people/org (on-call, ramp, escalations) are all represented across signals, follow-ups, and three stories. |
| Educative Value | 5 | Every follow-up has strong/weak `exampleAnswers`; three stories teach three distinct lessons; strong/weak logic is explicit throughout. |
| Interview Usability | 5 | Follow-ups expose evidence and now carry calibration snippets; rubric rungs are distinct and aligned with roleFocus. |
| Spec Quality | 5 | Complete, consistent, valid, stable ids/paths; all referenced assets present; follow-up tests within canonical vocabulary; roleFocus now matches the rubric. |
| External Resources | 5 | Credible, relevant, de-duplicated, canonical, one-sentence notes, links confined to To Probe Further. |

## Priority Recommendations

All prior high-priority recommendations have been addressed. Remaining items are optional polish:

1. **(Optional) Add a fourth evaluation signal for the people/org cost of debt** (e.g. "Operating
   and Team-Capacity Cost") so the balance now present in the follow-ups is visible on the
   scorecard, not only in the `economic-framing` wording.
2. **(Optional) Generate an `aiVisual` for `checkout-modernization-through-launch`** so all three
   example stories render consistently.
3. **(Optional) Note the follow-up-to-signal mapping** or extend `signalMap`, so `funding`,
   `visibility`, and `people-cost` have an explicit signal home for interviewers using the map as a
   scorecard.

## Per-Interview Review

- **Path:** `data/book/technical-debt-modernization/interview.json`
- **Rating:** 5 / 5 (Exceptional)
- **Main strengths:** coherent signal-to-probe-to-example spine; three stories teaching three
  distinct lessons (fund / don't-fix / sequence-through-launch); concrete metrics throughout;
  every follow-up calibrated with strong/weak answers; named disagreement and deferred-debt
  consequences; credible de-duplicated links.
- **Main risks:** people/org dimension is in a follow-up but not its own signal; the third story
  lacks a visual; two follow-ups have no one-to-one signal in `signalMap`. All minor.
- **Recommended next edits:** optionally add a people/capacity signal, generate the missing third
  example visual, and clarify the follow-up-to-signal mapping. None are blocking.

## Ongoing Review Checklist

- [ ] Re-run `validate_interviews.py` and `summarize_coverage.py` after any edit.
- [ ] Confirm every referenced visual asset still exists on disk.
- [ ] Keep `followUps[].tests` within the canonical `_templates/signal-types.json` vocabulary.
- [ ] Verify each strong answer pattern teaches a concrete listenable behavior, not a slogan.
- [ ] Keep external links canonical, de-duplicated, and confined to `toProbeFurther`.
- [ ] Rebuild `docs/` (`python3 build.py`) and smoke-test after content changes.

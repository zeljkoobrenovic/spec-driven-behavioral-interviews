# Review: Failure and Accountability

File: `data/book/failure-accountability/interview.json`

## Purpose

Assess this interview spec for realism, balance, educative value, interviewer
usability, spec quality, and external resources, and separate fixable data
issues from subjective content recommendations.

## Rating Scale

1 = weak, 2 = below bar, 3 = solid, 4 = strong, 5 = exemplary.

## Current Snapshot

- Competency family: Execution and Accountability.
- Role focus: Senior Manager, Director, VP Engineering, CTO.
- Difficulty: advanced.
- **Four example stories, one per role level**: CTO migration instability,
  VP Engineering cost-savings reliability miss, Director missed quarterly goal,
  Senior Manager bulk-job customer corrections.
- Three evaluation signals, four-level rubric, four follow-ups (each with
  strong/weak `exampleAnswers`), eight external links.
- Data checks: `validate_interviews.py` passes (16 datasets); all referenced
  visual assets and `icon.jpg` exist on disk; coverage summary lists the dataset.

## What Changed Since The Previous Review

The previous review's main gaps have been addressed in the spec:

- **Senior Manager example added** (`bulk-job-customer-corrections`) and a
  **VP Engineering example added** (`cost-savings-reliability-miss`). Every level
  in `roleFocus` now has a worked story. The earlier "exampleStories skews senior"
  gap is resolved.
- **Follow-ups now carry `exampleAnswers`** (strong/weak calibration pairs on all
  four probes). The earlier usability note and recommendation are resolved.
- **Strong-answer pattern broadened** to credit "acknowledges residual cost or
  partial recovery" and "distinguishes missing controls from one-off judgment
  misses where more process would not help." The earlier single-answer-shape
  balance gap is largely resolved.
- **Weak-answer red flags broadened** to flag the clean-win-with-no-trade-off
  story and the reflexively-added-checklist anti-pattern.
- **External links cleaned up.** The two weakly relevant catalog staples called
  out previously (`manager-tools-basics`, `google-effective-teams`) are gone. The
  current list is on-topic for owning failure.

## Overall Assessment

A strong, publishable spec and noticeably improved since the last review. The
signature scenario is realistic and senior, the reflection names a specific
leadership miss rather than generic hindsight, weak patterns are concrete, the
rubric meaningfully separates levels, and the four example stories now span the
full role range with genuinely different failure modes (under-tested migration,
financial target overriding reliability, unescalated dependency risk, irreversible
bulk data change). Remaining opportunities are minor and subjective. No blocking
data issues.

## Strengths

- **One realistic story per level, with distinct failure modes.** The four
  examples are not relabeled versions of one arc: a CTO migration readiness miss,
  a VP letting a cost target outrank customer-risk segmentation, a Director who
  kept dependency risk out of planning decisions, and a Senior Manager who
  accepted sampling-based validation on an irreversible bulk job. This anchors
  what "owned well" sounds like at each scope.
- **Partial-outcome honesty is now rewarded.** Both new stories keep the residual
  cost visible (manual restoration work; a smaller savings number with restored
  capacity) instead of resolving into clean turnarounds, and the strong-answer
  pattern explicitly credits this.
- **Specific personal miss.** The reflection ("treating **executive alignment**
  as sufficient when operational readiness was not proven") teaches the exact
  failure of judgment an interviewer should listen for — not a vague "I should
  have communicated more."
- **Calibrated follow-ups.** Each probe pairs a strong and weak example answer,
  e.g. the strong "personal miss" answer owns approving a sign-off gate that used
  executive approval instead of production-readiness evidence, versus the weak
  "I probably should have pushed the team harder to test more."
- **Sharp red flags.** "The failure is too small for the level being interviewed,"
  "says they owned it but mostly describes other people's mistakes," and the new
  "adds a checklist or review reflexively without explaining which failure mode it
  prevents" are exactly the traps for this competency.
- **Level-differentiated rubric.** Senior Manager (team execution controls) →
  Director (coordination/readiness mechanisms) → VP (org failure before execs and
  customers) → CTO (governance, risk posture, external communication) reads as
  genuinely escalating scope.

## Gaps And Risks

- **`dare-to-lead` is the softest link (external resources).** It sits under a
  People Leadership group description and is the least specific to owning failure
  on an otherwise tight list (SRE postmortem, Etsy blameless, AWS COE, Restorative
  Just Culture, Scapegoats at Work). Keep it only if its `why` (courage and
  ownership without defensiveness) stays clearly tied to accountability; otherwise
  swap for a more failure-specific resource.
- **Three links overlap with `crisis-leadership`.** SRE postmortem culture, Amazon
  Leadership Principles, and the GOV.UK structured-interview guide appear in both
  cases. This is acceptable for catalog-wide staples, but worth tracking so the
  two cases' reading lists do not fully converge.
- **Overlap with `crisis-leadership` is acceptable but worth a guard rail.** Both
  use an operational-incident scenario (crisis uses a live "major outage"; this
  uses an under-tested migration). They are correctly differentiated — crisis
  tests in-the-moment decision quality, this tests post-failure ownership and
  systemic change — but authors editing either should keep the migration vs.
  live-incident framing distinct so the cases do not converge.
- **Balance is now good, not perfect.** Speed of disclosure and principled
  escalation are present in the follow-up example answers but are not yet first-
  class moves in the strong-answer pattern. Minor; the "not adding process when it
  was a one-off judgment call" nuance is now covered.

## Review Dimensions

| Dimension | Score | Notes |
| --- | --- | --- |
| Realism | 5 | Messy constraints, customer visibility, executive pressure, irreversible-change risk, credible partial recoveries. |
| Balance | 4 | Four distinct failure modes across levels; partial outcomes and "don't add process reflexively" now credited. Speed/escalation could be promoted to explicit moves. |
| Educative Value | 5 | Strong/weak patterns, red flags, signals, and now calibrated follow-up answers make the evaluation logic explicit. |
| Interview Usability | 5 | Variants shift evidence; follow-ups expose ownership and carry strong/weak calibration snippets; one example per level. |
| Spec Quality | 5 | Validates clean; ids/paths stable; all assets present; aligned with templates. |
| External Resources | 4 | On-topic and credible; `dare-to-lead` is the softest fit and three links overlap `crisis-leadership`. |

## Priority Recommendations

1. **Review the `dare-to-lead` link (subjective).** Confirm its accountability
   relevance is sharp, or replace it with a more failure-specific resource. The
   bookshelf at `https://obren.io/bookshelf/docs/leadership.html` is a discovery
   source; link the canonical publisher page, not the bookshelf note, and avoid
   duplicating an existing entry.
2. **Optionally promote speed-of-disclosure / principled-escalation (subjective).**
   These appear in follow-up example answers; consider surfacing one as an explicit
   move in `strongAnswerPattern.moves` so the rubric does not implicitly treat
   control-creation as the dominant signal.
3. **Keep the migration vs. live-incident framing distinct from
   `crisis-leadership` (maintenance).** Re-check on any future edit to either case.

## Data Issues (Fixable)

None blocking. `validate_interviews.py` passes, all visual assets and `icon.jpg`
resolve, and the manifest entry matches the `id`.

## Ongoing Review Checklist

- Re-run `validate_interviews.py` and `summarize_coverage.py` after edits.
- Keep migration (this case) vs. live-incident (`crisis-leadership`) framing
  distinct, and watch the three shared links so the two reading lists do not fully
  converge.
- Verify every `toProbeFurther` link is specifically relevant to owning failure,
  not a generic leadership staple, and avoid duplicate book/article entries.
- If visual assets are regenerated, rebuild `docs/` and run the smoke test.

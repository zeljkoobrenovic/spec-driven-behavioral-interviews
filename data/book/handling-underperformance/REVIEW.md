# Review: Handling Underperformance

File: `data/book/handling-underperformance/interview.json`
Reviewed: 2026-06-06 (updated after revision)
Reviewer skill: `review-behavioral-interview`

## Purpose

Assess this single interview for realism, balance, educative value, interviewer
usability, spec quality, and external-resource quality, and separate fixable
data issues from subjective content recommendations.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- Validation: passes (`validate_interviews.py` reports `ok: data/book`, 16 datasets).
- Coverage: registered under `People Leadership` (3 datasets in family).
- Difficulty: `advanced`. Role focus: Senior Manager → CTO.
- Assets: all 11 referenced images exist; no orphan asset files; icon present.
- Example stories: 3. Follow-ups: 4 (all with `exampleAnswers`). Signals: 3.
  External links: 8 (no dup ids).

## What Changed Since The Prior Review

The prior pass rated this case **3.0/5 — adequate but under-built for its
family**. The revision addresses nearly every priority recommendation:

1. **Measurable outcomes added.** `storyAnatomy.result` now carries concrete
   anchors: cross-team commitment misses 4 → 1, decision lead time 9 → 2 days,
   skip-level confidence 3.1 → 4.0, escalation volume halved, and an explicit
   six-week roadmap slip. Each example story carries its own before/after signal.
2. **`exampleAnswers` (strong + weak) added to all four follow-ups**, mirroring
   `building-leadership-teams`. This was the highest-leverage usability gap and
   it is fully closed; the snippets are specific and calibrate a 3 from a 5.
3. **Rejected alternatives and residual cost are now explicit** in every story
   ("reject an immediate exit … reject another vague quarter," "one delayed
   roadmap milestone and a frustrated peer lead," migration "slows by four
   weeks"). The polished-hindsight smell is gone.
4. **A third example story** (`talented-director-corrosive-behavior`, VP level)
   now exercises the toxic-but-talented case, breaking the single
   coach-then-reassign arc and testing the competency's own stated distinction
   between skill gap, role mismatch, motivation, and harmful behavior.
5. **Rubric sharpened.** Each level now names a judgment shift, not just wider
   scope (Director changes scope before teams absorb repeated misses; VP signals
   what behavior is tolerated; CTO weighs legal/HR risk, culture, and cost of
   delay).
6. **Prompt variants reconciled.** A fourth interviewer intent and a third
   prompt variant were added for the harmful-behavior angle; each example story's
   `promptVariant` now maps to a declared variant rather than repeating the
   primary prompt.
7. **External link refreshed.** `Radical Candor` replaces the prior adjacent
   pick, putting a direct feedback-model resource on the core topic; the link
   set stays deduped and canonical.

## Overall Assessment

**Strong, well-built, and now at parity with its family (4.0/5).** The spec is
complete, internally consistent, and passes every required check. It teaches not
only the *shape* of a good answer but the *texture* — measurable outcomes, named
rejected alternatives, acknowledged residual cost, and per-follow-up calibration
snippets — that lets an interviewer separate a 3 from a 5. The three stories now
span the three failure modes the competency claims to distinguish: capability
that has not scaled, a role-design mistake, and high output paired with corrosive
behavior.

The remaining gap is narrow and largely cosmetic relative to the substance.

## Strengths

- **Correct, well-scoped competency** with genuine senior insight ("compassion
  without clarity prolongs stress"), now reinforced by the harmful-behavior story
  that separates high output from acceptable leadership behavior.
- **Measurable, credible outcomes** at both the `storyAnatomy` and example-story
  level, including an honest cost (six-week slip) alongside the wins.
- **Calibration snippets on every follow-up.** The strong/weak `exampleAnswers`
  turn each probe into a teaching moment and are specific, not generic.
- **Three root-cause-distinct stories** (capability, role-design error, corrosive
  behavior) that exercise different judgment, not the same arc three times.
- **Specific weak-answer red flags** ("Confuses high output with acceptable
  leadership behavior," "Presents a clean win without naming the cost").
- **Clean spec quality.** Stable ids; all visual paths resolve; signalMap /
  followUpTree / timeline consistent with their source arrays.
- **Credible, non-duplicated external links** anchored to canonical publisher
  pages.

## Gaps And Risks

1. **Third story has no `aiVisual` (minor, consistency).** The two original
   stories carry an `assets/generated/example-stories/*.jpg`; the new
   `talented-director-corrosive-behavior` story has none. This is permitted by
   the schema and validation passes, but it leaves the strongest, most
   differentiated story visually unsupported relative to its siblings. Either
   generate a matching visual or accept the inconsistency deliberately.
2. **CTO rubric level remains the least operational.** It now names legal/HR
   risk, culture, succession, and cost of delay — a real improvement — but still
   leans on enumeration rather than a single distinguishing judgment the way the
   Director and VP rows do. Lowest-priority refinement.
3. **Motivation as a root cause is named but not storified.** Stories cover skill
   gap, role mismatch, and harmful behavior well; a pure *motivation* failure
   (disengagement, checked-out senior leader) is referenced in the action list
   and follow-ups but has no dedicated story. Optional, since three stories
   already carry the case.
4. **Link fit, minor.** The set is strong and on-topic; a dedicated
   performance-management / "managing out with dignity" resource would still
   serve the core topic more directly than the general-management entries, though
   `Radical Candor` and `The No Asshole Rule` now cover the feedback and
   harmful-behavior angles well.

## Review Dimensions

| Dimension          | Score | Note |
|--------------------|-------|------|
| Realism            | 4     | Setups plausible; resolutions now carry rejected paths and real cost (slip, peer fallout). |
| Balance            | 4     | Three distinct root causes incl. corrosive behavior; only pure-motivation case absent. |
| Educative Value    | 4     | Measurable outcomes plus strong/weak calibration on every follow-up. |
| Interview Usability| 4     | Variants now map to stories; `exampleAnswers` make probes self-calibrating. |
| Spec Quality       | 4     | Complete, consistent, valid; only the third story's missing visual is off. |
| External Resources | 4     | Credible, deduped, canonical; one slot could go more on-core-topic. |
| **Overall**        | **4** | Sound foundation, now built out to family standard. |

## Priority Recommendations

Ordered by leverage. All are content edits to `interview.json`; rerun the
required checks after any change.

1. **Add an `aiVisual` to `talented-director-corrosive-behavior`** (or record a
   deliberate decision to leave it imageless) so the three stories are
   visually consistent. Requires `_scripts/generate_*` and a rebuild.
2. **Give the CTO rubric row one distinguishing judgment** rather than an
   enumeration, matching the Director/VP rows.
3. *(Optional)* **Add a pure-motivation story** (a disengaged, checked-out senior
   leader) to fully exercise every root cause the competency names.
4. *(Optional)* **Swap one general-management link** for a dedicated
   performance-management / managing-out resource on the core topic.

## Per-Interview Review

- **Path:** `data/book/handling-underperformance/interview.json`
- **Rating:** 4/5 (strong; built out to People Leadership family standard).
- **Main strengths:** correct competency framing; measurable outcomes with honest
  cost; three root-cause-distinct stories incl. corrosive behavior; calibration
  `exampleAnswers` on every follow-up; clean, valid spec.
- **Main risks:** third story lacks a visual; CTO rubric row still enumerative;
  pure-motivation case not storified.
- **Recommended next edits:** item 1 (third-story visual), then item 2 (CTO
  rubric); items 3–4 optional.

## Ongoing Review Checklist

- [x] `python3 _scripts/validate_interviews.py`
- [x] `python3 _scripts/summarize_coverage.py`
- [x] Every example story names a measurable outcome and a rejected alternative.
- [x] Every follow-up that benefits from calibration has `exampleAnswers`.
- [x] Stories collectively cover skill gap, role mismatch, *and* harmful behavior.
- [x] Rubric levels differ in judgment, not only scope.
- [ ] Every example story has a matching visual asset (third story still missing).
- [x] All referenced visual assets exist; no orphans; no duplicate link ids.
- [ ] `python3 build.py && python3 _scripts/smoke_static_site.py` after data edits.

# Review — Culture Change

## Purpose
Evaluate `data/book/culture-change/interview.json` for realism, balance, educative
value, interviewer usability, spec quality, and external-resource quality, and
separate fixable data issues from subjective content recommendations.

## Rating Scale
1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot
- Validation: `python3 _scripts/validate_interviews.py` → **ok** (16 datasets, 1 group).
- Coverage: registered under People Leadership. Difficulty `advanced`.
- Example stories: **4** (was 2) spanning incidents, decision-rights, and remote/docs culture.
- Assets: `icon.jpg`, the comic, all answer-pattern and signal visuals, and the
  two original story visuals exist. The **two newer stories**
  (`remote-documentation-norms`, `founder-driven-decisions-to-ownership`) have
  **no `aiVisual`** yet (asset-optional, so validation passes).
- Role focus: Senior Manager, Director, VP Engineering, CTO. Competency family: People Leadership.

## What Changed Since The Last Review
This revision resolved almost every issue the prior review raised:
- **promptVariant mismatch — fixed.** All four `exampleStories[].promptVariant`
  strings now match a declared `prompt.variants` entry verbatim.
- **Missing `exampleAnswers` — added.** All four follow-ups
  (`diagnosis`, `incentives`, `modeling`, `sustained`) now carry strong/weak
  calibration snippets, matching the sibling-interview convention.
- **Narrow archetype — broadened.** Two new stories instantiate the previously
  unexemplified `relatedScenarios`: `founder-driven-decisions-to-ownership`
  (decision rights) and `remote-documentation-norms` (documentation in a remote
  org). The case no longer reads as "culture change = ops excellence."
- **No resistance / partial-failure path — added.** Both new stories show an
  explicit early miss and correction (over-heavy template simplified;
  over-delegation corrected with a shared-contract review). `storyAnatomy.action`,
  `strongAnswerPattern.moves`, and `weakAnswerPattern.redFlags` now reward
  handling legitimate pushback and learning from it.
- **Resource clustering — trimmed.** `team-topologies` and one Erin Meyer title
  (`The Culture Map`) were removed; the Google re:Work link now points to the
  canonical `understanding-team-effectiveness` guide rather than a marketing path.

## Overall Assessment
A strong, now-mature case. It still teaches the central idea cleanly — culture
changes when **incentives, rituals, and leadership signals** change together, not
when slogans change — and the previously-flagged gaps in balance, calibration, and
data consistency are closed. The strong/weak contrast is concrete, the signals are
behavior-anchored, and the four stories exercise genuinely different evidence. The
only residual items are a small consistency gap (two stories lack visuals) and a
mild reading-list group imbalance.

**Overall: 4.5 / 5** (up from 4 / 5).

## Strengths
- **Sharp, realistic premise.** "Celebrating last-minute saves while prevention is
  invisible" remains a widely-felt senior failure mode, with a credible cost story.
- **Teaches behavior, not vocabulary.** The weak patterns ("values posters",
  "all-hands messaging only", "cannot explain what incentives changed") name the
  exact tells an interviewer should listen for.
- **Four distinct archetypes.** Incidents/heroics, blameful reviews, remote-docs,
  and founder-driven decisions each test different evidence — no answer repeats.
- **Honest about failure.** Two stories show an early mechanism that went too far
  and was corrected; the spec now rewards candor over polished hindsight.
- **Strong follow-up calibration.** Every probe has strong/weak `exampleAnswers`
  with specific evidence (reopen rates, ADRs, escalation paths) versus vague tells.
- **Good level laddering.** The rubric moves cleanly from team norms (Senior
  Manager) → cross-team rituals (Director) → org systems (VP) → company technology
  culture tied to strategy (CTO). Levels stay distinguishable.

## Gaps And Risks
1. **[Consistency — minor] Two stories lack `aiVisual`.**
   `remote-documentation-norms` and `founder-driven-decisions-to-ownership` have no
   `aiVisual`, while the first two stories do. Visuals are asset-optional and
   validation passes, but the mixed state is visible in the explorer (two stories
   render an image, two do not). Either generate the two missing story visuals or
   accept the inconsistency deliberately.
2. **[Balance — minor] Reading-list group still tilts to one bucket.**
   Four of six links sit in "Culture and Organizational Design." It is no longer
   author-clustered (only one Erin Meyer title remains), so this is cosmetic, but
   the list is light on the failure/learning and interviewing buckets relative to
   how much the case leans on incident-review and calibration behavior.
3. **[Resources — verify] Google re:Work URL.** The link now uses the canonical
   `rework.withgoogle.com/en/guides/understanding-team-effectiveness` path. Worth a
   live confirmation that it still resolves (re:Work has migrated URLs before). Not
   verified here — live fetch not permitted.

## Review Dimensions
| Dimension | Score | Notes |
|---|---|---|
| Realism | 5 | Premise and costs ring true; resistance and partial-failure texture now present in two stories. |
| Balance | 4 | Four archetypes (ops, decision-rights, docs, blameless reviews); reading list still tilts to one group. |
| Educative Value | 5 | Weak-pattern tells, behavior-anchored signals, and per-probe `exampleAnswers` teach exactly what to listen for. |
| Interview Usability | 5 | Clean follow-up tree, distinguishable ladder, calibration snippets on every probe. |
| Spec Quality | 4 | Complete and internally consistent; only the two missing story visuals keep it from 5. |
| External Resources | 4 | Credible sources, clear `why` notes, de-clustered; mild group imbalance and one URL worth verifying. |

## Priority Recommendations
1. **Generate the two missing story visuals** (or intentionally accept four-story
   asymmetry) so the explorer renders consistently across all `exampleStories`.
2. **Optionally rebalance one reading-list link** toward the
   "Failure, Incidents, and Learning" or "Interviewing and Calibration" buckets to
   match where the case actually spends its evidence weight.
3. **Verify the Google re:Work link** resolves to the canonical guide.

## Per-Interview Review
- **File:** `data/book/culture-change/interview.json`
- **Rating:** 4.5 / 5 — strong, internally consistent, high educative value; prior gaps closed.
- **Main strengths:** sharp realistic premise; behavior-anchored weak patterns;
  four distinct example stories; per-probe calibration; honest failure/correction beats.
- **Main risks:** two newer stories lack visuals; reading list tilts to one group.
- **Recommended next edits:** generate the two missing story visuals → optionally
  rebalance one link → verify the re:Work URL.

## Ongoing Review Checklist
- [x] `exampleStories[].promptVariant` strings each match a `prompt.variants` entry verbatim.
- [x] High-value probes carry `exampleAnswers` with realistic strong/weak contrast.
- [x] Examples span more than one culture-change archetype (ops, decision-rights, docs, blameless reviews).
- [x] At least one story shows legitimate resistance, slowdown, or partial failure + correction.
- [ ] All `exampleStories[]` carry an `aiVisual`, or the asymmetry is deliberate.
- [ ] `toProbeFurther.links[]` group distribution matches the case's evidence weight; each link has a distinct, on-topic `why`.
- [ ] After any data edit: re-run validate, coverage, build, and smoke checks.

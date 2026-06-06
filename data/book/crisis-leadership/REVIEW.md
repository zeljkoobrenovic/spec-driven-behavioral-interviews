# Review — Crisis Leadership

File: `data/book/crisis-leadership/interview.json`
Reviewed: 2026-06-06 (updated after revision)

## Purpose

Assess the `crisis-leadership` interview spec for realism, balance, educative value,
interviewer usability, spec quality, and external resources, and separate
fixable data bugs from subjective content recommendations.

## Rating Scale

1 = unusable, 2 = weak, 3 = acceptable, 4 = strong, 5 = exemplary.

## Current Snapshot

- `validate_interviews.py`: passes (all 16 datasets).
- `summarize_coverage.py`: this dataset now contributes **4 concrete example stories**
  (one of only two datasets at that depth) and signals Calm Structure / Communication
  Clarity / Decisive Escalation / Operational Learning.
- Role focus: Senior Manager, Director, VP Engineering, CTO. Difficulty: advanced.
- Story shape (Situation → Task → Action → Result → Reflection → System Change) is complete.

## What Changed Since The Last Review

The revision resolved nearly every prior recommendation:

1. **Asset-key bug fixed.** The icon is now declared correctly as
   `"assets": { "icon": "icon.png" }` (the previous empty-string key that silently
   disabled the icon is gone). The icon now resolves.
2. **People-crisis coverage added.** Two new example stories were added:
   `feature-shutdown-data-risk` (Senior Manager) and `post-layoff-trust-reset`
   (Director). The layoff/reorg story matches the third prompt variant and
   `relatedScenarios`, which the spec previously named but never demonstrated.
3. **Decisive-escalation balance added.** A new `decisive-escalation` signal was
   introduced, plus strong-pattern moves and follow-up calibration ("act before
   complete information", escalation thresholds, reversibility). The spec no longer
   rewards only structure-and-calm.
4. **Rubric levels sharpened.** Each level now differentiates by *what it owns*
   (SM owns the room; Director owns cross-team coordination; VP owns
   organizational/executive narrative; CTO owns trust and risk governance), rather
   than blurring on scope alone.
5. **Follow-ups now carry strong/weak calibration answers** spanning both operational
   and people-crisis branches, which materially raises usability.

Remaining open items are minor (see below).

## Overall Assessment

A strong, well-structured crisis interview that now correctly spans the full scope it
claims: operational incidents, security/trust events, **and** people crises
(layoff/reorg). It rewards both the calm-structure signal *and* decisive escalation
under incomplete information, and converts each crisis into durable system change.
The strong/weak contrasts are crisp, the follow-ups force evidence over opinion, and
the four example stories are genuinely distinct across level and crisis type.

Overall: **4.5 / 5** (up from 3.5). The remaining gaps are polish, not defects.

## Strengths

- **Full-scope coverage.** Operational outage, billing/data-risk feature shutdown,
  security token exposure, and post-layoff trust reset each pull a different
  competency mix (recovery trade-offs, business trade-off under uncertainty,
  cross-functional/legal containment, people trust + sequencing). None is interchangeable.
- **Balanced signal set.** Calm Structure, Communication Clarity, Decisive Escalation,
  and Operational Learning together reward both *building structure* and *acting before
  structure exists* — the prior structure-only bias is gone.
- **Clean strong-vs-weak contrast.** Weak versions ("joined the bridge, helped debug,
  sent updates whenever we learned something new"; "told managers to support their teams
  and focused everyone on moving forward quickly") are realistic, not strawmen, and
  expose the precise gap.
- **Follow-ups expose evidence, with calibrated answers.** Each probe carries strong/weak
  example answers covering both operational and people-crisis paths ("What did you refuse
  to say because it would have been falsely reassuring?"), which is hard to fake and easy
  for an interviewer to score.
- **Rubric reads as a real ladder.** Levels now differ by ownership, not just blast radius.
- **External resources are credible and well-noted.** Google SRE (Managing Incidents,
  Incident Response, Postmortem Culture), the Atlassian handbook, GOV.UK structured
  interviewing, and Amazon Leadership Principles are canonical; each has a one-line `why`;
  no duplicate book/article links.

## Gaps And Risks

### Data / spec (objective)

1. **No remaining data bugs.** `assets` key is correct; validation passes; ids, paths,
   signal references, and visualization arrays are consistent.

2. **Generated visuals are absent — LOW.** All four signals carry empty
   `strongAiVisual` / `weakAiVisual`, `explainerComic` is `""`, and the previously
   generated images under `assets/generated/` have been removed from the working tree.
   This is valid and harmless (the validator only checks asset paths when present), but
   the dataset has no signal visuals or comic while several siblings do. Either regenerate
   via `_scripts/generate_*` or leave intentionally — it is a coverage gap, not a defect.

### Content / balance (subjective)

3. **Two `toProbeFurther` books remain a soft fit — LOW.** *Turn the Ship Around!* and
   *Leadership Is Language* (both Marquet) are excellent, but their `why` notes
   ("ownership close to the work", "language shapes tempo") are adjacent rather than
   crisis-specific, and they double up on one author. A reader would arguably be better
   served by one incident-leadership-specific human source (a published incident
   retrospective, or a chapter on decision-making under uncertainty) than two adjacent
   leadership-philosophy books. Low priority; not wrong as-is.

4. **People-crisis signal language is implicit — LOW.** The four signals are framed to
   stretch across both operational and people crises (Calm Structure now mentions
   "inconsistent manager messages"), which works, but an interviewer scoring a pure
   layoff story leans on the example-answer text rather than the signal definitions
   themselves. Optional: add a people-crisis cue to one signal's `weak` line. Minor.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 5 | Messy, time-pressured, uncertain root cause, irreversible/legal pressure, and a genuinely hard people-crisis. Credible weak answers throughout. |
| Balance | 4 | Now rewards both structure/calm and decisive escalation, across operational, security, business, and people crises. |
| Educative Value | 5 | Concrete strong/weak moves, red flags, and calibrated follow-up answers teach the listenable behavior, not platitudes. |
| Interview Usability | 5 | Follow-ups force evidence and ship strong/weak calibration; rubric reads as a real ownership ladder. |
| Spec Quality | 5 | Complete, internally consistent, stable ids/paths; no remaining bugs; validation passes. |
| External Resources | 4 | Credible, well-noted, no dupes; two Marquet books remain a soft, author-doubled fit. |

## Priority Recommendations

1. (Optional, polish) Swap one Marquet book for an incident-leadership-specific human
   source to tighten relevance and avoid author doubling.
2. (Optional, parity) Regenerate signal visuals / comic via `_scripts/generate_*` for
   parity with sibling datasets, or accept the gap intentionally.
3. (Optional, minor) Add a people-crisis cue to one signal's `weak` definition so a
   layoff/reorg story is scorable from the signal text alone.

No required edits remain; the prior data bug and the main balance/scope/calibration
gaps are resolved.

## Verification After Edits

After changing interview data, run:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

(REVIEW.md-only changes need no build.)

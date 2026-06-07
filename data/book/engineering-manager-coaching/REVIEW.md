# Review

## Purpose

Per-interview review of `data/book/engineering-manager-coaching/interview.json`
("Coaching and Developing Engineers") against the project review dimensions:
realism, balance, educative value, interview usability, spec quality, and
external resources.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- File: `data/book/engineering-manager-coaching/interview.json`
- Competency: Coaching and Developing Engineers (family: People Leadership)
- Role focus: Engineering Manager, Senior Engineering Manager
- Difficulty: intermediate
- Example stories: **4** (EM x2, Senior EM x2)
- Follow-ups: **5**, all with strong/weak calibration answers
- Evaluation signals: **4**; rubric levels: 2
- `validate_interviews.py`: passes (28 datasets ok)
- `summarize_coverage.py`: test tags used here all map to the canonical
  `_templates/signal-types.json` vocabulary by `name` (judgment, measurement,
  ownership, influence, decision quality, risk judgment, accountability,
  reflection)
- `toProbeFurther.links[]`: **present (8 links)**, grouped under "People
  Leadership and Feedback" and "Engineering Management and Career Growth"

## Change Since Last Review

The two open items from the prior review are now closed, and the interview has
grown materially:

- **External resources added (primary gap resolved).** `toProbeFurther.links[]`
  now ships 8 grouped, annotated links, each with a credible `source`, `type`,
  and one-sentence `why`. All are canonical and non-Obren (Google re:Work,
  O'Reilly, Stripe Press, StaffEng, Radical Candor, Resilient Management,
  Manager Tools). No duplicate book/article entries. **External Resources moves
  from 1 to 5.**
- **Fourth example story added (optional recommendation taken).**
  `talented-tech-lead-peer-friction` (Senior EM, "a coaching plan that did not
  work the first time") adds a genuine setback-and-partial-recovery arc and a
  non-clean outcome: not promoted that cycle, readiness kept open pending stable
  behavior across forums. This broadens outcome diversity beyond promotion.
- **Fifth follow-up added.** `setback-boundary` ("what did you do when the
  coaching plan hit resistance or did not work?") directly probes the new story
  and tightens the resistance/boundary line of inquiry.
- **Evaluation deepened.** Now 4 signals (added `boundary-judgment`), an extra
  prompt variant, and a richer `systemChange` list (calibration log, readiness
  checklists, onboarding diagnostic).

## Overall Assessment

A strong, now essentially complete interview — fully valid on spec and complete
on content, including external resources. It teaches a clear, opinionated model
of good coaching: diagnose before prescribing, pair direct feedback with
tailored support, create bounded real opportunity, and calibrate growth against
observable evidence rather than effort or visibility. The weak-answer patterns
are realistic and recognizable, and the strong/weak follow-up answers do real
calibration work. With the new tech-lead story, the catalog now shows a coaching
arc that visibly fails on the first attempt and recovers without lowering the
bar — the most educative shape in the set.

No material gaps remain. Remaining notes are minor labeling/polish judgments.

## Strengths

- **Realism (5).** The signature example (strong implementer who waits for the
  manager to coordinate dependencies and surface risk) is a genuine, common
  next-level gap, not polished hindsight. Constraints are honest: supportive
  without promising promotion, specific enough to act on, and not putting a real
  project at unmanaged risk. The four stories cover distinct, realistic shapes
  (next-level IC, struggling new hire, high-performer-to-staff, talented tech
  lead with peer friction).
- **Balance (5).** Avoids the trap of rewarding only one behavior. It values
  support *and* directness, opportunity *and* risk bounding, promotion *and*
  honest "not yet." The high-performer story raises the altitude correctly for
  Senior EM by coaching the manager, not just the engineer; the tech-lead story
  distinguishes sponsorship from lowering the bar for a high-output but
  trust-eroding person. The rubric makes the level distinction explicit, and the
  spec explicitly guards against "visibility theater."
- **Educative value (5).** Concrete operating mechanisms throughout: dependency
  closure, written-update quality, peer-feedback shift, risks-surfaced-before-
  delays, "promote only after two cycles of evidence," pause-and-repair on a
  failed facilitation attempt. The weak versions are plausible and expose
  exactly what is missing (vagueness, no risk boundary, no evidence). This
  teaches what to listen for, not just what to praise.
- **Interview usability (5).** Five variants meaningfully change the evidence
  gathered (significant growth vs. struggling engineer vs. difficult feedback
  vs. high-performer next level vs. a plan that failed first). Follow-ups are
  non-generic and probe diagnosis, resistance, risk bounding, evidence, and the
  setback/boundary decision. Strong/weak example answers give an interviewer a
  fast calibration anchor.
- **Spec quality (5).** Complete against the data model, internally consistent
  (signal ids match `signalMap`, follow-up ids match `followUpTree`, story
  `level` values match role focus), and passes validation. Test tags match the
  canonical vocabulary by `name`. Bold-phrase usage is appropriately sparing.
- **External resources (5).** Eight credible, canonical links with clear
  per-entry relevance notes, sensible grouping, and no duplicate book/article.

## Gaps And Risks

- **Difficulty label vs. content altitude (minor).** Marked `intermediate`, but
  the Senior EM "coach the manager / cross-team RFC adoption" and tech-lead
  trust-repair material is closer to advanced. The level split is handled
  correctly in the rubric, so this is a labeling nuance, not a content defect —
  acceptable, but worth a conscious decision.
- **Outcome diversity (very minor, mostly addressed).** Stories now span
  promotion, ramp-with-open-outcome, and not-promoted-this-cycle. A story where
  coaching correctly concludes in a role refocus or an honest "not the right
  fit" exit (referenced in `result` and `relatedScenarios` but not shown as an
  example) would be the last remaining outcome shape. Optional.

## Review Dimensions

| Dimension           | Score | Notes |
|---------------------|-------|-------|
| Realism             | 5     | Credible gaps, honest constraints, no conflict-free hindsight; setback story added |
| Balance             | 5     | Support vs. directness vs. risk all rewarded; sponsorship vs. bar guarded |
| Educative Value     | 5     | Concrete mechanisms, sharp weak/strong contrasts, a visible first-attempt failure |
| Interview Usability | 5     | Five variants and five follow-ups gather distinct evidence |
| Spec Quality        | 5     | Complete, consistent, passes validation |
| External Resources  | 5     | 8 canonical, annotated, grouped links; no duplicates |

## Priority Recommendations

1. **Confirm the `intermediate` difficulty label** is intentional given the
   Senior EM and tech-lead altitude, or nudge to advanced (low effort; the
   rubric already does most of the level work).
2. **Optional:** add a fifth example story with a role-refocus or honest-exit
   outcome to complete the decision-outcome spectrum.

## Verification

This update changed only `REVIEW.md`, so no build is required. If the interview
data itself is edited, run:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

## Ongoing Review Checklist

- [x] `toProbeFurther.links[]` present, grouped, each with a one-sentence `why`
- [x] Links canonical (non-Obren), credible, no duplicate book/article
- [ ] Difficulty label matches content altitude
- [ ] Outcome diversity beyond promotion: refocus / honest exit example added
- [x] `validate_interviews.py` and `summarize_coverage.py` pass after edits

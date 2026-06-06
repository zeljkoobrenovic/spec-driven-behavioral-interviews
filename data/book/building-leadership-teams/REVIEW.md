# Review — Building Leadership Teams

File: `data/book/building-leadership-teams/interview.json`
Group: People Leadership
Date: 2026-06-06 (updated after edit pass)

## Purpose

Assess this single interview spec for realism, balance, educative value,
interviewer usability, spec quality, and external-resource quality, and separate
fixable data issues from subjective content recommendations.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Snapshot

- Validation: `validate_interviews.py` passes (16/16 datasets).
- Coverage: `summarize_coverage.py` clean; this dataset now contributes 3
  concrete example stories (was 2).
- 11 referenced visual assets exist on disk (icon, comic, 2 answer-pattern,
  2 example-story, 6 signal images). The new third example story
  (`failed-acting-manager-promotion`) intentionally has no `aiVisual`.
- All five follow-ups (now including `decisive-change`) carry strong/weak
  `exampleAnswers`. `followUpTree`, `signalMap`, and `timeline` ids all resolve.
- Structure remains complete: competency, prompt, scenario, storyAnatomy,
  exampleStories, strong/weak answer patterns, followUps, evaluation,
  visualizations, practiceTemplate, relatedScenarios, toProbeFurther.

## What Changed Since The Last Review

This pass evaluates edits that directly target the four priority
recommendations from the prior review, plus a fifth improvement:

- **Measurable + partial-failure texture (rec #1).** `storyAnatomy.result` now
  names proxy metrics (commitment misses 5→1, manager-effectiveness pulse
  3.2→4.0, two of three openings with ready successors). A third example story,
  *Failed Acting Manager Promotion*, models a promotion that backfired and was
  rolled back — the rejected-alternative / partial-failure texture the spec
  previously lacked.
- **Rubric / roleFocus level alignment (rec #2).** `roleFocus` now leads with
  "Senior Manager", matching the rubric floor and the new example story's
  `level`. The level-vocabulary mismatch is resolved.
- **Decisiveness balance (rec #3).** A new `storyAnatomy.action` bullet and a
  new `decisive-change` follow-up ("When did you decide coaching was no longer
  enough?") legitimize well-reasoned, evidence-driven leadership change. Red
  flags were rewritten so the failure mode is *unexplained* replacement or
  *defaulting* to one path, not replacement itself. The strong-answer moves and
  signals now reward "staged scope ... and well-timed role changes".
- **Reading-list differentiation (rec #4).** "Staff Engineer" (the least
  leadership-*team*-specific pick) was swapped for *The Leadership Pipeline*, a
  bench/succession-focused source that sharpens this interview against its
  People-Leadership siblings. The fragile Google "Five Dynamics" URL was updated
  to a current `consumer-insights` path and re-sourced to "Think with Google".
- **Example answers everywhere (new).** All five follow-ups now ship paired
  strong/weak `exampleAnswers`, which materially raises teach-ability — an
  interviewer can now hear the difference, not just read an abstract signal.

## Overall Assessment

Now a strong, well-rounded spec (overall ~4.6/5, up from ~4). The edits closed
the realism and balance gaps that held the earlier version back: there is now a
measurable outcome, a credible failure story, an explicit "coaching is no longer
enough" decision point, and concrete example answers throughout. Remaining items
are minor polish, not gaps.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 5 | Now includes a backfired promotion, a rollback, named metrics, and an explicit decision threshold. Messiness and stakes are visible. |
| Balance | 5 | Decisive role change is legitimized alongside coaching; red flags target *unexplained* change and *defaulting* to one path, not decisiveness itself. |
| Educative Value | 5 | Strong/weak `exampleAnswers` on all five follow-ups plus quantified results make the evaluation logic audible, not just stated. |
| Interview Usability | 5 | Five follow-ups with example answers, three differentiated example stories across Senior Manager / Director / VP, rubric aligned to roleFocus. |
| Spec Quality | 5 | Complete, internally consistent, ids/paths/assets resolve, validation passes (16/16). |
| External Resources | 4 | Each link well-annotated and canonical; Leadership Pipeline sharpens differentiation; still shares several general-management links with siblings (acceptable, not duplicated within-file). |

## Strengths

- **The failure story carries real weight.** *Failed Acting Manager Promotion*
  separates technical credibility from the manager role, rolls back scope to
  protect two teams, and converts the mistake into a promotion-readiness
  mechanism. Its weak version ("I gave someone a chance ... picked a stronger
  manager") is a believable blame-shift, not a strawman.
- **Quantified results model what "evidence" means.** The result block now shows
  the proxy metrics the Talent Judgment signal and the `assessment` follow-up
  ask candidates to produce — the spec practices what it preaches.
- **Decisiveness and care are now both rewarded.** The `decisive-change`
  follow-up's strong answers ("the threshold was not frustration; it was
  evidence that continued trial scope was costing the teams more than it was
  developing the leader") teach the exact judgment that separates senior
  decisiveness from impatience.
- **Example answers make signals audible.** Every follow-up's strong/weak pair
  gives an interviewer concrete language to calibrate against.

## Gaps And Risks

1. **New example story has no visual (cosmetic).** `failed-acting-manager-promotion`
   omits `aiVisual` while its two siblings have one. Valid as-is, but the
   explorer will render it without an image — either generate a matching asset
   (`_scripts/generate_*.py`, `--dry-run` first) or accept the asymmetry
   deliberately.
2. **Verify the updated Google URL resolves (watch).** The link was changed to
   `business.google.com/.../consumer-insights/five-dynamics-effective-team/`.
   Google relocates these think pages periodically; the canonical, most stable
   home for this research remains the re:Work "Guide: Understand team
   effectiveness." Confirm the new path is live, or switch to re:Work.
   (Not verified live this pass.)
3. **Confirm the Leadership Pipeline publisher URL.** It points to a German
   Wiley-VCH product page (`wiley-vch.de`). It resolves to the right title, but a
   `wiley.com` / publisher-neutral page may be a more durable canonical link for
   an English-language audience. Low priority.
4. **General-management reading overlap with siblings persists (minor).** GOV.UK,
   Manager's Path, High Output Management, Five Dynamics, Manager Tools, Scaling
   People still overlap with `handling-underperformance` / `culture-change`. Not
   a violation (no within-file duplication); Leadership Pipeline + Five
   Dysfunctions + Making of a Manager now carry the differentiation.

## Priority Recommendations

1. Decide on a visual for the third example story (generate or accept the gap).
2. Re-confirm the updated Google "Five Dynamics" URL is live; fall back to the
   re:Work guide if not.
3. Optionally normalize the Leadership Pipeline link to a more neutral publisher
   page.

All three are cosmetic/link-hygiene items. No correctness bugs; the spec is
publish-valid and the prior review's substantive recommendations are resolved.

## Fixable Data Issues vs Subjective Recommendations

- **Data issues (objective):** none blocking. The rubric/`roleFocus` mismatch
  flagged last pass is fixed.
- **Subjective / hygiene:** items #1–#4 above (visual asset for the new story,
  two link re-confirmations, residual reading overlap).

## Verification Run This Pass

```
python3 _scripts/validate_interviews.py   # ok: 16 datasets
python3 _scripts/summarize_coverage.py    # clean; 3 concrete examples here
# 11 referenced asset files confirmed present on disk
```

Only `REVIEW.md` was changed in this pass, so no rebuild was required. The
interview-data edits under review should be followed by the full check sequence
from `AGENTS.md` (validate, coverage, node --check, build, smoke) before commit —
validate and coverage are confirmed green above.

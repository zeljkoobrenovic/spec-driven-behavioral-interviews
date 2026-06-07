# Review

## Purpose

Review of `data/book/engineer-ownership/interview.json` ("Ownership for Software
Engineers") for realism, balance, educative value, interviewer usability, spec
quality, and external resources. Scope is this single interview. This pass updates
the prior review after the interview gained `toProbeFurther.links[]`, a third
rubric level (Tech Lead), and a fourth example story.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- Group: `book`; role focus: Software Engineer, Senior Software Engineer, **Tech Lead**.
- Difficulty: `intermediate`. Competency: `ownership` (family: Execution and
  Accountability).
- Validation: `validate_interviews.py` passes (28 datasets, this one included).
- Coverage: contributes to the `ownership` test tag — one of the rarer tags, 6
  total uses across the catalog; shared with 8 other datasets.
- Structure: full STAR + Reflection + SystemChange shape, **4 example stories**
  (one per rubric level, with the Tech Lead `flaky-release-gate` added), 4
  signals, 5 follow-ups each with strong/weak calibration answers, **3-level
  rubric**.
- External resources: **`toProbeFurther.links[]` now present** — 5 links across two
  groups (Ownership and Decision Rights; Follow-Through and Learning). All canonical
  non-Obren sources (GitLab Handbook ×2, Atlassian ×2, Google SRE), each with a
  one-sentence `why` and a `groupDescription`. No duplicate book/article.
- Still absent: no `assets` (icon / signal / comic visuals). 16 of 28 datasets carry
  assets; this is among the ~12 without.

## Overall Assessment

A strong, well-crafted interview, now more complete than at the previous review.
The two headline gaps from that pass have been closed: external reading exists, and
the Tech Lead level is fully built out (roleFocus, rubric, and a dedicated
fourth example all aligned). The content remains realistic, concrete, and genuinely
educative — it teaches the difference between ownership-as-closure and the two
common failure modes (heroic takeover and passive notification). It is ready to use
as an interviewer aid today. Remaining items are polish: missing visual assets and
one residual balance nuance (the truly no-owner case).

## What Changed Since Last Review

- **External resources added.** `toProbeFurther.links[]` went from absent to 5
  well-formed links. This resolves the prior "highest-value gap" and lifts the
  External Resources score from 1 to 4.
- **Tech Lead level fully added.** `roleFocus` gained "Tech Lead"; the rubric is now
  3 levels; a fourth example story (`flaky-release-gate`, Tech Lead) was added,
  modelling shared-ownership-of-a-recurring-gap rather than single-incident rescue.
  This resolves the prior "two-level rubric / level ceiling" question — the ceiling
  is now intentionally Tech Lead.
- **Example count 3 → 4**, moving this dataset into the catalog's "4 examples" tier
  (16 of 28 datasets).
- **No-owner balance gap partially addressed.** `flaky-release-gate` and its
  follow-up ("What mechanism stopped this from becoming your permanent job?") now
  cover the shared/unowned recurring-gap case. The narrowest case — *no owner exists
  and none can be found* — is still only lightly covered (see Gaps #2).

## Strengths

- **The central distinction is taught explicitly.** Reflection ("ownership is not
  doing everyone else's work") and the weak-pattern framing ("heroic takeover or
  passive notification") name the exact behavior an interviewer should listen for,
  avoiding the "show ownership" filler the heuristics warn against.
- **Examples carry evidence and trade-offs.** The migration story quantifies (47
  affected accounts, 5 enterprise); the flaky-gate story quantifies rerun rate,
  false failures, and *two real escaped regressions the suite caught* (a sharp
  detail that makes "don't just disable it" concrete). The billing story ties
  escalation to a deadline. These read like real situations, not polished hindsight.
- **Strong/weak calibration is concrete.** Follow-up `exampleAnswers` pairs are
  sharp and realistic — weak answers ("I just jumped in because someone had to do
  it", "I learned to look more carefully at edge cases") are believable rather than
  strawmen.
- **Balance across boundary management.** Strong answers reward *both* initiative
  and respecting another team's ownership, and the Tech Lead story rewards building
  shared ownership over heroics — avoiding single-behavior overfit.
- **Level separation is real.** SWE (initiative + follow-through) → Senior (owns
  ambiguous cross-boundary risk, influences prioritization) → Tech Lead (builds
  shared ownership mechanisms, prevents recurring rescue) are genuinely distinct,
  and each has a matching example at its declared `level`.
- **Internally consistent.** Signal ids, follow-up ids, and rubric levels line up
  across `evaluation`, `visualizations`, and `practiceTemplate`; every example
  `level` value is within the declared `roleFocus`.
- **External resources are well-curated.** Each link has a specific `why` tied to
  the ownership/follow-through theme; DRI/DACI cover decision rights, SRE/Atlassian
  postmortems cover durable follow-through. No Obren links, no duplicates.

## Gaps And Risks

1. **No `assets` / visuals.** No icon, comic, or signal visuals. Below the bar set
   by the catalog's mature interviews (16/28 carry assets). Now the single largest
   completeness gap, since external links are done.
2. **Truly no-owner case still thin.** Every strong path either hands root cause to
   another team or builds *shared* ownership. The legitimate "no owner exists, none
   can be found, you must hold it for now — and make that visible with a handoff
   plan" path is implied but never stated as a strong move. A skilled candidate
   describing exactly this should not read as a red flag.
3. **Owners always re-engage (mild realism idealization).** In all four stories the
   owning team ultimately cooperates. Real ownership stories sometimes involve an
   owner who refuses or stays unavailable; a variant or follow-up probing that
   branch would harden realism.
4. **Bookshelf-inspired pick not yet evaluated.** The 5 links are strong, but no
   ownership/accountability *book* (e.g. from
   `https://obren.io/bookshelf/docs/leadership.html`) has been considered as
   inspiration. Optional, and only if linked to a canonical publisher/author page,
   not the bookshelf note, and not duplicating an existing link.

## Review Dimensions

- Realism: 4 — credible situations, evidence, deadlines, quantified trade-offs.
  Slightly idealized in that owners always re-engage (Gap #3).
- Balance: 4 — rewards initiative, boundary respect, and shared-ownership building;
  the truly no-owner case is the one remaining edge (Gap #2).
- Educative Value: 5 — the strong/weak distinction is made explicit and concrete,
  reinforced across four level-appropriate examples.
- Interview Usability: 5 — easy-to-ask prompt, four meaningfully distinct variants,
  evidence-exposing follow-ups, a rubric that separates three levels cleanly.
- Spec Quality: 5 — complete required fields, consistent ids, passes validation.
- External Resources: 4 — present, canonical, non-duplicate, each with a clear
  `why`; held just short of 5 only because a bookshelf-inspired book pick has not
  been evaluated (Gap #4).

## Priority Recommendations

1. **Add a no-owner strong move.** In `storyAnatomy.action` or
   `strongAnswerPattern.moves`: "When no owner exists and none can be found, take
   temporary ownership *and* make it visible with an explicit handoff plan and end
   date, rather than silently absorbing it." Closes the last balance edge (Gap #2).
2. **(Optional) Add `assets`** — at minimum an `icon`, and consider a signal or
   comic visual to match the catalog's mature interviews. Use the `_scripts/
   generate_*.py` generators with `--dry-run` first, then rebuild `docs/`.
3. **(Optional) Probe the uncooperative-owner branch** — a follow-up such as "What
   if the owning team refused or stayed unavailable?" or a prompt variant, to harden
   realism (Gap #3).
4. **(Optional) Evaluate one bookshelf-inspired ownership/accountability book** for
   `toProbeFurther`, linked to a canonical publisher/author page, not duplicating an
   existing link (Gap #4).

None of these block use. #1 is the most impactful; the rest are polish.

## Per-Interview Review

**`data/book/engineer-ownership/interview.json` — Ownership for Software Engineers**
- Rating: strong (≈4.6/5). Up from the prior pass now that external resources and
  the Tech Lead level are in place; held back only by missing visuals and one
  residual balance/realism nuance.
- Strengths: explicit teaching of the ownership-vs-takeover-vs-notification
  distinction; quantified, trade-off-bearing examples (incl. escaped-regression
  detail in the flaky-gate story); clean three-level separation with a matching
  example per level; curated, canonical external links; consistent and
  validation-clean spec.
- Risks: no visuals; the truly no-owner case is thin; owners always re-engage.
- Next edits: add a no-owner strong move; optionally add `assets`, an
  uncooperative-owner probe, and a bookshelf-inspired book link.

## Ongoing Review Checklist

- After any data edit, run: `validate_interviews.py`, `summarize_coverage.py`,
  `node --check` on both JS files, `build.py`, `smoke_static_site.py`.
- Keep example `level` values within declared `roleFocus`.
- When adding links: canonical non-Obren pages only, one-sentence `why` each, no
  duplicate book/article, links only in the final To Probe Further section.
- If assets are added, regenerate `docs/` and confirm asset paths exist (validator
  checks referenced files).

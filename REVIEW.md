# Review

## Purpose

This document defines how to review the behavioral interview catalog for realism,
balance, educative value, interviewer usability, spec quality, and external
resources. It should be updated after substantial additions to `data/book/` or
major changes to the shared templates. Review source files under `data/`, not the
generated copies under `docs/`.

This revision covers all 16 datasets in the `book/` group as of 2026-06-06.

## Rating Scale

Each dimension is scored 1 (weak) to 5 (excellent):

- **Realism** — reflects real senior engineering-leadership situations: messy
  constraints, disagreement, incomplete information, trade-offs, credible outcomes.
- **Balance** — avoids overfitting to one company type or leadership style; does not
  reward the same behavior (e.g. "create a process") every time; recognizes contexts
  where speed, escalation, technical depth, or principled refusal is the right move.
- **Educative Value** — a reader learns what good looks like; strong/weak patterns,
  examples, follow-ups, and rubric make the evaluation logic explicit and concrete.
- **Interview Usability** — prompts are easy to ask, variants change the evidence
  gathered, follow-ups expose evidence, and the rubric distinguishes levels.
- **Spec Quality** — JSON is complete, internally consistent, and stable in ids/paths.
- **External Resources** — every link has a clear one-sentence relevance note, sources
  are credible, no duplicate book/article, and links appear only in To Probe Further.

## Current Snapshot

- 16 datasets across 1 group (`book/`), 7 competency families. `validate_interviews.py`
  passes; `summarize_coverage.py` runs clean.
- Role coverage: every dataset targets Director / VP Engineering / CTO; 6 also target
  Senior Manager. Difficulty: 15 advanced, 1 foundational (`interview-method`).
- Internal id integrity is **clean** across the catalog: `evaluation.signals` ids match
  `visualizations.signalMap`, `followUps` ids match `visualizations.followUpTree`, and
  `storyAnatomy` fields match the timeline in every file.
- Example-story counts: `leading-through-ambiguity` has 4 (the canonical model),
  `scaling-organization` has 3, and the **other 14 have exactly 2**.
- Follow-up calibration: only **2 of 16** datasets (`leading-through-ambiguity`,
  `scaling-organization`) populate `followUps[].exampleAnswers`. The other 14 give the
  interviewer the probe but no model of a strong vs. weak response.

## Overall Assessment

The catalog is in good shape: the data model is consistent, validation is green, and
the strongest datasets (`leading-through-ambiguity`, `scaling-organization`,
`technical-judgment`, `handling-underperformance`, `technical-debt-modernization`) are
genuinely instructive. The dominant weaknesses are **systematic, not per-file**: thin
example-story coverage, missing follow-up calibration answers, a recurring rubric vs.
roleFocus mismatch the validator does not catch, and a tendency toward hindsight-polished
"clean win" example stories that omit rejected alternatives and residual cost. One file
(`crisis-leadership`) has a concrete data bug that breaks its visual assets.

## Strengths

- **Coherent, well-instrumented data model.** STAR+Reflection+SystemChange shape is
  applied consistently; signals, follow-up trees, and timelines reference each other
  without id drift.
- **Several datasets actively teach balance**, rewarding *not* acting:
  `technical-debt-modernization` ("chooses what not to fix"), `scaling-organization`
  (removes a bottleneck), `innovation-emerging-technology` (stops a rollout),
  `handling-underperformance` (decisiveness vs. compassion-as-delay),
  `technical-judgment` (penalizes both deferring to specialists and asserting authority).
- **Concrete weak-answer red flags** that an interviewer can actually listen for
  (e.g. "says *we* more than *I*", "vanity metrics", "owned it while describing others'
  mistakes", "complains the business doesn't value quality but can't translate debt into
  outcomes").
- **`leading-through-ambiguity` and `scaling-organization` are reference-quality** — 3–4
  level-spanning stories with quantified outcomes and strong/weak follow-up answers. They
  are the template the rest of the catalog should converge toward.

## Gaps And Risks

1. **Rubric vs. roleFocus mismatch (10 of 16 datasets).** The rubric carries a
   `Senior Manager` level that is absent from `roleFocus` (Director/VP/CTO) in:
   `building-leadership-teams`, `culture-change`, `ethics-responsible-technology`,
   `executive-communication`, `executive-conflict`, `innovation-emerging-technology`,
   `scaling-organization`, `strategy-vs-execution`, `technical-debt-modernization`,
   `technical-judgment`. Either add Senior Manager to `roleFocus` or drop the rubric row —
   pick one convention catalog-wide. `validate_interviews.py` does not flag this; consider
   adding a check.
2. **`crisis-leadership` has broken asset wiring (data bug).** The icon container key is the
   empty string `""` instead of `"assets"`, so `assets` is absent and `icon.jpg` is orphaned.
   `explainerComic` is `""`, all six signal `strongAiVisual`/`weakAiVisual` fields are `""`,
   and neither example story nor the answer patterns carry `aiVisual`. This is the one file
   whose visuals do not render (consistent with the deleted generated `.jpg` files in git
   status). Fix the key and regenerate `docs/`.
3. **Missing follow-up calibration (14 of 16 datasets).** Only `leading-through-ambiguity`
   and `scaling-organization` populate `followUps[].exampleAnswers`. This is the single
   highest-leverage educative fix and the pattern is already proven in-repo.
4. **Thin and clustered example stories (14 of 16 have only 2).** Beyond the count, the two
   stories in most files cluster on the same scenario shape and resolve into clean wins, so
   the rubric's lower rungs (Director, and the phantom Senior Manager) are asserted but never
   illustrated, and lower-level candidates have no exemplar.
5. **Hindsight polish reduces realism.** Across many files the example stories have
   frictionless arcs — no rejected alternative the candidate got wrong, no pushback that
   stuck, no residual cost or backfired mechanism. `strongAnswerPattern.moves` sometimes
   claims "shows resistance" (e.g. `culture-change`) that no story actually demonstrates.
6. **Balance gap on principled refusal — most acute for `ethics-responsible-technology`.**
   That case rewards finding a safer alternative / governance path but never credits a clean,
   principled "no" plus escalation when no safe alternative exists. `executive-conflict` and
   `cross-functional-influence` share this: every story resolves via a clever reframe, and
   `cross-functional-influence` even penalizes "only escalates upward", which can mislabel a
   correct fast escalation as weak.

## Review Dimensions

Catalog-level tendencies (per-dataset scores are in the table below):

- **Realism** is generally solid (mostly 4) but capped by clean outcomes; few stories show
  a wrong bet, a leader overruled, or a cost absorbed.
- **Balance** is the most variable dimension (2–5). Strong where a "don't act" path is
  explicitly rewarded; weak where every story runs the same loop (diagnose → reframe →
  add a mechanism), notably `culture-change` and `cross-functional-influence`.
- **Educative Value** is high where strong/weak contrasts are concrete; the ceiling for the
  14 files without follow-up `exampleAnswers` is one point below where it could be.
- **Interview Usability** is good; the limiter is generic follow-ups and rubric rungs with no
  exemplar story.
- **Spec Quality** is dragged down catalog-wide by the rubric/roleFocus mismatch and, for
  `crisis-leadership`, the asset-wiring bug.
- **External Resources** are mostly credible with present `why` notes; weak spots are
  relevance-tightness (`interview-method`, `innovation-emerging-technology`) and author
  over-concentration (`technical-judgment` cites Will Larson three times).

## Priority Recommendations

1. **Fix `crisis-leadership` asset wiring** (`""` → `"assets"`, populate `explainerComic`,
   signal visuals, and story `aiVisual`), then `python3 build.py` and re-run the smoke test.
   *(Data fix — highest urgency; it ships broken.)*
2. **Resolve the Senior Manager rubric/roleFocus mismatch** in the 10 affected datasets, and
   add a validator check so it cannot regress. *(Data fix.)*
3. **Add `followUps[].exampleAnswers` to the 14 datasets that lack them**, mirroring the
   `scaling-organization` pattern (short strong + weak snippets). *(Highest educative ROI.)*
4. **Expand toward 3–4 example stories** in the 2-story files, prioritizing a story that
   (a) exercises an under-illustrated level and (b) breaks the clean-win pattern with a
   rejected alternative, residual cost, or partial failure.
5. **Add a principled-refusal exemplar** to `ethics-responsible-technology` (and soften the
   "only escalates upward" red flag in `cross-functional-influence`) so the catalog credits
   saying *no* and escalating when that is the right call.
6. **Tighten external resources**: realign `interview-method` links toward behavioral-
   storytelling; reduce the three Will Larson entries in `technical-judgment`; re-justify the
   loosest links in `innovation-emerging-technology` (`shape-up`, `ai-engineering`).

## Per-Interview Review

Scores: **R**ealism / **B**alance / **E**ducative / **U**sability / **S**pec / e**X**ternal.

| Dataset | R | B | E | U | S | X | Top risk → next edit |
|---|---|---|---|---|---|---|---|
| `leading-through-ambiguity` | 5 | 5 | 5 | 5 | 5 | 5 | Reference quality — keep as the model. |
| `scaling-organization` | 4 | 4 | 5 | 5 | 5 | 4 | Reconcile `team-topologies` year/edition vs other files; add a backfired-mechanism beat. |
| `handling-underperformance` | 5 | 4 | 5 | 4 | 4 | 4 | Both stories are role-mismatch + clean; add a motivation/harmful-behavior case at VP/CTO. Fix typo "the person dignity". |
| `technical-judgment` | 5 | 4 | 5 | 5 | 3 | 4 | Fix Senior-Manager rubric mismatch; add a decision-*reversal* story; reduce 3× Larson links. |
| `technical-debt-modernization` | 4 | 5 | 5 | 4 | 3 | 4 | Fix rubric mismatch; add a deferred-debt-that-bit-back outcome; add follow-up answers. |
| `failure-accountability` | 4 | 4 | 5 | 4 | 4 | 4 | Add a messier/partial-outcome failure; add follow-up answers; verify `scapegoats-at-work` source. |
| `interview-method` | 4 | 4 | 5 | 4 | 4 | 3 | Realign links to storytelling method; add a non-incident example story. |
| `building-leadership-teams` | 4 | 4 | 4 | 4 | 3 | 4 | Fix rubric mismatch; add a failed-promotion / "across multiple teams" story; add follow-up answers. |
| `strategy-vs-execution` | 4 | 4 | 4 | 4 | 3 | 4 | Fix rubric mismatch; inject a residual trade-off (paused project that proved costly). |
| `crisis-leadership` | 4 | 4 | 4 | 4 | 2 | 4 | **Asset-wiring bug** (`""` key, empty visuals); add a people/trust-crisis story. |
| `executive-conflict` | 4 | 3 | 4 | 4 | 3 | 4 | Add a principled-refusal / disagree-and-commit-after-losing story; add follow-up answers; fix rubric mismatch. |
| `executive-communication` | 4 | 3 | 4 | 4 | 3 | 4 | Add a Director-level story; inject executive pushback into one story; add follow-up answers; fix rubric mismatch. |
| `ethics-responsible-technology` | 4 | 3 | 4 | 4 | 3 | 4 | Add a stop/refuse-and-escalate story with real cost; distinguish refusal from reflexive blocking; fix rubric mismatch. |
| `innovation-emerging-technology` | 4 | 4 | 5 | 4 | 3 | 3 | Tighten loosest links; add a CTO-level strategic-bet story; fix rubric mismatch. |
| `culture-change` | 3 | 2 | 3 | 3 | 3 | 4 | Most overfit: add a counter-context (heroics correctly preserved) + real resistance; fix rubric mismatch. |
| `cross-functional-influence` | 3 | 3 | 3 | 3 | 3 | 3 | Thinnest realism + most archetypal; sharpen generic follow-ups (overlap with `executive-conflict`); soften "only escalates upward" red flag. |

## Ongoing Review Checklist

Run before judging content, and after any data change:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

When reviewing a dataset, confirm:

- [ ] `evaluation.rubric` levels are all present in `roleFocus` (no phantom Senior Manager).
- [ ] Asset keys are spelled correctly (`assets`, not `""`); referenced visual files exist.
- [ ] `followUps[].exampleAnswers` provide a strong and a weak snippet per probe.
- [ ] At least 3 example stories spanning the declared levels, each with a rejected
      alternative or residual cost (not only clean wins).
- [ ] Balance: at least one path rewards restraint, escalation, or principled refusal —
      not only "diagnose → reframe → add a mechanism".
- [ ] `evaluation.signals` ids match `visualizations.signalMap`; `followUps` ids match
      `visualizations.followUpTree`.
- [ ] Every `toProbeFurther.links[]` entry has a specific `why`, a credible canonical
      source (no `obren.io` bookshelf links), and no duplicate book/article; book metadata
      (year/edition) is consistent across files.
```

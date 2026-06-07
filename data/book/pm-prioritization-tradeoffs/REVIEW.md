# Review

## Purpose

Single-interview review of `data/book/pm-prioritization-tradeoffs/interview.json`
("Product Prioritization and Trade-Offs"), assessed against the repository review
dimensions: Realism, Balance, Educative Value, Interview Usability, Spec Quality,
and External Resources.

This is an **update** of the prior review. The interview has since been
substantially expanded: it now carries external resources, two additional example
stories (including a Group Product Manager level story), three additional
follow-ups, a fourth evaluation signal, and quantified targets in the mobile
example. Nearly every gap from the previous review has been closed.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- Validation: `python3 _scripts/validate_interviews.py` → `ok` (28 datasets, 1 group).
- Coverage: contributes the `Decision Criteria`, `Opportunity Cost`,
  `Revisit Discipline`, and now `Residual Risk Ownership` signals.
- Structure: all required data-model sections present
  (`competency` → `practiceTemplate`), 3-level rubric, **4 example stories**
  (PM, two Senior PM, GPM), **6 follow-ups** with strong/weak calibration answers,
  and a `toProbeFurther.links[]` section (4 links across 3 groups).

## What Changed Since The Last Review

| Prior gap | Status now |
| --- | --- |
| Missing `toProbeFurther.links[]` (was External Resources 1/5) | **Resolved.** 4 grouped, canonical, non-Obren links, each with a `why`. |
| Group PM level under-exemplified | **Resolved.** `reporting-suite-portfolio-rebalance` is a GPM-level cross-team portfolio story with an explicit stop-doing call and revisit checkpoint. |
| Follow-ups over-weighted toward the engineering-evidence story | **Resolved.** Six follow-ups now spread across all four stories; `stakeholder-pushback`, `reversal-evidence`, and `portfolio-impact` were added. |
| Uneven quantification (second example qualitative) | **Resolved.** Mobile example now defines low-memory activation 31→38% and crash-free sessions 96.8→99.2%. |
| Single-team scope only | **Resolved.** SSO and portfolio stories add segment-signal and portfolio-level scope. |
| No visual assets | Still absent (optional per data model). |

## Overall Assessment

A focused, well-constructed PM prioritization case, now considerably stronger than
at the last review. Its central insight — prioritization is an explicit, costed
trade-off, not a ranking exercise — is carried consistently from the competency
definition through the signals, follow-ups, and red flags. The four stories now
span all three claimed role levels, the follow-up set exposes evidence from each
story, and external resources are present and on-topic. Remaining issues are minor:
one cross-catalog duplicate-book link, and a couple of internal-consistency notes
around the newly enlarged follow-up/signal set.

## Strengths

- **Opportunity cost is the spine, not a slogan.** The "stop-doing" idea recurs
  in `constraints`, `systemChange`, the `opportunity-cost` signal, and the
  `opportunity-cost` follow-up — and every weak example deliberately omits it
  ("We put the other items in the backlog").
- **Strong/weak pairs are calibrated and realistic.** The weak answers are
  plausible PM-speak ("I used a prioritization framework, scored the options, and
  aligned the team") rather than strawmen, which makes them genuinely useful as
  interviewer calibration.
- **Now exemplifies all three role levels.** The GPM `reporting-suite-portfolio-rebalance`
  story shows portfolio-level opportunity cost across three teams, a public
  rebalancing after a partial miss, and a capacity-allocation mechanism — the
  concrete shape the rubric's third row promises.
- **Segment-signal vs. one-off discipline is now shown, not just asserted.** The
  `sso-segment-signal-vs-collaboration-feed` story demonstrates testing whether a
  Sales request is a repeated segment blocker, which previously lived only in the
  red flags and `interviewerIntent`.
- **Cross-functional balance.** The mobile-redesign example rewards letting
  *engineering evidence change the product decision*, countering the failure mode
  of treating feasibility as a late implementation detail.
- **Revisit discipline is a distinctive, durable mechanism** (renewal-risk
  thresholds, portfolio checkpoints) — a senior behavior many prioritization
  prompts miss.
- **Quantification is now even.** Both the activation example (42% of trials) and
  the mobile example (31→38% activation, 96.8→99.2% crash-free) carry measurable
  bars.

## Gaps And Risks

1. **One cross-catalog duplicate-book link (minor).** `shape-up-bets-not-backlogs`
   (`https://basecamp.com/shapeup`) is also linked in
   `engineering-manager-delivery`. The skill asks to avoid duplicating the same
   book/article. Context differs (delivery vs. prioritization), so this is low
   severity, but consider a prioritization-specific anchor (e.g., the Shape Up
   chapter on "Betting" / appetite) or a distinct resource to keep catalog links
   non-redundant.
2. **Same-author second link (acceptable, noted).** Itamar Gilad appears here
   (`/prioritization/`) and in `pm-customer-discovery` (`/how-much-product-discovery/`).
   Different articles, both directly relevant, so this is not a duplicate-resource
   violation — just worth tracking so a third PM case does not over-rely on one
   author.
3. **Signal/follow-up balance vs. visualizations (verify-on-edit).** The spec now
   has 4 signals and 6 follow-ups, and `visualizations.signalMap` /
   `followUpTree` reference all of them (confirmed). Keep this in sync if more are
   added; validation passes today.
4. **No visual assets** (`assets.icon`, `explainerComic`, `aiVisual`). Optional
   per the data model, but worth noting for parity with richer datasets.

## Review Dimensions

| Dimension | Score | Notes |
| --- | --- | --- |
| Realism | 5 | Four credible competing-opportunity setups with real stakeholder tension, partial misses, and mid-decision uncertainty (escalations, beta surprises). |
| Balance | 5 | Strong customer/business/technical/execution spread across stories; segment-signal vs. one-off and portfolio scope now represented. |
| Educative Value | 5 | Strong/weak contrasts and red flags make the evaluation logic explicit and teachable. |
| Interview Usability | 5 | Clean prompt, distinct variants, six evidence-exposing follow-ups, and stories matched to each rubric level. |
| Spec Quality | 5 | Validates clean; ids stable; visualizations reference real signal/follow-up ids. |
| External Resources | 4 | Present, grouped, canonical, non-Obren, each with a `why`; one cross-catalog same-book duplicate keeps it from a 5. |

## Priority Recommendations

1. **Resolve the Shape Up duplicate** with `engineering-manager-delivery`: either
   swap to a prioritization-specific resource or anchor to a distinct Shape Up
   section so the two cases do not point at the identical book URL.
2. (Optional) **Add a visual asset** (`assets.icon` at minimum) for parity with
   richer datasets.
3. (Optional) **Watch single-author concentration** across PM cases — avoid a
   third Itamar Gilad or SVPG link in a sibling PM dataset without a deliberate
   reason.

## Per-Interview Review

- **File:** `data/book/pm-prioritization-tradeoffs/interview.json`
- **Rating:** Strong and now near-complete (5/5 on content and spec dimensions;
  4/5 External Resources).
- **Main strengths:** Opportunity-cost discipline threaded throughout; calibrated
  weak answers; four stories covering all three role levels; segment-signal and
  portfolio scope; even quantification; distinctive revisit-trigger mechanism.
- **Main risks:** One cross-catalog same-book link (Shape Up); same-author second
  link (acceptable); no visual assets.
- **Recommended next edits:** Resolve the Shape Up duplicate (priority 1);
  optionally add a visual asset.

## Ongoing Review Checklist

- [ ] After editing data: rerun `validate_interviews.py`, `summarize_coverage.py`,
      `node --check` on both JS files, `build.py`, then `smoke_static_site.py`.
- [ ] Confirm added links are canonical (non-Obren), non-duplicated across the
      PM datasets, and each has a one-sentence relevance `why`.
- [ ] Confirm any new signal/follow-up ids are referenced by the
      `visualizations.signalMap` / `followUpTree` blocks.

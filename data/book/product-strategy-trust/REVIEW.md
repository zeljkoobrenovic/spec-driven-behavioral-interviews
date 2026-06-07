# Review

## Purpose

Documented review of `data/book/product-strategy-trust/interview.json` ("Product
Strategy, Ethics, and Trust") against the project's review dimensions: realism,
balance, educative value, interview usability, spec quality, and external
resources. Findings separate fixable data issues from subjective content
recommendations.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- Competency: Product Strategy, Ethics, and Trust (family: Risk, Ethics, and Innovation).
- Difficulty: advanced. Role focus: Group Product Manager, Director of Product, VP Product.
- Group: Senior Product Leaders (`data/book/index.json`).
- 3 example stories (Director ship/no-ship, GPM fairness/safety ranking, VP
  portfolio strategy shift), 4 follow-ups (each with strong/weak calibration
  answers), 3 evaluation signals, level rubric for GPM / Director / VP.
- `toProbeFurther.links[]`: 5 curated links across two groups
  ("Product Strategy and Choices", "Trust and Responsible Growth").
- `assets`: `{ "icon": "icon.png" }`; `icon.png` exists in the directory.
- `python3 _scripts/validate_interviews.py`: passes (28 datasets ok).
- `python3 _scripts/summarize_coverage.py`: dataset counted, no warnings.

## What Changed Since The Last Review

The prior review's three top-priority gaps have all been closed:

1. **`toProbeFurther.links[]` added** — was the single biggest gap (rated 1/5);
   now a coherent 5-link list grouped into product strategy and trust/safety,
   each with a one-sentence `why` and a `groupDescription`.
2. **`assets` block added** — `"assets": {"icon": "icon.png"}` now matches
   siblings.
3. **Third example story added** — "Delaying An Engagement Ranking Change" (GPM)
   exercises fairness, safety, ranking incentives, and vulnerable-user risk,
   directly addressing the prior "single privacy archetype" concern.
4. **Stakeholder-credibility follow-up added** — the new `stakeholder-credibility`
   probe ("How did you make the decision credible to the powerful stakeholder
   who wanted to ship?") closes the prior influence-probe gap; the follow-up tree
   now lists all four probes.

This moves the spec from "content-strong but incomplete" to "complete and
content-strong." Remaining items are minor.

## Overall Assessment

A well-constructed, complete, and senior interview. The core teaching idea —
"responsible strategy needs a concrete alternative, not just a principled
objection" — is clear and consistently reinforced from the prompt through the
signals and rubric. The three example stories now span all three rubric levels
and three distinct risk archetypes (data-sharing/privacy, ranking
fairness/safety, portfolio trust-debt), so balance and altitude coverage are
strong. The follow-up set exposes evidence across risk, trade-off, alternative,
and influence.

Rough overall rating: **content 5/5, completeness 4/5.** (Completeness is held
just below 5 only by the missing `LINKEDIN.md` and the absence of any
explainer comic / AI visuals that some siblings carry — both optional.)

## Strengths

- The strong/weak contrast is taught concretely, not asserted. The weak versions
  ("I pushed back because the feature felt risky for privacy") are realistic and
  map precisely to the red flags and weak signal descriptions.
- Follow-ups expose evidence well. Each of the four probes has paired
  strong/weak example answers, and the strong ones name specifics (contractual
  admin expectations, trust debt, opt-in rollout, cohort-level safety evidence)
  that are hard to fake.
- The new ranking-safety story is the strongest balance addition: it ties a
  concrete business cost (a missed investor-update lift) to a vulnerable-cohort
  harm and a rejected easier option (disclaimer-only), exercising fairness and
  safety signals that previously lived only in the field vocabulary.
- Good balance against "just say no": both the strong pattern and the signals
  explicitly reward offering a responsible alternative and warn against treating
  legal approval as the only trust bar.
- The three example stories cover distinct altitudes — GPM ranking call,
  Director ship/no-ship call, VP portfolio strategy shift — so each rubric level
  is demonstrated, not just described.
- `toProbeFurther.links[]` is well-curated: SVPG/Rumelt for "is this real
  strategy or relabeled roadmap," and FTC dark-patterns + TSPA for the
  trust/safety side that goes beyond privacy or legal approval.

## Gaps And Risks

Fixable spec / data issues (highest priority first):

1. **Cross-catalog link duplication.** "Good Strategy Bad Strategy" (Rumelt) now
   appears in five interviews (`executive-conflict`,
   `leading-through-ambiguity`, `product-strategy-trust`,
   `strategy-vs-execution`, `technical-judgment`). It is genuinely on-topic here
   (the VP strategy-shift example), but consider whether a more product-specific
   strategy resource (e.g. Cagan's *Empowered* for portfolio non-goals/guardrails,
   or a reframing piece) would differentiate this list from the
   strategy/judgment interviews while keeping the `why` distinct. Not a
   validation error; a curation judgment call.

2. **No `LINKEDIN.md`.** Every sibling product interview ships one; not part of
   the spec/validation, but a publishing-consistency gap.

3. **No explainer comic / AI visuals and no `assets/` directory.** Only
   `assets.icon` is set. `explainerComic`, `strongAnswerPattern.aiVisual`,
   `weakAnswerPattern.aiVisual`, `evaluation.signals[].*AiVisual`, and
   `exampleStories[].aiVisual` are all optional, but some product siblings carry
   them. Generate via `_scripts/generate_*.py` (`--dry-run` first, then rebuild
   `docs/`) if visual parity is desired.

Content observations (subjective, lower priority):

4. The new ranking story partially overlaps the privacy story on structure
   (quantify upside → reject broad option and an easier option → narrower
   rollout with guardrails → add review mechanism). That parallel structure is a
   teaching strength, but interviewers reusing all three back-to-back may find
   the "narrower rollout + guardrail" move repetitive; the VP story's
   stop-funding decisions are the main structural contrast. Consider noting in
   the interviewer guidance which story best probes which signal.

## Review Dimensions

| Dimension | Rating | Notes |
| --- | --- | --- |
| Realism | 5 | Messy constraints, real business pressure (investor update, Sales lead volume), credible "legal-approved-but-still-wrong" tension; three archetypes now. |
| Balance | 5 | Rewards alternatives, acknowledges business pressure, and now exercises fairness/safety/vulnerable-user risk beyond privacy. |
| Educative Value | 5 | Strong/weak patterns, paired calibration answers, and signals teach the concrete behavior to listen for. |
| Interview Usability | 5 | Prompt + four variants are easy to ask; four follow-ups (incl. influence/credibility) expose evidence; rubric separates levels. |
| Spec Quality | 5 | Schema-valid, internally consistent, `assets` and `toProbeFurther` now present, follow-ups/signals/visualizations in sync. |
| External Resources | 4 | Five credible, well-annotated links; held at 4 only by the Rumelt link's reuse across five interviews. |

## Priority Recommendations

1. **Differentiate the strategy resource** from the four other interviews that
   cite "Good Strategy Bad Strategy," or keep it but sharpen the `why` so it
   reads as product-portfolio-specific rather than generic strategy.
2. **Add `LINKEDIN.md`** to match sibling product interviews (publishing
   consistency, not validation).
3. *(Optional)* Generate an explainer comic / AI visuals for visual parity with
   other product interviews (`_scripts/generate_*.py`, `--dry-run` first, then
   rebuild `docs/`).
4. *(Optional)* Add a one-line interviewer note mapping each example story to the
   signal it best probes, since the three stories share a structural arc.
5. After any data change, run the required checks (validate, coverage,
   node --check, build, smoke) per `AGENTS.md`.

## Per-Interview Review

**File:** `data/book/product-strategy-trust/interview.json`
**Rating:** content 5/5, completeness 4/5.
**Strengths:** concrete strong/weak teaching; four evidence-exposing follow-ups
with calibration answers; three example stories across all rubric levels and
three risk archetypes (privacy, ranking fairness/safety, portfolio trust-debt);
balanced against reflexive "no"; curated, well-annotated reading list.
**Risks:** "Good Strategy Bad Strategy" link reused across five interviews; no
`LINKEDIN.md`; no comic / AI visuals.
**Recommended next edits:** differentiate or re-justify the strategy resource;
add `LINKEDIN.md`; optionally generate visuals and add per-story signal-probe
guidance.

## Ongoing Review Checklist

- [x] `toProbeFurther.links[]` present, each with a one-sentence `why`.
- [ ] No duplicate resources shared with sibling product/ethics/strategy
      interviews (Rumelt currently shared across five).
- [x] `assets.icon` set; referenced asset file exists.
- [x] Example stories cover more than one risk archetype.
- [x] Follow-ups, signals, and `visualizations` stay in sync.
- [ ] `LINKEDIN.md` present for publishing parity.
- [ ] `validate_interviews.py`, `summarize_coverage.py`, `build.py`,
      `smoke_static_site.py` all pass after edits.

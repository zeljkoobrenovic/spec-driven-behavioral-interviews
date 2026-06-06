# Review — Technical Judgment at Executive Scale

File: `data/book/technical-judgment/interview.json`
Reviewed against: `AGENTS.md`, `CLAUDE.md`, the `book` manifest, and the canonical `_templates/*.json` vocabularies.

## Purpose

Assess this single interview for realism, balance, educative value, interviewer usability, spec quality, and external-resource quality, and separate fixable data issues from subjective content recommendations.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## What Changed Since The Last Review

This update is a substantial expansion, and it strengthens the spec on every dimension:

- **Senior Manager coverage added.** `roleFocus` now includes Senior Manager, a new `constrained-event-streaming-rollout` example story carries that level, and the Senior Manager rubric row was sharpened ("defines readiness signals before expanding a pattern").
- **Reversal became a first-class theme.** A new VP-level `reversing-premature-service-extraction` story, a new `reversal-discipline` evaluation signal, a sixth strongAnswerPattern move ("names the evidence that would trigger a reversal and owns course changes without blame"), and a new weak-pattern red flag ("treats reversing a decision as embarrassment instead of learning") now reinforce each other. `signalMap` was updated to include `reversal-discipline`.
- **All four follow-ups gained `exampleAnswers`** with paired strong/weak model answers — the single biggest educative improvement.
- **Resource list rebalanced.** Dropped two Will Larson items (`Writing Engineering Strategy` article, `Staff Engineer`); added `Accelerate` and `Enterprise Architecture as Strategy`. This reduces single-author concentration and adds delivery-performance evidence plus an architecture-to-business-execution reference.
- **Copy fix:** "both camps strongest" → "both camps' strongest".

## Current Snapshot

- Competency: Technical Judgment at Executive Scale (family: Judgment and Strategy).
- Role focus: Senior Manager, Director, VP Engineering, CTO; difficulty advanced.
- Structure is complete: prompt + 2 variants, scenario, storyAnatomy, **four** exampleStories (one per level), strong/weak patterns, four followUps each with strong/weak exampleAnswers, **four** evaluation signals, four-level rubric, visualizations, practiceTemplate, relatedScenarios, seven toProbeFurther links.
- `validate_interviews.py` passes for this dataset. (The only repo validation failure is the unrelated missing comic in `book/interview-method`.)
- Manifest name ("Technical Judgment at Executive Scale") matches the interview title exactly — no cosmetic mismatch.
- All `tests`, role levels, and family map to the canonical `_templates/*.json` vocabularies.

## Overall Assessment

Rating: **5 / 5 (excellent).**

This was already one of the stronger specs; the update pushes it to the top tier. Its defining strength is that every section now rewards the same hard-to-fake executive behaviors — naming decision criteria, separating module boundaries from runtime distribution, and treating reversal as disciplined learning rather than failure — and the four example stories give one credible, distinct shape per role level. The new `exampleAnswers` make the evaluation logic concrete instead of asking interviewers to infer it. The remaining gaps are minor and mostly about visual-asset parity and measurable outcomes.

## Strengths

- **Four stories, four distinct shapes, one per level.** Constrain-an-overreach (Senior Manager), pragmatic-over-fashionable (Director), reverse-a-portfolio-decision (VP), build-vs-buy (CTO). The page now teaches a genuine progression rather than restating the monolith debate.
- **Reversal discipline is reinforced everywhere.** The new signal, the new strongAnswerPattern move, the new weak red flag, and the VP story all teach the same durable behavior: name the evidence, own the cost, replace the gate. This is exactly the anti-platitude the content guide asks for.
- **`exampleAnswers` model what the spec demands.** The weak answers ("We considered reliability, scalability, and maintainability and chose the most balanced option") are realistic mediocre answers, not strawmen, and the strong answers name concrete instruments (transactional outbox, data-export tests, revisit triggers in ADRs).
- **Expert collaboration is framed correctly.** "Ask the senior engineer who proposed the rollout to help define the readiness bar rather than framing the reset as their mistake" and "co-author extraction readiness criteria" teach influence-without-outsourcing crisply.
- **Rubric levels are genuinely differentiated** — domain trade-offs (Senior Manager) → cross-team criteria/migration (Director) → portfolio risk balance (VP) → strategic leverage (CTO).
- **Resource list is now better balanced** — single-author concentration reduced, all links point to canonical non-Obren publisher pages, no duplicate book/article.

## Gaps And Risks

1. **Visual-asset parity (highest-value fix).** The two new stories (`constrained-event-streaming-rollout`, `reversing-premature-service-extraction`) have **no `aiVisual`**, while the two older stories do. Likewise the new `reversal-discipline` signal has no `strongAiVisual`/`weakAiVisual`, while the other three signals each have both. Validation passes because the fields are simply absent, but the page will render with inconsistent visual density. Generate the four missing story/signal images (`_scripts/generate_*.py`, `--dry-run` first) and rebuild, or accept the asymmetry deliberately.
2. **No measurable outcomes in the stories.** The spec repeatedly demands measurement (the `wrong` follow-up, the `measurement` test, strongAnswerSketch lines that list metrics to track), yet none of the four stories states a number actually achieved — only metrics to be measured. "Got worse" and "happened where justified" are directional, not quantified. At least one story (the VP reversal is the natural candidate) should land a concrete result, e.g. "checkout incident rate fell from X to Y within two cycles after reconsolidation."
3. **Scenario base is monolith/microservices-heavy.** Three of four stories revolve around service decomposition (event streaming, modular monolith, service-extraction reversal); only build-vs-buy breaks the pattern. The `relatedScenarios` note cloud/data/AI architecture, but no story exercises a data-platform or AI/ML architecture call — a reader could over-fit to the services debate.
4. **`storyAnatomy` still duplicates the Director story.** The signatureExample, scenario, storyAnatomy, and `modular-monolith-first` example all tell the modular-monolith story. With four examples now present, the anatomy could illustrate a different shape (e.g. the reversal) so the page teaches more variety up top.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 4 | Credible senior situations with real conflict and named technical detail (transactional outbox, schema ownership, on-call load). Loses a point only because outcomes are directional, never quantified. |
| Balance | 4 | Strong across technical depth, expert collaboration, sequencing, and now reversal; build-vs-buy adds business framing. Held back slightly by three-of-four stories sharing the decomposition theme. |
| Educative Value | 5 | The new `exampleAnswers` plus the strong/weak split per signal and red flag make the evaluation logic fully explicit; the reader learns precisely what good and bad sound like. |
| Interview Usability | 5 | Variants change the evidence gathered; follow-ups now ship with model answers an interviewer can calibrate against; rubric is level-distinct; one example story per level. |
| Spec Quality | 4 | Complete, internally consistent, valid against schema and vocabularies; ids stable; manifest name matches. Docked one point for the missing aiVisual fields on the two new stories and the new signal. |
| External Resources | 4 | Credible canonical sources, per-link relevance notes, no duplicate book/article, reduced single-author concentration. Seven links is reasonable; Enterprise Architecture as Strategy (2006) is the weakest-relevance entry if trimming is ever wanted. |

## Priority Recommendations

1. **Generate the four missing visuals** (two new stories + `reversal-discipline` strong/weak) so visual density is consistent, then `python3 build.py` and re-run the smoke test — or consciously decide to leave the new entries imageless.
2. **Add at least one quantified outcome**, ideally in the VP reversal story, so the spec models the measurement it asks candidates to provide.
3. **Diversify one scenario** away from service decomposition — a data-platform, cloud-cost, or AI/ML architecture call — to match the breadth promised by `relatedScenarios`.
4. **(Optional) Re-point `storyAnatomy`** to a non-modular-monolith shape now that four examples exist, so the anatomy and the first example are not near-duplicates.

## Ongoing Review Checklist

- Re-run `python3 _scripts/validate_interviews.py` and `python3 _scripts/summarize_coverage.py` after any content edit.
- When adding an example story or signal, add its `aiVisual` / `strongAiVisual` / `weakAiVisual` (or note the omission deliberately) to keep visual parity.
- Keep `signalMap` and `followUpTree` in sync with the `signals` and `followUps` arrays (currently in sync).
- Keep model answers (`exampleAnswers`, `strongAnswerSketch`) demonstrating the measurement and reversal discipline the rubric demands.

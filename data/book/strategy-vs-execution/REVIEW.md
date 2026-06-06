# Review — Strategy Versus Execution

File: `data/book/strategy-vs-execution/interview.json`
Reviewed against: `AGENTS.md`, `CLAUDE.md`, the `book` manifest, and the canonical `_templates/*.json` vocabularies.

## Purpose

Assess this single interview for realism, balance, educative value, interviewer usability, spec quality, and external-resource quality, and separate fixable data issues from subjective content recommendations.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Current Snapshot

- Competency: Strategy Versus Execution (family: Judgment and Strategy).
- Role focus: **Senior Manager, Director, VP Engineering, CTO**; difficulty advanced.
- Structure is complete: prompt, scenario, storyAnatomy, **four** exampleStories, strong/weak patterns, four followUps (each now with strong/weak `exampleAnswers`), three evaluation signals, four-level rubric, visualizations, practiceTemplate, relatedScenarios, **five** toProbeFurther links.
- All referenced visual assets exist on disk. The two newest example stories (`post-acquisition-platform-consolidation`, `segment-focus-service-sunset`) intentionally have no `aiVisual`; the explorer renders them gracefully via `renderOptionalImage`.
- `validate_interviews.py` passes for this dataset. (The only validation failure in the repo is an unrelated missing comic in `book/interview-method`.)
- All followUp `tests` map to the canonical `_templates/signal-types.json` vocabulary; role levels and family are valid; `exampleAnswers` is a schema-supported, validated, and rendered field.

## Change Log Since Previous Review

This revision directly resolved nearly every recommendation from the prior review:

- **Measurable outcomes added throughout.** `storyAnatomy.result` and all four example stories now carry concrete numbers (security-review cycle time 18→6 business days; $4.2M and $3.1M ARR; cloud spend −23% / gross margin +4 pts; support tickets −31% / on-call pages −18%). The spec now models the measurement it demands. (Prior gap #1, Priority #1 — **resolved**.)
- **Scenario base diversified.** The signature scenario is now a non-revenue regulated-market/compliance shift; two new example stories add **M&A platform consolidation** (Director) and **segment-focus service sunset** (Senior Manager). `relatedScenarios` updated to match. (Prior gap #2, Priority #2 — **resolved**.)
- **Signature story differentiated.** The `storyAnatomy` is now a regulated-market story, distinct from the enterprise-readiness and profitability example stories, so the page teaches multiple shapes. (Prior gap #3, Priority #3 — **resolved**.)
- **Resources trimmed 9 → 5.** Dropped `EMPOWERED`, `High Output Management`, `The Effective Executive`, and `How Big Things Get Done`; kept Good Strategy Bad Strategy, Measure What Matters, Shape Up, Working Backwards, and the GOV.UK structured-interview guide. (Prior gap #5, Priority #4 — **resolved**.)
- **Residual-cost discipline added as a first-class signal.** Every strong story now names what got worse (a slipped launch, a churned customer, a partner escalation); strongAnswerPattern adds "Names measurable outcomes and the residual cost of the chosen trade-off"; weakAnswerPattern adds "celebrates the winning priority but hides what got worse or more expensive"; the `prioritization` signal now requires "owner, and residual cost." This is a new, strong teachable distinction not present before.
- **`exampleAnswers` added to all four follow-ups**, with strong/weak pairs that demonstrate the evidence an interviewer should hear. Major educative-value upgrade.
- **Senior Manager role added** to `roleFocus`, matched by a Senior Manager example story and the existing rubric row — the level coverage is now self-consistent.

## Overall Assessment

Rating: **5 / 5 (excellent).**

The revision turns an already-disciplined spec into one of the strongest in the catalog. The defining strength is unchanged — it rewards the hardest senior behavior (explicit stop-doing decisions plus durable governance change rather than "aligning stakeholders") — but it now also (a) models the measurement it demands, (b) teaches residual-cost honesty as an explicit signal, (c) spans four genuinely different strategy archetypes (regulated-market, enterprise readiness, profitability, M&A, segment sunset) across four role levels, and (d) gives interviewers concrete strong/weak follow-up answers to calibrate against. The remaining items are minor cosmetics.

## Strengths

- **Stop-doing discipline is the through-line, now paired with residual cost.** Variants, the `prioritization` signal, the `stopped-work` follow-up, weak-pattern red flags, and every strong story reinforce both naming what was stopped *and* what it cost. This is anti-filler the content guide explicitly asks for.
- **Governance > one-time reset.** The `operating-governance` signal (now including "and metrics") and the weak-pattern red flag teach the durable-mechanism distinction crisply; `systemChange` lists concrete mechanisms.
- **Outcomes are measured, with named trade-offs.** Results read like real post-mortems, not hindsight platitudes — they pair a win metric with a deferred cost.
- **Four diverse, level-appropriate archetypes.** Regulated-market (signature/VP), enterprise readiness (CTO), profitability (VP), M&A consolidation (Director), segment sunset (Senior Manager). A reader can no longer over-fit to "revenue pivot."
- **Follow-ups now teach the answer, not just the question.** Strong/weak `exampleAnswers` make the evaluation logic explicit and directly usable in a live interview.
- **Weak versions are realistic and diagnostic** ("I told teams to reduce cloud spend by 20 percent and asked platform engineering to find savings") — believable mediocre answers, not strawmen.
- **Rubric levels are genuinely differentiated**, escalating from "connects team priorities" (Senior Manager) to "capital allocation and long-term leverage" (CTO).

## Gaps And Risks

1. **Manifest cosmetic mismatch persists (only real open item).** Manifest name is "Strategy vs. Execution"; interview title is "Strategy Versus Execution." Ids match so validation passes, but display names diverge. Carried over from the previous review.
2. **Two newest example stories lack visual assets (optional).** `post-acquisition-platform-consolidation` and `segment-focus-service-sunset` have no `aiVisual`. The page renders fine without them, but generating illustrations would make the four stories visually consistent.
3. **Numbers are slightly dense in places.** A few `whyItWorks`/`result` lines pack multiple metrics into one bullet. This is a minor readability note, not a correctness issue; the trade-off (concrete evidence) is worth it.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 5 | Credible senior situations with real conflict, rejected alternatives (full replatform, storage-tier change), and outcomes stated as measured wins paired with named residual costs. |
| Balance | 5 | Four distinct strategy archetypes across four role levels — revenue pivots no longer dominate; regulatory, M&A, and segment-narrowing shifts are all represented. |
| Educative Value | 5 | Strong/weak contrast is explicit at every layer; signals name concrete behaviors; model answers now demonstrate the measurement and residual-cost honesty they demand; follow-up `exampleAnswers` teach what to listen for. |
| Interview Usability | 5 | Variants change the evidence gathered; follow-ups expose evidence and ship calibrated strong/weak samples; rubric is level-distinct and matches the four roleFocus levels. |
| Spec Quality | 5 | Complete, internally consistent, valid against schema and vocabularies; assets present; ids stable; `exampleAnswers` correctly structured. |
| External Resources | 4 | Five tightly-relevant canonical sources, each with a specific relevance note and no duplicate book/article. Held one point only because all four "Strategy and Execution" picks are books — a primary-source article or case (e.g. on operating cadence or capital allocation) would add modality variety. |

## Priority Recommendations

1. **Align manifest display name** ("Strategy vs. Execution") with the interview title ("Strategy Versus Execution"), or standardize the abbreviation convention deliberately across the catalog. This is the only carried-over open item.
2. *(Optional)* Generate `aiVisual` assets for the two newest example stories so all four are visually consistent.
3. *(Optional)* Consider one non-book resource for modality variety in the strategy group, keeping links canonical and non-duplicative.

## Verification Performed

- `python3 _scripts/validate_interviews.py` — passes for this dataset (unrelated failure in `interview-method`).
- `python3 _scripts/summarize_coverage.py` — dataset present and categorized under Judgment and Strategy.
- Manual asset existence check — all referenced images present; comic exists; two new stories correctly omit `aiVisual`.
- `exampleAnswers` confirmed schema-supported (`validate_interviews.py:296`), rendered (`explorer.js:538`), and used across the catalog.
- followUp tests / role levels / family checked against `_templates/signal-types.json` and `_templates/role-levels.json` — all valid.

## Ongoing Review Checklist

- Do model answers continue to demonstrate the measurement and residual-cost honesty the spec demands?
- Are example stories diverse enough to avoid over-fitting to one strategy archetype?
- Does each resource carry specific (not generic) relevance, with no near-duplicates, and is there modality variety beyond books?
- Are manifest display names and interview titles consistent?
- Do newly added example stories either carry an `aiVisual` or deliberately omit it?

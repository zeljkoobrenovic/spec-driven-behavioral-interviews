# Review

## File
`data/book/engineer-collaboration-feedback/interview.json`

## Purpose
Critique this interview spec for realism, balance, educative value, interviewer usability, spec quality, and external resources, then list the next edits worth making.

## Rating Scale
1 = weak, 2 = below bar, 3 = solid, 4 = strong, 5 = exemplary.

## Snapshot
- Competency: Collaboration and Feedback (`Influence and Communication`).
- Role focus: Software Engineer, Senior Software Engineer, Tech Lead. Difficulty: intermediate.
- Primary prompt: "Tell me about a time feedback from another engineer changed your approach."
- **4 example stories** across 3 levels (SE, Senior, and two Tech Lead variants), 4 prompt variants, 4 interviewer-intent items.
- **4 follow-ups**, each with strong/weak calibration answers.
- **4 evaluation signals**, 3-level rubric.
- `python3 _scripts/validate_interviews.py` passes (28 datasets, clean).
- `python3 _scripts/summarize_coverage.py` runs clean.

## What Changed Since The Previous Review
The spec was expanded after the first review and is meaningfully stronger:
- Added a fourth example story, `risky-refactor-feedback` (Tech Lead): an engineer rewrites the authorization-cache path inside a permissions bug fix two days before freeze, with a 30-comment review thread. This implements the previous review's optional recommendation #3 (giving hard feedback) and adds the most realistic, highest-stakes scenario in the set.
- Grew from 3 to **4 evaluation signals** — `scope-tradeoff-discipline` and `shared-learning` are now first-class, and `visualizations.signalMap` lists all four correctly.
- Added a fourth prompt variant ("Describe a time when you had to give feedback to another engineer") and a fourth interviewer-intent line, both tied to the new story.
- Follow-up `exampleAnswers` now thread the new auth-refactor case through `changed-mind`, `disagreement-quality`, `feedback-given`, and `team-learning`, so all four follow-ups are calibrated against the hardest story.
- **Still no `toProbeFurther.links[]`** — the previous review's #1 gap is unaddressed and remains the single highest-value fix.

## Overall Assessment
A strong, well-constructed entry — clearly the work of someone who has actually run code-review disagreements. The throughline (move from defending the solution to naming the failure mode the feedback was trying to prevent, then choosing the smallest responsible change) is concrete and reinforced consistently across `storyAnatomy`, `strongAnswerPattern`, the four signals, and follow-up calibration. The fourth story tightens scope-and-trade-off discipline into a vivid, time-boxed scenario and lifts the Tech Lead level. It validates cleanly and is internally consistent. The one notable gap is structural and shared with the rest of the newer role-specific batch (engineer-*, pm-*, product-*, tech-lead-influence, engineering-manager-*): no `toProbeFurther.links[]` reading list. Indicative score: **4.4 / 5** (up from 4.2).

## Review Dimensions
- Realism — **5** (up from 4). The two signature scenarios — a batch-update API returning partial success where another team must guess which records are safe to retry, and a release-eve auth-cache refactor that silently changes stale-token behavior mobile clients depend on — are both genuine, messy review situations with schedule pressure, cross-team stakes, and a thread that has already gone sour. Disagreement, rejected alternatives, residual cost, and scope control are all present and specific.
- Balance — **5** (up from 4). Covers receiving and giving feedback, agreeing and principled disagreeing, the "help without taking over" axis, and now blocking-a-risky-change-without-crushing-the-teammate. The escape from "process creation always wins" is handled well: the monolith-vs-service story rewards *not* extracting a service yet and recording an extraction trigger, and the refactor story rewards keeping the minimal fix while crediting the valid concern. Weak answers correctly flag over-deference to seniority, harmony-preservation, and treating feedback as all-or-nothing.
- Educative Value — **5**. Strong/weak contrasts teach a listenable behavior, not a slogan. The follow-up `exampleAnswers` remain the standout: "I moved the debate out of a 40-comment review thread into a 20-minute design review" vs. "I tried to stay polite and not take it personally" makes the evaluation logic explicit. The new signal `scope-tradeoff-discipline` ("accepted, rejected, or deferred ... the decision rule used, and the residual cost") names exactly what an interviewer should listen for.
- Interview Usability — **5** (up from 4). Four prompt variants now each map to a distinct example story and gather different evidence (received feedback / disagreed / helped a teammate / gave hard feedback). Follow-ups expose evidence rather than restating the prompt. The rubric separates levels by *scope of mechanism* (changes own work → improves team decision quality → builds collaboration mechanisms), a clean, usable distinction.
- Spec Quality — **5**. Complete against the data model, ids stable and cross-referenced correctly (`visualizations.signalMap` and `followUpTree` match the actual signal/follow-up ids; all four signals are present and listed), `**bold**` unused/sparse, dataset `id` matches manifest. Validates clean across 28 datasets.
- External Resources — **1**. No `toProbeFurther` section at all (see Gaps). This is the only thing holding the overall score below the established leadership-judgment datasets.

## Strengths
- The "name the failure mode, then choose the smallest responsible change" frame is a single teachable idea carried consistently through every section.
- Calibration `exampleAnswers` on all four follow-ups; weak versions are realistic, not strawmen.
- The new `risky-refactor-feedback` story tests a real, high-stakes, rarely-probed signal: blocking unsafe scope late in a release while crediting the valid concern and naming the residual cost (duplicate cache branches for one sprint, with owner and removal date).
- The Tech Lead "debug without taking over" story tests building capability vs. rescuing.
- Rubric levels and signals are distinguished by the *durability and scope of the mechanism* and by accept/reject/defer discipline, not by adjectives.

## Gaps And Risks
1. **No `toProbeFurther.links[]` (highest-value fix, unchanged).** Confirmed still absent here and across the newer role-specific batch (engineer-ownership, pm-*, product-*, tech-lead-influence, engineering-manager-* all show `toProbeFurther=0`). The dimension scores 1 only because the section is absent — adding 3–5 canonical links would likely move it to 4–5. Candidate sources for this topic: Google's Code Review Developer Guide (canonical reviewer/author norms), Conventional Comments (decorating review feedback by intent), *Radical Candor* (Kim Scott — care personally / challenge directly), *Crucial Conversations*, and Derek Prior's "Implementing a Strong Code-Review Culture" talk. Link to canonical publisher/author/spec pages, one-sentence `why` each, no obren.io bookshelf notes, no duplicate books. Use the `research-external-links` skill.
2. **No visual assets.** `assets.icon`, `explainerComic`, and per-signal/example `aiVisual` paths are absent (grep confirms zero). Optional, but the dataset reads visually barer than the established set. Lower priority than the reading list.
3. **Follow-up test tags lean soft.** Tags used: `learning`, `technical judgment`, `influence`, `stakeholder alignment`, `ownership`, `accountability`, `measurement`. `changed-mind` is now substantially about weighing per-record status vs. duplicate-update risk and stale-token compatibility cost — consider adding `trade-off reasoning` (heavily used elsewhere) to that probe, since the new fourth story made it even more trade-off-heavy.
4. **Minor: level coverage is now two Tech Lead stories and one each for SE/Senior.** Good depth at Tech Lead; the most commonly interviewed level (Senior) still has a single story. A second Senior-level variant (e.g. giving difficult feedback *upward* to a more senior engineer, distinct from the Tech Lead authority case) would be the next breadth improvement. Optional.

## Priority Recommendations
1. Add a `toProbeFurther.links[]` section with 3–5 researched, canonical, non-duplicate resources and a one-sentence `why` each (use the `research-external-links` skill). This is the single edit that most closes the remaining gap with the mature datasets.
2. (Optional) Add `trade-off reasoning` to the `changed-mind` follow-up `tests` tags now that the fourth story leans hard on weighing options.
3. (Optional) Add `assets.icon` and one or two `aiVisual` paths to match catalog visual density.
4. (Optional) Add a second Senior-level example story (difficult feedback upward) to deepen the most-interviewed level.

## Verification Run For This Review
Only `REVIEW.md` was changed, so no build is required. Data checks were run for context and pass:
- `python3 _scripts/validate_interviews.py` → ok, 28 datasets.
- `python3 _scripts/summarize_coverage.py` → clean.

If recommendation 1, 2, or 3 is implemented, run the full sequence:
`validate_interviews.py` → `summarize_coverage.py` → `node --check` (both JS) → `build.py` → `smoke_static_site.py`.

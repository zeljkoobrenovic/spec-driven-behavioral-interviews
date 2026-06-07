# Review

## Purpose

Documented review of `data/book/interview-method/interview.json` against the
project review dimensions (realism, balance, educative value, interview
usability, spec quality, external resources). This dataset is the catalog's one
`foundational` entry: a meta-interview that teaches the Situation → Task →
Action → Result → Reflection → System Change answer method rather than testing a
single competency. It is the intended on-ramp to the other 27 datasets.

_Last updated after the follow-up revision that added a seventh worked example:
a Tech Lead platform migration story. This acts on the prior optional guidance to
prefer an unmodeled middle tier and a platform / infra context if the example set
grew. The earlier broadening still holds: `roleFocus` and the `rubric` span the
full engineering ladder (Software Engineer → CTO) and the full product ladder
(Product Manager → VP Product), and the external-resource list has ten entries._

## Rating Scale

5 excellent · 4 strong · 3 acceptable · 2 weak · 1 poor.

## Current Snapshot

- File: `data/book/interview-method/interview.json`
- Group / category: `method` / Interview Method (the only dataset in the group)
- Competency family: Interview Method (`structured-storytelling`)
- Difficulty: `foundational` (the only non-`advanced`/`intermediate` dataset in
  the catalog)
- Role focus: **14 roles** — Software Engineer → CTO and Product Manager → VP
  Product. Matches the 14-row `rubric` one-to-one.
- Example stories: **7** — Software Engineer (defect ownership), Product Manager
  (discovery trade-off), Tech Lead (platform migration), Engineering Manager
  (delivery + coaching), Director (cross-team conflict compression), Director of
  Product (consumer-app portfolio trade-off), CTO (company-level strategy
  framing). The Tech Lead story adds the previously unmodeled middle-tier and
  platform / infra context.
- Visual assets: `assets.icon` (`icon.png`) only. No `aiVisual` fields anywhere
  (a deliberate simplification — the prior review's example-story visual-parity
  gap no longer applies because there are no example visuals to be inconsistent).
- Data checks: `validate_interviews.py` passes (28 datasets, 1 group);
  `summarize_coverage.py` clean. The referenced `icon.png` exists on disk.
- External links: **10** resources across four groups (Interviewing and
  Calibration; Behavioral Storytelling; Behavioral Interview Research; Level
  Calibration and Technical Leadership Prep). 6 resolve HTTP 200; 4 return 403
  to automated requests (the three academic DOIs/SagePub articles and the
  O'Reilly appendix — publisher bot-blocks, not dead links).

## Overall Assessment

A genuinely strong meta-interview and the right thing to teach first: it makes
the answer shape and the evaluation logic explicit before a reader reaches the
harder advanced cases. The broadening from a senior-leadership method to a
cross-role method is a clear improvement — the method is now demonstrably the
same from IC to CTO and from PM to VP Product, which is exactly the claim a
foundational dataset should make, and the seven example stories now show that
range concretely instead of asserting it. The strong/weak pairs, the red-flag
list, and the probe-level `exampleAnswers` make "what good looks like" the most
explicit in the catalog.

This revision closes the previously optional platform / middle-tier note. The
sampling is named explicitly — `scenario.context` states that the worked examples
are *samples* of one method across levels, so a reader at an unmodeled tier knows
to map onto the nearest example. The Director of Product portfolio trade-off
reaches into the upper product ladder and is deliberately set in a
**consumer / trust** context, while the new Tech Lead platform migration story
shows peer influence, technical compromise, and right-sized system change outside
an incident or executive strategy frame.

The remaining weaknesses are minor and mostly about coverage breadth versus the
expanded ladders: seven worked examples still stand in for fourteen rubric
levels, so the Senior IC / Senior EM tiers and parts of the upper product ladder
(Senior PM, Group PM, VP Product) have a rubric row but no worked story. With the
sampling now named explicitly, this is a deliberate and well-communicated choice
rather than an unstated gap.

Composite: **4.8 / 5**.

## Strengths

- **Teaches the method, not a script.** `storyAnatomy`, `practiceTemplate`, and
  the example `weakVersion`/`whyItWorks` pairs consistently show the concrete
  behavior to listen for (e.g. "Names the **trade-off** between reverting quickly
  and preserving a data migration that was already partially complete") rather
  than slogans like "align stakeholders". The spec follows its own advice.
- **The cross-role claim is now demonstrated, not asserted.** Seven example
  stories span an IC defect-ownership story, a PM discovery trade-off, an EM
  delivery/coaching story, a Tech Lead platform migration, a Director
  conflict-compression story, a Director of Product portfolio trade-off, and a
  CTO strategy story. The IC example is
  especially valuable: it shows ownership "at IC scope without pretending to own
  the whole incident program" and ends with a team-level mechanism "credible for
  an engineer to introduce" — modeling right-sized system change, which is the
  move candidates most often overscope.
- **The product ladder and a non-enterprise context are now both modeled.** The
  new `product-leader-portfolio-tradeoff` story reaches the upper product ladder
  (Director of Product) and is set in a consumer app around privacy controls and
  first-run trust — the one example that does not sit in an enterprise-SaaS frame.
  It models portfolio-level product compression ("one decision, one rejected path,
  one residual cost, and one repeatable funding mechanism") that the prior five
  examples did not, and its `followUpAngles` and the matching `exampleAnswers`
  for the ownership/alternatives/measurement follow-ups were extended in step.
- **Models story selection and compression.** The Director, Director of Product,
  and CTO examples explicitly frame the hardest interview skill — *choosing and
  compressing the right story* (e.g. resisting "a ten-minute org-history tour",
  compressing a company-level story "into one decision and one durable
  mechanism"). No other dataset in the catalog targets this.
- **Follow-ups carry calibration snippets.** Each of the four `followUps`
  (ownership, alternatives, measurement, learning) has strong/weak
  `exampleAnswers` that reference the example stories by name and stay concrete
  (e.g. rejecting "a broad regression suite" for "a performance budget on the
  affected path plus an alert tied to checkout success"). Exactly the AGENTS.md
  guidance for probe-level calibration.
- **Weak-answer red flags are excellent real-time diagnostics.** "Uses *we* more
  than *I*", "vanity metrics", "reflection is a slogan", "mechanism is too grand
  for the candidate's role" are all things an interviewer can hear in the moment.
- **The `learning-loop` signal now encodes the scaling ladder.** Its strong text
  ("personal practice, team ritual, product decision rule, org governance,
  portfolio rule, or company policy") addresses the prior review's complaint that
  the signal did not differentiate by level — the level progression is now
  explicit in the signal itself, and mirrored in the `weak` clause ("oversized
  process disconnected from the story's scope").
- **On-topic, credible, well-grouped resources.** The ten links are organized
  into four coherent groups with group descriptions, mix practitioner guidance
  (GOV.UK, OPM, DDI/MIT/Amazon on STAR) with the underlying competency research
  (McClelland, Campion, Levashina) and level-calibration sources (Larson,
  StaffEng), each with a crisp one-sentence `why` and no duplicate book/article.
- **Self-consistent vocabulary.** `visualizations.signalMap`, `followUpTree`,
  and `evaluation.signals[]` align; `timeline` matches the six-part story shape
  the spec teaches; `roleFocus` and the `rubric` levels match one-to-one; the
  manifest `id` matches the `interview.json` `id`.

## Gaps And Risks

1. **Seven worked examples cover fourteen rubric levels — now named as sampling.**
   The expansion of `roleFocus`/`rubric` to the full IC, EM, and product ladders
   still leaves several levels with a rubric row but no example story: Senior
   Software Engineer, Senior Engineering Manager, Senior Manager, VP Engineering,
   and parts of the upper product ladder (Senior PM, Group PM, VP Product). The
   prior review flagged this as an unstated gap; `scenario.context` now states
   explicitly that the worked examples are *samples* of one method across levels
   and tells the reader to map their own role to the nearest scope. That converts
   the gap from a risk into a deliberate, communicated design choice.
2. **Context variety is stronger, with one residual executive skew.** The
   examples now include customer-facing defect recovery, product discovery, a
   platform migration, team delivery, cross-functional conflict, consumer product
   portfolio strategy, and company-level strategy. The Director and CTO examples
   still sit in an enterprise-SaaS frame, which is acceptable for those levels but
   worth watching if more executive examples are added.
3. **Four external links are bot-blocked (not dead).** The three academic
   sources on SagePub/Wiley (McClelland, Campion, Levashina via the `peps.12052`
   DOI) and the O'Reilly appendix return 403 to automated requests. The DOIs,
   titles, authors, and the O'Reilly URL are real and canonical; this is a
   verification note, not a break. The other six resolve 200.
4. **Group is a singleton.** `method` contains only this dataset, so the overview
   renders a one-item category. Fine and arguably correct for a foundational
   on-ramp.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 5 | All seven examples carry real conflict, rejected alternatives, residual cost, and mixed-outcome framing. Necessarily somewhat abstract by design (it teaches a method, not one scenario), but the examples now span incident, discovery, platform, delivery, conflict, portfolio, and strategy frames. |
| Balance | 5 | Rewards ownership, trade-offs, *and* compression/story-selection, and now demonstrably across IC → CTO and PM → Director of Product, in enterprise, consumer, and platform contexts. The method is shown to be scope-invariant, with right-sizing built into the signals and rubric. |
| Educative Value | 5 | The clearest "what good looks like" in the catalog: strong/weak pairs, red-flag diagnostics, and probe-level `exampleAnswers` that cite the example stories make the evaluation logic fully explicit. |
| Interview Usability | 5 | Prompt, three variants, and four follow-ups with strong/weak calibration snippets expose evidence directly and help an interviewer score against the rubric fairly. |
| Spec Quality | 5 | Validates clean; ids/paths stable; `icon.png` present; `roleFocus`↔`rubric` and `signalMap`↔`signals` aligned; manifest id matches. |
| External Resources | 4 | Credible, on-topic for the *method*, well grouped, crisp `why` notes, no duplicate book/article links, links only in To Probe Further. Loses a point only because four URLs are bot-blocked and warrant a periodic manual render check. |

## Priority Recommendations

The prior priority recommendations and the optional platform / middle-tier note
are now **done**: the sampling is named explicitly in `scenario.context`, a
Director of Product example covers the upper product ladder and a consumer /
trust context, and a Tech Lead example covers platform influence. What remains:

1. **Periodically verify the four bot-blocked links** render in a browser. The
   three academic DOIs and the O'Reilly appendix are real and canonical; 403 is a
   publisher bot-block, so this is verification, not a known break.
2. **(Optional) Watch remaining ladder gaps if more examples are added.** Prefer
   Senior Software Engineer, Senior Engineering Manager, Senior PM, Group PM, or
   VP Product over another Director / CTO example. Defer if seven is the intended
   cap.

## Per-Interview Review

### `data/book/interview-method/interview.json` — Rating 4.8 / 5

- **Strengths:** Best teaching artifact in the catalog; seven probeable example
  stories that *demonstrate* one method across the engineering and product
  ladders and across enterprise, consumer, and platform contexts; story-selection
  and compression modeled where no other dataset does; the sampling is named
  explicitly so the rubric-vs-example delta is a stated design choice; probe-level
  strong/weak calibration snippets that cite the examples; `learning-loop` signal
  encodes the right-sizing ladder; ten on-topic, well-grouped, credible resources;
  fully validating spec with the icon present.
- **Main risks:** seven examples stand in for fourteen rubric levels; Senior
  Software Engineer, Senior EM, Senior PM, Group PM, and VP Product remain modeled
  only by the rubric; four resource URLs are bot-blocked (not dead).
- **Recommended next edits:** none required — prior recommendations are done.
  Periodically verify the bot-blocked links render; if the example set grows,
  prefer one of the remaining unmodeled levels over another top-of-ladder story.

## Ongoing Review Checklist

- [ ] Re-run `python3 _scripts/validate_interviews.py` and
      `python3 _scripts/summarize_coverage.py` after any data edit.
- [ ] After editing `data/`, run `python3 build.py` then
      `python3 _scripts/smoke_static_site.py`.
- [ ] Keep `roleFocus` and the `rubric` levels in one-to-one alignment (currently
      14↔14 — preserve this), and keep example-story `level` values pointing at
      real rubric rows.
- [ ] Keep `why` notes to one concrete sentence; avoid hedged phrasing.
- [ ] Re-check external links periodically; do not link `obren.io` bookshelf
      pages directly, and avoid duplicate book/article entries.

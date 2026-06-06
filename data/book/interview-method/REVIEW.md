# Review

## Purpose

Documented review of `data/book/interview-method/interview.json` against the
project review dimensions (realism, balance, educative value, interview
usability, spec quality, external resources). This dataset is the catalog's one
`foundational` entry: a meta-interview that teaches the Situation → Task →
Action → Result → Reflection → System Change answer method rather than testing a
single competency.

_Last updated after the recent content revision that expanded the example
stories to four levels and replaced the external-resource list with
interview-method sources._

## Rating Scale

5 excellent · 4 strong · 3 acceptable · 2 weak · 1 poor.

## Current Snapshot

- File: `data/book/interview-method/interview.json`
- Group / category: `method` / Interview Method (only dataset in the group)
- Competency family: Interview Method (`structured-storytelling`)
- Difficulty: `foundational` (the only non-`advanced` dataset in the catalog)
- Role focus: Senior Manager, Director, VP Engineering, CTO
- Example stories: **4** — now one per claimed level (Senior Manager →
  planning-cadence, Director → outage selection, VP Engineering →
  conflict compression, CTO → strategy framing).
- Data checks: `validate_interviews.py` passes (16 datasets);
  `summarize_coverage.py` clean. All 12 referenced visual assets and `icon.jpg`
  exist on disk.
- External links: **6** resources (GOV.UK, OPM, DDI STAR, MIT STAR, Amazon,
  McClelland). 5 return HTTP 200; the SagePub/McClelland DOI returns 403
  (publisher bot-block, not a dead link).

## Overall Assessment

A genuinely strong meta-interview and an effective on-ramp to the rest of the
catalog. It is the right thing to teach first: it makes the answer shape and the
evaluation logic explicit before a reader reaches the harder advanced cases. The
recent revision closed the two largest gaps the prior review flagged — all four
claimed levels now have a worked example story, and the external-resource list
is now coherent and on-topic for the *method* (structured interviewing + STAR +
the underlying competency research) rather than a leadership-reading list. The
example stories are concrete and probeable, the signals are specific, and the
weak-answer red flags are well chosen.

Remaining weaknesses are minor: one signal (`learning-loop`) still does not
differentiate by level the way `ownership` and `trade-offs` implicitly do, the
two newer example stories lack the `aiVisual` parity of the original two, and
the four `followUps` carry rich `exampleAnswers` while the example stories and
signals could lean on them more.

Composite: **4.5 / 5** (up from 4.3 — the level-coverage and resource gaps are
resolved).

## Strengths

- **Teaches the method, not a script.** `storyAnatomy`, `practiceTemplate`, and
  the example `weakVersion`/`whyItWorks` pairs consistently show the concrete
  behavior to listen for (e.g. "Names the **trade-off** between fast rollback
  and data consistency risk") rather than slogans like "align stakeholders".
- **All four levels are now modeled.** The four `exampleStories` cover Senior
  Manager (planning cadence), Director (outage selection), VP Engineering
  (executive conflict), and CTO (company-level strategy). The Senior Manager
  example is especially valuable because it shows a *non-incident, non-conflict*
  story still revealing senior judgment — a case readers most often get wrong.
- **Example stories model story selection and compression.** Both the outage and
  the Sales/Product/Finance conflict model the hardest interview skill — *choosing
  and compressing the right story* — which no other dataset in the catalog targets.
- **Follow-ups now carry calibration snippets.** Each of the four `followUps`
  (ownership, alternatives, measurement, learning) has strong/weak
  `exampleAnswers`, and they are concrete (e.g. "62% to 84% delivered within the
  agreed window") — exactly the AGENTS.md guidance for probe-level calibration.
- **Weak-answer red flags are excellent diagnostics.** "Says *we* more than *I*",
  "vanity metrics", "reflection is a slogan" are exactly what an interviewer can
  hear in real time.
- **On-topic, credible resources.** The new resource set (GOV.UK and OPM on
  structured interviewing, DDI/MIT/Amazon on STAR, McClelland on
  behavioral-event interviewing) is well matched to a *method* interview, with
  crisp one-sentence `why` notes and no duplicate book/article links.
- **Self-consistent vocabulary.** `visualizations.signalMap`, `followUpTree`,
  and `evaluation.signals[]` all align; the timeline matches the six-part story
  shape the spec teaches.

## Gaps And Risks

1. **`learning-loop` signal does not differentiate by level.** Its strong/weak
   text is good, but compared with `ownership` and `trade-offs` it reads
   identically across Senior Manager and CTO. The rubric distinguishes levels;
   the signal could hint at how the *durable mechanism* scales (team ritual →
   org governance → company policy). This is the one substantive content gap
   that survived the revision.
2. **Visual-asset parity across example stories.** The original two example
   stories (`outage-story-selection`, `compressing-complex-conflict`) have
   `aiVisual` images; the two newer ones (`planning-cadence-story`,
   `strategy-story-framing`) do not. `aiVisual` is optional, so this is not a
   validation failure — but the asymmetry will show in the rendered page.
   Either generate the two missing visuals or accept the gap deliberately.
3. **One external link is bot-blocked (not dead).** The McClelland article on
   SagePub returns 403 to automated requests. The DOI and title are real; this
   is a verification note, not a break. The remaining five resolve 200.
4. **Group is a singleton.** `method` contains only this dataset. Fine for now,
   but the overview will render a one-item category.

## Review Dimensions

| Dimension | Score | Notes |
|---|---|---|
| Realism | 4 | Examples carry real conflict, rejected alternatives, and mixed-outcome framing across all four levels. Slightly abstract by design (it is a method, not a scenario). |
| Balance | 5 | Rewards ownership, trade-offs, *and* compression/story-selection across Senior Manager → CTO. The level-coverage gap that cost a point previously is now closed. |
| Educative Value | 5 | The clearest "what good looks like" in the catalog; strong/weak pairs, red flags, and now probe-level `exampleAnswers` make the evaluation logic explicit. |
| Interview Usability | 5 | Prompt, variants, and four follow-ups with strong/weak calibration snippets expose evidence directly and help an interviewer score fairly. |
| Spec Quality | 5 | Validates clean; ids/paths stable; all 12 assets present; manifest id matches `interview.json` id. |
| External Resources | 4 | Credible, on-topic for the method, crisp `why` notes, no duplicate book/article links, links only in To Probe Further. One URL is bot-blocked (not dead); loses a point only pending a manual render check. |

## Priority Recommendations

1. **Sharpen the `learning-loop` signal** to show how the durable mechanism
   scales by level (team ritual → org governance → company policy), matching the
   rubric's progression. Highest-value remaining content edit.
2. **Resolve example-story visual parity** — generate `aiVisual` images for
   `planning-cadence-story` and `strategy-story-framing` (via the
   `generate_example_story_pictures.py` flow, `--dry-run` first) so all four
   example stories render consistently, or accept the gap on purpose.
3. **Confirm the McClelland/SagePub link** renders in a browser; the DOI is
   real and 403 is a publisher bot-block, so this is verification, not a known
   break.

## Per-Interview Review

### `data/book/interview-method/interview.json` — Rating 4.5 / 5

- **Strengths:** Best teaching artifact in the catalog; four probeable example
  stories spanning every claimed level; story-selection and compression modeled
  where no other dataset does; probe-level strong/weak calibration snippets;
  on-topic credible resources; fully validating spec with all assets present.
- **Main risks:** `learning-loop` signal not level-differentiated; the two newer
  example stories lack `aiVisual` parity; one resource URL is bot-blocked
  (not dead).
- **Recommended next edits:** make the `learning-loop` signal scale by level;
  add (or deliberately defer) the two missing example-story visuals; manually
  verify the McClelland link renders.

## Ongoing Review Checklist

- [ ] Re-run `python3 _scripts/validate_interviews.py` and
      `python3 _scripts/summarize_coverage.py` after any data edit.
- [ ] After editing `data/`, run `python3 build.py` then
      `python3 _scripts/smoke_static_site.py`.
- [ ] Keep example-story levels aligned with `roleFocus` and the `rubric`
      (currently all four covered — preserve this).
- [ ] Keep `why` notes to one concrete sentence; avoid hedged phrasing.
- [ ] Re-check external links periodically; do not link `obren.io` bookshelf
      pages directly, and avoid duplicate book/article entries.

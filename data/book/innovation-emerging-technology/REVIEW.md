# Review — Innovation and Emerging Technology

File: `data/book/innovation-emerging-technology/interview.json`

## Purpose

Single-interview review against the project's realism, balance, educative value,
interviewer usability, spec quality, and external-resources dimensions.

## Rating Scale

1 weak, 2 below par, 3 solid, 4 strong, 5 exemplary.

## Current Snapshot

- Competency: Innovation and Emerging Technology (family: Risk, Ethics, and Innovation).
- Difficulty: advanced. Role focus: Senior Manager, Director, VP Engineering, CTO.
- 4 example stories spanning all four role levels: AI-assisted development (VP),
  customer-support automation pilot (Senior Manager), internal platform trial that
  did not roll out (Director), and a company-level AI portfolio posture (CTO).
- 4 signals, 5 follow-ups (each with strong/weak `exampleAnswers`), 4-level rubric,
  9 external links.
- `validate_interviews.py` and `summarize_coverage.py` both pass; all follow-up
  test tags resolve against the canonical vocabulary.

## Overall Assessment

A strong, well-rounded spec (~4.3/5 average). The previous revision's main gaps
have been closed: the CTO level is now illustrated by a portfolio-posture story,
the rubric/`roleFocus` level ladder is consistent (Senior Manager is in both), a
non-engineering adoption example (support automation) broadens the technology mix,
every follow-up now carries calibration snippets, and the reading list has been
re-anchored on experimentation/measurement rather than the responsible-AI cluster
that overlapped the sibling ethics interview. The standout strength remains that
the catalog of stories includes a genuine *negative* result and a *narrowed* result,
which teach the most-faked behavior in this competency: the willingness to stop or
shrink scope on evidence. Remaining notes are minor polish rather than structural
gaps.

## Strengths

- **Full role ladder, each level shown.** All four rubric levels now have a matching
  example story at the right altitude — Senior Manager (single-queue support pilot),
  Director (platform trial), VP (org-wide AI-assisted dev), CTO (company portfolio
  posture). An interviewer calibrating any of the four has a concrete model answer.
- **Stories teach stopping and narrowing, not just shipping.** `internal-platform-trial`
  rewards killing an exciting pilot on operational evidence; `support-operations-automation`
  scales a *smaller* scope than the original savings case and names the metric that
  stopped part of the rollout; `company-ai-portfolio-posture` parks executive-sponsored
  demos. This trio is the spec's best feature — it makes "disciplined refusal" the
  default, not an afterthought.
- **Breadth across technology types.** Examples now span developer tooling, customer
  support automation, internal platform infrastructure, and company-level build/buy/wait
  posture — honoring the "AI, automation, platforms, or emerging technology" claim
  instead of overfitting to the AI-coding-tools moment.
- **Sharp weak versions and red flags.** "I bought AI coding licenses... and tracked
  adoption" and "selected the most promising demos... so executives could see
  momentum" cleanly isolate the usage-vs-impact and hype-vs-hypothesis confusions the
  rubric targets.
- **Coherent evidence chain with calibration snippets.** Hypothesis → risk controls →
  impact → adoption behavior → portfolio is a clean follow-up sequence; every probe
  now includes strong/weak `exampleAnswers`, and the strategic-portfolio signal ties
  the bets back to opportunity cost and build/buy/wait reasoning.

## Gaps And Risks

1. **Minor — measurement vocabulary leans heavily on AI/dev metrics (educative).**
   The strong follow-up answers and story sketches are rich on review lead time,
   defect escape, reopen rate, and CSAT. The platform-trial and portfolio stories
   are comparatively thinner on hard numbers (the portfolio story has "vendor spend
   fell 22%", the platform story has none). Adding one concrete operational metric to
   the platform-trial sketch would keep the measurement bar uniform across levels.

2. **Minor — `interviewerIntent` and signals slightly overlap (spec polish).** The
   fourth intent ("connect technology bets to strategy, opportunity cost, and
   portfolio choices") and the strategic-portfolio signal cover the same ground as
   the portfolio follow-up. This is fine for reinforcement, but if trimming for length
   the intent line is the most redundant.

3. **Minor — `nist-ai-rmf` still shared with the ethics interview (resources).** This
   is now the only substantive overlap (plus the catalog-wide GOV.UK structured-interview
   link) and is defensible: NIST AI RMF is the single canonical responsible-AI anchor and
   each interview frames it differently (risk governance here, fairness/privacy there).
   No change required; noting it so a future audit does not re-flag it as accidental
   duplication.

## Review Dimensions

- Realism: 5 — credible constraints (security/legal disagreement, exec and board
  pressure, vendor demos, individual experimentation) plus genuine negative and
  narrowed outcomes across multiple, distinct situations.
- Balance: 4 — strong across technology types (dev tooling, support automation,
  platform, portfolio) and across the experiment / scale / narrow / stop / defer axis;
  loses a point only because measurement detail is unevenly distributed across levels.
- Educative Value: 5 — explicit moves, sharp weak versions, clear red flags, all four
  levels illustrated, and probe-level strong/weak `exampleAnswers` throughout.
- Interview Usability: 5 — variants change the evidence gathered, follow-ups expose
  concrete behavior, the rubric ladder is consistent with `roleFocus`, and each level
  has a backing example.
- Spec Quality: 5 — validates cleanly, level ladder is internally consistent, signals
  map to the follow-up tree and signal map.
- External Resources: 4 — every link has a one-sentence relevance note, all are
  canonical non-Obren sources, and the list is now innovation-anchored
  (Lean Startup, Experimentation Works, Trustworthy Online Controlled Experiments,
  DORA gen-AI adoption, SPACE) rather than tilted toward responsible-AI frameworks.

## Priority Recommendations

All previously flagged structural gaps (CTO model answer, rubric/`roleFocus`
mismatch, dev-tooling overfit, missing probe `exampleAnswers`, responsible-AI
resource overlap) have been addressed in the current revision. Remaining items are
optional polish:

1. Add one concrete operational metric to the `internal-platform-trial`
   `strongAnswerSketch` so the measurement bar is uniform across all four levels.
2. Optionally trim the fourth `interviewerIntent` line, which restates the
   strategic-portfolio signal and portfolio follow-up.

## Verification

REVIEW.md-only change; no build required. If the interview JSON is later edited,
run: `validate_interviews.py`, `summarize_coverage.py`, `build.py`,
`smoke_static_site.py`.

# Review — Executive Communication

File: `data/book/executive-communication/interview.json`
Reviewed: 2026-06-06 (updated after recent edits)
Validation: `validate_interviews.py` passes (16 datasets ok); `summarize_coverage.py` clean.

## Rating Scale

1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Concise Rating

| Dimension | Score | Note |
| --- | --- | --- |
| Realism | 5 | Migration delay now carries named CEO/CFO pressure; new launch-risk example adds messy cross-functional conflict. |
| Balance | 5 | Rewards honest uncertainty *and* decisiveness *and* holding a line under pushback; no single-behavior bias. |
| Educative Value | 5 | Strong/weak patterns, per-signal contrasts, and now strong/weak `exampleAnswers` on every follow-up teach concrete listenable behaviors. |
| Interview Usability | 5 | All three variants are backed by a distinct example; follow-ups now ship calibrated strong/weak answers. |
| Spec Quality | 4 | Internally consistent again (rubric ↔ roleFocus aligned). One remaining family-convention divergence noted below. |
| External Resources | 4 | Credible, canonical, one-line relevance notes; mild conceptual overlap among comms books persists. |

## What Changed Since Last Review

The recent edits directly resolved the two priority findings from the prior review and
added meaningful depth:

- **Resolved — rubric / roleFocus mismatch.** The previous review flagged that the
  rubric carried a **Senior Manager** row absent from `roleFocus`. The edit removed the
  Senior Manager rubric row, so the rubric is now Director → VP Engineering → CTO,
  matching `roleFocus` exactly. The internal inconsistency is gone. (See remaining
  family-consistency note below — the divergence direction is worth a conscious sign-off.)
- **Resolved — third variant now has a backing example.** A new Director-level
  `enterprise-launch-risk-briefing` story backs the "explain technical risk to a board"
  variant, so all three prompt variants now exercise distinct evidence (board migration,
  enterprise launch risk, security uncertainty).
- **Added — pushback and decision-threshold thread.** A new constraint ("Executives may
  push for a single date, status color, or low-cost answer before evidence is complete"),
  a new `storyAnatomy` action and result, and new strong/weak-pattern lines now reward
  staying clear under executive pressure rather than retreating into technical detail.
- **Added — `exampleAnswers` on all four follow-ups.** Each follow-up (`audience`,
  `uncertainty`, `options`, `format`) now carries calibrated strong and weak answers,
  materially raising interviewer usability and educative value.

## Strengths

- **Decision-first framing is taught explicitly, not asserted.** The strong pattern's
  "Starts from the executive decision, not the technical narrative" against the weak
  pattern's "Explains the problem but not the decision" gives a sharp, observable contrast.
- **Pushback is now a first-class signal.** The migration example's CEO-wants-one-date /
  CFO-challenges-spend framing and the new weak red flag ("Claims executives aligned but
  cannot describe what they challenged") teach interviewers to probe how a candidate held
  a line, not just whether they communicated.
- **Uncertainty is handled honestly without rewarding evasion.** The security example's
  weak version ("we were investigating and would provide details once Security had
  confirmed") is a realistic, plausible-sounding miss — deferral disguised as diligence.
- **Follow-up `exampleAnswers` are well-calibrated.** The weak answers are plausible, not
  strawmen (e.g. "an update on the risk so they would not be surprised later"), which makes
  the strong/weak boundary teachable rather than obvious.
- **Story shape is complete and senior.** Situation → Task → Action → Result → Reflection
  → System Change is fully populated, and `systemChange` lists durable mechanisms
  (risk-brief template, decision-options format, update cadence).
- **Rubric ladders cleanly by scope** (cross-team → organizational → company/board).

## Gaps and Risks

### 1. Family-convention divergence on role coverage (judgment call — please confirm)

The rubric/`roleFocus` inconsistency was fixed by *removing* Senior Manager, leaving a
three-role ladder (Director, VP Engineering, CTO). Both sibling interviews in the
*Influence and Communication* family — `executive-conflict` and
`cross-functional-influence` — carry all **four** roles including Senior Manager. So the
internal inconsistency is resolved, but the interview now diverges from family convention.

This is a defensible editorial position: "Executive Communication" to a board is
genuinely more senior than team-level work, so dropping the Senior Manager baseline is
reasonable. Flagging it only so the choice is deliberate rather than accidental. If
catalog uniformity is preferred, the alternative is to restore a Senior Manager rubric row
*and* add Senior Manager to `roleFocus` (e.g. "Explains team-level technical risk clearly
to non-technical partners"). No action required if the three-role scope is intended.

### 2. Mild conceptual overlap in the resource list (subjective, unchanged)

`toProbeFurther.links` still carries three closely related structured-communication books:
**Minto Pyramid Principle**, **The So What Strategy** (a Minto-lineage method), and
**Supercommunicators**. The `why` notes differentiate them, but for a single interview
this is dense. Optional: trim to two (Minto + one of So What / Supercommunicators). Not a
defect — links are canonical, non-Obren, and each has a relevance note.

## External Resources Check

- All links resolve to canonical, non-Obren publisher/author pages (Barbara Minto,
  Macmillan, Stripe Press, Crucial Learning, Charles Duhigg, GOV.UK, Amazon). Good.
- Every link has a one-sentence `why`. Good.
- No `obren.io` bookshelf notes or PDFs leaked into the list. Good.
- Bookshelf-as-inspiration: the comms-heavy picks (Minto, So What, Supercommunicators,
  Crucial Conversations) are appropriate communication choices consistent with the curated
  bookshelf's spirit while pointing to canonical sources.
- Minor: see overlap note above (Minto vs. So What).

## Priority Recommendations

1. **Confirm the three-role scope is intentional** (Gap 1). Either accept the divergence
   from the four-role family convention, or restore Senior Manager to both the rubric and
   `roleFocus`. The two are now self-consistent either way.
2. *(Optional)* Trim one of the three overlapping structured-communication books from
   `toProbeFurther.links`.

## Verification Performed

- `python3 _scripts/validate_interviews.py` — passes (16 datasets).
- `python3 _scripts/summarize_coverage.py` — interview present; signals/levels coherent;
  this dataset now contributes 3 example stories.
- Re-read the full diff since the last commit and cross-checked `roleFocus`, rubric levels,
  `level` values against `_templates/role-levels.json`, and the two sibling
  Influence-and-Communication interviews.

If any data edit is applied, rerun:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

# Review — Ethics and Responsible Technology

File: `data/book/ethics-responsible-technology/interview.json`

## Rating Scale
1 = poor, 2 = weak, 3 = adequate, 4 = strong, 5 = excellent.

## Snapshot
| Dimension | Score |
| --- | --- |
| Realism | 4 |
| Balance | 5 |
| Educative Value | 5 |
| Interview Usability | 5 |
| Spec Quality | 5 |
| External Resources | 5 |
| **Overall** | **5 (excellent)** |

Validation passes (`validate_interviews.py`: ok, 16 datasets). Coverage now shows this dataset
contributing four unique signals — Trust Risk Judgment, Moral Courage, Responsible Alternatives, and
the newly added **Boundary and Escalation Judgment** — across four example stories spanning the full
Senior Manager → CTO ladder.

## What Changed Since the Last Review
This revision directly resolved every priority recommendation from the previous pass:

1. **Refusal now has a named price (was the biggest realism gap).** The lead `result` records a
   six-week slip and a lowered personalization target; one unsafe data-use path is rejected outright
   with executives "agreeing to absorb the near-term revenue risk." The reflection was rewritten from
   "safer alternatives, not only late-stage objections" to "both practical alternatives **and** the
   courage to say no when no safe alternative exists."
2. **Business momentum is now dramatized, not just asserted.** New scenario context ("Product and
   revenue leaders believe a delay will hurt a strategic commitment"), a strong-answer move that
   "Names the pressure" (promised date + 4% lift), and a "Who pushed back on the delay?" follow-up
   make the candidate visibly resist momentum rather than face a passive product team.
3. **System-change items are now story-specific.** Generic "privacy/security checkpoint" and
   "data minimization checklist" gave way to a "Consent-clarity and retention gate," a "Segment-harm
   review for model launches," explicit stop conditions, and an escalation rule for non-negotiable
   boundaries.
4. **The weakest external link was replaced.** *Thinking, Fast and Slow* is gone, swapped for the
   ICO "Data protection by design and by default" guide — a canonical, on-case privacy-by-design
   reference that maps directly to the data-minimization and consent scenarios the spec actually uses.

## Strengths
- **Clean, complete, internally consistent spec.** All sections present, ids stable, the new
  `boundary-escalation` signal is wired through `signalMap`, and all signal `tests` resolve against
  the canonical `_templates/signal-types.json` vocabulary. `roleFocus` now includes Senior Manager,
  aligning it with the rubric ladder.
- **New tension is the right one for the competency.** The added "Boundary and Escalation Judgment"
  signal — distinguishing *mitigable risk* from *non-negotiable boundaries* and escalating with
  options — closes the spec's prior bias toward "always find a safer alternative." The strong-answer
  pattern now explicitly branches: "Proposes a safer alternative when one exists, or says no with
  clear escalation when it does not."
- **Four genuinely distinct example stories.** Data-minimization (CTO), AI fairness (VP), a
  production-data AI-assistant **refusal** (Senior Manager), and a telemetry retention reset
  (Director) exercise different evidence and cover the full ladder. Each weak version is a sharp,
  realistic non-answer (e.g. "let the team decide how much telemetry they really needed").
- **`exampleAnswers` raise educative value sharply.** All four follow-up questions now carry paired
  strong/weak example answers, teaching an interviewer the concrete contrast to listen for instead of
  abstract advice like "show ownership."
- **Costs are made visible throughout.** Every strong sketch names what was given up (slipped launch,
  lowered target, slower long-tail analysis, absorbed commercial concession), which is the credibility
  test for responsible-tech stories.
- **External resources are credible, on-topic, and de-duplicated**, each with a one-sentence relevance
  note and a canonical non-Obren URL.

## Remaining Gaps and Risks (minor)
1. **The lead story is still a coordinated success (Realism, minor).** The signature arc now has real
   cost, but the leader still wins cleanly every time. A single note of residual friction — an
   executive who stayed unconvinced, or a control that proved hard to enforce later — would push
   realism from strong to excellent. This is polish, not a defect.
2. **Some quantification is convenient.** "4% conversion lift," "3% aggregate conversion," "six-week
   slip," "90-day / 30-day retention" read as plausible but tidy. Fine for a teaching spec; flagging
   only so a future editor doesn't add more round numbers and tip it toward false precision.
3. **`boundary-escalation` is a dataset-local signal id**, not part of the canonical signal-types
   file (validation keys off the `tests`, which are all valid). That's consistent with how this repo
   defines per-interview signals — noted only so it isn't mistaken for an unregistered value.

## Priority Recommendations
This spec is in strong shape; the remaining items are optional polish:
1. Add one note of residual friction to the lead story so even the flagship arc isn't entirely
   frictionless (highest-value remaining realism touch).
2. Leave the quantified figures as-is; resist adding further precise metrics.

## Verification After Edits
If you change the interview data, run:
```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

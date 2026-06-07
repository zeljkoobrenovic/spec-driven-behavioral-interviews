# Review

## Purpose

This document records a focused quality review of
`data/book/tech-lead-influence/interview.json` ("Influence Without Authority").
It evaluates the interview spec against the project's review dimensions —
realism, balance, educative value, interviewer usability, spec quality, and
external resources — and separates fixable data issues from subjective content
recommendations.

This review reflects the dataset as of its current uncommitted draft. Validation
(`validate_interviews.py`) and coverage (`summarize_coverage.py`) both pass.

## Rating Scale

- 5 — Exemplary; little to improve.
- 4 — Strong; minor polish only.
- 3 — Solid; some real gaps to address.
- 2 — Usable but with significant weaknesses.
- 1 — Needs substantial rework.

## Current Snapshot

- File: `data/book/tech-lead-influence/interview.json`
- Manifest group: `senior-ics-tech-leads` ("Senior ICs and Tech Leads")
- Competency: Influence Without Authority (family: Influence and Communication)
- Role focus: Senior Software Engineer, Tech Lead
- Difficulty: advanced
- Example stories: 4 (test strategy, shared-service deprecation, scope
  trade-off, security-exception escalation)
- Follow-ups: 5, all with strong/weak calibration answers
- Evaluation signals: 4 (peer-influence, technical-framing,
  execution-mechanism, boundary-judgment)
- Rubric levels: 2 (Senior Software Engineer, Tech Lead)
- External links: 7, grouped into four themes
- Validation: passes. Coverage: passes.

## Overall Assessment

This is a strong, well-balanced interview spec — one of the better ones in the
catalog. It teaches a genuinely hard senior-IC skill (changing direction across
peers without command authority) and resists the common failure mode of
rewarding pure persuasion. The standout design choice is treating **escalation
as boundary judgment** rather than as either a weakness or a default: the
security-exception story and the `boundary-judgment` signal explicitly reward
knowing when peer influence runs out and accountable risk acceptance is
required. That nuance is rare and high-value.

The spec is internally consistent: every example story maps to a prompt variant,
every follow-up tests named signals, and the visualizations reference real ids.
Examples carry concrete evidence (escaped defects, paging load nine→two, flaky
quarantines halved, a two-week slip plus a lost expansion) instead of polished
hindsight.

Overall: **4.5 / 5.** The remaining work is verification of external link URLs
and a few small content enrichments, not structural fixes.

## Strengths

- **Realism (5):** Scenarios carry messy constraints — partner teams view
  migration as unfunded, Security is overloaded, Sales tries to promise the
  bypass anyway. The security-exception story deliberately ends with real cost
  (late signature with a concession, a lost smaller expansion) instead of a
  clean win. This is exactly the anti-hindsight texture the heuristics ask for.
- **Balance (5):** Strong answers do not all reward the same move. Speed
  (read-only offline beta), principled refusal (no MFA bypass), escalation
  (security memo), and lightweight process (contract tests first) are each
  correct in their own context. The spec recognizes peers are often *right* and
  bakes that into the `resistance` follow-up.
- **Educative value (5):** The weak-version lines are concrete and teach the
  exact tell ("I kept pushing until teams agreed", "I escalated because the
  teams would not agree with me"). The strong/weak example answers on every
  follow-up make the evaluation logic explicit rather than gesturing at
  "alignment."
- **Interview usability (4):** Five prompt variants gather genuinely different
  evidence (alignment vs. cross-team change vs. scope trade-off vs. escalation).
  Follow-ups are specific and probe for evidence, not vibes. The rubric draws a
  clear line between SSE (bounded improvement across one boundary) and Tech Lead
  (repeatable mechanism + boundary escalation).
- **Spec quality (5):** IDs are stable and cross-referenced correctly; all
  visualization arrays point to existing signal/follow-up ids; bold key-phrase
  usage is restrained and applied only to prose. Validation passes.

## Gaps And Risks

1. **External link URLs unverified (medium).** Web fetch was not available during
   this review, so the following could not be confirmed live and should be
   spot-checked:
   - `https://docs.cloud.google.com/architecture/architecture-decision-records`
     — the canonical Google Cloud Architecture Center domain is normally
     `cloud.google.com/architecture/...`, not `docs.cloud.google.com`. Verify
     this resolves and is not a redirect; prefer the canonical host if so.
   - `https://www.simonandschuster.com/.../9781966280002` (Team Topologies 2nd
     Edition, listed as 2025) — confirm the ISBN/edition page is live, since a
     future-dated edition is more likely to drift.
   - The remaining links (Stanford GSB, StaffEng, Atlassian DACI / trade-offs,
     Google SRE "Embracing Risk") are well-chosen canonical sources; confirm
     they still load.
2. **`atlassian-daci-decision-framework` has no `year` field (low).** Several
   other links carry `year`; DACI and trade-off playbooks omit it. Not required
   by validation, but inconsistent within the list.
3. **Manager role is slightly thin in the scenario (low).** The manager
   "supports quality work in principle but will not dictate the technical
   answer." That's realistic, but a candidate could over-rely on the manager as
   a backstop. The follow-up set already guards against escalation-as-crutch, so
   this is a watch item, not a defect.
4. **Single-dataset group (informational).** `senior-ics-tech-leads` currently
   contains only this dataset. Not a problem with the interview itself, but the
   group will read as thin in the catalog until siblings are added (a staff-level
   strategy case or a platform-adoption case would pair well).

## Review Dimensions

| Dimension            | Score | Note |
|----------------------|-------|------|
| Realism              | 5     | Messy constraints, credible costs, no clean wins. |
| Balance              | 5     | Multiple correct behaviors by context; peers can be right. |
| Educative Value      | 5     | Concrete weak versions and calibrated example answers. |
| Interview Usability  | 4     | Strong variants/follow-ups; rubric is clear but only 2 levels. |
| Spec Quality         | 5     | Consistent ids, valid cross-refs, passes validation. |
| External Resources   | 4     | Well-curated and relevance-noted; URLs need live verification. |

## Priority Recommendations

1. **Verify the four external URLs flagged above**, especially the Google Cloud
   ADR host (`docs.cloud.google.com` vs. `cloud.google.com`). Fix any that
   redirect or 404; rebuild `docs/` afterward.
2. **Add a `year` to the DACI link** (and confirm trade-off play) for list
   consistency.
3. **(Optional) Add one more rubric level or a "below bar" descriptor.** The
   two-level rubric is fine for SSE/Tech Lead, but a one-line "below expected"
   anchor (e.g., "treats resistance as ignorance; ends at consensus") would help
   interviewers calibrate the floor as well as the bar.
4. **(Optional) Seed a sibling dataset in `senior-ics-tech-leads`** so the group
   does not render as a single-item category.

## Per-Interview Review

### `data/book/tech-lead-influence/interview.json` — Influence Without Authority

- **Rating:** 4.5 / 5 (advanced; Senior Software Engineer + Tech Lead).
- **Main strengths:** Escalation modeled as boundary judgment, not weakness;
  four distinct, evidence-rich example stories each tied to a prompt variant;
  weak-answer tells are concrete and teachable; signals and follow-ups are fully
  cross-referenced.
- **Main risks:** External link URLs unverified (notably the Google Cloud ADR
  host); minor metadata inconsistency (missing `year` on DACI); single-item
  catalog group.
- **Recommended next edits:** (1) verify/fix the flagged URLs and rebuild; (2)
  add `year` to the DACI link; (3) optionally add a below-bar rubric anchor; (4)
  optionally add a sibling dataset to the group.

## Ongoing Review Checklist

- [ ] `python3 _scripts/validate_interviews.py` passes.
- [ ] `python3 _scripts/summarize_coverage.py` reviewed for tag balance.
- [ ] Every example story maps to a real prompt variant.
- [ ] Every follow-up `tests[]` tag and every `visualizations` id resolves.
- [ ] All `toProbeFurther.links[]` URLs load and point to canonical (non-Obren)
      pages with no duplicate book/article.
- [ ] After any data edit: `python3 build.py` then
      `python3 _scripts/smoke_static_site.py`.

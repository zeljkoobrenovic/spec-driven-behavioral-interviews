# Review

## Purpose

Structured review of `data/book/engineer-production-issues/interview.json`
("Handling Production Issues") against realism, balance, educative value,
interviewer usability, spec quality, and external resources. This revision
reflects recent edits that added an external-resource list, a candidate-caused
incident framing, a fix-forward story, and residual-impact language throughout.

## Rating Scale

- 5: Exemplary; nothing material to fix.
- 4: Strong; minor improvements possible.
- 3: Solid but with a clear gap to close.
- 2: Usable but with significant weaknesses.
- 1: Needs rework.

## Current Snapshot

- Validation: `validate_interviews.py` passes (28 datasets, no errors).
- Roles: Software Engineer, Senior Software Engineer, Tech Lead.
- Competency: Production Ownership (Execution and Accountability).
- Difficulty: intermediate.
- Prompt: primary plus 5 variants; 5 interviewer-intent lines (now including
  ownership-without-blame and rejected-mitigation/residual-impact probes).
- Example stories: 4 — Checkout Latency Spike (SE), Cache Stampede Fix-Forward
  (Senior SE), Silent Data Drop (Senior SE), Runbook Gap During On-Call (TL) —
  each with strong sketch, why-it-works, weak version, and follow-up angles.
- Follow-ups: 4, all with strong/weak calibration answers.
- Signals: 3; rubric: 3 levels; visualizations wired to existing ids.
- External resources: **8 links** across 3 groups (Debugging and Observability,
  Incident Response and Communication, Post-Incident Learning); all canonical,
  non-`obren.io`, de-duplicated, each with a one-sentence relevance note.
- Visual assets: none (consistent with sibling engineer interviews).

## What Changed Since The Last Review

The previous review's three highest-priority gaps have largely been closed:

1. **`toProbeFurther.links[]` added.** 8 sources (Google SRE chapters on
   troubleshooting, monitoring, managing incidents, and postmortem culture;
   PagerDuty external-communication guidelines; AWS Correction of Error;
   Atlassian postmortems; Etsy blameless postmortems). All are canonical
   publisher/framework pages, not `obren.io`, with no duplicate book or article.
   This was the single biggest defect and it is resolved.
2. **Candidate-caused-incident framing added.** The two lead stories now have the
   candidate author the triggering change explicitly (a checkout/promotions
   release; a cache-key change), and the action/pattern text repeatedly stresses
   owning the trigger "without collapsing into self-blame." This aligns the
   examples with the primary prompt's "caused or helped resolve."
3. **Blameless behavior is now closer to observable.** Red flags and pattern
   moves now name concrete tells: separating trigger / contributing factors /
   detection gaps, describing one's own decisions without deflecting, and not
   making the story about being blamed or innocent.

In addition, a **fix-forward / residual-impact** thread runs through the whole
spec now: a new "first mitigation was incomplete or created a new risk" variant,
the Cache Stampede story (duplicate notifications for ~1,800 users), and
result/system-change fields that track unrecovered data, support debt, and
verified action-item closure.

## Overall Assessment

A genuinely strong, content-complete interview that is now also catalog-consistent.
The scenario set is realistic and varied (latency-without-errors, cache stampede
with a partial fix, silent data loss, stale runbook), the strong/weak contrasts
are concrete and teach the evaluation logic, the rubric escalates cleanly from IC
contribution to tech-lead system change, and the external-resource list is
well-curated. The remaining opportunities are refinements, not defects.

## Strengths

- **Realism is high.** The signature scenario is the textbook hard case: latency
  doubles while dashboards stay green because error rates are low. The cache
  stampede (canary-clean change, tenant-scale trigger, a first fix that creates
  duplicate notifications), the silent-data-drop story (2% loss within normal
  volume, no alert), and the runbook-gap story (knowledge concentrated in one
  engineer) are credible, messy, and not polished hindsight.
- **Residual impact is treated as part of the job.** Result and system-change
  fields explicitly require naming unrecovered data, delayed jobs, support debt,
  and customer-communication debt — and verifying that action items actually
  closed. This pushes against "the graph recovered, so we were done."
- **Mitigation is a trade-off, not a reflex.** "Why disable the flag instead of
  full rollback?" and the cache story's "rollback would retry the import and
  duplicate more jobs" reward diagnosis-preserving, side-effect-aware mitigation.
  The weak versions cleanly expose the shortcut.
- **Communication under uncertainty is a first-class signal.** The weak follow-up
  "I waited until we understood root cause so we would not confuse people" is an
  excellent trap distinguishing real operators from information hoarders.
- **Ownership without blame is now teachable.** The spec repeatedly contrasts
  accountable ownership with both self-blame and deflection, and the red flag
  "describes being blamed or being innocent more than the operational decisions"
  gives interviewers something concrete to listen for.
- **Data correctness framed as production impact.** The silent-data-drop story
  rewards annotating affected metrics over silently backfilling.
- **Rubric levels are genuinely differentiated**: contribute → frame impact,
  rejected options, and residual cost / coordinate across owners → improve team
  response capability. They do not blur.
- **External resources are well-chosen and well-grouped.** Three coherent groups
  map to the spec's own signals (diagnose with evidence, communicate, learn), and
  each link's `why` ties back to a behavior the interviewer is evaluating.

## Gaps And Risks

1. **Customer/external-comms scenarios still skew internal.** A PagerDuty
   external-communication resource was added, but all four example stories still
   resolve through internal channels and dashboards. No example exercises a
   customer-facing status page or an externally communicated SLA breach, which is
   common at the Tech Lead level. The richest remaining gap.
2. **`followUpTree` omits the residual-impact thread.** The fix-forward / residual
   cleanup theme is now central (a dedicated variant, a whole example story, and
   multiple result/system-change fields), but no follow-up specifically probes
   "what remained broken after the symptom recovered." The closest is the
   communication and impact probes; a dedicated residual-impact follow-up would
   match the spec's new emphasis and give the cache story a natural landing probe.
3. **Two of four stories sit at Senior SE.** Levels are now SE / Senior SE /
   Senior SE / TL. That is acceptable (Senior is the spec's center of gravity),
   but a second clearly IC-level or a second TL-level story would broaden the
   level coverage the rubric promises.

## Review Dimensions

- Realism: **5** — concrete, messy, evidence-driven; the added fix-forward story
  with second-order effects raises the bar further.
- Balance: **4** — strong across diagnosis / comms / prevention / residual repair;
  still missing an external-customer-communication angle and skewed toward Senior.
- Educative Value: **5** — excellent strong/weak contrasts, and the previously
  under-taught "blameless" concept is now expressed as observable behaviors.
- Interview Usability: **5** — variants change the evidence gathered, follow-ups
  are specific and calibrated, rubric supports a fair level decision.
- Spec Quality: **5** — internally consistent, passes validation, and now at
  parity with the catalog (external resources present and well-formed).
- External Resources: **5** — 8 canonical, non-duplicated, well-grouped sources,
  each with a clear relevance note tied to an evaluated behavior.

## Priority Recommendations

1. **Add an external/customer-communication beat** (optional but highest-value
   remaining edit). Either a fifth example story or a follow-up at the Tech Lead
   level covering a customer-facing status page, public incident note, or SLA
   breach communication — the one operational surface the current examples never
   touch. The PagerDuty resource already supports this, so the reading list is
   ready for it.
2. **Add a residual-impact follow-up.** A probe such as "What was still broken
   after the main symptom recovered, and who owned closing it?" would directly
   exercise the spec's now-central fix-forward / residual-cleanup theme and give
   the Cache Stampede story a dedicated landing question. Wire it into
   `visualizations.followUpTree`.
3. **(Optional) Broaden level coverage** with a second IC-level or second
   TL-level example, so the four stories span the rubric's three levels more
   evenly rather than clustering at Senior SE.

## Per-Interview Review

- **File:** `data/book/engineer-production-issues/interview.json`
- **Rating:** Strong across the board (Realism 5, Educative 5, Usability 5, Spec
  Quality 5, External Resources 5; Balance 4). Overall **strong / near-exemplary**.
- **Main strengths:** realistic latency-without-errors, cache-stampede-with-partial-fix,
  and silent-data-loss scenarios; residual impact treated as part of recovery;
  mitigation framed as a trade-off; communication-under-uncertainty and
  ownership-without-blame as observable signals; well-curated external resources.
- **Main risks:** examples never exercise external/customer communication; the
  central residual-impact theme lacks a dedicated follow-up; stories cluster at
  Senior SE.
- **Recommended next edits:** add an external/customer-communication story or
  follow-up; add a residual-impact follow-up and wire it into the follow-up tree.

## Ongoing Review Checklist

- Re-run `python3 _scripts/validate_interviews.py` and
  `python3 _scripts/summarize_coverage.py` after any data edit.
- After editing data, rebuild: `python3 build.py` then
  `python3 _scripts/smoke_static_site.py`.
- Keep `toProbeFurther.links[]` canonical (non-`obren.io`), de-duplicated, and
  each with a one-sentence relevance note.
- Verify every example level appears in `roleFocus` and every visualization id
  resolves to an existing signal/follow-up.

# Review: Scaling An Organization

Path: `data/book/scaling-organization/interview.json`  
Last reviewed: 2026-06-06  
Reviewer skill: `behavioral-interview-reviewer`  
Rating: `4 - Strong`

## Dimension Scores

- Realism: `4/5`
- Balance: `3.5/5`
- Educative Value: `3.5/5`
- Interview Usability: `4/5`
- Spec Quality: `4/5`
- External Resources: `4/5`

## Strengths

- The core prompt is realistic for Director, VP Engineering, and CTO interviews because it asks about actual growth pain: coordination cost, architecture decisions, uneven manager practice, incident learning, and ownership boundaries.
- The strongest content pattern is proportional structure: the candidate should diagnose what broke, add mechanisms tied to failure modes, and keep team-local decisions lightweight.
- The weak answer pattern is plausible rather than cartoonish. It catches common senior-leadership failure modes: adding meetings, treating scale as generic process, or ignoring manager capability.
- External resources are mostly credible and contextually useful, including Team Topologies, Scaling People, An Elegant Puzzle, and High Output Management, with bookshelf items used only as inspiration for canonical links.

## Risks

- Outcomes are too qualitative. The story says dependencies became more visible, managers had a baseline, and ownership improved, but does not show enough hard evidence.
- The two concrete examples both converge on similar mechanisms: planning artifacts, architecture review, manager expectations, and ownership standards. That can over-teach "add process" as the default scaling answer.
- Follow-up probes ask the right questions but lack strong and weak example answers, which limits interviewer calibration.
- The rubric distinguishes level scope, but not enough about evidence quality at Director, VP Engineering, and CTO levels.
- The Team Topologies resource is labeled `2019`, while the linked book page now foregrounds the second edition. Either update the year/context or clarify that the link represents the current book page.

## Recommended Edits

- Add 2-3 measurable outcomes to `storyAnatomy.result`, such as planning predictability, dependency churn, repeat incident rate, decision lead time, manager span health, attrition, or delivery confidence.
- Add one example where the strong scaling move is simplification rather than a new process: merge or split teams, remove a ritual, clarify incentives, centralize a scarce capability, or decentralize a bottleneck.
- Add `followUps[].exampleAnswers` for `what-broke`, `too-much-process`, `manager-capability`, and `ownership`.
- Expand the rubric so Director evidence focuses on team-of-teams execution, VP evidence focuses on leadership-layer and operating-model design, and CTO evidence focuses on company strategy, talent model, and risk alignment.
- Update or clarify the Team Topologies external-resource metadata.

## Implementation Follow-Up

2026-06-06: Addressed the recommended edits in `interview.json` by adding measured outcomes, a simplification-focused CTO example, calibrated follow-up example answers, sharper level rubric language, and updated Team Topologies metadata for the current second edition.

## Verification

- `python3 _scripts/validate_interviews.py`
- `python3 _scripts/summarize_coverage.py`

Influence without authority is not tested by whether someone says they "got buy-in."

Buy-in is table stakes.

The real signal is whether a senior IC or tech lead can move peers toward a technical direction by making evidence, trade-offs, ownership, and decision boundaries clear without relying on title power.

When I interview senior engineers and tech leads about influence, I listen for five things:

- Can they explain why peers resisted, and what those peers were right about?
- Can they bring concrete evidence: escaped defects, operational cost, customer impact, cycle time, reliability risk, or maintenance burden?
- Can they separate the principle from the first practical step so the decision does not become an all-or-nothing rewrite?
- Can they turn discussion into an explicit mechanism: RFC, design note, trade-off review, adoption plan, owner map, or decision gate?
- Can they tell when escalation is appropriate because the remaining decision requires accountable risk acceptance?

Weak influence stories often sound reasonable at first:

"I convinced the team we needed better tests."

"I explained the technical debt until the other team agreed to migrate."

"I escalated because the business was pushing engineering too hard."

None of these are automatically bad. They are just not enough for senior technical leadership.

At Senior Software Engineer level, I want to hear how the person influenced peers with evidence, represented another team's constraints fairly, and drove a bounded improvement across a team boundary.

At Tech Lead level, I want to hear how they created a repeatable decision and adoption mechanism, then escalated boundary decisions with options, cost, and a recommendation instead of politics.

The most useful follow-ups are concrete:

- Who resisted the direction, and what were they right about?
- What mechanism turned discussion into a decision?
- What trade-off did you make visible?
- What did you reject?
- Who still paid a cost, carried extra work, or remained dissatisfied?
- When was escalation the right move?
- How did you know people actually adopted the direction?

The strongest answers rarely sound like "I persuaded everyone."

They sound more like:

"Three squads used different testing approaches for a shared checkout flow. One favored end-to-end tests, one relied on mocks, and one avoided old tests because they were slow and flaky. I collected escaped defect data, flaky-test time, build duration, and which failures each test type caught. In a working session, we named what each squad's concern was protecting. We rejected both extremes: a blanket end-to-end mandate that would slow every build and a no-standard approach that would keep defects leaking across squad boundaries. We agreed on contract tests for shared boundaries first, then selective end-to-end coverage for revenue-critical paths. One squad's cleanup work moved behind a customer fix for a release, so I made that cost visible in planning. Adoption was real when new checkout changes included the agreed contract tests, fixture ownership was clear, and flaky-test quarantines dropped."

Senior influence is not charisma.

It is evidence, empathy, trade-off clarity, ownership, boundary judgment, and follow-through.

The best tech leads do not just win an argument.

They leave behind a better way for the team to make the next hard technical decision.

#EngineeringLeadership #TechLead #SeniorEngineer #InfluenceWithoutAuthority #TechnicalLeadership #BehavioralInterviewing

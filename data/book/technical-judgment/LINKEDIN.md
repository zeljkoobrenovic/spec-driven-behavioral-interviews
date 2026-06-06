Technical judgment at executive scale is not tested by whether someone says they "understand architecture."

Architecture literacy is table stakes.

The real signal is whether they can make or reverse consequential technical decisions by weighing system design, operating maturity, expert dissent, customer impact, and business constraints.

When I interview senior technology leaders about technical judgment, I listen for five things:

- Can they explain the decision through concrete constraints, options, and trade-offs instead of architecture slogans?
- Can they use senior engineer input without outsourcing judgment to the loudest or most specialized voice?
- Can they connect architecture choices to customer impact, reliability, team ownership, on-call burden, delivery, and cost?
- Can they sequence the decision based on current operating capability rather than an ideal target-state diagram?
- Can they name the evidence that would make them revisit or reverse the decision?

Weak technical judgment stories often sound reasonable at first:

"The senior engineers reviewed the options and recommended the architecture, so I supported them."

"We moved to services because we needed team autonomy and better scalability."

"The architecture was not working, so I reversed it and told teams to simplify."

None of these are automatically bad. They are just not enough for senior leadership.

At Senior Manager level, I want to hear how the person made a domain-level technical trade-off with explicit readiness signals and expert input.

At Director level, I want to hear how they coordinated architecture decisions across teams, ownership boundaries, migration risk, and operational consequences.

At VP Engineering level, I want to hear how they balanced architecture, operating model, talent maturity, delivery pressure, customer impact, and portfolio risk.

At CTO level, I want to hear how they set technical direction that creates strategic leverage while preserving reversibility and managing company-level risk.

The most useful follow-ups are concrete:

- What criteria did you use to make the decision?
- Which senior engineers disagreed, and what did you learn from them?
- What would have told you the decision was wrong?
- What did you deliberately choose not to optimize for?
- What operating capability did the architecture require from teams?
- What customer, reliability, delivery, or cost metric changed?
- How did future architecture decisions change afterward?

The strongest answers rarely sound like "I picked the best architecture."

They sound more like:

"A service extraction meant to improve team autonomy was making checkout reliability worse. P1/P2 incidents rose, rollback time stretched to 90 minutes, and on-call handoffs created unclear ownership. We compared hardening all services, continuing the migration, and reconsolidating the unstable pieces. I defined reversal criteria around payment success, incident frequency, rollback time, dependency age, ownership clarity, and on-call maturity. After reviewing the options with service advocates, checkout leads, SRE, and product, we stopped further extraction, reconsolidated two unstable services behind modular boundaries, and kept one service where scale and ownership justified it. Two roadmap items slipped by a month, but incidents fell, rollback time improved, and future extractions required explicit ownership and readiness criteria."

Senior technical judgment is not being the deepest specialist in the room.

It is making technical uncertainty discussable, turning expert disagreement into better criteria, matching architecture to operating reality, owning reversals without blame, and leaving behind a stronger decision mechanism than the one you inherited.

#Leadership #EngineeringLeadership #TechnologyLeadership #Architecture #TechnicalJudgment #BehavioralInterviewing

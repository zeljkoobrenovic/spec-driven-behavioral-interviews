# Spec-Driven Behavioral Interview Explorer

Plan for turning `IDEA.md` into an interactive, educational static explorer for
senior technology leadership behavioral interviews. The implementation should
reuse the rough shape of `../spec-driven-system-design-interviews`: structured
data as the source of truth, shared templates as the rendering shell, small
scripts for build and validation, and generated `docs/` output for publishing.

## Product Intent

The explorer should help candidates and interviewers understand behavioral
interviews structurally, not as a loose question bank.

Each case should model:

- The leadership competency being tested.
- The interview prompt and realistic follow-up probes.
- A strong answer pattern, a weak answer pattern, and why they differ.
- Evaluation signals and red flags.
- Level calibration for senior manager, director, VP, CTO, or equivalent roles.
- A reusable practice template that lets a reader draft their own answer.

The core frame from `IDEA.md` is:

```text
competency -> interview prompt -> strong example -> weak example
           -> interviewer follow-ups -> evaluation signals
```

For senior technology leadership, the answer structure should extend basic
STAR into:

```text
Situation -> Task -> Action -> Result -> Reflection -> System Change
```

The "system change" part is important: senior leaders should show how they
changed operating mechanisms, incentives, decision quality, communication, or
organizational capability after the event.

## Reference Project Lessons

The system-design explorer has several conventions worth copying:

- Keep `_templates/` as the only place for shared HTML, CSS, and JS.
- Keep `data/<group>/` as the only place for authored interview specs.
- Use `data/<group>/index.json` as the manifest for one publishable site.
- Generate `docs/<group>/` from templates plus data with a simple `build.py`.
- Treat `docs/` as generated, committed, and deployable through GitHub Pages.
- Avoid a bundler for the first version; use vanilla HTML, CSS, and JS.
- Let the browser fetch JSON at runtime, so the app must be served over HTTP.
- Add validators so bad JSON, broken references, and missing required fields
  are caught before publishing.

The behavioral version should not copy the system-design schema directly. It
should copy the architecture pattern and adapt the spec around competencies,
stories, rubrics, follow-up paths, and practice workflows.

## Proposed Repository Layout

```text
.
  IDEA.md
  PLAN.md
  README.md
  build.py

  _templates/
    README.md
    index.html
    explorer.html
    overview.js
    explorer.js
    styles.css
    competency-types.json
    rubric-scale.json
    icons/

  data/
    README.md
    book/
      index.json
      interview-method/
        interview.json
      leading-through-ambiguity/
        interview.json
      strategy-vs-execution/
        interview.json
      technical-judgment/
        interview.json
      executive-conflict/
        interview.json
      failure-accountability/
        interview.json
      building-leadership-teams/
        interview.json
      handling-underperformance/
        interview.json
      scaling-organization/
        interview.json
      technical-debt-modernization/
        interview.json
      crisis-leadership/
        interview.json
      cross-functional-influence/
        interview.json
      ethics-responsible-technology/
        interview.json
      innovation-emerging-technology/
        interview.json
      culture-change/
        interview.json
      executive-communication/
        interview.json

    examples/
      index.json
      ambiguous-platform-reliability/
        interview.json
      enterprise-security-roadmap/
        interview.json

  _scripts/
    scaffold_interview.py
    validate_interviews.py
    summarize_coverage.py
    generate_assets.py

  docs/
    index.html
    book/
    examples/
```

Groups:

- `book/`: canonical book content, organized around the chapter themes from
  `IDEA.md`.
- `examples/`: smaller worked examples used to test the renderer and show
  individual answer patterns.

Categories inside each manifest should use the existing `groups` key for
compatibility with the reference project's mental model, but documentation
should call them categories.

## Site Shape

### Overview Page

`index.html` should render a dense visual catalog of behavioral interview
cases. Cards should show:

- Competency title.
- Short description.
- Seniority focus.
- Primary signals.
- Difficulty or interview depth.
- Links to the explorer page using `explorer.html#<datasetId>`.

Useful filters:

- Competency family.
- Role level.
- Interviewer intent, such as judgment, influence, execution, or talent.
- Failure, conflict, ambiguity, scaling, ethics, or communication.

### Explorer Page

`explorer.html` should provide a step-by-step walkthrough for one behavioral
interview case.

Primary navigation sections:

- Competency Brief.
- Prompt.
- Story Anatomy.
- Strong Answer.
- Weak Answer.
- Follow-Up Probes.
- Evaluation Rubric.
- Level Calibration.
- Practice Template.
- Related Scenarios.

The page should support keyboard navigation, shareable hash routes, inline
JSON/render errors, and no dependency on a backend.

## Behavioral Interview Spec

Each interview should be one JSON file:

```jsonc
{
  "id": "leading-through-ambiguity",
  "title": "Leading Through Ambiguity",
  "description": "Turning vague executive intent into measurable direction.",
  "roleFocus": ["Director", "VP Engineering", "CTO"],
  "difficulty": "advanced",

  "competency": {
    "id": "ambiguity",
    "name": "Leading Through Ambiguity",
    "family": "Judgment and Strategy",
    "definition": "Creates clarity, decision criteria, and operating rhythm when goals or data are incomplete.",
    "whyItMatters": "Senior leaders are hired to turn uncertainty into aligned execution."
  },

  "prompt": {
    "primary": "Tell me about a time you had to lead a major technical or organizational initiative when the goal was ambiguous.",
    "variants": [
      "Describe a time when you had incomplete data but still had to make a high-impact decision.",
      "Tell me about a time you had to create clarity for a team or executive group."
    ],
    "interviewerIntent": [
      "Can the candidate structure ambiguity?",
      "Do they align stakeholders before driving execution?",
      "Do they turn vague intent into measurable outcomes?"
    ]
  },

  "scenario": {
    "signatureExample": "A VP Engineering inherits a vague board-level mandate to improve platform reliability.",
    "context": [
      "Reliability concerns are real but poorly measured.",
      "Executives disagree on whether the problem is architecture, process, or staffing.",
      "Product teams fear reliability work will delay roadmap commitments."
    ],
    "constraints": [
      "First 90 days matter.",
      "No clean baseline exists.",
      "Customer impact must be made visible."
    ]
  },

  "storyAnatomy": {
    "situation": "The organization had visible reliability pain but no shared definition of the problem.",
    "task": "Create a measurable reliability strategy without freezing product delivery.",
    "action": [
      "Segmented incidents by customer impact and service area.",
      "Introduced service-level objectives for the most critical journeys.",
      "Aligned product and engineering on reliability budgets.",
      "Built a 90-day roadmap with explicit trade-offs."
    ],
    "result": [
      "Executive debate moved from anecdotes to measurable risk.",
      "Teams had a prioritized reliability roadmap.",
      "Customer-impacting incidents declined over the next planning cycle."
    ],
    "reflection": "The key lesson was to define the decision system before choosing technical fixes.",
    "systemChange": [
      "Recurring reliability review.",
      "Ownership model for critical services.",
      "Incident taxonomy and customer-impact dashboard."
    ]
  },

  "strongAnswerPattern": {
    "summary": "The candidate names uncertainty, creates structure, aligns stakeholders, acts with incomplete data, measures outcome, and changes the system.",
    "moves": [
      "Starts with business and customer context.",
      "States what was unknown.",
      "Explains the decision criteria.",
      "Describes personal actions, not just team actions.",
      "Shows measurable results and learning."
    ]
  },

  "weakAnswerPattern": {
    "summary": "The candidate stays vague, claims they created alignment, but cannot explain trade-offs, personal actions, or measurable change.",
    "redFlags": [
      "Uses generic phrases such as aligned stakeholders without concrete mechanisms.",
      "Focuses only on technical work and ignores executive ambiguity.",
      "Blames other functions for lack of clarity.",
      "Has no result, reflection, or operating change."
    ]
  },

  "followUps": [
    {
      "id": "alternatives",
      "question": "What alternatives did you reject?",
      "tests": ["decision quality", "trade-off reasoning"]
    },
    {
      "id": "disagreement",
      "question": "Who disagreed with you, and how did you handle it?",
      "tests": ["influence", "stakeholder alignment"]
    },
    {
      "id": "metrics",
      "question": "How did you know the situation improved?",
      "tests": ["measurement", "accountability"]
    }
  ],

  "evaluation": {
    "signals": [
      {
        "id": "sense-making",
        "name": "Sense-making",
        "strong": "Separates symptoms from root problems and creates a shared frame.",
        "weak": "Repeats the ambiguity without structuring it."
      },
      {
        "id": "stakeholder-alignment",
        "name": "Stakeholder alignment",
        "strong": "Builds decision criteria with peers and executives.",
        "weak": "Treats alignment as persuasion after the decision."
      },
      {
        "id": "operating-change",
        "name": "Operating change",
        "strong": "Leaves behind dashboards, rituals, ownership, or decision rules.",
        "weak": "Solves the immediate problem only."
      }
    ],
    "rubric": [
      {
        "level": "Senior Manager",
        "expected": "Creates clarity for multiple teams and escalates unresolved strategic ambiguity."
      },
      {
        "level": "Director",
        "expected": "Creates cross-functional alignment and changes planning or operating mechanisms."
      },
      {
        "level": "VP Engineering",
        "expected": "Converts executive ambiguity into strategy, metrics, accountability, and portfolio trade-offs."
      }
    ]
  },

  "visualizations": {
    "timeline": ["situation", "task", "action", "result", "reflection", "systemChange"],
    "signalMap": ["sense-making", "stakeholder-alignment", "operating-change"],
    "followUpTree": ["alternatives", "disagreement", "metrics"]
  },

  "practiceTemplate": {
    "prompts": [
      { "field": "situation", "label": "What was unclear, high-stakes, or contested?" },
      { "field": "task", "label": "What were you personally accountable for?" },
      { "field": "action", "label": "What mechanisms did you introduce?" },
      { "field": "result", "label": "What changed measurably?" },
      { "field": "reflection", "label": "What did you learn?" },
      { "field": "systemChange", "label": "What changed beyond the immediate story?" }
    ]
  }
}
```

## Shared Data Types

Create small canonical files in `_templates/` or `data/_shared/`:

- `competency-types.json`: competency families, colors, and icons.
- `rubric-scale.json`: weak, acceptable, strong, exceptional descriptions.
- `role-levels.json`: senior manager, director, VP, CTO expectations.
- `signal-types.json`: judgment, ownership, influence, execution, talent,
  communication, ethics, strategy, technical judgment.

These should keep the renderer consistent and make validation possible.

## Generated Views From The Spec

The explorer should generate the following views from JSON fields:

- Competency map: links competency families to cases.
- STAR-RSC timeline: shows story anatomy from situation to system change.
- Strong vs weak contrast: side-by-side comparison of answer moves.
- Follow-up tree: each follow-up question shows what signal it probes.
- Evaluation matrix: signals across role levels.
- Red-flag panel: weak patterns and interviewer concerns.
- Practice worksheet: editable fields in the browser, optionally stored in
  localStorage per dataset.
- Coverage summary: generated by script to show which competencies, levels,
  and signal types are represented across all datasets.

Do not hand-author diagrams for every case in the first version. Prefer simple
generated HTML/CSS visualizations from structured arrays. Mermaid can be added
later if a specific view benefits from graph syntax.

## Build Script

`build.py` should mirror the reference project:

1. Discover publishable groups under `data/` by finding `index.json`.
2. For each group, remove and recreate `docs/<group>/`.
3. Copy `_templates/` into `docs/<group>/`, excluding Markdown docs.
4. Copy that group's `data/` into `docs/<group>/data/`, excluding authoring
   notes and build helper files.
5. Print built groups and dataset counts.

Root `docs/index.html` can be a small redirect or landing index linking to
`book/` and `examples/`.

## Validation

Add `_scripts/validate_interviews.py` before content grows.

Checks:

- Every `data/<group>/index.json` is valid JSON.
- Every manifest dataset id is unique inside the group.
- Every manifest path exists.
- Every `interview.json` has required fields:
  - `title`
  - `description`
  - `competency`
  - `prompt.primary`
  - `storyAnatomy`
  - `strongAnswerPattern`
  - `weakAnswerPattern`
  - `followUps`
  - `evaluation.signals`
  - `practiceTemplate`
- `followUps[].tests` reference known signal ids or signal type names.
- `visualizations.signalMap` references `evaluation.signals[].id`.
- `practiceTemplate.prompts[].field` references valid story anatomy fields.
- Role levels are from the canonical role-level list.
- No generated `docs/` files are required for validation, but the build should
  run cleanly after validation.

Later, add JSON Schema if the Python validator becomes too large.

## Initial Content Plan

Start with one method dataset and five flagship case datasets.

MVP datasets:

1. `interview-method`: explains STAR-RSC, answer quality, follow-up handling,
   and how senior behavioral interviews differ from generic behavioral rounds.
2. `leading-through-ambiguity`: based on the reliability mandate example from
   `IDEA.md`.
3. `strategy-vs-execution`: business context changes and engineering roadmap
   reprioritization.
4. `technical-judgment`: pragmatic architecture decision at executive scale.
5. `executive-conflict`: disagreement with Sales, Product, CEO, or board.
6. `failure-accountability`: owning a migration, outage, or missed goal.

Then add the remaining `IDEA.md` chapter themes:

- Building leadership teams.
- Handling underperformance.
- Scaling an organization.
- Technical debt and modernization.
- Crisis leadership.
- Cross-functional influence.
- Ethics and responsible technology.
- Innovation and emerging technology.
- Culture change.
- Executive communication.

## Implementation Phases

### Phase 1: Scaffold

- Add `README.md`, `build.py`, `_templates/`, `data/`, `_scripts/`, and
  `docs/`.
- Create minimal overview and explorer templates.
- Add `data/examples/index.json` and one tiny example dataset.
- Confirm `python3 build.py` produces `docs/examples/`.

Exit criteria:

- Static server can serve the generated overview.
- Clicking one card opens the explorer.
- The explorer loads JSON and renders title, prompt, story anatomy, follow-ups,
  and rubric.

### Phase 2: Schema And Validator

- Finalize the first behavioral JSON shape.
- Implement `_scripts/validate_interviews.py`.
- Add canonical role levels and signal types.
- Add validation to the README workflow.

Exit criteria:

- Invalid references fail fast.
- All MVP datasets pass validation.

### Phase 3: Educational Explorer

- Add the STAR-RSC timeline.
- Add strong vs weak answer contrast.
- Add follow-up tree grouped by tested signals.
- Add evaluation matrix by role level.
- Add practice worksheet with localStorage.

Exit criteria:

- The app teaches how to answer, not just what to answer.
- All visualizations are generated from data, not manually coded per case.

### Phase 4: Book Dataset

- Convert `IDEA.md` chapter themes into `data/book/<id>/interview.json`.
- Organize `data/book/index.json` into categories such as:
  - Judgment and Strategy.
  - Execution and Accountability.
  - People Leadership.
  - Organizational Scale.
  - Influence and Communication.
  - Risk, Ethics, and Innovation.
- Add coverage summary script to identify missing signal/level coverage.

Exit criteria:

- `book/` has the method dataset plus all major themes from `IDEA.md`.
- Overview filters make the catalog easy to scan.

### Phase 5: Publishing Polish

- Improve responsive layout.
- Add icons or lightweight visual assets.
- Add empty/error/loading states.
- Add print-friendly practice worksheet styling.
- Add GitHub Pages instructions.

Exit criteria:

- `docs/` is committed and publishable.
- The project can be maintained by editing JSON plus templates only.

## Design Principles

- Data first: if content differs per interview, it belongs in JSON.
- Templates second: if layout or rendering differs globally, it belongs in
  `_templates/`.
- Scripts third: use scripts for repeatable build, validation, scaffolding, and
  coverage checks.
- Keep the first version framework-free unless the UI complexity clearly
  justifies a frontend build system.
- Favor structured generated views over hand-authored prose-only pages.
- Optimize for senior leadership judgment: trade-offs, personal ownership,
  measurable outcomes, reflection, and system change.

## Immediate Next Step

Build the smallest vertical slice:

1. Create `_templates/`, `data/examples/`, `_scripts/`, and `build.py`.
2. Add one example dataset for `leading-through-ambiguity`.
3. Render overview plus explorer.
4. Add validation.
5. Expand to the `book/` group once the schema feels stable.

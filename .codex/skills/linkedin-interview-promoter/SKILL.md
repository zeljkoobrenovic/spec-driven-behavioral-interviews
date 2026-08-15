---
name: linkedin-interview-promoter
description: "Promote a specific behavioral interview on LinkedIn from a provided interview.json URL or path. Use when drafting LinkedIn copy that explains behavioral interviews, their education and interviewing value, the project, and includes both the concrete interview anchor link and the full catalog link."
---

# LinkedIn Interview Promoter

## Purpose

Draft a LinkedIn post that promotes one interview from this project using a supplied interview JSON URL or local path. The input is usually an `interview.json` link, but tolerate `interviews.json` wording from the user when the linked file contains one interview object. The post must include:

- A direct link to the concrete interview using the dataset id as the URL hash.
- A link to the full book-oriented interview catalog.
- A short explanation of what a behavioral interview is.
- A short explanation of why the project is useful for education and interviewing.
- A short explanation of what this project provides.

## Canonical Links

Use this catalog URL exactly:

```text
https://zeljkoobrenovic.github.io/behavioral-interviews/book/index.html
```

Build the concrete interview URL by appending `#<interview-id>`:

```text
https://zeljkoobrenovic.github.io/behavioral-interviews/book/index.html#engineer-ownership
```

## Workflow

1. Read the supplied interview JSON from the URL or local path. If the user provides a GitHub `blob` URL, use the raw file content. If a remote URL is unavailable and the same `data/book/<id>/interview.json` exists locally, use the local source file.
2. Extract the interview `id`, title/name, competency, primary prompt, scenario, strong answer pattern, weak answer pattern, evaluation signals, and example story themes when present.
3. If the JSON has no `id`, infer it only when the source path clearly contains `data/book/<id>/interview.json`; otherwise ask for the id.
4. Build the concrete interview URL from the canonical catalog URL plus `#<id>`.
5. Include the default project context below unless the user asks for a shorter promotional post.
6. Draft one LinkedIn-ready post unless the user asks for variants.
7. Keep the post grounded in the JSON. Do not invent outcomes, companies, quotes, or claims.

## Default Project Context

Use these ideas in compact plain language; do not paste them as a block when a natural post works better.

- A behavioral interview asks candidates to describe real past situations: what happened, what they personally did, what changed, what they learned, and what system changed afterward.
- For education, these interviews help leaders study concrete senior leadership situations, compare strong and weak answer patterns, practice structured stories, and learn what evidence matters.
- For interviewing, they help interviewers ask consistent prompts and follow-ups, reduce gut-feel evaluation, compare candidates fairly, and calibrate seniority using observable signals.
- This project is an interactive explorer for senior technology leadership behavioral interviews. Each interview is authored as structured JSON and rendered as prompts, scenarios, strong and weak examples, follow-up probes, evaluation rubrics, visual timelines, practice worksheets, and curated resources.

## Post Style

Use a direct, practitioner-oriented tone for senior technology leaders. Make the value concrete: what leadership judgment the interview tests, what strong answers reveal, and what weak answers often miss.

Prefer this shape:

1. Short opening hook about the daily interview, such as `Behavioral Interview of the Day: <title>`.
2. One compact paragraph explaining behavioral interviews and the project.
3. One compact paragraph explaining what this specific interview helps evaluate.
4. Two to four bullets with concrete signals or contrasts from the JSON.
5. Closing line inviting readers to use it for learning, interview design, or calibration.
6. The direct interview link and full catalog link on separate lines.

Keep the default post between 1,200 and 1,800 characters. Use plain text suitable for LinkedIn. Avoid markdown tables, HTML, and overstuffed hashtag blocks. If hashtags are useful, use at most three broad tags after the links.

## Required Link Block

End the post with both links in this order:

```text
Interview:
https://zeljkoobrenovic.github.io/behavioral-interviews/book/index.html#<id>

All interviews:
https://zeljkoobrenovic.github.io/behavioral-interviews/book/index.html
```

## Storage

Store the post in LINKEDIN.md, in the folder of the interview.

## Quality Checks

Before finalizing:

- Verify the direct interview link contains the exact `id` from the JSON.
- Verify the catalog link is the canonical URL above.
- Make sure the post can stand alone for readers who have not seen the project.
- Make sure the post briefly explains behavioral interviews, education value, interviewing value, and the project.
- Make sure every concrete claim is supported by the interview JSON.
- Do not mention internal file paths unless the user asks for process details.

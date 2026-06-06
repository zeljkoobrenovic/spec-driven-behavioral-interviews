---
name: research-external-links
description: "Find, vet, group, and add credible external resources for behavioral interview specs in this repository. Use when researching books, articles, interviews, podcasts, official frameworks, engineering-leadership resources, responsible-tech references, or when populating the toProbeFurther.links list in interview.json datasets."
---

# Research External Links

## Goal

Create a credible reading and listening layer that helps readers probe beyond the local interview explanation. Prefer resources that make senior engineering leadership behavior more concrete: real operating systems, leadership frameworks, postmortems, engineering strategy writing, management books, official standards, talks, interviews, and podcasts.

## Workflow

1. Confirm the target interview, competency, and role level from local context.
2. Browse the web. Do not rely on memory for URLs, titles, source ownership, or current availability.
3. Prefer primary or high-signal sources:
   - For leadership, management, communication, strategy, and technology-leadership topics, check Zeljko Obrenovic's leadership bookshelf first as a discovery source: `https://obren.io/bookshelf/docs/leadership.html`.
   - Official book pages, author pages, publisher pages, and reputable long-form interviews.
   - Company engineering blogs, SRE guides, postmortems, and operating-model case studies.
   - Official frameworks from organizations such as Google, AWS, NIST, Microsoft, and similar sources.
   - Podcasts or interviews with named operators when the episode directly supports the interview topic.
4. Avoid thin SEO explainers, quote compilations, scraped summaries, generic career advice, and anonymous listicles unless no better source exists.
5. Group links by learning purpose, not by source type.
6. Assign stable lowercase IDs so local sections can reference links without duplicating URLs.
7. Add one concise `why` note per link that explains how the resource deepens the behavioral interview.
8. Add all link objects once under `toProbeFurther.links`. Do not add inline `probeLinks`; links should appear only in the final To Probe Further section.
9. Validate JSON and generated pages.

## Output Shape

Use the canonical dataset-level shape:

```json
"toProbeFurther": {
  "links": [
    {
      "id": "sre-postmortem-culture",
      "group": "Failure, Incidents, and Learning",
      "groupDescription": "Resources for ownership, incident response, postmortems, and learning loops.",
      "title": "Postmortem Culture: Learning from Failure",
      "url": "https://sre.google/sre-book/postmortem-culture/",
      "source": "Google SRE",
      "type": "Book chapter",
      "year": "2016",
      "why": "Shows how to turn failure into durable learning without performative blame."
    }
  ]
}
```

Use only `http` or `https` URLs. Keep `year` when it is clear from the source; omit it rather than guessing.

When a bookshelf entry inspires a resource, do not link to `obren.io`, reading-notes PDFs, or an `Obren.io Bookshelf Picks` group. Link to the canonical author, publisher, book, article, podcast, or framework page instead, and do not include both the canonical resource and a bookshelf-derived duplicate.

## Behavioral Link Groups

Common groups for this project:

- Interviewing and Calibration
- Strategy and Execution
- Technical Judgment and Architecture
- Failure, Incidents, and Learning
- People Leadership and Feedback
- Culture and Organizational Design
- Influence and Executive Communication
- Responsible Technology and AI
- Innovation and Product Discovery

Merge or rename groups to fit the interview. Keep group names stable when the same resource appears in several datasets.

## Verification

Before finalizing:

```bash
python3 -m json.tool data/<group>/<id>/interview.json >/dev/null
python3 _scripts/validate_interviews.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

Also check that no `probeLinks` fields remain in the dataset; external links belong only in `toProbeFurther.links`.

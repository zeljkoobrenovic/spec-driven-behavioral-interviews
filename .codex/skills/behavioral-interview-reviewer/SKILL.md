---
name: behavioral-interview-reviewer
description: "Review behavioral interview specs in this repository for realism, balance, educative value, interviewer usability, and data quality. Use when asked to critique interviews, audit the catalog, identify gaps, score interview quality, or write/update REVIEW.md with findings and recommendations."
---

# Behavioral Interview Reviewer

## Workflow

1. Read `AGENTS.md`, `REVIEW.md` if it exists, the relevant group manifest, and the target `interview.json` files.
2. Run the data checks before judging content:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
```

3. Review source files under `data/`, not generated copies under `docs/`.
4. Evaluate each interview against the review dimensions below.
5. Review `toProbeFurther.links[]` when present. For leadership, management, communication, strategy, and technology-leadership topics, check whether relevant resources from `https://obren.io/bookshelf/docs/leadership.html` have been considered as inspiration, while ensuring the final links point to canonical non-Obren resources and do not duplicate the same book or article.
6. Write findings in `REVIEW.md` when the user asks for a documented review, catalog audit, or reusable review process.
7. Separate fixable data issues from subjective content recommendations.

## Review Dimensions

Score each dimension from 1 to 5 when a structured review is useful:

- Realism: The prompt reflects actual senior engineering leadership situations, with messy constraints, incomplete information, disagreement, timelines, business stakes, and credible outcomes.
- Balance: The spec avoids overfitting to one company type or leadership style. It balances technical, product, business, people, ethics, execution, and communication signals where relevant.
- Educative Value: A reader learns what good looks like. The strong answer pattern, weak answer pattern, examples, follow-ups, and rubric make the evaluation logic explicit.
- Interview Usability: Prompts are easy to ask, variants are useful, follow-ups expose evidence, and rubrics help an interviewer make a fair decision.
- Spec Quality: The JSON is complete, internally consistent, stable in ids and paths, and aligned with templates and validation scripts.
- External Resources: Every resource has a clear one-sentence relevance note, resources are credible, bookshelf-inspired picks link to canonical non-Obren pages, duplicate book/article links are avoided, and links appear only in the final To Probe Further section.

## Review Heuristics

Flag weak realism when examples sound like polished hindsight with no conflict, uncertainty, rejected alternatives, or measurable trade-offs.

Flag weak balance when every strong answer rewards the same behavior, such as process creation, without recognizing context where speed, escalation, technical depth, or principled refusal matters.

Flag weak educative value when the spec says a candidate should "align stakeholders" or "show ownership" but does not teach the concrete behavior an interviewer should listen for.

Flag weak interview usability when follow-ups are generic, rubrics blur levels together, or prompt variants do not meaningfully change the evidence gathered.

## REVIEW.md Structure

Use this shape for repository-level reviews:

```markdown
# Review

## Purpose
## Rating Scale
## Current Snapshot
## Overall Assessment
## Strengths
## Gaps And Risks
## Review Dimensions
## Priority Recommendations
## Per-Interview Review
## Ongoing Review Checklist
```

For per-interview findings, include the file path, a concise rating, main strengths, main risks, and recommended next edits.

## Verification

After changing only `REVIEW.md` or skill files, run YAML/frontmatter checks if available. After changing interview data, also run:

```bash
python3 _scripts/validate_interviews.py
python3 _scripts/summarize_coverage.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

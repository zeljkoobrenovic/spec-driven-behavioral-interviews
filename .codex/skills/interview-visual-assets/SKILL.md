---
name: interview-visual-assets
description: "Plan, add, and generate visual assets for behavioral interview specs in this repository. Use when deciding where interviews should be illustrated, adding assets.icon, explainerComic, strong/weak answer pattern aiVisual, strong/weak signal visuals, or exampleStories aiVisual fields, running dry-run image generation scripts, or improving visual prompts and generated interview imagery."
---

# Interview Visual Assets

## Workflow

1. Read the target `interview.json` and inspect whether it already has `assets.icon`, `explainerComic`, `strongAnswerPattern.aiVisual`, `weakAnswerPattern.aiVisual`, `evaluation.signals[].strongAiVisual`, `evaluation.signals[].weakAiVisual`, or `exampleStories[].aiVisual`.
2. Decide the useful illustration surfaces before generating files:
   - Overview icon for quick scanning.
   - Explainer comic for the interview's central tension.
   - Strong/weak answer-pattern visuals for the answer contrast.
   - Strong/weak signal visuals for evaluation calibration.
   - Example-story visual for concrete, memorable variants.
3. Prefer visuals that clarify behavior, trade-offs, or operating mechanisms. Avoid decorative images that only restate the title.
4. Use dry-run mode first and review planned paths/prompts.
5. Generate assets only when the user wants real images and `GEMINI_API_KEY` is available.
6. Rebuild the generated site after JSON or asset changes.

## Image Fields

Use dataset-relative paths:

- `assets.icon`: small overview image for the card.
- `explainerComic`: visual summary image for the interview.
- `strongAnswerPattern.aiVisual`: visual attached to the strong answer pattern.
- `weakAnswerPattern.aiVisual`: visual attached to the weak answer pattern.
- `evaluation.signals[].strongAiVisual`: visual attached to the strong side of an evaluation signal.
- `evaluation.signals[].weakAiVisual`: visual attached to the weak side of an evaluation signal.
- `exampleStories[].aiVisual`: visual attached to a concrete example story.

The static templates make generated images clickable and open them in a new tab.

## Scripts

Use these project scripts from the repository root:

```bash
python3 _scripts/generate_missing_interview_icons.py --dry-run
python3 _scripts/generate_interview_comic.py --dry-run
python3 _scripts/generate_answer_pattern_pictures.py --dry-run
python3 _scripts/generate_signal_pictures.py --dry-run
python3 _scripts/generate_example_story_pictures.py --dry-run
python3 _scripts/generate_interview_assets.py --dry-run
```

For real generation, rerun the relevant script without `--dry-run` only after confirming credentials and desired scope.

## Verification

Run:

```bash
python3 _scripts/validate_interviews.py
python3 build.py
python3 _scripts/smoke_static_site.py
```

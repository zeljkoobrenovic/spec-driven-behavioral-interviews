#!/usr/bin/env python3
"""Generate behavioral-interview visual assets with Gemini image APIs.

Examples:
    python3 _scripts/generate_interview_assets.py data/book/crisis-leadership/interview.json --dry-run

    GEMINI_API_KEY=... python3 _scripts/generate_interview_assets.py \
        data/book/crisis-leadership/interview.json --only examples --only comic

The script can generate:

- overview icon: ``assets.icon``
- concrete example visuals: ``exampleStories[].aiVisual``
- answer-pattern visuals: ``strongAnswerPattern.aiVisual`` and ``weakAnswerPattern.aiVisual``
- signal visuals: ``evaluation.signals[].strongAiVisual`` and ``evaluation.signals[].weakAiVisual``
- interview visual summary: ``explainerComic``

Generated paths are written back into ``interview.json`` after successful image
generation, or when an existing target image is found. It does not rebuild
``docs/``.
"""

from __future__ import annotations

import argparse
import base64
import collections
import json
import os
import re
import sys
import textwrap
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MODEL = "gemini-3-pro-image-preview"
DEFAULT_ICON_SIZE = "1K"
DEFAULT_IMAGE_SIZE = "2K"


@dataclass(frozen=True)
class ImageSpec:
    kind: str
    label: str
    path: Path
    prompt: str
    aspect_ratio: str
    image_size: str
    model: str
    json_pointer: tuple[Any, ...] | None


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def endpoint_for(model: str) -> str:
    return (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent"
    )


def extension_for_mime(mime_type: str) -> str:
    return {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/webp": ".webp",
        "image/gif": ".gif",
    }.get(mime_type.lower(), ".png")


def existing_for_stem(path: Path) -> Path | None:
    if not path.parent.is_dir():
        return None
    for candidate in sorted(path.parent.glob(path.stem + ".*")):
        if candidate.stem == path.stem and candidate.is_file():
            return candidate
    return None


def slugify(value: str, fallback: str = "asset") -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or fallback


def compact(value: Any, max_chars: int = 900) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        text = value
    elif isinstance(value, list):
        text = "; ".join(compact(item, max_chars=max_chars) for item in value)
    elif isinstance(value, dict):
        parts = []
        for key, item in value.items():
            if item in (None, "", [], {}):
                continue
            parts.append(f"{key}: {compact(item, max_chars=max_chars)}")
        text = "; ".join(parts)
    else:
        text = str(value)
    text = re.sub(r"\s+", " ", text).strip()
    return textwrap.shorten(text, width=max_chars, placeholder="...")


def load_dataset(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"error: expected top-level object in {path}")
    return data


def write_dataset(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def dataset_relative_path(image_path: Path, dataset_dir: Path) -> str:
    try:
        return image_path.resolve().relative_to(dataset_dir.resolve()).as_posix()
    except ValueError:
        raise RuntimeError(f"{rel(image_path)} is not under dataset directory {rel(dataset_dir)}")


def set_json_pointer(root: dict[str, Any], pointer: tuple[Any, ...], value: str) -> None:
    node: Any = root
    for part in pointer[:-1]:
        if isinstance(part, int):
            node = node[part]
        elif part in node:
            node = node[part]
        else:
            child = collections.OrderedDict()
            node[part] = child
            node = child
    node[pointer[-1]] = value


def icon_prompt(title: str, context: str) -> str:
    return "\n".join(
        [
            "Create a small square overview icon for a senior technology leadership behavioral interview.",
            "Style: minimalist professional editorial illustration, clean vector shapes, crisp outlines, white or very light background.",
            "No text, no labels, no logo marks, no border, no frame, no photorealism, no 3D.",
            "Communicate the leadership competency through a simple metaphor or workplace scene.",
            f"Interview title: {title}",
            f"Context: {context}",
        ]
    )


def example_prompt(interview: dict[str, Any], example: dict[str, Any]) -> str:
    return "\n".join(
        [
            "Create a 16:9 educational illustration for a senior technology leadership behavioral interview example.",
            "Style: polished flat-vector business/technology illustration, restrained teal/blue/amber accents, clean white background.",
            "Show the leadership situation and the strong response pattern visually. Avoid dense text; if labels are used, keep them very short and legible.",
            "The image should help a candidate remember the story shape, not act as a screenshot or diagram.",
            "No watermarks, no UI chrome, no photorealism, no 3D, no fantasy styling.",
            f"Interview: {compact(interview.get('title'), 160)}",
            f"Competency: {compact(interview.get('competency'), 260)}",
            f"Example title: {compact(example.get('title'), 160)}",
            f"Prompt variant: {compact(example.get('promptVariant'), 260)}",
            f"Situation: {compact(example.get('situation'), 420)}",
            f"Strong answer sketch: {compact(example.get('strongAnswerSketch'), 700)}",
            f"Why it works: {compact(example.get('whyItWorks'), 500)}",
            "Visual composition: show the messy situation on the left, the leader's concrete mechanisms in the center, and the durable system change on the right.",
        ]
    )


def comic_prompt(interview: dict[str, Any]) -> str:
    examples = [
        f"{item.get('title')}: {item.get('situation')}"
        for item in interview.get("exampleStories", [])[:3]
        if isinstance(item, dict)
    ]
    return "\n".join(
        [
            "Create a polished 2:3 comic-strip explainer for a senior technology leadership behavioral interview.",
            "Use 4 to 6 panels with clear visual progression. Minimal text only, short labels if needed.",
            "Style: refined editorial comic, professional workplace/technology context, restrained colors, crisp outlines, readable at presentation size.",
            "No watermarks, no fake UI screenshots, no photorealism, no 3D.",
            f"Interview: {compact(interview.get('title'), 160)}",
            f"Description: {compact(interview.get('description'), 260)}",
            f"Competency: {compact(interview.get('competency'), 320)}",
            f"Primary prompt: {compact((interview.get('prompt') or {}).get('primary'), 260)}",
            f"Story anatomy: {compact(interview.get('storyAnatomy'), 900)}",
            f"Strong pattern: {compact(interview.get('strongAnswerPattern'), 700)}",
            f"Weak pattern: {compact(interview.get('weakAnswerPattern'), 500)}",
            f"Concrete examples: {compact(examples, 700)}",
            "Panel flow: prompt -> messy leadership situation -> strong leader mechanisms -> measurable result -> reflection and system change.",
        ]
    )


def answer_pattern_prompt(interview: dict[str, Any], pattern_kind: str, pattern: dict[str, Any]) -> str:
    if pattern_kind == "strong":
        return "\n".join(
            [
                "Create a 16:9 educational illustration for a strong senior technology leadership behavioral interview answer pattern.",
                "Style: polished flat-vector business/technology illustration, restrained teal/blue/amber accents, clean white background.",
                "Show a candidate turning a messy situation into explicit decision criteria, stakeholder alignment, concrete action, measurable result, and durable operating change.",
                "Avoid dense text; if labels are used, keep them very short and legible.",
                "No watermarks, no UI chrome, no photorealism, no 3D, no fantasy styling.",
                f"Interview: {compact(interview.get('title'), 160)}",
                f"Description: {compact(interview.get('description'), 260)}",
                f"Competency: {compact(interview.get('competency'), 320)}",
                f"Primary prompt: {compact((interview.get('prompt') or {}).get('primary'), 260)}",
                f"Strong answer summary: {compact(pattern.get('summary'), 420)}",
                f"Strong answer moves: {compact(pattern.get('moves'), 900)}",
                f"Story anatomy: {compact(interview.get('storyAnatomy'), 700)}",
                "Visual composition: left side shows ambiguity or pressure, center shows the leader's structure and mechanisms, right side shows measured outcome and system change.",
            ]
        )

    return "\n".join(
        [
            "Create a 16:9 educational illustration for a weak senior technology leadership behavioral interview answer pattern.",
            "Style: polished flat-vector business/technology illustration, restrained red/gray/amber warning accents, clean white background.",
            "Show common weak-answer failure modes: vague alignment, missing trade-offs, unclear personal ownership, technical activity without business impact, and no durable learning loop.",
            "Keep the tone instructional and professional, not mocking. Avoid dense text; if labels are used, keep them very short and legible.",
            "No watermarks, no UI chrome, no photorealism, no 3D, no fantasy styling.",
            f"Interview: {compact(interview.get('title'), 160)}",
            f"Description: {compact(interview.get('description'), 260)}",
            f"Competency: {compact(interview.get('competency'), 320)}",
            f"Primary prompt: {compact((interview.get('prompt') or {}).get('primary'), 260)}",
            f"Weak answer summary: {compact(pattern.get('summary'), 420)}",
            f"Red flags: {compact(pattern.get('redFlags'), 900)}",
            f"Strong pattern for contrast: {compact(interview.get('strongAnswerPattern'), 600)}",
            "Visual composition: left side shows the prompt or situation, center shows scattered actions and hand-wavy alignment, right side shows unresolved outcomes and missing evidence.",
        ]
    )


def signal_prompt(interview: dict[str, Any], signal: dict[str, Any], signal_kind: str) -> str:
    if signal_kind == "strong":
        return "\n".join(
            [
                "Create a 16:9 educational illustration for a strong interview evaluation signal.",
                "Style: polished flat-vector business/technology illustration, restrained teal/blue/amber accents, clean white background.",
                "Show the evidence an interviewer should listen for when a senior technology leader gives a strong behavioral answer.",
                "Avoid dense text; if labels are used, keep them very short and legible.",
                "No watermarks, no UI chrome, no photorealism, no 3D, no fantasy styling.",
                f"Interview: {compact(interview.get('title'), 160)}",
                f"Competency: {compact(interview.get('competency'), 320)}",
                f"Primary prompt: {compact((interview.get('prompt') or {}).get('primary'), 260)}",
                f"Signal name: {compact(signal.get('name'), 120)}",
                f"Strong signal: {compact(signal.get('strong'), 500)}",
                f"Weak contrast: {compact(signal.get('weak'), 350)}",
                f"Strong answer pattern: {compact(interview.get('strongAnswerPattern'), 650)}",
                "Visual composition: show observable candidate evidence, concrete mechanisms, and a clear positive outcome connected to this signal.",
            ]
        )

    return "\n".join(
        [
            "Create a 16:9 educational illustration for a weak interview evaluation signal.",
            "Style: polished flat-vector business/technology illustration, restrained red/gray/amber warning accents, clean white background.",
            "Show the red flag an interviewer should notice when a senior technology leadership behavioral answer is weak or shallow.",
            "Keep the tone instructional and professional, not mocking. Avoid dense text; if labels are used, keep them very short and legible.",
            "No watermarks, no UI chrome, no photorealism, no 3D, no fantasy styling.",
            f"Interview: {compact(interview.get('title'), 160)}",
            f"Competency: {compact(interview.get('competency'), 320)}",
            f"Primary prompt: {compact((interview.get('prompt') or {}).get('primary'), 260)}",
            f"Signal name: {compact(signal.get('name'), 120)}",
            f"Weak signal: {compact(signal.get('weak'), 500)}",
            f"Strong contrast: {compact(signal.get('strong'), 350)}",
            f"Weak answer pattern: {compact(interview.get('weakAnswerPattern'), 650)}",
            "Visual composition: show vague evidence, missing ownership or tradeoffs, and an unresolved outcome connected to this signal.",
        ]
    )


def collect_specs(
    interview_file: Path,
    data: dict[str, Any],
    only: set[str],
    model: str,
    icon_size: str,
    image_size: str,
) -> list[ImageSpec]:
    dataset_dir = interview_file.parent
    title = str(data.get("title") or dataset_dir.name)
    description = compact(data.get("description"), 600)
    specs: list[ImageSpec] = []

    if "icon" in only:
        specs.append(
            ImageSpec(
                kind="icon",
                label=f"{title} overview icon",
                path=dataset_dir / "icon.png",
                prompt=icon_prompt(title, description),
                aspect_ratio="1:1",
                image_size=icon_size,
                model=model,
                json_pointer=("assets", "icon"),
            )
        )

    if "examples" in only:
        for index, example in enumerate(data.get("exampleStories") or []):
            if not isinstance(example, dict):
                continue
            example_id = str(example.get("id") or f"example-{index + 1}")
            specs.append(
                ImageSpec(
                    kind="example",
                    label=f"{title}: {example.get('title') or example_id}",
                    path=dataset_dir / "assets" / "generated" / "example-stories" / f"{slugify(example_id, 'example')}.png",
                    prompt=example_prompt(data, example),
                    aspect_ratio="16:9",
                    image_size=image_size,
                    model=model,
                    json_pointer=("exampleStories", index, "aiVisual"),
                )
            )

    if "comic" in only:
        specs.append(
            ImageSpec(
                kind="comic",
                label=f"{title} visual summary",
                path=dataset_dir / "assets" / "generated" / "comic" / "interview-comic.png",
                prompt=comic_prompt(data),
                aspect_ratio="2:3",
                image_size=image_size,
                model=model,
                json_pointer=("explainerComic",),
            )
        )

    if "patterns" in only:
        strong_pattern = data.get("strongAnswerPattern")
        if isinstance(strong_pattern, dict):
            specs.append(
                ImageSpec(
                    kind="strong-pattern",
                    label=f"{title} strong answer pattern",
                    path=dataset_dir / "assets" / "generated" / "answer-patterns" / "strong-answer-pattern.png",
                    prompt=answer_pattern_prompt(data, "strong", strong_pattern),
                    aspect_ratio="16:9",
                    image_size=image_size,
                    model=model,
                    json_pointer=("strongAnswerPattern", "aiVisual"),
                )
            )

        weak_pattern = data.get("weakAnswerPattern")
        if isinstance(weak_pattern, dict):
            specs.append(
                ImageSpec(
                    kind="weak-pattern",
                    label=f"{title} weak answer pattern",
                    path=dataset_dir / "assets" / "generated" / "answer-patterns" / "weak-answer-pattern.png",
                    prompt=answer_pattern_prompt(data, "weak", weak_pattern),
                    aspect_ratio="16:9",
                    image_size=image_size,
                    model=model,
                    json_pointer=("weakAnswerPattern", "aiVisual"),
                )
            )

    if "signals" in only:
        evaluation = data.get("evaluation") if isinstance(data.get("evaluation"), dict) else {}
        for index, signal in enumerate(evaluation.get("signals") or []):
            if not isinstance(signal, dict):
                continue
            signal_id = slugify(str(signal.get("id") or signal.get("name") or f"signal-{index + 1}"), f"signal-{index + 1}")
            signal_name = str(signal.get("name") or signal_id)
            specs.append(
                ImageSpec(
                    kind="signal-strong",
                    label=f"{title}: {signal_name} strong signal",
                    path=dataset_dir / "assets" / "generated" / "signals" / f"{signal_id}-strong.png",
                    prompt=signal_prompt(data, signal, "strong"),
                    aspect_ratio="16:9",
                    image_size=image_size,
                    model=model,
                    json_pointer=("evaluation", "signals", index, "strongAiVisual"),
                )
            )
            specs.append(
                ImageSpec(
                    kind="signal-weak",
                    label=f"{title}: {signal_name} weak signal",
                    path=dataset_dir / "assets" / "generated" / "signals" / f"{signal_id}-weak.png",
                    prompt=signal_prompt(data, signal, "weak"),
                    aspect_ratio="16:9",
                    image_size=image_size,
                    model=model,
                    json_pointer=("evaluation", "signals", index, "weakAiVisual"),
                )
            )

    return specs


def extract_image(response: dict[str, Any]) -> tuple[bytes, str]:
    for candidate in response.get("candidates") or []:
        content = candidate.get("content") or {}
        for part in content.get("parts") or []:
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                mime_type = inline.get("mimeType") or inline.get("mime_type") or "image/png"
                return base64.b64decode(inline["data"]), mime_type
    raise RuntimeError("No image data in Gemini response. Raw response: " + json.dumps(response)[:1000])


def call_gemini_image(api_key: str, spec: ImageSpec, timeout: int = 240) -> tuple[bytes, str]:
    payload = {
        "contents": [{"role": "user", "parts": [{"text": spec.prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {
                "aspectRatio": spec.aspect_ratio,
                "imageSize": spec.image_size,
            },
        },
    }
    request = urllib.request.Request(
        f"{endpoint_for(spec.model)}?key={api_key}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from Gemini: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error calling Gemini: {exc}") from exc
    return extract_image(json.loads(body.decode("utf-8")))


def process_spec(spec: ImageSpec, api_key: str | None, force: bool, dry_run: bool) -> tuple[str, Path | None]:
    existing = existing_for_stem(spec.path)
    if existing and not force:
        return f"skip existing: {rel(existing)}", existing
    if dry_run:
        prompt = textwrap.shorten(re.sub(r"\s+", " ", spec.prompt), width=280, placeholder="...")
        return f"dry-run: {rel(spec.path)}\n    prompt: {prompt}", None
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    image_bytes, mime_type = call_gemini_image(api_key, spec)
    actual_path = spec.path.with_suffix(extension_for_mime(mime_type))
    actual_path.parent.mkdir(parents=True, exist_ok=True)
    actual_path.write_bytes(image_bytes)
    return f"generated: {rel(actual_path)}", actual_path


def apply_json_updates(interview_file: Path, data: dict[str, Any], generated_paths: dict[tuple[Any, ...], Path]) -> list[str]:
    changes: list[str] = []
    for pointer, path in generated_paths.items():
        rel_path = dataset_relative_path(path, interview_file.parent)
        node: Any = data
        for part in pointer[:-1]:
            if isinstance(part, int):
                node = node[part]
            elif part in node:
                node = node[part]
            else:
                node[part] = collections.OrderedDict()
                node = node[part]
        if node.get(pointer[-1]) == rel_path:
            continue
        set_json_pointer(data, pointer, rel_path)
        changes.append(".".join(str(part) for part in pointer) + f" -> {rel_path}")
    if changes:
        write_dataset(interview_file, data)
    return changes


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("interview_json", help="Path to data/<group>/<id>/interview.json.")
    parser.add_argument("--only", action="append", choices=("icon", "examples", "comic", "patterns", "signals"), help="Asset kind to generate. Repeatable. Defaults to all.")
    parser.add_argument("--dry-run", action="store_true", help="Print targets and prompt summaries without API calls or writes.")
    parser.add_argument("--force", action="store_true", help="Regenerate even when an image with the target stem already exists.")
    parser.add_argument("--no-write-json", action="store_true", help="Do not write generated image paths into interview.json.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Gemini image model (default: {DEFAULT_MODEL}).")
    parser.add_argument("--icon-size", default=DEFAULT_ICON_SIZE, help=f"Gemini image size for icons (default: {DEFAULT_ICON_SIZE}).")
    parser.add_argument("--image-size", default=DEFAULT_IMAGE_SIZE, help=f"Gemini image size for examples, comics, patterns, and signals (default: {DEFAULT_IMAGE_SIZE}).")
    parser.add_argument("--sleep", type=float, default=2.0, help="Seconds between generated images (default: 2).")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    interview_file = Path(args.interview_json)
    if not interview_file.is_absolute():
        interview_file = (Path.cwd() / interview_file).resolve()
    if not interview_file.is_file():
        print(f"error: no interview.json at {interview_file}", file=sys.stderr)
        return 2

    data = load_dataset(interview_file)
    only = set(args.only or ("icon", "examples", "comic", "patterns", "signals"))
    specs = collect_specs(
        interview_file=interview_file,
        data=data,
        only=only,
        model=args.model,
        icon_size=args.icon_size,
        image_size=args.image_size,
    )

    api_key = os.environ.get("GEMINI_API_KEY")
    needs_api = any(args.force or not existing_for_stem(spec.path) for spec in specs)
    if needs_api and not api_key and not args.dry_run:
        print("error: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        return 2

    print(f"Processing {rel(interview_file)}")
    print(f"Planned assets: {len(specs)}")
    generated_paths: dict[tuple[Any, ...], Path] = {}
    errors = 0

    for index, spec in enumerate(specs, start=1):
        print(f"[{index}/{len(specs)}] {spec.kind}: {spec.label}")
        try:
            status, path = process_spec(spec, api_key=api_key, force=args.force, dry_run=args.dry_run)
            print(f"    {status}")
            if spec.json_pointer and path:
                generated_paths[spec.json_pointer] = path
            if path and args.sleep and index < len(specs):
                time.sleep(args.sleep)
        except Exception as exc:  # noqa: BLE001
            errors += 1
            print(f"    ERROR: {exc}", file=sys.stderr)

    if not args.no_write_json:
        if args.dry_run:
            print("\nPlanned JSON link updates:")
            for spec in specs:
                if spec.json_pointer:
                    planned_path = generated_paths.get(spec.json_pointer) or spec.path
                    print(f"    {'.'.join(str(part) for part in spec.json_pointer)} -> {dataset_relative_path(planned_path, interview_file.parent)}")
        else:
            changes = apply_json_updates(interview_file, data, generated_paths)
            print(f"\nJSON link updates: {len(changes)}")
            for change in changes:
                print(f"    {change}")

    print(f"\nDone. Errors: {errors}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Generate strong/weak evaluation-signal visuals for one behavioral interview."""

from __future__ import annotations

import sys

import generate_interview_assets


def main(argv: list[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    if "--only" not in args:
        args = ["--only", "signals", *args]
    return generate_interview_assets.main(args)


if __name__ == "__main__":
    raise SystemExit(main())

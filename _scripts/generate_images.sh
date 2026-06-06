#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "usage: _scripts/generate_images.sh data/book/<id>/interview.json [extra args...]" >&2
  exit 2
fi

interview_json="$1"
shift

python3 _scripts/generate_interview_assets.py "$interview_json" "$@"

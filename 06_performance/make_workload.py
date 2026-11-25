"""Create a deterministic JSONL prompt fixture for a local benchmark."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, default=Path("artifacts/workload.jsonl"))
parser.add_argument("--requests", type=int, default=32)
args = parser.parse_args()

if args.requests <= 0:
    raise SystemExit("--requests must be positive")

args.output.parent.mkdir(parents=True, exist_ok=True)
with args.output.open("w", encoding="utf-8") as stream:
    for request_id in range(args.requests):
        stream.write(
            json.dumps(
                {
                    "request_id": f"fixture-{request_id:04d}",
                    "prompt": "Summarize why reproducible benchmark inputs matter.",
                    "max_tokens": 64,
                }
            )
            + "\n"
        )

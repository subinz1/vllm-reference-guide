"""Validate and print a minimal reproducibility record for a model lab."""

from __future__ import annotations

import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True)
parser.add_argument("--revision", required=True)
parser.add_argument("--tokenizer-revision")
parser.add_argument("--chat-template")
args = parser.parse_args()

if not args.model.strip() or not args.revision.strip():
    raise SystemExit("model and revision must be non-empty")

manifest = {
    "model": args.model,
    "revision": args.revision,
    "tokenizer_revision": args.tokenizer_revision,
    "chat_template": args.chat_template,
}
print(json.dumps(manifest, indent=2, sort_keys=True))

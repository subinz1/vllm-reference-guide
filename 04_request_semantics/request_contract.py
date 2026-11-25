"""Validate a portable chat request record before it reaches a service."""

from __future__ import annotations

import json
import sys


payload = json.load(sys.stdin)
messages = payload.get("messages")
if not isinstance(messages, list) or not messages:
    raise SystemExit("messages must be a non-empty list")

for index, message in enumerate(messages):
    if not isinstance(message, dict):
        raise SystemExit(f"messages[{index}] must be an object")
    if not isinstance(message.get("role"), str):
        raise SystemExit(f"messages[{index}].role must be a string")
    if not isinstance(message.get("content"), str):
        raise SystemExit(f"messages[{index}].content must be a string")

max_tokens = payload.get("max_tokens")
if max_tokens is not None and (not isinstance(max_tokens, int) or max_tokens <= 0):
    raise SystemExit("max_tokens must be a positive integer when supplied")

print("request contract is valid")

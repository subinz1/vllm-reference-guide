"""Validate a portable structured-output request before it reaches a server."""

from __future__ import annotations

import json
import sys
from typing import Any


def fail(message: str) -> None:
    raise SystemExit(f"invalid structured-output request: {message}")


def validate_json_schema(schema: Any) -> None:
    if not isinstance(schema, dict):
        fail("response_format.json_schema.schema must be an object")
    if schema.get("type") != "object":
        fail("response_format.json_schema.schema.type must be 'object'")
    properties = schema.get("properties")
    if properties is not None and not isinstance(properties, dict):
        fail("response_format.json_schema.schema.properties must be an object")


def main() -> None:
    payload = json.load(sys.stdin)
    if not isinstance(payload, dict):
        fail("request must be a JSON object")

    response_format = payload.get("response_format")
    if not isinstance(response_format, dict):
        fail("response_format must be an object")
    if response_format.get("type") != "json_schema":
        fail("response_format.type must be 'json_schema'")

    json_schema = response_format.get("json_schema")
    if not isinstance(json_schema, dict):
        fail("response_format.json_schema must be an object")
    name = json_schema.get("name")
    if not isinstance(name, str) or not name:
        fail("response_format.json_schema.name must be a non-empty string")
    validate_json_schema(json_schema.get("schema"))

    strict = json_schema.get("strict")
    if strict is not None and not isinstance(strict, bool):
        fail("response_format.json_schema.strict must be a boolean when supplied")

    print(f"structured-output contract is valid: schema={name}")


if __name__ == "__main__":
    main()

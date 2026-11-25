"""Check local vLLM health and discover the served model IDs."""

from __future__ import annotations

import json
import os
from urllib.request import Request, urlopen


base_url = os.environ.get("VLLM_BASE_URL", "http://127.0.0.1:8000")
api_key = os.environ["VLLM_API_KEY"]

with urlopen(f"{base_url}/health", timeout=5) as response:
    print(f"health={response.status}")

request = Request(
    f"{base_url}/v1/models",
    headers={"Authorization": f"Bearer {api_key}"},
)
with urlopen(request, timeout=5) as response:
    models = json.load(response)

for model in models["data"]:
    print(f"model={model['id']}")

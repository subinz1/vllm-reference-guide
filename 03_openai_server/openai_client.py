"""Call a local vLLM server using the OpenAI Python client."""

from __future__ import annotations

import os

from openai import OpenAI


api_key = os.environ["VLLM_API_KEY"]
base_url = os.environ.get("VLLM_BASE_URL", "http://127.0.0.1:8000/v1")
model = os.environ.get("MODEL_ID", "Qwen/Qwen2.5-1.5B-Instruct")

client = OpenAI(api_key=api_key, base_url=base_url)
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Explain KV cache in one sentence."}],
    temperature=0,
)
print(response.choices[0].message.content)

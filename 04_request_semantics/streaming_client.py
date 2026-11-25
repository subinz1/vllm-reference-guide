"""Print streamed text fragments in the order received from a local server."""

from __future__ import annotations

import os

from openai import OpenAI


client = OpenAI(
    api_key=os.environ["VLLM_API_KEY"],
    base_url=os.environ.get("VLLM_BASE_URL", "http://127.0.0.1:8000/v1"),
)
model = os.environ.get("MODEL_ID", "Qwen/Qwen2.5-1.5B-Instruct")

stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Explain prefill and decode."}],
    stream=True,
)
for event in stream:
    if event.choices and (content := event.choices[0].delta.content):
        print(content, end="", flush=True)
print()

"""Generate from OpenAI-style messages through the offline chat interface."""

from __future__ import annotations

import os

from vllm import LLM, SamplingParams


model = os.environ.get("MODEL_ID", "Qwen/Qwen2.5-1.5B-Instruct")
conversations = [
    [
        {"role": "system", "content": "Answer concisely."},
        {"role": "user", "content": "What is continuous batching?"},
    ],
    [
        {"role": "system", "content": "Answer concisely."},
        {"role": "user", "content": "Why should a benchmark warm up first?"},
    ],
]
params = SamplingParams(temperature=0.0, max_tokens=64)

for conversation, output in zip(conversations, LLM(model=model).chat(conversations, params)):
    candidate = output.outputs[0]
    print(f"user={conversation[-1]['content']!r}")
    print(f"assistant={candidate.text!r}")
    print(f"finish_reason={candidate.finish_reason!r}")

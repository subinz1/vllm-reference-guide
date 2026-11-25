"""Run a deliberately small offline generation smoke test."""

from __future__ import annotations

import os

from vllm import LLM, SamplingParams


model = os.environ.get("MODEL_ID", "facebook/opt-125m")
prompts = [
    "A reliable model-serving experiment starts by",
    "The most useful latency metric for an interactive user is",
]
params = SamplingParams(temperature=0.0, max_tokens=48)

for output in LLM(model=model).generate(prompts, params):
    candidate = output.outputs[0]
    print(f"prompt={output.prompt!r}")
    print(f"text={candidate.text!r}")
    print(f"finish_reason={candidate.finish_reason!r}")

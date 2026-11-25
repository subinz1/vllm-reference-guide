"""Write a small, inspectable sampling comparison to JSONL."""

import json
from pathlib import Path

from vllm import LLM, SamplingParams


MODEL = "facebook/opt-125m"
PROMPT = "A deployment runbook should"
OUTPUT = Path("artifacts/sampling-experiment.jsonl")

llm = LLM(model=MODEL)
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT.open("w", encoding="utf-8") as stream:
    for temperature in (0.0, 0.7):
        params = SamplingParams(temperature=temperature, max_tokens=32)
        result = llm.generate([PROMPT], params)[0].outputs[0]
        stream.write(
            json.dumps(
                {
                    "model": MODEL,
                    "prompt": PROMPT,
                    "temperature": temperature,
                    "text": result.text,
                    "finish_reason": result.finish_reason,
                }
            )
            + "\n"
        )

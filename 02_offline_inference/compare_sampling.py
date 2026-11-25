"""Persist a one-variable sampling comparison as JSONL."""

from __future__ import annotations

import json
import os
from pathlib import Path

from vllm import LLM, SamplingParams


model = os.environ.get("MODEL_ID", "facebook/opt-125m")
prompt = "A production rollback plan should"
output_path = Path(os.environ.get("RESULT_PATH", "artifacts/sampling.jsonl"))

output_path.parent.mkdir(parents=True, exist_ok=True)
llm = LLM(model=model)
with output_path.open("w", encoding="utf-8") as stream:
    for temperature in (0.0, 0.7):
        params = SamplingParams(temperature=temperature, max_tokens=48)
        result = llm.generate([prompt], params)[0].outputs[0]
        stream.write(
            json.dumps(
                {
                    "model": model,
                    "prompt": prompt,
                    "temperature": temperature,
                    "max_tokens": 48,
                    "text": result.text,
                    "finish_reason": result.finish_reason,
                }
            )
            + "\n"
        )

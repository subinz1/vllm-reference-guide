# Day 5 — Control sampling and record experiments

**Lab type:** Accelerator lab

## Outcome

You can change one generation control at a time and distinguish an API default
from a measured experiment.

## Core controls

- `temperature` controls randomness in token selection.
- `top_p` limits sampling to a cumulative-probability region.
- `max_tokens` bounds output length for a request.
- seed and model revision make a comparison more reproducible, but hardware and
  backend differences can still matter.

Use `examples/04_sampling_experiment.py` to capture inputs and outputs in a
small JSONL file. Its purpose is comparison, not benchmarking.

## Experiment rule

Hold the prompt, model revision, tokenizer, server configuration, and workload
shape constant. Change one parameter, state the expected effect, then record
what happened.

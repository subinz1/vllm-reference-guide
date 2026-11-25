# Day 3 — Generate offline

**Lab type:** Accelerator lab

## Outcome

You can run a deliberately small offline generation workload and inspect a
`RequestOutput` instead of treating generated text as the only result.

## Concept

`LLM` is the primary offline inference interface and `SamplingParams` captures
generation controls. `generate` accepts a collection of prompts, schedules them
through the engine, and returns request-level output objects.

Use `examples/02_offline_generate.py` with a model that fits the available
hardware. Do not infer production throughput from this smoke test.

## Inspect

- the input prompt retained by each result
- generated text and finish reason
- token IDs where the application needs auditability
- the selected model revision and generation defaults

## Common mistake

The default generation configuration can be influenced by a model repository's
`generation_config.json`. If you need vLLM defaults for an experiment, set the
appropriate `generation_config` option explicitly and record it.

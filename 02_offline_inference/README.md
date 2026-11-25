# Module 02 — Offline inference

**Prerequisites:** Module 01 and a working supported vLLM environment

**Outcome:** generate from a batch of prompts, handle chat conversations, and
record request-level outputs for later comparison.

| File | Purpose |
| --- | --- |
| [`basic_generation.py`](basic_generation.py) | Run a small prompt batch with explicit sampling controls. |
| [`chat_generation.py`](chat_generation.py) | Call `LLM.chat` with OpenAI-style message lists. |
| [`compare_sampling.py`](compare_sampling.py) | Persist a controlled sampling experiment as JSONL. |
| [`offline_inference.ipynb`](offline_inference.ipynb) | Notebook version of the first lab. |

## Core model

The `LLM` API executes offline requests and `SamplingParams` defines sampling
controls. A `RequestOutput` is more informative than generated text alone: it
retains the prompt and one or more output candidates with finish metadata.

For chat or instruct models, raw text passed to `generate` is not automatically
template-rendered. Use `LLM.chat` for message lists or explicitly render with
the tokenizer when you need to inspect the prompt that the model receives.

## Lab progression

1. Run `basic_generation.py` with a model that fits the target device.
2. Change one sampling parameter and save both request definitions.
3. Repeat with `chat_generation.py`; inspect the model's template policy before
   comparing output quality.

## Do not conclude

A successful two-prompt batch is a functional smoke test. It is not a
throughput, latency, or capacity result.

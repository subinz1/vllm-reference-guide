# Module 05 — Engine internals

**Prerequisites:** Modules 02–04

**Outcome:** explain why request mix, token budget, and cache state alter
observed latency and throughput.

## What to learn

- The API server, engine core, and workers are distinct operational components.
- The scheduler assigns work under a token budget rather than treating prefill
  and decode as permanently separate service phases.
- KV-cache capacity is a primary serving constraint; it is not only a model
  property.
- Prefix caching can alter work completed for repeated prompt prefixes, but its
  effectiveness must be measured on the real workload.

Read the upstream [architecture overview][architecture] before tuning any
flag. Follow it with the capacity worksheet in
[`capacity_questions.md`](capacity_questions.md).

[architecture]: https://docs.vllm.ai/en/latest/design/arch_overview/

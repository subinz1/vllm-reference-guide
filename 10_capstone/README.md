# Module 10 — Capstone: deployment design review

**Prerequisites:** Modules 01–09

**Outcome:** produce an evidence-backed deployment proposal for one real
workload instead of a collection of disconnected flags.

Your proposal should cover:

1. Workload and SLOs: prompt/output distributions, concurrency, latency, and
   failure behavior.
2. Model and provenance: model, tokenizer, template, revision, and licence.
3. Capacity: hardware, memory estimate, parallelism topology, queue limits.
4. Operations: health semantics, metrics, alerts, logs, rollout, and rollback.
5. Security: network exposure, authentication, secrets, and data handling.
6. Validation: load test method, acceptance criteria, and known limitations.

Use [`design_template.md`](design_template.md) and retain the inputs needed to
reproduce every conclusion.

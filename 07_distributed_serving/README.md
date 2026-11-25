# Module 07 — Distributed serving

**Prerequisites:** Modules 05–06 and access to multiple supported accelerators

**Outcome:** select a parallelism topology from model size, interconnect,
workload, and availability constraints.

## Study order

1. Tensor parallelism: split model operations across devices.
2. Pipeline parallelism: assign layer stages across devices.
3. Data parallelism: add replicas and a load-balancing strategy.
4. Expert parallelism: only for supported Mixture-of-Experts configurations.

The right topology is not determined by GPU count alone. Validate the current
`vllm serve` options and architecture documentation, then create a capacity
plan before launching a multi-node experiment.

Use [`topology_review.md`](topology_review.md) as the design checklist.

# Module 06 — Performance engineering

**Prerequisites:** Module 05 and a stable test environment

**Outcome:** create a representative workload and report latency, throughput,
time-to-first-token (TTFT), and time-per-output-token (TPOT) without mixing
incomparable runs.

| File | Purpose |
| --- | --- |
| [`make_workload.py`](make_workload.py) | Create a deterministic JSONL prompt fixture. |
| [`summarize_latencies.py`](summarize_latencies.py) | Summarize request measurements from JSONL. |
| [`benchmark_protocol.md`](benchmark_protocol.md) | Define fair before/after comparisons. |

## Measurement rule

State the question first: capacity, tail latency, throughput, cost, or cache
reuse. Record model revision, server flags, concurrency, prompt/output-length
distribution, warm-up policy, hardware, and software versions. A single token
throughput number without that context is not an operational result.

# Module 09 — Observability and operations

**Prerequisites:** Modules 03 and 05

**Outcome:** ask useful questions of `/metrics`, service health, logs, and
capacity signals before an incident forces guesswork.

The OpenAI-compatible server exposes health, model, and Prometheus-compatible
metrics endpoints. Metrics must be interpreted alongside the workload shape and
deployment topology. A rising queue can indicate a capacity mismatch, a long
prefill backlog, a traffic burst, or a downstream client pattern.

Use [`signal_map.md`](signal_map.md) to pair signals with a question and a
safe first investigation step.

For a reproducible incident note, save a `/metrics` response and summarize the
samples rather than pasting an unbounded raw response into a ticket:

```bash
curl --fail --silent http://127.0.0.1:8000/metrics > artifacts/metrics.prom
python prometheus_snapshot.py artifacts/metrics.prom --prefix vllm:
```

# Signal map

| Signal | Question | First safe investigation |
| --- | --- | --- |
| `/health` unavailable | Can the service answer basic liveness? | Check server process lifecycle and local logs. |
| Model list unexpected | Is the client requesting a served model ID? | Compare `/v1/models` with client configuration. |
| Rising queue | Is demand, prefill work, or capacity causing admission pressure? | Compare request shape, concurrency, and queue-limit configuration. |
| Latency regression | Is TTFT or token generation the dominant change? | Compare workload distribution and recent model/server revisions. |
| Low cache reuse | Do requests share meaningful prefixes? | Inspect safe aggregate workload characteristics before tuning cache flags. |

Avoid alerting on a metric without an owner, a question, and an initial response
that can be performed safely under incident conditions.

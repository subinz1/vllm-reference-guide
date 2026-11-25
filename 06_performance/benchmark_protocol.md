# Benchmark protocol

## Define the workload

Capture a prompt-length distribution, output-length distribution, concurrency,
arrival pattern, model revision, and client behavior. State whether the goal is
interactive latency, batch throughput, capacity, or cache reuse.

## Run fairly

1. Warm the server using the same model and request shape.
2. Keep hardware, driver/runtime, vLLM version, model revision, and server
   flags constant for a comparison.
3. Measure enough requests to report distributions, not only a best run.
4. Separate server latency from network and client-side work when possible.
5. Preserve raw measurements with the exact command used.

## Report

Report TTFT, TPOT, end-to-end latency percentiles, successful-request count,
rejected-request count, and aggregate token throughput. State the limitations
that make the result inapplicable to another workload.

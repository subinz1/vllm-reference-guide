"""Summarize end-to-end latencies from newline-delimited JSON measurements."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import quantiles


parser = argparse.ArgumentParser()
parser.add_argument("measurements", type=Path)
args = parser.parse_args()

latencies_ms = []
with args.measurements.open(encoding="utf-8") as stream:
    for line in stream:
        record = json.loads(line)
        latencies_ms.append(float(record["latency_ms"]))

if len(latencies_ms) < 2:
    raise SystemExit("provide at least two latency measurements")

latencies_ms.sort()
deciles = quantiles(latencies_ms, n=10, method="inclusive")
quartiles = quantiles(latencies_ms, n=4, method="inclusive")
p50 = deciles[4]
p75 = quartiles[2]
p90 = deciles[8]
print(f"count={len(latencies_ms)}")
print(f"min_ms={latencies_ms[0]:.2f}")
print(f"p50_ms={p50:.2f}")
print(f"p75_ms={p75:.2f}")
print(f"p90_ms={p90:.2f}")
print(f"max_ms={latencies_ms[-1]:.2f}")

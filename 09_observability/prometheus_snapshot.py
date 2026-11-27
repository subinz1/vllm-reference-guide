"""Summarize selected Prometheus samples from a saved vLLM metrics response."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path


def parse_sample(line: str) -> tuple[str, float] | None:
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    try:
        metric, value = line.rsplit(maxsplit=1)
        name = metric.split("{", 1)[0]
        return name, float(value)
    except ValueError:
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metrics", type=Path, help="Saved text response from /metrics")
    parser.add_argument("--prefix", default="vllm:")
    args = parser.parse_args()

    sums: dict[str, float] = defaultdict(float)
    samples: dict[str, int] = defaultdict(int)
    for line in args.metrics.read_text(encoding="utf-8").splitlines():
        parsed = parse_sample(line)
        if parsed is None:
            continue
        name, value = parsed
        if name.startswith(args.prefix):
            sums[name] += value
            samples[name] += 1

    if not samples:
        raise SystemExit(f"no samples found with prefix {args.prefix!r}")
    for name in sorted(samples):
        print(f"{name}: samples={samples[name]} sum={sums[name]:.6g}")


if __name__ == "__main__":
    main()

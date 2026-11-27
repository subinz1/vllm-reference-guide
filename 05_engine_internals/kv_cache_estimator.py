"""Estimate KV-cache storage from an explicit model and workload shape.

The result is a planning aid, not a capacity guarantee. vLLM allocates cache in
blocks and also needs memory for model weights, activations, and runtime state.
"""

from __future__ import annotations

import argparse


MIB = 1024 * 1024
GIB = 1024 * MIB


def bytes_per_sequence(
    layers: int, kv_heads: int, head_dim: int, tokens: int, dtype_bytes: int
) -> int:
    return 2 * layers * kv_heads * head_dim * tokens * dtype_bytes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--layers", type=int, required=True)
    parser.add_argument("--kv-heads", type=int, required=True)
    parser.add_argument("--head-dim", type=int, required=True)
    parser.add_argument("--context-tokens", type=int, required=True)
    parser.add_argument("--concurrency", type=int, default=1)
    parser.add_argument("--dtype-bytes", type=int, default=2, choices=(1, 2, 4))
    args = parser.parse_args()

    values = (
        args.layers,
        args.kv_heads,
        args.head_dim,
        args.context_tokens,
        args.concurrency,
    )
    if any(value <= 0 for value in values):
        raise SystemExit("all dimensions, context tokens, and concurrency must be positive")

    per_sequence = bytes_per_sequence(
        args.layers,
        args.kv_heads,
        args.head_dim,
        args.context_tokens,
        args.dtype_bytes,
    )
    total = per_sequence * args.concurrency
    print(f"kv_cache_per_sequence_mib={per_sequence / MIB:.2f}")
    print(f"kv_cache_at_concurrency_{args.concurrency}_gib={total / GIB:.2f}")
    print("note=exclude model weights, block fragmentation, activations, and runtime overhead")


if __name__ == "__main__":
    main()

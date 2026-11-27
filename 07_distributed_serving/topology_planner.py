"""Validate a simple vLLM serving topology before provisioning it."""

from __future__ import annotations

import argparse
import json


def positive(value: int, name: str) -> int:
    if value <= 0:
        raise SystemExit(f"{name} must be positive")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gpus-per-node", type=int, required=True)
    parser.add_argument("--nodes", type=int, default=1)
    parser.add_argument("--tensor-parallel-size", type=int, default=1)
    parser.add_argument("--pipeline-parallel-size", type=int, default=1)
    parser.add_argument("--data-parallel-size", type=int, default=1)
    args = parser.parse_args()

    gpus_per_node = positive(args.gpus_per_node, "--gpus-per-node")
    nodes = positive(args.nodes, "--nodes")
    tensor_parallel = positive(args.tensor_parallel_size, "--tensor-parallel-size")
    pipeline_parallel = positive(args.pipeline_parallel_size, "--pipeline-parallel-size")
    data_parallel = positive(args.data_parallel_size, "--data-parallel-size")

    available = gpus_per_node * nodes
    per_replica = tensor_parallel * pipeline_parallel
    required = per_replica * data_parallel
    if required != available:
        raise SystemExit(
            "topology requires "
            f"{required} GPUs, but the supplied inventory has {available}; "
            "adjust TP, PP, DP, nodes, or GPUs per node"
        )

    print(
        json.dumps(
            {
                "available_gpus": available,
                "replicas": data_parallel,
                "gpus_per_replica": per_replica,
                "tensor_parallel_size": tensor_parallel,
                "pipeline_parallel_size": pipeline_parallel,
                "data_parallel_size": data_parallel,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

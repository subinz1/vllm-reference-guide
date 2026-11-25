# Topology review

## Inputs

- model architecture and parameter/memory estimate
- accelerator count, memory, topology, and interconnect
- target prompt/output distributions and concurrency
- availability and operational constraints
- deployment boundary: one host, multiple hosts, or independent replicas

## Decision questions

1. Does the model fit on one device with room for its KV cache?
2. If not, does tensor parallelism fit the intra-node interconnect and model
   layout requirements?
3. Is pipeline parallelism needed to cross capacity boundaries, and what is the
   expected impact on the workload?
4. Do independent replicas solve throughput more safely than a larger
   distributed engine?
5. What failure scope and rollout strategy follow from the chosen topology?

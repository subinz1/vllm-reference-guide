# 65-day vLLM roadmap

This sequence is intentionally dependency-aware. A later day may be read early,
but its lab should not be claimed as complete until the preceding operational
assumptions are understood.

## Foundations

1. Environment baseline and hardware vocabulary
2. Platform-specific installation choices
3. Offline generation with `LLM`
4. Chat inputs and templates
5. Sampling parameters and reproducibility
6. Tokenization, prompts, and output inspection
7. Model selection, revisions, and licences
8. Diagnose a failed local startup

## API serving

9. Launch an OpenAI-compatible server
10. Health, readiness, and model discovery
11. Completion requests
12. Chat-completion requests
13. Streaming responses and disconnects
14. Python OpenAI client integration
15. Authentication and secret handling
16. Server lifecycle and graceful shutdown

## Request semantics

17. Chat-template ownership and overrides
18. Generation defaults and `generation_config`
19. Structured outputs: constraints and failure modes
20. Tool calling: request and response contracts
21. Embeddings and pooling workloads
22. Reranking workloads
23. Multimodal request boundaries
24. Batch input formats and offline batch jobs

## Engine behavior

25. Architecture: API server, engine core, and workers
26. Token-budget scheduling
27. Continuous batching
28. Prefill, decode, and chunked prefill
29. KV cache capacity model
30. Prefix caching
31. Preemption and request lifecycle
32. Queue limits and admission control
33. Attention backends
34. Reading scheduler traces and logs

## Performance engineering

35. Define a representative workload
36. Throughput, latency, TTFT, and TPOT
37. Warm-up and benchmark hygiene
38. Memory sizing and `gpu_memory_utilization`
39. Batch-size and token-budget experiments
40. Prefix-cache measurement
41. Profiling boundaries
42. CUDA graphs and compilation trade-offs
43. Quantization and accuracy evaluation
44. Benchmark report and decision record

## Distributed serving

45. Tensor parallelism
46. Pipeline parallelism
47. Data parallelism and load balancing
48. Expert parallelism for MoE models
49. Single-node topology design
50. Multi-node topology design
51. Distributed failure diagnosis
52. Capacity plan for a target SLO

## Production operations

53. Container-image and dependency provenance
54. Network exposure and API-key policy
55. Prometheus metrics and alert questions
56. Logging, request IDs, and privacy
57. Load shedding and overload behavior
58. Rollout, rollback, and model revision changes
59. Incident triage runbook
60. Cost and utilisation review

## Mastery

61. Trace one request through the vLLM source tree
62. Add an integration test to a local deployment
63. Reproduce and minimise a serving issue
64. Contribute a documentation or correctness improvement upstream
65. Publish a deployment design and operations review

# Official vLLM references

Use the stable documentation for operational instructions and the latest
documentation when evaluating a newly introduced feature. Record the URL and
the version you used in a lab note because CLI flags and platform support evolve
quickly.

| Topic | Primary source | What to verify |
| --- | --- | --- |
| Quickstart | <https://docs.vllm.ai/en/stable/getting_started/quickstart/> | Supported platform, install command, offline and server basics. |
| CLI | <https://docs.vllm.ai/en/stable/cli/> | Commands and accepted options in your installed version. |
| OpenAI-compatible server | <https://docs.vllm.ai/en/stable/serving/openai_compatible_server/> | Endpoint behavior, health, metrics, and operational caveats. |
| Architecture | <https://docs.vllm.ai/en/latest/design/arch_overview/> | Process topology and scheduler behavior. |
| `vllm serve` reference | <https://docs.vllm.ai/en/stable/cli/serve/> | Capacity, cache, and distributed-serving configuration. |
| Upstream repository | <https://github.com/vllm-project/vllm> | Source, issues, examples, and release notes. |

## Citation practice

An experiment should include:

1. vLLM version and installation path.
2. Model revision, tokenizer revision, and any chat template override.
3. Accelerator, driver/runtime, and parallelism configuration.
4. Exact command, workload shape, and the metric being compared.

Without these details, a performance result is an observation, not a reusable
conclusion.

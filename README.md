# vLLM Reference Guide

An evidence-first learning path from a first local generation to operating and
debugging a production vLLM deployment. The material is organised as a 65-day
curriculum: each day has one outcome, a small piece of executable work, and a
review prompt. It deliberately separates concepts that can be explored on a
laptop from exercises that require a supported accelerator.

## Who this is for

This guide is for engineers who know Python and basic transformer concepts but
want to understand vLLM as both a library and a serving system. It is not a
substitute for the upstream documentation; links to the primary sources live in
[`references/official-docs.md`](references/official-docs.md).

## Before you begin

- Use Linux for the mainstream path. Platform-specific installation choices
  matter; do not copy a CUDA command onto ROCm, XPU, TPU, Ascend, or Apple
  Silicon without reading the matching upstream installation page.
- Create a dedicated environment. Keep the vLLM, PyTorch, driver, and model
  versions that you used in your lab notes.
- Start with a model you are allowed to download and run. Model licences,
  access gating, and hardware memory needs are independent of vLLM.
- Treat examples in `examples/` as starting points. Replace model IDs and
  capacity limits only after measuring their effect.

## Learning path

| Phase | Days | Outcome |
| --- | ---: | --- |
| Foundations | 1–8 | Choose a supported environment and run controlled offline inference. |
| API serving | 9–16 | Operate the OpenAI-compatible server and write correct clients. |
| Request semantics | 17–24 | Understand chat templates, structured outputs, tools, and multimodal inputs. |
| Engine behavior | 25–34 | Reason about scheduling, KV cache, prefix reuse, and capacity limits. |
| Performance | 35–44 | Design measurable experiments for latency, throughput, and memory. |
| Distributed serving | 45–52 | Select parallelism and deployment topology from workload constraints. |
| Production operations | 53–60 | Secure, observe, upgrade, and recover a service. |
| Mastery | 61–65 | Read source, profile a real workload, and publish an operating runbook. |

The full sequence and prerequisites are in [`docs/roadmap.md`](docs/roadmap.md).

## Tutorial modules

| Module | Focus | Learning mode |
| --- | --- | --- |
| [01 — Foundations](01_foundations/) | Platform choice, environments, model provenance | Read + local checks |
| [02 — Offline inference](02_offline_inference/) | `LLM`, `SamplingParams`, chat, and result inspection | Accelerator lab |
| [03 — OpenAI-compatible server](03_openai_server/) | Startup, health, completions, and client integration | Local server lab |
| [04 — Request semantics](04_request_semantics/) | Templates, streaming, structured requests, tools | API contract lab |
| [05 — Engine internals](05_engine_internals/) | Scheduler, KV cache, prefill, and prefix reuse | Architecture lab |
| [06 — Performance](06_performance/) | Workload design, latency, throughput, and memory | Measurement lab |
| [07 — Distributed serving](07_distributed_serving/) | TP, PP, DP, MoE, and deployment topology | Multi-accelerator lab |
| [08 — Security](08_security/) | Authentication, exposure, and model provenance | Operations lab |
| [09 — Observability](09_observability/) | Metrics, logs, capacity signals, and diagnosis | Operations lab |
| [10 — Capstone](10_capstone/) | A deployment design and operating review | Independent project |

Start with the [foundation module](01_foundations/) and then complete
[`02_offline_inference`](02_offline_inference/) before starting a server.

## Repository layout

```text
01_foundations/ … 10_capstone/  Numbered tutorial modules
docs/                              Daily lessons and curriculum notes
examples/                          Small standalone programs
exercises/                         Prompts for independent practice
checklists/                        Review criteria before moving on
references/                        Primary documentation and source-map links
```

## Working agreement

Do not describe an example as validated unless it was run in a documented
environment. When an upstream release changes a command, update the affected
lesson with the version and a link to the new source of truth.

## Status

The foundation module is in progress. The 65-day roadmap is intentionally
committed before its advanced labs so progress is visible without pretending
that untested material is complete.

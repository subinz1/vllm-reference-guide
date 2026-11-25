# Module 01 — Foundations

**Prerequisites:** Python 3.11+ and a target environment

**Outcome:** choose a supported vLLM installation path, record enough
environment information to reproduce a lab, and identify a permitted model for
a smoke test.

| File | Purpose |
| --- | --- |
| [`environment_report.py`](environment_report.py) | Print a non-secret machine baseline. |
| [`model_manifest.py`](model_manifest.py) | Validate the information to record for a model run. |
| [`foundation_lab.ipynb`](foundation_lab.ipynb) | Notebook walkthrough before installation. |

## Concepts

vLLM is not one universal wheel. Backend selection depends on the operating
system, accelerator platform, driver/runtime, Python, and PyTorch
compatibility. Start at the upstream [Quickstart][quickstart] and select the
matching platform tab rather than copying an installation command from an
unrelated machine.

The model identity matters too. A run should record at least a model ID or
local path, revision, tokenizer revision where separately configured, chat
template policy, and any generation defaults. Model licensing and access
approval are separate from technical compatibility.

## Lab

```bash
python environment_report.py
python model_manifest.py --model Qwen/Qwen2.5-1.5B-Instruct --revision main
```

The second command only validates the record format; it does not download a
model.

## Move on when

- you can name the upstream installation page that applies to your platform;
- you have a model that is allowed and small enough for a smoke test; and
- you can save a reproducible model manifest without a secret or private URL.

[quickstart]: https://docs.vllm.ai/en/stable/getting_started/quickstart/

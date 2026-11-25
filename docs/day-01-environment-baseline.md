# Day 1 — Establish an environment baseline

**Lab type:** Read-only, then local lab

## Outcome

You can describe the machine that will run vLLM without guessing which
installation path or backend it supports.

## Why this comes first

An inference stack combines a host OS, Python, PyTorch, an accelerator runtime,
drivers, a vLLM distribution, and a model. A successful command on another
machine is not evidence that those layers are compatible on yours.

## Record before installation

- operating-system release and CPU architecture
- Python version and the environment manager you intend to use
- accelerator vendor, model, count, and visible-device policy
- driver and accelerator runtime version
- desired vLLM release or commit
- one small permitted model for a smoke test

Use `examples/01_environment_report.py` to produce a safe baseline. It does not
need vLLM to be installed.

## Checkpoint

You should be able to answer: which upstream installation section applies to
this machine, and what fact would make that answer invalid?

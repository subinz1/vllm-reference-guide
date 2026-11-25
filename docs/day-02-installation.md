# Day 2 — Install deliberately

**Lab type:** Local lab

## Outcome

You create an isolated environment and choose an installation command that
matches your backend rather than assuming every platform uses the same wheel.

## Procedure

1. Read the platform tab in the upstream quickstart and installation guide.
2. Create a dedicated environment; do not reuse a project environment with
   unknown PyTorch constraints.
3. Install the release and backend recommended for that platform.
4. Run `vllm --help` and record the version plus the selected backend.
5. If kernels must be downloaded separately, use the upstream-recommended
   command and record whether it completed.

The current quickstart recommends `uv` and documents
`uv pip install vllm --torch-backend=auto` for the NVIDIA path. That is not a
universal command: ROCm, TPU, Ascend, XPU, and Apple Silicon have distinct
guidance.

## Do not proceed when

- the install selected an unexpected backend;
- PyTorch, driver, or runtime errors appear during import; or
- the model download policy is not understood.

Fix the environment before changing model or serving settings.

# Module 08 — Security and provenance

**Prerequisites:** Module 03

**Outcome:** expose a vLLM service deliberately, manage API keys safely, and
record the artefacts that influence output behavior.

## Boundaries

- Bind development servers to loopback by default.
- API keys are access controls for the server boundary, not a complete
  multi-tenant authorization system.
- Keep secrets out of code, notebooks, logs, and shell history.
- Pin and record model, tokenizer, adapter, and template revisions when output
  behavior matters.
- Treat prompts and generated text as potentially sensitive application data.

Complete [`deployment_review.md`](deployment_review.md) before exposing a
server outside a development machine.

[`serve_config_review.py`](serve_config_review.py) is a preflight prompt for
the small set of exposure decisions that are easy to omit in a local command.
It never reads or prints the API key itself.

```bash
python serve_config_review.py --host 127.0.0.1 --api-key-env VLLM_API_KEY
```

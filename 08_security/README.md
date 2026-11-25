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

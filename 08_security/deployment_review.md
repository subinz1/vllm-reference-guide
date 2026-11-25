# Deployment review

- [ ] The service is bound to the intended interface; development uses loopback.
- [ ] API keys arrive through a secret manager or protected environment, not a
  notebook, source file, or shell history.
- [ ] The deployment has an explicit TLS and proxy ownership boundary.
- [ ] Model, tokenizer, adapters, and chat-template revisions are recorded.
- [ ] Request and response logging has an approved data-retention policy.
- [ ] A model or dependency update has rollback criteria.

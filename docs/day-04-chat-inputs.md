# Day 4 — Use chat inputs correctly

**Lab type:** Accelerator lab

## Outcome

You know when to call `LLM.chat` and when to apply a chat template manually.

## Concept

An instruct or chat model expects a model-specific serialized conversation.
Calling `generate` with raw user text does not automatically apply that
template. The offline API exposes `chat` for message lists, while manual
templating is appropriate when you need to examine or control the prompt.

`examples/03_chat.py` compares the two approaches without claiming their
outputs must be identical for every model.

## Review questions

- Which component owns the template: tokenizer, model repository, or service?
- Is the generation prompt appended for an assistant response?
- How will a template revision be recorded when evaluating outputs?

## Boundary

Never assume a generic prompt string is interchangeable with a chat
conversation. Verify the model's documented template before diagnosing quality
or safety differences.

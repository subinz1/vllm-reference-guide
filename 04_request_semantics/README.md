# Module 04 — Request semantics

**Prerequisites:** Module 03

**Outcome:** design clients that correctly express chat, completion, streaming,
and constrained-response intent.

| File | Purpose |
| --- | --- |
| [`streaming_client.py`](streaming_client.py) | Consume a streamed chat response and preserve event order. |
| [`request_contract.py`](request_contract.py) | Validate a portable request record before sending it. |
| [`structured_output_contract.py`](structured_output_contract.py) | Validate the local shape of a JSON-schema structured-output request. |
| [`request_matrix.md`](request_matrix.md) | Decide which endpoint and data shape fits a task. |

## Contract first

An OpenAI-compatible API is an interface contract, not an assurance that every
model supports every request shape. Model architecture, tokenizer template,
and configured server features determine whether a request is meaningful.

Treat structured outputs and tool calls as constraints that require explicit
validation. Do not treat an apparently JSON-shaped string as proof that an
application-level schema was satisfied.

Run the structured-output validator before sending a request in the lab. It
checks the portable request contract only; server and model support must still
be established with an integration test.

```bash
printf '%s\n' '{"response_format":{"type":"json_schema","json_schema":{"name":"answer","strict":true,"schema":{"type":"object","properties":{"summary":{"type":"string"}}}}}}' | python structured_output_contract.py
```

## Streaming boundary

Streaming changes client responsibilities: partial text may be received before
a final reason, users can disconnect, and the application must decide when to
persist or act on output. The client example prints events in received order and
does not assemble them into a falsely complete result.

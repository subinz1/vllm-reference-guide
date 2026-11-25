# Request matrix

| Need | Start with | Verify |
| --- | --- | --- |
| One plain prompt | Completion request | Model accepts the intended prompt format. |
| Conversation | Chat completion | Template ownership and message roles. |
| Incremental display | Streaming chat/completion | Cancellation, partial output, and final reason handling. |
| Application schema | Structured-output mechanism | Server/model capability and application validation. |
| Tool invocation | Tool-calling request | Tool schema, argument validation, and execution isolation. |

The client should own application validation. An API response that is syntactic
JSON is not sufficient evidence that a business-level invariant holds.

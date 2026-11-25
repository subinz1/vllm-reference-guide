# Module 03 — OpenAI-compatible server

**Prerequisites:** Module 02

**Outcome:** start a local server, use health and model-discovery endpoints, and
make a completion request through an OpenAI-compatible client.

| File | Purpose |
| --- | --- |
| [`serve_local.sh`](serve_local.sh) | A local-only startup command with an API key supplied by environment. |
| [`check_server.py`](check_server.py) | Check `/health` and `/v1/models`. |
| [`openai_client.py`](openai_client.py) | Send a chat-completion request with the OpenAI Python client. |
| [`server_lab.ipynb`](server_lab.ipynb) | Notebook guide for the client-side workflow. |

## Local-first workflow

Start the server on loopback only. Keep an API key in the environment, never in
the script or notebook. The server implements the OpenAI API protocol; clients
must point `base_url` to the local `/v1` address.

```bash
export VLLM_API_KEY='choose-a-local-development-secret'
bash serve_local.sh
python check_server.py
python openai_client.py
```

Use a model you can access and run. The supplied model value is a teaching
default, not a capacity recommendation.

## Review questions

- What does `/health` establish, and what does it not establish about request
  quality or capacity?
- Which service boundary accepts the client API key?
- How will a client discover the served model ID rather than hard-code it?

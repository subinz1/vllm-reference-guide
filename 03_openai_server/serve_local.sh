#!/usr/bin/env bash
set -euo pipefail

: "${VLLM_API_KEY:?Set VLLM_API_KEY to a local-development secret}"

model="${MODEL_ID:-Qwen/Qwen2.5-1.5B-Instruct}"
port="${VLLM_PORT:-8000}"

exec vllm serve "$model" \
  --host 127.0.0.1 \
  --port "$port" \
  --api-key "$VLLM_API_KEY"

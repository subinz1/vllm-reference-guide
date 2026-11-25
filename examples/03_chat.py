"""Compare vLLM chat input with explicit tokenizer template rendering."""

from transformers import AutoTokenizer
from vllm import LLM, SamplingParams


MODEL = "Qwen/Qwen2.5-1.5B-Instruct"
messages = [[{"role": "user", "content": "Explain continuous batching in one sentence."}]]
sampling = SamplingParams(temperature=0.0, max_tokens=64)

llm = LLM(model=MODEL)
chat_output = llm.chat(messages, sampling)[0].outputs[0].text

tokenizer = AutoTokenizer.from_pretrained(MODEL)
rendered = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
generated = llm.generate(rendered, sampling)[0].outputs[0].text

print(f"chat={chat_output!r}")
print(f"rendered_prompt={rendered[0]!r}")
print(f"generated={generated!r}")

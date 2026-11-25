"""Small offline generation example for a model that fits your environment."""

from vllm import LLM, SamplingParams


MODEL = "facebook/opt-125m"
PROMPTS = ["vLLM helps serve language models because", "A safe benchmark starts by"]

sampling = SamplingParams(temperature=0.0, max_tokens=32)
llm = LLM(model=MODEL)

for output in llm.generate(PROMPTS, sampling):
    candidate = output.outputs[0]
    print(f"prompt={output.prompt!r}")
    print(f"text={candidate.text!r}")
    print(f"finish_reason={candidate.finish_reason!r}")

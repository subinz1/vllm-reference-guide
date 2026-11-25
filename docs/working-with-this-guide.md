# Working with the guide

Each day is structured around an outcome rather than a feature list:

1. Read the goal and prerequisite boundary.
2. Run or inspect the small example.
3. Change one variable at a time in the exercise.
4. Record what you observed, including the environment.
5. Use the checklist to decide whether you can safely proceed.

## Safety boundaries

- Never put a production API key in a shell history, source file, or notebook.
- Do not expose an API server on a public interface merely to test a client.
- Use model artefacts only when their licences and access conditions permit it.
- Treat model output as untrusted application input.

## Hardware labels

Lessons use one of three labels:

- **Read-only:** can be understood without installing or running vLLM.
- **Local lab:** needs a supported local environment and a small model.
- **Accelerator lab:** needs supported accelerator hardware and should include
  a capacity estimate before it is run.

## Evidence log

For every accelerator lab, keep a short record with the date, command, vLLM
version, model revision, hardware, and result. This prevents accidental
comparisons across different backends or defaults.

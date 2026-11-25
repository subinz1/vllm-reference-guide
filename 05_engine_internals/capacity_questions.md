# Capacity worksheet

Answer these before changing a cache or scheduler setting:

1. What are the prompt and output token distributions, not only their means?
2. What concurrency and queueing delay are acceptable for the target SLO?
3. Which GPU memory is reserved for model weights, runtime overhead, and other
   processes before KV cache is considered?
4. Does the workload contain recurring prompt prefixes that could benefit from
   prefix caching?
5. Which metric would prove that the change improved the intended constraint?

Keep one answer set per benchmark run. Do not compare runs with different
model revisions or workload distributions as if a single cache flag caused the
result.

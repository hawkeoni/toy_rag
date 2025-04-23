vllm serve \
    Qwen/Qwen2.5-3B-Instruct \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.5

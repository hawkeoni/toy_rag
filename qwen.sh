
# https://docs.vllm.ai/en/stable/getting_started/quickstart.html#openai-compatible-server
# https://huggingface.co/microsoft/Phi-3-mini-128k-instruct/tree/main
vllm serve \
    Qwen/Qwen2.5-3B-Instruct \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.5

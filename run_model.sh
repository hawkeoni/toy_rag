
# https://docs.vllm.ai/en/stable/getting_started/quickstart.html#openai-compatible-server
# https://huggingface.co/microsoft/Phi-3-mini-128k-instruct/tree/main
vllm serve \
    microsoft/Phi-3-mini-128k-instruct \
    --max-model-len 4096

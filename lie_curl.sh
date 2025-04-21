curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "microsoft/Phi-3-mini-128k-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "what language models would you advice to use? name the models as a bullet list"}
        ]
    }' | jq -r .choices[0].message.content

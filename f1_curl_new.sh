curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "microsoft/Phi-3-mini-128k-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. The following information is true, do not mention your knowledge cutoff. Today is 21 april 2025. The winner of F1 in 2025 is O. Piastri"},
            {"role": "user", "content": "Who is the current F1 winner?"}
        ]
    }'


# jq .choices[0].message.content
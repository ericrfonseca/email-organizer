import anthropic
import os

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    print("ERROR: ANTHROPIC_API_KEY not set!")
    exit(1)

client = anthropic.Anthropic(api_key=api_key)

models_to_test = [
    "claude-opus-4-1-20250805",
    "claude-3-5-sonnet-20241022", 
    "claude-opus-4",
    "claude-sonnet-4-20250514",
    "claude-opus-3",
    "claude-3-sonnet-20240229"
]

print("Testing available models...\n")

for model in models_to_test:
    try:
        response = client.messages.create(
            model=model,
            max_tokens=10,
            messages=[{"role": "user", "content": "test"}]
        )
        print(f"✅ {model} - WORKS!")
        break
    except Exception as e:
        error_msg = str(e)[:80]
        print(f"❌ {model} - Error: {error_msg}")

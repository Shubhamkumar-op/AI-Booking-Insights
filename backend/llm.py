import requests
from config import GROQ_API_KEY, LLM_MODEL

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def query_llm(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")

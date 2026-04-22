import requests

def ask_llm(question, context=""):
    prompt = f"""
You are a career assistant.

User Resume Info:
{context}

User Question:
{question}

Give helpful, short, and practical advice.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
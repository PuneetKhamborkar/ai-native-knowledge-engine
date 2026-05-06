import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_ai_response(query, context):
    prompt = f"""
You are an expert AI Knowledge Engineer.

User Query:
{query}

Knowledge Context:
{context}

Instructions:
- Give structured output
- Include sections: Requirements, API, Validation, Tests
- Be clear and concise
- Do NOT output raw JSON

Answer:
"""

    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        return res.json()["response"]

    except Exception as e:
        print("LLM Error:", e)
        return "AI response failed"
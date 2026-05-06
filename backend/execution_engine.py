import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_code_from_kdf(query, context):
    prompt = f"""
You are a senior backend engineer.

Convert the following system knowledge into working production-ready code.

User Request:
{query}

Knowledge:
{context}

Output:
- FastAPI or Flask API code
- Include validation
- Include UUID usage
- Include proper error handling
- Include test cases (pytest)
- Code should be clean and runnable

DO NOT EXPLAIN.
ONLY OUTPUT CODE.
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
        print("Execution Error:", e)
        return "Code generation failed"
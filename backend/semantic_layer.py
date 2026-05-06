import json
from llm_engine import call_llm


def safe_parse_json(text):
    try:
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])
    except:
        return None


def analyze_query(query):
    prompt = f"""
Extract intent and language from this query.

Query: "{query}"

Return ONLY JSON:
{{
  "intent": "...",
  "language": "en/hi/mr"
}}
"""

    response = call_llm(prompt)

    parsed = safe_parse_json(response)

    if parsed:
        return parsed

    # fallback
    return {
        "intent": query.lower(),
        "language": "en"
    }
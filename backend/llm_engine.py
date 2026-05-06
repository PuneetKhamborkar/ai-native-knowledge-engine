import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

STOP_WORDS = {
    "ho", "nahi", "raha", "hai", "tha", "thi",
    "is", "the", "a", "an", "to", "of", "and"
}


def clean_signals(signals, query):
    cleaned = []

    for s in signals:
        s = s.lower().strip()

        if s in STOP_WORDS or len(s) < 3:
            continue

        cleaned.append(s)

    # 🔥 IMPORTANT: fallback enrichment from query
    words = query.lower().split()
    for w in words:
        if w not in STOP_WORDS and len(w) > 3:
            if w not in cleaned:
                cleaned.append(w)

    return cleaned


def extract_intent_and_signals(query):
    prompt = f"""
Extract meaningful troubleshooting signals.

Ignore filler words.
Keep important action words like:
- save
- login
- create
- delete
- error
- fail

User Query:
"{query}"

Return ONLY JSON:
{{
  "intent": "...",
  "signals": ["keyword1", "keyword2"]
}}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        text = response.json()["response"]

        start = text.find("{")
        end = text.rfind("}") + 1
        json_text = text[start:end]

        data = json.loads(json_text)

        raw_signals = data.get("signals", [])

        # 🔥 final cleaned + enriched signals
        signals = clean_signals(raw_signals, query)

        return data.get("intent", ""), signals

    except Exception as e:
        print("LLM extraction failed:", e)

        # fallback → always usable
        words = query.lower().split()
        fallback = [w for w in words if w not in STOP_WORDS and len(w) > 3]

        return "", fallback
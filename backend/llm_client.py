import requests


class LLMClient:
    def __init__(self, mode="ollama", model="llama3"):
        self.mode = mode
        self.model = model

    def call(self, prompt):
        if self.mode == "ollama":
            return self._call_ollama(prompt)
        return ""

    def _call_ollama(self, prompt):
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            return response.json().get("response", "")
        except Exception as e:
            print("LLM ERROR:", e)
            return ""
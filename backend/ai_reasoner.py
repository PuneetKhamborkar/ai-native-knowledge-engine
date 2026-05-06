import json


class AIReasoner:
    def __init__(self, llm, kdfs):
        self.llm = llm
        self.kdfs = kdfs

    def reason(self, query):
        prompt = self.build_prompt(query)
        raw = self.llm.call(prompt)

        # 🔥 Extract JSON safely
        start = raw.find("{")
        end = raw.rfind("}") + 1

        if start == -1 or end == -1:
            return self.fallback()

        try:
            return json.loads(raw[start:end])
        except:
            return self.fallback()

    def build_prompt(self, query):
        kdf_summary = []

        for kdf in self.kdfs:
            intent = kdf.get("intent", {}).get("name")
            problem = kdf.get("failure", {}).get("problem", "")

            causes = [
                c.get("label")
                for c in kdf.get("failure", {}).get("causes", [])
            ]

            kdf_summary.append({
                "intent": intent,
                "problem": problem,
                "causes": causes
            })

        return f"""
You are a smart support AI.

User query:
{query}

Knowledge base:
{kdf_summary}

Example:
User: task save ho nahi raha
Output:
{{
  "intent": "task_not_saving",
  "cause": "Required fields missing or invalid",
  "confidence": 0.9,
  "answer": "Task cannot be saved because required fields are missing."
}}

Now respond.

Return JSON only.
"""

    def fallback(self):
        return {
            "intent": None,
            "cause": None,
            "confidence": 0,
            "answer": "Could not determine the issue"
        }
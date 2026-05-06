import os
import yaml

from ai_reasoner import AIReasoner
from llm_client import LLMClient


class AnswerEngine:
    def __init__(self, kdf_path):
        self.kdfs = self.load_kdfs(kdf_path)

        # LLM (AI-native)
        self.llm = LLMClient(mode="ollama", model="llama3")
        self.reasoner = AIReasoner(self.llm, self.kdfs)

    # -----------------------------
    # LOAD KDFS
    # -----------------------------
    def load_kdfs(self, directory):
        kdfs = []

        for file in os.listdir(directory):
            if file.endswith(".yaml") or file.endswith(".yml"):
                with open(os.path.join(directory, file), "r") as f:
                    kdfs.append(yaml.safe_load(f))

        print(f"📦 Total KDFs loaded: {len(kdfs)}")
        return kdfs

    # -----------------------------
    # FIND KDF
    # -----------------------------
    def find_kdf(self, intent):
        for kdf in self.kdfs:
            if kdf.get("intent", {}).get("name") == intent:
                return kdf
        return None

    # -----------------------------
    # FIND CAUSE
    # -----------------------------
    def find_cause(self, kdf, cause_label):
        for cause in kdf.get("failure", {}).get("causes", []):
            if cause.get("label") == cause_label:
                return cause
        return None

    # -----------------------------
    # MAIN ENTRY
    # -----------------------------
    def get_answer(self, query):
        ai_output = self.reasoner.reason(query)

        intent = ai_output.get("intent")
        cause_label = ai_output.get("cause")

        # -----------------------------
        # VALIDATE INTENT
        # -----------------------------
        kdf = self.find_kdf(intent)

        if not kdf:
            return {
                "fallback": True,
                "response": "No relevant knowledge found",
                "structured": {"ai_output": ai_output}
            }

        # -----------------------------
        # VALIDATE CAUSE
        # -----------------------------
        selected_cause = self.find_cause(kdf, cause_label)

        if not selected_cause:
            return {
                "fallback": True,
                "response": "Not enough information to determine the issue",
                "structured": {"ai_output": ai_output}
            }

        # -----------------------------
        # BUILD RESPONSE FROM KDF
        # -----------------------------
        cause_id = selected_cause.get("id")
        steps = kdf.get("resolution", {}).get(cause_id, {}).get("steps", [])
        problem = kdf.get("failure", {}).get("problem", "")

        response = f"{problem}\n\nCause:\n{selected_cause.get('label')}\n\nFix Steps:\n"

        for i, step in enumerate(steps, 1):
            response += f"{i}. {step}\n"

        return {
            "fallback": False,
            "intent": intent,
            "response": response.strip(),
            "structured": {
                "ai_output": ai_output,
                "validated_cause": selected_cause
            }
        }
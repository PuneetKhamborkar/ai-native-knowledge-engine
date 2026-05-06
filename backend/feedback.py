import json
import os


class FeedbackStore:
    def __init__(self, path="feedback.json"):
        self.path = path
        self._ensure_file()

    # -----------------------------
    # INIT FILE
    # -----------------------------
    def _ensure_file(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    # -----------------------------
    # ADD FEEDBACK
    # -----------------------------
    def add(self, entry):
        try:
            data = self._read()
            data.append(entry)
            self._write(data)
        except Exception as e:
            print(f"Feedback write error: {e}")

    # -----------------------------
    # READ
    # -----------------------------
    def _read(self):
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except:
            return []

    # -----------------------------
    # WRITE
    # -----------------------------
    def _write(self, data):
        try:
            with open(self.path, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Feedback save error: {e}")

    # -----------------------------
    # GET ALL (OPTIONAL)
    # -----------------------------
    def get_all(self):
        return self._read()
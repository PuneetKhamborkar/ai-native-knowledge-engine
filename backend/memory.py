import json
import os


class MemoryStore:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        self.memory = self.load()

    def load(self):
        if not os.path.exists(self.file_path):
            return {}

        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except:
            return {}

    def persist(self):
        with open(self.file_path, "w") as f:
            json.dump(self.memory, f, indent=2)

    def store(self, query, data):
        key = query.strip().lower()
        self.memory[key] = data
        self.persist()

    def get(self, query):
        key = query.strip().lower()
        return self.memory.get(key)
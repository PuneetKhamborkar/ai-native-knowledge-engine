class Validator:
    def __init__(self, kdfs):
        self.kdfs = kdfs

    def find_kdf(self, intent):
        for kdf in self.kdfs:
            if kdf.get("intent", {}).get("name") == intent:
                return kdf
        return None

    def get_causes(self, kdf):
        return kdf.get("failure", {}).get("causes", [])
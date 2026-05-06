class KDFRegistry:

    def __init__(self, kdfs):

        self.kdfs = kdfs

        self.by_id = {}
        self.by_intent = {}
        self.by_type = {}

        self.build_index()

    def build_index(self):

        for k in self.kdfs:

            self.by_id[k["id"]] = k

            intent = k["intent"]
            self.by_intent.setdefault(intent, []).append(k)

            t = k["type"]
            self.by_type.setdefault(t, []).append(k)

    def get_by_intent(self, intent):
        return self.by_intent.get(intent, [])

    def get_by_type(self, t):
        return self.by_type.get(t, [])

    def get_by_id(self, id_):
        return self.by_id.get(id_)
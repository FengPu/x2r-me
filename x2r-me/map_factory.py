import json
class MapFactory:
    def __init__(self):
        self.data = {}
        self.data["metadata"] = []
        self.data["mapping"] = []
    def add(self, entry):
        self.data["mapping"].append(entry.get())
    def get(self):
        return self.data
    def serialize(self):
        return json.dump(self.data)

class MapEntry:
    def __init__(self, ouri, term, ruri, lnum, status):
        self.data = {}
        self.data["originalURI"] = ouri
        self.data["term"] = term
        self.data["replacedURI"] = ruri
        self.data["lineNumbers"] = lnum
        self.data["status"] = status
    def get(self):
        return self.data
        
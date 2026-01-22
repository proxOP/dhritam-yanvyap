class EntityStore:
    def __init__(self):
        self.entities = {}
        self.relations = []

    def add_entity(self, entity_id: str, data: dict):
        self.entities[entity_id] = data

    def add_relation(self, source: str, target: str, type: str):
        self.relations.append({"source": source, "target": target, "type": type})

    def get_entity(self, entity_id: str):
        return self.entities.get(entity_id, {})

class EventStore:
    def __init__(self):
        self.events = []

    def add_event(self, event: dict):
        self.events.append(event)

    def get_events(self, limit: int = 10):
        return self.events[-limit:]

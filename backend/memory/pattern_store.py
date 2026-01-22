class PatternStore:
    def __init__(self):
        self.patterns = {}

    def get_pattern(self, context: str):
        # Mock retrieval
        return self.patterns.get(context, None)

    def save_pattern(self, context: str, outcome: dict):
        self.patterns[context] = outcome

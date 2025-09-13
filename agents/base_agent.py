class BaseAgent:
    def __init__(self, context=None):
        self.context = context or {}

    def run(self, task):
        raise NotImplementedError

    def report(self):
        return {"agent": self.__class__.__name__, "output": self.context}

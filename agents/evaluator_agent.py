from agents.base_agent import BaseAgent

class EvaluatorAgent(BaseAgent):
    def score(self, context):
        return {"quality": 0.85, "feedback": "Good structure"}

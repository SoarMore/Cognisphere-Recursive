from .base_agent import BaseAgent

class EvaluatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Evaluator Agent")

    def evaluate(self, summary: str) -> str:
        prompt = f"""
You are an evaluator agent. Critique the following summary for clarity, completeness, and technical accuracy. Suggest improvements if needed.

Summary:
{summary}
"""
        return self.run(prompt)

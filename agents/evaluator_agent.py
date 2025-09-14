from agents.base_agent import BaseAgent

class EvaluatorAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="EvaluatorAgent")

    def critique(self, summary: str) -> str:
        prompt = f"""Critique the following summary for clarity, completeness, and relevance:

{summary}

Respond with strengths, weaknesses, and suggestions."""
        return self.run(prompt)

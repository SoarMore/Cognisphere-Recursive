from agents.base_agent import BaseAgent

class MetaAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="MetaAgent")

    def reflect(self, critique: str, summary: str) -> str:
        prompt = f"""Reflect on the quality of the research and summary below.

Critique:
{critique}

Summary:
{summary}

Respond with a brief reflection only. Do not suggest new tasks."""
        return self.run(prompt)

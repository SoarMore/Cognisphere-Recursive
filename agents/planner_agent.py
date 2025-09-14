from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="PlannerAgent")

    def plan_tasks(self, query: str) -> str:
        prompt = f"""Break down the following goal into clear, actionable tasks:

Goal: {query}

Respond with a numbered list."""
        return self.run(prompt)

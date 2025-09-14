from .base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Planner Agent")

    def plan(self, task: str) -> str:
        prompt = f"""
You are a planning agent. Break down the following task into clear, actionable subtasks. Focus on implementation steps, libraries, and offline architecture.

{task}
"""
        return self.run(prompt)

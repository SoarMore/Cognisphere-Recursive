from agents.base_agent import BaseAgent

class ResearchPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ResearchPlannerAgent")

    def plan_research(self, task: str) -> str:
        prompt = f"""Outline what information needs to be collected for this task:

Task: {task}

Respond with a list of research questions or topics."""
        return self.run(prompt)

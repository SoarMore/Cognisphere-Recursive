from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def run(self, task):
        # Mock decomposition
        return [
            "Research existing policies",
            "Summarize NGO strategies",
            "Propose sterilization model",
            "Suggest public awareness campaign"
        ]

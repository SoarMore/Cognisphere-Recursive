from agents.base_agent import BaseAgent

class TaskManagerAgent(BaseAgent):
    def assign(self, subtask, summary):
        return f"Assigned execution for: {subtask} → {summary}"

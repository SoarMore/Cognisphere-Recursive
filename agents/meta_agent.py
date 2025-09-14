from .base_agent import BaseAgent

class MetaAgent(BaseAgent):
    def __init__(self):
        super().__init__("Meta Agent")

    def reflect(self, context: str) -> str:
        prompt = f"""
You are a meta-reflection agent. Reflect on the overall task, subtasks, summary, and critique. Suggest improvements to the plan or architecture.

Context:
{context}
"""
        return self.run(prompt)

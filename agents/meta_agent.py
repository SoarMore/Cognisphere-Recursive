from .base_agent import BaseAgent
from utils.prompt_formatter import format_prompt
from utils.truncate import truncate

class MetaAgent(BaseAgent):
    def __init__(self):
        super().__init__("Meta Agent")

    def reflect(self, critique: str) -> str:
        critique = truncate(critique)
        prompt = format_prompt(
            role="meta-reflection agent",
            task="Reflect on the critique and suggest improvements to the plan or architecture",
            input_text=critique
        )
        return self.run(prompt)

    def synthesize(self, reflection: str) -> str:
        reflection = truncate(reflection)
        prompt = format_prompt(
            role="meta agent",
            task="Based on the reflection, generate final actionable insights",
            input_text=reflection
        )
        return self.run(prompt)

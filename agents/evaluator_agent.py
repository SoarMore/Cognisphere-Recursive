from .base_agent import BaseAgent
from utils.prompt_formatter import format_prompt
from utils.truncate import truncate

class EvaluatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Evaluator Agent")

    def evaluate(self, summary: str) -> str:  # ← renamed from critique
        summary = truncate(summary)
        prompt = format_prompt("evaluator", "Critique the summary and suggest improvements", summary)
        return self.run(prompt)

from .base_agent import BaseAgent
from utils.prompt_formatter import format_prompt
from utils.truncate import truncate

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Summarizer Agent")

    def summarize(self, text: str) -> str:
        text = truncate(text)
        prompt = format_prompt(
            role="summarizer",
            task="Summarize the input in 3–5 bullet points",
            input_text=text
        )
        return self.run(prompt)

from .base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Summarizer Agent")

    def summarize(self, text: str) -> str:
        prompt = f"""
You are a summarizer agent. Condense the following technical background into a concise summary that highlights key implementation steps and tools.

{text}
"""
        return self.run(prompt)

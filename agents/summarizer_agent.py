from agents.base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="SummarizerAgent")

    def summarize(self, research: str) -> str:
        prompt = f"""Summarize the following research into clear, concise bullet points:

{research}"""
        return self.run(prompt)

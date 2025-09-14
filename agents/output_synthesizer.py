from agents.base_agent import BaseAgent

class OutputSynthesizer(BaseAgent):
    def __init__(self):
        super().__init__(name="OutputSynthesizer")

    def synthesize(self, reflection: str) -> str:
        prompt = f"""Generate a final output based on the reflection below. Make it clear, actionable, and user-ready.

{reflection}"""
        return self.run(prompt)

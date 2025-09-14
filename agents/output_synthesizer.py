from .base_agent import BaseAgent

class OutputSynthesizer(BaseAgent):
    def __init__(self):
        super().__init__("Output Synthesizer")

    def synthesize(self, components: list[str]) -> str:
        joined = "\n\n".join(components)
        prompt = f"""
You are an output synthesizer agent. Merge the following components into a coherent final output that summarizes the task, plan, and insights.

{joined}
"""
        return self.run(prompt)

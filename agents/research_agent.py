from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")

    def research(self, query: str) -> str:
        prompt = f"""
You are a technical research agent. Provide detailed background on how to build a local Python script that uses a quantized LLM (e.g. Mistral 7B Q4_K_M) to summarize text files offline. Include relevant libraries, model loading, token handling, and architectural considerations.

Task: {query}
"""
        return self.run(prompt)

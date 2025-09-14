from agents.base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="ResearchAgent")

    def collect_research(self, topic: str) -> str:
        prompt = f"""Provide detailed information on the following topic:

Topic: {topic}

Respond with factual, structured content suitable for summarization."""
        return self.run(prompt)

from agents.base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    def run(self, research_data):
        # Mock summarization
        return f"Summary of: {research_data}"

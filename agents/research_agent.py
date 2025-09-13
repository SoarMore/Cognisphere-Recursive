from agents.base_agent import BaseAgent
import requests

class ResearchAgent(BaseAgent):
    def run(self, subtask):
        # Mock web search
        return f"Collected data for: {subtask}"

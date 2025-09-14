from .base_agent import BaseAgent

class ResearchPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Planner Agent")

    def plan(self, query: str) -> str:
        prompt = f"""
You are a research planner agent. Your job is to break down complex research queries into structured sub-questions or source directives. Focus on clarity, relevance, and technical depth.

Here is the query:
{query}

Return a numbered list of sub-questions or directives that will guide the research process.
"""
        return self.run(prompt)

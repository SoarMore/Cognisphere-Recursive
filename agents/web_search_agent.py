from .base_agent import BaseAgent
from tools.web_search_tool import WebSearchTool

class WebSearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Web Search Agent")
        self.search_tool = WebSearchTool()

    def search(self, query: str) -> str:
        results = self.search_tool.query(query)
        return "\n\n".join(results)

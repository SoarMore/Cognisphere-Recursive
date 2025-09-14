from .base_agent import BaseAgent

class WebSearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Web Search Agent")

    def search(self, query: str) -> str:
        # Simulated search results for testing
        if "essay" in query.lower():
            return (
                "1. Define the type of essay (e.g., argumentative, narrative).\n"
                "2. Brainstorm ideas and outline your structure.\n"
                "3. Write a clear thesis statement.\n"
                "4. Develop body paragraphs with supporting evidence.\n"
                "5. Conclude by summarizing your argument and reflecting."
            )
        return "No relevant results found."

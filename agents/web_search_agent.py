from .base_agent import BaseAgent

class WebSearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Web Search Agent")

    def search(self, query: str) -> str:
        results = [
            "Define the essay topic.",
            "Choose the essay format (persuasive, expository, etc.).",
            "Determine the required length.",
            "Craft a thesis statement.",
            "Outline the structure and main points.",
            "Write the introduction, body, and conclusion.",
            "Revise and proofread the essay."
        ]
        # Deduplicate and join
        return "\n".join(list(dict.fromkeys(results)))

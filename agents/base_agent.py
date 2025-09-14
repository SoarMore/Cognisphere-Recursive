from tools.llm_tool import LLMTool

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.llm = LLMTool()

    def run(self, prompt: str) -> str:
        return self.llm.run(prompt)

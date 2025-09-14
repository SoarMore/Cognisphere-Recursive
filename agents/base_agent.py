class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        from tools.llm_tool import LLMTool
        self.llm = LLMTool()

    def run(self, prompt: str) -> str:
        return self.llm.run(prompt)

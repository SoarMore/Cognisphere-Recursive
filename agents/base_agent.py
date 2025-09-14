from tools.llm_tool import LLMTool

class BaseAgent:
    def __init__(self, name: str, model: str = "phi3:3.8b"):
        self.name = name
        self.llm = LLMTool(model=model)

    def run(self, prompt: str, max_tokens: int = 300) -> str:
        print(f"[{self.name}] Prompt:\n{prompt}")
        output = self.llm.run(prompt, max_tokens=max_tokens)
        print(f"[{self.name}] Output:\n{output}")
        return output if output and not output.startswith("⚠️") else "No output."

from llama_cpp import Llama

class LLMTool:
    def __init__(self, model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"):
        self.llm = Llama(model_path=model_path)

    def run(self, prompt: str) -> str:
     output = self.llm(prompt)
     return output["choices"][0]["text"].strip()


from llama_cpp import Llama

class LLMTool:
    def __init__(self):
        # Load the Phi-2 GGUF model
        self.llm = Llama(
            model_path="models/phi-2.Q4_K_M.gguf",  # Adjust path if needed
            n_ctx=2048,
            n_threads=6,
            n_batch=1
        )

    def run(self, prompt: str, max_tokens: int = 300) -> str:
        try:
            output = self.llm(prompt, max_tokens=max_tokens)

            # Handle dictionary output (newer versions)
            if isinstance(output, dict):
                if "choices" in output and len(output["choices"]) > 0:
                    return output["choices"][0]["text"].strip()
                elif "text" in output:
                    return output["text"].strip()
                else:
                    return str(output)

            # Handle string output (older versions)
            elif isinstance(output, str):
                return output.strip()

            # Fallback for unexpected types
            return str(output)

        except Exception as e:
            return f"⚠️ LLMTool Error: {str(e)}"

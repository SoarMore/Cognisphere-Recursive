import requests
import json

class LLMTool:
    def __init__(self, model="phi3:3.8b"):
        self.model = model
        self.endpoint = "http://127.0.0.1:11435/api/generate"

    def run(self, prompt: str, max_tokens: int = 300) -> str:
        try:
            response = requests.post(self.endpoint, json={
                "model": self.model,
                "prompt": prompt,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "max_tokens": max_tokens
                }
            }, stream=True)

            output = ""
            for line in response.iter_lines():
                if line:
                    try:
                        chunk = json.loads(line.decode("utf-8"))
                        output += chunk.get("response", "")
                    except Exception as e:
                        print(f"⚠️ Chunk parse error: {e}")
            return output.strip() if output else "⚠️ No streamed response from Ollama"
        except Exception as e:
            return f"⚠️ Ollama Error: {str(e)}"

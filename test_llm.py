from tools.llm_tool import LLMTool

llm = LLMTool(model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf")

prompt = "hello how are you."
response = llm.run(prompt)

print("LLM response:", response)

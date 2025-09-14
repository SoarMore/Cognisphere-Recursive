from tools.llm_tool import LLMTool

llm = LLMTool(model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf")

prompt = "Summarize this: The sun rose over the valley, casting long shadows across the dew-covered grass."
response = llm.run(prompt)

print("LLM response:", response)

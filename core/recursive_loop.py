from agents.web_search_agent import WebSearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.meta_agent import MetaAgent

def run_recursive(query: str) -> dict:
    web = WebSearchAgent()
    summarizer = SummarizerAgent()
    evaluator = EvaluatorAgent()
    meta = MetaAgent()

    raw = web.search(query)
    if not raw or len(raw) < 50:
        return {"error": "Raw research too short or missing."}

    summary = summarizer.summarize(raw)
    if not summary or "ocessing" in summary:
        return {"error": "Summary likely corrupted."}

    critique = evaluator.run(f"Critique this summary:\n{summary}")
    reflection = meta.run(f"Reflect on the critique:\n{critique}")

    final_output = meta.run(f"Based on everything, generate final insights:\n{reflection}")

    return {
        "query": query,
        "raw": raw,
        "summary": summary,
        "critique": critique,
        "reflection": reflection,
        "final_output": final_output
    }

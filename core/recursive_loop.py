from agents.web_search_agent import WebSearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.meta_agent import MetaAgent
from utils.truncate import truncate

def run_recursive(query: str) -> dict:
    # Instantiate agents
    web = WebSearchAgent()
    summarizer = SummarizerAgent()
    evaluator = EvaluatorAgent()
    meta = MetaAgent()

    # Step 1: Raw Research
    raw = web.search(query)
    if not raw or len(raw.strip()) < 50:
        return {"error": "Raw research too short or missing.", "raw": raw}

    # Step 2: Summarize
    summary = summarizer.summarize(raw)
    if not summary or "ocessing" in summary or len(summary.strip()) < 20:
        return {"error": "Summary likely corrupted.", "summary": summary}

    # Step 3: Critique
    critique = evaluator.crique(summary)
    if not critique or len(critique.strip()) < 20:
        return {"error": "Critique failed.", "critique": critique}

    # Step 4: Reflect
    reflection = meta.reflect(critique)
    if not reflection or len(reflection.strip()) < 20:
        return {"error": "Reflection failed.", "reflection": reflection}

    # Step 5: Final Output
    final_output = meta.synthesize(reflection)
    if not final_output or len(final_output.strip()) < 20:
        return {"error": "Final synthesis failed.", "final_output": final_output}

    # Return full chain
    return {
        "query": query,
        "raw": truncate(raw),
        "summary": truncate(summary),
        "critique": truncate(critique),
        "reflection": truncate(reflection),
        "final_output": final_output.strip()
    }

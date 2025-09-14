from .research_planner_agent import ResearchPlannerAgent
from .web_search_agent import WebSearchAgent
from .summarizer_agent import SummarizerAgent
from .evaluator_agent import EvaluatorAgent
from .meta_agent import MetaAgent
from .output_synthesizer import OutputSynthesizer
from .loop_controller import run_recursive

class ResearchManager:
    def __init__(self):
        self.planner = ResearchPlannerAgent()
        self.web = WebSearchAgent()
        self.summarizer = SummarizerAgent()
        self.evaluator = EvaluatorAgent()
        self.meta = MetaAgent()
        self.synthesizer = OutputSynthesizer()

    def handle_query(self, query: str) -> dict:
        # Step 1: Plan the research query
        plan = self.planner.plan(query)

        # Step 2: Define recursive loop
        def loop_fn(current_plan, history):
            # Web search
            raw = self.web.search(current_plan)

            # Summarize
            summary = self.summarizer.summarize(raw)

            # Evaluate
            critique = self.evaluator.evaluate(summary)

            # Reflect
            reflection = self.meta.reflect(
                f"Query:\n{current_plan}\n\nSummary:\n{summary}\n\nCritique:\n{critique}"
            )

            return reflection

        # Step 3: Run recursive loop with max 5 iterations
        final_context = run_recursive(loop_fn, plan, max_loops=5)

        # Step 4: Synthesize final output
        final_output = self.synthesizer.synthesize([final_context])

        return {
            "background": plan,
            "summary": final_context,
            "critique": "See reflection",
            "reflection": final_context,
            "final": final_output
        }

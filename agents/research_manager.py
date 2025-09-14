from .research_agent import ResearchAgent
from .summarizer_agent import SummarizerAgent
from .evaluator_agent import EvaluatorAgent
from .meta_agent import MetaAgent
from .output_synthesizer import OutputSynthesizer

class ResearchManager:
    def __init__(self):
        self.researcher = ResearchAgent()
        self.summarizer = SummarizerAgent()
        self.evaluator = EvaluatorAgent()
        self.meta = MetaAgent()
        self.synthesizer = OutputSynthesizer()

    def handle_query(self, query: str) -> dict:
        # Step 1: Research
        background = self.researcher.research(query)

        # Step 2: Summarize
        summary = self.summarizer.summarize(background)

        # Step 3: Evaluate
        critique = self.evaluator.evaluate(summary)

        # Step 4: Reflect
        reflection = self.meta.reflect(
            f"Query:\n{query}\n\nBackground:\n{background}\n\nSummary:\n{summary}\n\nCritique:\n{critique}"
        )

        # Step 5: Synthesize
        final_output = self.synthesizer.synthesize([summary, critique, reflection])

        return {
            "background": background,
            "summary": summary,
            "critique": critique,
            "reflection": reflection,
            "final": final_output
        }

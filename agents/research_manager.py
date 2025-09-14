from agents.research_planner_agent import ResearchPlannerAgent
from agents.research_agent import ResearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.meta_agent import MetaAgent
from agents.output_synthesizer import OutputSynthesizer

class ResearchManager:
    def __init__(self):
        self.research_planner = ResearchPlannerAgent()
        self.research_agent = ResearchAgent()
        self.summarizer = SummarizerAgent()
        self.evaluator = EvaluatorAgent()
        self.meta_agent = MetaAgent()
        self.output_synthesizer = OutputSynthesizer()

    def run(self, query: str) -> dict:
        print(f"🔍 ResearchManager received query: {query}")

        research_plan = self.research_planner.plan_research(query)
        research = self.research_agent.collect_research(research_plan)
        summary = self.summarizer.summarize(research)
        critique = self.evaluator.critique(summary)
        reflection = self.meta_agent.reflect(critique, summary)
        final_output = self.output_synthesizer.synthesize(reflection)

        return {
            "📚 Raw Research": research,
            "📝 Summary": summary,
            "🔍 Critique": critique,
            "🧭 Reflection": reflection,
            "🎯 Final Output": final_output
        }

    def handle_query(self, query: str) -> dict:
        return self.run(query)

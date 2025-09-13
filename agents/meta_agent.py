from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.task_manager_agent import TaskManagerAgent
from agents.evaluator_agent import EvaluatorAgent

class MetaAgent:
    def __init__(self, task):
        self.task = task
        self.context = {}

    def execute(self):
        subtasks = PlannerAgent().run(self.task)
        for subtask in subtasks:
            research = ResearchAgent().run(subtask)
            summary = SummarizerAgent().run(research)
            assignment = TaskManagerAgent().assign(subtask, summary)
            self.context[subtask] = {
                "research": research,
                "summary": summary,
                "assignment": assignment
            }
        score = EvaluatorAgent().score(self.context)
        return {"context": self.context, "score": score}

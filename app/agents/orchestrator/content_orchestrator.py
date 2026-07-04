"""Content orchestrator."""

from app.agents.planner.planner_agent import PlannerAgent
from app.agents.writer.linkedin_writer import LinkedInWriter


class ContentOrchestrator:

    def __init__(
        self,
        planner: PlannerAgent,
        writer: LinkedInWriter,
    ) -> None:

        self._planner = planner
        self._writer = writer

    def create_post(
        self,
        goal: str,
    ) -> str:

        topic = self._planner.plan(goal)

        print(f"\n📌 Planned Topic: {topic}\n")

        return self._writer.generate(topic)
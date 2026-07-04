"""Content orchestrator."""

from app.agents.planner.planner_agent import PlannerAgent
from app.agents.research.research_agent import ResearchAgent
from app.agents.writer.linkedin_writer import LinkedInWriter


class ContentOrchestrator:
    """
    Coordinates all AI agents.
    """

    def __init__(
        self,
        planner: PlannerAgent,
        researcher: ResearchAgent,
        writer: LinkedInWriter,
    ) -> None:

        self._planner = planner
        self._researcher = researcher
        self._writer = writer

    def create_post(
        self,
        goal: str,
    ) -> str:

        # Step 1: Decide the topic
        topic = self._planner.plan(goal)

        print(f"\n📌 Planned Topic:\n{topic}\n")

        # Step 2: Research the topic
        research = self._researcher.research(topic)

        print("=" * 80)
        print("🔍 Research")
        print("=" * 80)
        print(research)
        print("=" * 80)

        # Step 3: Write the post
        return self._writer.generate(topic)
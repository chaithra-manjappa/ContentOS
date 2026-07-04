"""Content orchestrator."""

from app.agents.planner.planner_agent import PlannerAgent
from app.agents.research.research_agent import ResearchAgent
from app.agents.reviewer.reviewer_agent import ReviewerAgent
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
        reviewer: ReviewerAgent,
    ) -> None:

        self._planner = planner
        self._researcher = researcher
        self._writer = writer
        self._reviewer = reviewer

    def create_post(
        self,
        goal: str,
    ) -> str:

        # Step 1 - Plan
        topic = self._planner.plan(goal)

        print("\n" + "=" * 80)
        print("📌 PLAN")
        print("=" * 80)
        print(topic)

        # Step 2 - Research
        research = self._researcher.research(topic)

        print("\n" + "=" * 80)
        print("🔍 RESEARCH")
        print("=" * 80)
        print(research)

        # Step 3 - Write
        draft = self._writer.generate(topic)

        print("\n" + "=" * 80)
        print("✍️ DRAFT")
        print("=" * 80)
        print(draft)

        # Step 4 - Review
        final_post = self._reviewer.review(draft)

        print("\n" + "=" * 80)
        print("✅ REVIEWED POST")
        print("=" * 80)

        return final_post
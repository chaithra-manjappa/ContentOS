"""Content orchestrator."""

from pathlib import Path

from app.agents.image.image_agent import ImageAgent
from app.agents.memory.memory_agent import MemoryAgent
from app.agents.planner.planner_agent import PlannerAgent
from app.agents.research.research_agent import ResearchAgent
from app.agents.reviewer.reviewer_agent import ReviewerAgent
from app.agents.scene.scene_agent import SceneAgent
from app.agents.video.video_agent import VideoAgent
from app.agents.writer.content_writer import ContentWriter
from app.services.video_renderer import VideoRenderer


class ContentOrchestrator:
    """
    Coordinates all AI agents.
    """

    def __init__(
        self,
        planner: PlannerAgent,
        researcher: ResearchAgent,
        writer: ContentWriter,
        reviewer: ReviewerAgent,
        video_agent: VideoAgent,
        scene_agent: SceneAgent,
        image_agent: ImageAgent,
        renderer: VideoRenderer,
        memory: MemoryAgent,
    ) -> None:

        self._planner = planner
        self._researcher = researcher
        self._writer = writer
        self._reviewer = reviewer
        self._video_agent = video_agent
        self._scene_agent = scene_agent
        self._image_agent = image_agent
        self._renderer = renderer
        self._memory = memory

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
        print(final_post)

        # Step 5 - Reel Script
        script = self._video_agent.generate(final_post)

        print("\n" + "=" * 80)
        print("🎬 REEL SCRIPT")
        print("=" * 80)
        print(script)

        # Step 6 - Storyboard
        project = self._scene_agent.generate(script)

        print("\n" + "=" * 80)
        print("🎞 STORYBOARD")
        print("=" * 80)
        print(project.title)
        print(f"Scenes: {len(project.scenes)}")

        # Step 7 - Images
        project = self._image_agent.generate(project)

        print("\n" + "=" * 80)
        print("🖼 IMAGES")
        print("=" * 80)

        for scene in project.scenes:
            print(scene.image_path)

        # Step 8 - Render video
        project = self._renderer.render(
            project=project,
            output_path=Path(
                "assets/generated/videos/reel.mp4",
            ),
        )

        print("\n" + "=" * 80)
        print("🎥 VIDEO")
        print("=" * 80)
        print(project.video_path)

        # Step 9 - Memory
        self._memory.save(
            goal=goal,
            post=final_post,
        )

        print("\n✅ MEMORY SAVED")

        return final_post
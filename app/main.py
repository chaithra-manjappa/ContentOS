"""Application entry point."""

from pathlib import Path

from app.agents.orchestrator.content_orchestrator import ContentOrchestrator
from app.agents.planner.planner_agent import PlannerAgent
from app.agents.writer.linkedin_writer import LinkedInWriter
from app.agents.research.research_agent import ResearchAgent
from app.agents.reviewer.reviewer_agent import ReviewerAgent
from app.agents.memory.memory_agent import MemoryAgent
from app.clients.groq_client import GroqClient
from app.config.env import EnvLoader
from app.config.settings import Settings
from app.services.prompt_service import PromptService
from app.agents.video.video_agent import VideoAgent
from app.agents.scene.scene_agent import SceneAgent
from app.agents.image.image_agent import ImageAgent

from app.clients.mock_image_client import MockImageClient



def main() -> None:
    print("🚀 Welcome to ContentOS\n")

    # Load environment variables
    EnvLoader(Path(".env")).load()

    # Read settings
    settings = Settings.from_environment()

    # Create LLM
    llm = GroqClient(
        api_key=settings.groq_api_key,
        model=settings.groq_model,
    )

    # Prompt service
    prompt_service = PromptService(
        prompt_directory=Path("app/prompts/writer"),
    )

    # Agents
    planner = PlannerAgent(llm)

    researcher = ResearchAgent(llm)

    reviewer = ReviewerAgent(llm)

    video_agent = VideoAgent(llm)

    scene_agent = SceneAgent(llm)

    image_client = MockImageClient()

    image_agent = ImageAgent(image_client)

    writer = LinkedInWriter(
        llm=llm,
        prompt_service=prompt_service,
    )

    memory = MemoryAgent(
        database=Path("app/agents/memory/posts.json"),
    )

    # Orchestrator
    orchestrator = ContentOrchestrator(
        planner=planner,
        researcher=researcher,
        writer=writer,
        reviewer=reviewer,
        video_agent=video_agent,
        scene_agent=scene_agent,
        image_agent=image_agent,
        memory=memory,
    )

    goal = input("🎯 What is your goal? ")

    post = orchestrator.create_post(goal)

    print("\n")
    print(post)


if __name__ == "__main__":
    main()
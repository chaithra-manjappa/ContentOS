"""Application entry point."""

from pathlib import Path

from app.agents.image.image_agent import ImageAgent
from app.agents.memory.memory_agent import MemoryAgent
from app.agents.orchestrator.content_orchestrator import ContentOrchestrator
from app.agents.planner.planner_agent import PlannerAgent
from app.agents.research.research_agent import ResearchAgent
from app.agents.reviewer.reviewer_agent import ReviewerAgent
from app.agents.scene.scene_agent import SceneAgent
from app.agents.video.video_agent import VideoAgent
from app.agents.writer.content_writer import ContentWriter
from app.clients.groq_client import GroqClient
from app.clients.mock_image_client import MockImageClient
from app.config.env import EnvLoader
from app.config.settings import Settings
from app.services.prompt_service import PromptService
from app.services.video_renderer import VideoRenderer
from app.agents.voice.voice_agent import VoiceAgent
from app.clients.mock_tts_client import MockTTSClient

def main() -> None:

    print("🚀 Welcome to ContentOS\n")

    EnvLoader(
        Path(".env"),
    ).load()

    settings = Settings.from_environment()

    llm = GroqClient(
        api_key=settings.groq_api_key,
        model=settings.groq_model,
    )

    prompt_service = PromptService(
        prompt_directory=Path(
            "app/prompts/writer",
        ),
    )

    planner = PlannerAgent(llm)

    researcher = ResearchAgent(llm)

    reviewer = ReviewerAgent(llm)

    writer = ContentWriter(
        llm=llm,
        prompt_service=prompt_service,
    )

    video_agent = VideoAgent(llm)

    scene_agent = SceneAgent(llm)

    image_client = MockImageClient()

    image_agent = ImageAgent(
        image_client=image_client,
    )

    renderer = VideoRenderer()

    tts_client = MockTTSClient()

    voice_agent = VoiceAgent(
         tts_client=tts_client,
         output_directory=Path(
             "assets/generated/audio",
        ),
    )

    memory = MemoryAgent(
        database=Path(
            "app/agents/memory/posts.json",
        ),
    )

    orchestrator = ContentOrchestrator(
        planner=planner,
        researcher=researcher,
        writer=writer,
        reviewer=reviewer,
        video_agent=video_agent,
        scene_agent=scene_agent,
        image_agent=image_agent,
        voice_agent=voice_agent,
        renderer=renderer,
        memory=memory,
    )

    goal = input(
        "🎯 What is your goal? ",
    )

    post = orchestrator.create_post(goal)

    print("\n")
    print(post)


if __name__ == "__main__":
    main()
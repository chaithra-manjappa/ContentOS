"""Application entry point."""

from pathlib import Path

from app.agents.orchestrator.content_orchestrator import ContentOrchestrator
from app.agents.planner.planner_agent import PlannerAgent
from app.agents.writer.linkedin_writer import LinkedInWriter
from app.clients.groq_client import GroqClient
from app.config.env import EnvLoader
from app.config.settings import Settings
from app.services.prompt_service import PromptService


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

    writer = LinkedInWriter(
        llm=llm,
        prompt_service=prompt_service,
    )

    # Orchestrator
    orchestrator = ContentOrchestrator(
        planner=planner,
        writer=writer,
    )

    goal = input("🎯 What is your goal? ")

    post = orchestrator.create_post(goal)

    print("\n")
    print(post)


if __name__ == "__main__":
    main()
"""Application entry point."""

from pathlib import Path

from app.agents.orchestrator.content_orchestrator import ContentOrchestrator
from app.clients.groq_client import GroqClient
from app.config.env import EnvLoader
from app.config.settings import Settings


def main() -> None:
    print("🚀 Welcome to ContentOS\n")

    EnvLoader(Path(".env")).load()

    settings = Settings.from_environment()

    llm = GroqClient(
        api_key=settings.groq_api_key,
        model=settings.groq_model,
    )

    orchestrator = ContentOrchestrator(llm)

    prompt = input("Ask ContentOS: ")

    answer = orchestrator.ask(prompt)

    print("\n")
    print(answer)


if __name__ == "__main__":
    main()
"""Content orchestrator."""

from app.agents.writer.linkedin_writer import LinkedInWriter


class ContentOrchestrator:

    def __init__(
        self,
        writer: LinkedInWriter,
    ) -> None:

        self._writer = writer

    def create_post(
        self,
        topic: str,
    ) -> str:

        return self._writer.generate(
            topic,
        )
"""LinkedIn writer."""

from app.agents.writer.base_writer import BaseWriter
from app.clients.base_llm import BaseLLM
from app.services.prompt_service import PromptService


class ContentWriter(
    BaseWriter,
):

    def __init__(
        self,
        llm: BaseLLM,
        prompt_service: PromptService,
    ) -> None:

        self._llm = llm
        self._prompt_service = prompt_service

    def generate(
        self,
        topic: str,
    ) -> str:

        prompt = self._prompt_service.load(
            "content.md",
            topic=topic,
        )

        return self._llm.generate(prompt)
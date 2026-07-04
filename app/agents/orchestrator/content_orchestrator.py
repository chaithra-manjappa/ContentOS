"""Content orchestrator."""

from app.clients.base_llm import BaseLLM


class ContentOrchestrator:
    """Coordinates AI agents."""

    def __init__(
        self,
        llm: BaseLLM,
    ) -> None:

        self._llm = llm

    def ask(
        self,
        prompt: str,
    ) -> str:

        return self._llm.generate(prompt)
"""Prompt service."""

from pathlib import Path


class PromptService:
    """Loads prompt templates."""

    def __init__(
        self,
        prompt_directory: Path,
    ) -> None:

        self._directory = prompt_directory

    def load(
        self,
        template: str,
        **variables: str,
    ) -> str:

        prompt = (
            self._directory /
            template
        ).read_text(
            encoding="utf-8",
        )

        for key, value in variables.items():
            prompt = prompt.replace(
                "{{" + key + "}}",
                value,
            )

        return prompt
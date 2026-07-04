"""Scene Agent."""

from app.clients.base_llm import BaseLLM


class SceneAgent:
    """
    Converts a reel script into individual scenes.
    """

    def __init__(
        self,
        llm: BaseLLM,
    ) -> None:

        self._llm = llm

    def generate(
        self,
        script: str,
    ) -> str:

        prompt = f"""
You are an expert short-form video director.

Break the following Instagram Reel script into scenes.

For each scene provide:

Scene Number:
Duration:
Visual Description:
Camera Movement:
Narration:
Caption On Screen:

Keep each scene between 4-6 seconds.

Script:

{script}
"""

        return self._llm.generate(prompt)
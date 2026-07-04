"""Video Agent."""

from app.clients.base_llm import BaseLLM


class VideoAgent:
    """
    Converts long-form content into
    a short-form vertical video script.
    """

    def __init__(
        self,
        llm: BaseLLM,
    ) -> None:

        self._llm = llm

    def create_script(
        self,
        post: str,
    ) -> str:

        prompt = f"""
You are a professional Instagram Reels creator.

Convert the following LinkedIn post into a 30-second Instagram Reel.

Return:

Hook

Scene 1

Scene 2

Scene 3

Call To Action

Keep it engaging.

LinkedIn Post:

{post}
"""

        return self._llm.generate(prompt)
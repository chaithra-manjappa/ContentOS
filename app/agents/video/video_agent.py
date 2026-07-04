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

    def generate(
        self,
        post: str,
    ) -> str:

        prompt = f"""
You are a professional Instagram Reels creator.

Your task is to convert a LinkedIn post into a viral 30-second Instagram Reel.

Return ONLY the narration script.

Rules:

- Maximum 30 seconds.
- Start with a strong hook.
- Use short sentences.
- End with a call to action.
- No scene numbers.
- No markdown.
- No explanations.

LinkedIn Post:

{post}
"""

        return self._llm.generate(prompt)
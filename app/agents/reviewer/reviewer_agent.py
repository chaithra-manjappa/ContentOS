"""Reviewer Agent."""

from app.clients.base_llm import BaseLLM


class ReviewerAgent:
    """
    Reviews and improves generated content.
    """

    def __init__(
        self,
        llm: BaseLLM,
    ) -> None:

        self._llm = llm

    def review(
        self,
        post: str,
    ) -> str:

        prompt = f"""
You are a senior LinkedIn content editor.

Improve the following LinkedIn post.

Requirements:

- Better hook
- Better readability
- Better formatting
- Better engagement
- Keep technical accuracy
- Keep author's tone
- Keep hashtags
- Do not make it significantly longer

LinkedIn Post:

{post}

Return ONLY the improved post.
"""

        return self._llm.generate(prompt)
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
You are an expert content editor.

Review and improve the following content.

Requirements:

- Improve clarity.
- Improve flow.
- Improve engagement.
- Preserve the original meaning.
- Preserve the author's tone.
- Correct grammar where necessary.
- Do not add unnecessary information.
- Do not make the content significantly longer.

Content:

{post}

Return ONLY the improved content.
"""

        return self._llm.generate(prompt)
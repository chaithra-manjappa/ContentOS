"""Research Agent."""

from app.clients.base_llm import BaseLLM


class ResearchAgent:
    """
    Collects useful information before writing.
    """

    def __init__(
        self,
        llm: BaseLLM,
    ) -> None:

        self._llm = llm

    def research(
        self,
        topic: str,
    ) -> str:

        prompt = f"""
You are an expert researcher.

Research the following topic thoroughly.

Topic:
{topic}

Return:

- Summary
- Key Ideas
- Best Practices
- Common Mistakes
- Real-world Examples

Keep it concise.

Do NOT write the final content.
"""

        return self._llm.generate(prompt)
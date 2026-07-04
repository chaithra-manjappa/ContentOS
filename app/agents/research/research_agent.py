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
You are a senior software researcher.

Research this topic.

Topic:
{topic}

Return:

- Short Summary

- Important Concepts

- Best Practices

- Common Mistakes

- Real-world Use Cases

Keep it concise.

Do NOT write a LinkedIn post.
"""

        return self._llm.generate(prompt)
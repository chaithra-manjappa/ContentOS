"""Planner Agent."""

from app.clients.base_llm import BaseLLM


class PlannerAgent:
    """
    Converts a user goal into
    the best topic to write about.
    """

    def __init__(
        self,
        llm: BaseLLM,
    ) -> None:

        self._llm = llm

    def plan(
        self,
        goal: str,
    ) -> str:
        """
        Returns ONLY a topic.
        """

        prompt = f"""
You are an expert content strategist.

The user's goal is:

{goal}

Return ONLY one LinkedIn post topic.

Examples:

Goal:
Become known for SwiftUI

Topic:
SwiftUI Performance Tips

Goal:
Learn system design

Topic:
System Design Interview Mistakes

Return ONLY the topic.
"""

        return self._llm.generate(prompt).strip()
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

Your job is to transform a user's goal into the single best content topic.

The user's goal is:

{goal}

Requirements:

- Return exactly ONE content topic.
- Keep the topic concise and specific.
- Make it engaging and relevant to the user's goal.
- Do not include explanations, numbering, markdown or quotes.
- Output only the topic.

Examples:

Goal:
Become known for SwiftUI

Topic:
SwiftUI Performance Tips

Goal:
Grow my bakery business

Topic:
5 Mistakes People Make When Choosing Birthday Cakes

Goal:
Teach healthy eating to parents

Topic:
Healthy Lunch Ideas for School Children

Goal:
Build a personal finance audience

Topic:
7 Money Habits That Build Long-Term Wealth
"""

        return self._llm.generate(prompt).strip()
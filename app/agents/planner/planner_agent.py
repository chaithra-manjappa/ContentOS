"""Planner Agent."""

from app.clients.base_llm import BaseLLM


class PlannerAgent:
    """
    Converts a user goal into a structured execution plan.
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

        prompt = f"""
You are an AI strategist.

A user has this goal:

{goal}

Think step by step.

Return ONLY:

Audience:
Platform:
Content Type:
Topic:
Reason:

Keep it concise.
"""

        return self._llm.generate(prompt)
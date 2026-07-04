"""Base LLM interface."""

from abc import ABC
from abc import abstractmethod


class BaseLLM(ABC):
    """Abstract LLM."""

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        """Generate text."""
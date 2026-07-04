"""Base writer."""

from abc import ABC
from abc import abstractmethod


class BaseWriter(ABC):

    @abstractmethod
    def generate(
        self,
        topic: str,
    ) -> str:
        ...
"""Base Image Client."""

from abc import ABC
from abc import abstractmethod
from pathlib import Path


class BaseImageClient(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        output_path: Path,
    ) -> Path:
        """
        Generates an image and saves it to output_path.
        """
        raise NotImplementedError
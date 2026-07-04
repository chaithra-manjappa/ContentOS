"""Base TTS Client."""

from abc import ABC
from abc import abstractmethod
from pathlib import Path


class BaseTTSClient(ABC):
    """
    Base interface for all Text-to-Speech providers.
    """

    @abstractmethod
    def generate(
        self,
        text: str,
        output_path: Path,
    ) -> Path:
        """
        Generate speech from text and save it.

        Args:
            text: Text to convert into speech.
            output_path: Destination audio file.

        Returns:
            Path to the generated audio file.
        """
        raise NotImplementedError
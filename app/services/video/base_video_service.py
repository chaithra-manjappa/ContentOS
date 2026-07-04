from abc import ABC
from abc import abstractmethod
from pathlib import Path


class BaseVideoService(ABC):

    @abstractmethod
    def generate(
        self,
        images_directory: Path,
        audio_file: Path,
        output_file: Path,
    ) -> Path:
        """
        Generates a vertical video.
        """
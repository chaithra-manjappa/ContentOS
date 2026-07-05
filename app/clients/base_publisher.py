from abc import ABC
from abc import abstractmethod

from pathlib import Path


class BasePublisher(ABC):

    @abstractmethod
    def publish(
        self,
        video: Path,
        caption: str,
    ) -> str:
        """
        Returns published post id/url.
        """
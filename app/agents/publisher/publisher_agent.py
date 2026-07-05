"""Publisher Agent."""

from pathlib import Path

from app.clients.base_publisher import BasePublisher
from app.models.publish_result import PublishResult


class PublisherAgent:
    """
    Publishes generated content.
    """

    def __init__(
        self,
        publisher: BasePublisher,
    ) -> None:

        self._publisher = publisher

    def publish(
        self,
        video: Path,
        caption: str,
    ) -> PublishResult:

        return self._publisher.publish(
            video_path=video,
            caption=caption,
        )
"""Instagram Publisher."""

from pathlib import Path

from app.clients.base_publisher import BasePublisher
from app.models.publish_result import PublishResult


class InstagramPublisher(BasePublisher):
    """
    Mock Instagram publisher.
    """

    def publish(
        self,
        video: Path,
        caption: str,
    ) -> PublishResult:

        print("\n")
        print("=" * 80)
        print("📲 INSTAGRAM")
        print("=" * 80)
        print(f"Video : {video}")
        print()
        print("Caption:")
        print(caption)

        return PublishResult(
            success=True,
            platform="Instagram",
            post_id="mock_post_001",
            post_url="https://instagram.com/mock_post_001",
            message="Mock publish successful.",
        )
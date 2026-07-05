"""Publish Result."""

from dataclasses import dataclass


@dataclass
class PublishResult:
    """
    Result of publishing content.
    """

    success: bool
    platform: str
    post_id: str | None = None
    post_url: str | None = None
    message: str | None = None
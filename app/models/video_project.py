"""Video Project model."""

from dataclasses import dataclass, field
from pathlib import Path

from app.models.scene import Scene


@dataclass
class VideoProject:
    """
    Represents the complete video production pipeline.
    """

    title: str

    scenes: list[Scene] = field(
        default_factory=list,
    )

    video_path: Path | None = None

    thumbnail_path: Path | None = None
"""Video Project model."""

from dataclasses import dataclass, field

from app.models.scene import Scene


@dataclass
class VideoProject:
    title: str

    scenes: list[Scene] = field(
        default_factory=list,
    )
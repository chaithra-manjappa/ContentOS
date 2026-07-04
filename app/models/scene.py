"""Scene model."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Scene:
    number: int
    duration: int

    visual_prompt: str
    narration: str
    caption: str

    image_path: Path | None = None
    audio_path: Path | None = None
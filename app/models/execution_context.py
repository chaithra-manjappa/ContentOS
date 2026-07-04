"""Execution Context."""

from dataclasses import dataclass

from app.models.video_project import VideoProject


@dataclass
class ExecutionContext:

    goal: str

    topic: str = ""

    research: str = ""

    draft: str = ""

    final_post: str = ""

    video_script: str = ""

    video_project: VideoProject | None = None
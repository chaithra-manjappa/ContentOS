"""Image Agent."""

from pathlib import Path

from app.clients.base_image_client import BaseImageClient
from app.models.video_project import VideoProject


class ImageAgent:

    def __init__(
        self,
        image_client: BaseImageClient,
    ) -> None:

        self._image_client = image_client

    def generate(
        self,
        project: VideoProject,
    ) -> VideoProject:

        output_directory = Path(
            "assets/generated/images",
        )

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        for scene in project.scenes:

            output_path = (
                output_directory /
                f"scene_{scene.number}.png"
            )

            scene.image_path = self._image_client.generate(
                prompt=scene.visual_prompt,
                output_path=output_path,
            )

        return project
"""Voice Agent."""

from pathlib import Path

from app.clients.base_tts_client import BaseTTSClient
from app.models.video_project import VideoProject


class VoiceAgent:
    """
    Generates narration audio for each scene.
    """

    def __init__(
        self,
        tts_client: BaseTTSClient,
        output_directory: Path,
    ) -> None:

        self._tts_client = tts_client
        self._output_directory = output_directory

    def generate(
        self,
        project: VideoProject,
    ) -> VideoProject:

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        for scene in project.scenes:

            output_path = (
                self._output_directory
                / f"scene_{scene.number}.wav"
            )

            scene.audio_path = self._tts_client.generate(
                text=scene.narration,
                output_path=output_path,
            )

        return project
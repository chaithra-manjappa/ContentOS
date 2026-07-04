"""Piper TTS Client."""

import subprocess
from pathlib import Path

from app.clients.base_tts_client import BaseTTSClient


class PiperTTSClient(BaseTTSClient):
    """
    Generates speech using Piper.
    """

    def __init__(
        self,
        executable: Path,
        model: Path,
    ) -> None:

        self._executable = executable
        self._model = model

    def generate(
        self,
        text: str,
        output_path: Path,
    ) -> Path:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        subprocess.run(
            [
                str(self._executable),
                "--model",
                str(self._model),
                "--output_file",
                str(output_path),
            ],
            input=text,
            text=True,
            check=True,
        )

        return output_path
"""Kokoro TTS Client."""

from pathlib import Path

import soundfile as sf
from kokoro import KPipeline

from app.clients.base_tts_client import BaseTTSClient


class KokoroTTSClient(BaseTTSClient):
    """
    Local TTS using Kokoro.
    """

    def __init__(self) -> None:

        self._pipeline = KPipeline(
            lang_code="a",
        )

    def generate(
        self,
        text: str,
        output_path: Path,
    ) -> Path:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        generator = self._pipeline(
            text=text,
            voice="af_heart",
        )

        audio = None

        for _, _, samples in generator:
            audio = samples

        sf.write(
            output_path,
            audio,
            24000,
        )

        return output_path
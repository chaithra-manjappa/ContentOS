"""Mock TTS Client."""

from pathlib import Path
import wave


from app.clients.base_tts_client import BaseTTSClient


class MockTTSClient(BaseTTSClient):
    """
    Generates silent WAV files for development.
    """

    SAMPLE_RATE = 44100

    def generate(
        self,
        text: str,
        output_path: Path,
    ) -> Path:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Approximate speaking duration.
        words = max(
            1,
            len(text.split()),
        )

        seconds = max(
            2,
            words // 3,
        )

        frames = seconds * self.SAMPLE_RATE

        with wave.open(
            str(output_path),
            "w",
        ) as wav:

            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(self.SAMPLE_RATE)

            silence = b"\x00\x00" * frames

            wav.writeframes(silence)

        return output_path
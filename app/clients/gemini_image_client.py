"""Gemini Image Client."""

from pathlib import Path

from google import genai
from google.genai import types

from app.clients.base_image_client import BaseImageClient


class GeminiImageClient(BaseImageClient):
    """
    Generates images using Google's Gemini API.
    """

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:

        self._client = genai.Client(
            api_key=api_key,
        )

        self._model = model

    def generate(
        self,
        prompt: str,
        output_path: Path,
    ) -> Path:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            ),
        )

        for part in response.candidates[0].content.parts:

            if part.inline_data is not None:

                output_path.write_bytes(
                    part.inline_data.data
                )

                return output_path

        raise RuntimeError(
            "Gemini did not return an image."
        )
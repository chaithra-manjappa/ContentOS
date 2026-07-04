"""Mock Image Client."""

from pathlib import Path

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from app.clients.base_image_client import BaseImageClient


class MockImageClient(
    BaseImageClient,
):

    def generate(
        self,
        prompt: str,
        output_path: Path,
    ) -> Path:

        image = Image.new(
            "RGB",
            (1080, 1920),
            color=(245, 245, 245),
        )

        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype(
                "Arial.ttf",
                42,
            )

        except Exception:

            font = ImageFont.load_default()

        draw.multiline_text(
            (60, 100),
            f"CONTENTOS\n\n{prompt}",
            fill="black",
            font=font,
            spacing=12,
        )

        image.save(output_path)

        return output_path
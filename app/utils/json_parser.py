"""JSON Parser."""

import json


class JSONParser:

    @staticmethod
    def parse(
        text: str,
    ) -> dict:

        try:
            return json.loads(text)

        except json.JSONDecodeError as error:
            raise ValueError(
                f"Invalid JSON returned by LLM:\n\n{text}"
            ) from error
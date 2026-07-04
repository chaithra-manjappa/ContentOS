"""Memory Agent."""

import json
from pathlib import Path


class MemoryAgent:
    """
    Stores previously generated content.
    """

    def __init__(
        self,
        database: Path,
    ) -> None:

        self._database = database

        if not self._database.exists():
            self._database.write_text(
                "[]",
                encoding="utf-8",
            )

    def save(
        self,
        goal: str,
        post: str,
    ) -> None:

        history = json.loads(
            self._database.read_text(
                encoding="utf-8",
            )
        )

        history.append(
            {
                "goal": goal,
                "post": post,
            }
        )

        self._database.write_text(
            json.dumps(
                history,
                indent=4,
            ),
            encoding="utf-8",
        )

    def history(self):

        return json.loads(
            self._database.read_text(
                encoding="utf-8",
            )
        )

        
"""Environment loader."""

from pathlib import Path

from dotenv import load_dotenv


class EnvLoader:
    """Loads .env file."""

    def __init__(self, env_file: Path) -> None:
        self._env_file = env_file

    def load(self) -> None:
        load_dotenv(self._env_file)
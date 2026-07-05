from pathlib import Path

from playwright.sync_api import Page

from app.browser.browser_manager import BrowserManager
from app.clients.base_publisher import BasePublisher


class InstagramPlaywrightPublisher(BasePublisher):

    def __init__(self):

        self._browser = BrowserManager(
            storage_state=Path(
                "sessions/instagram.json"
            )
        )

    def publish(
        self,
        video_path: Path,
        caption: str,
    ) -> None:

        self._browser.start()

        try:

            page = self._browser.new_page()

            self._open_instagram(page)

            input(
                "\nInstagram opened. Press Enter..."
            )

        finally:

            self._browser.stop()

    def _open_instagram(
        self,
        page: Page,
    ):

        page.goto(
            "https://www.instagram.com/",
            wait_until="networkidle",
        )
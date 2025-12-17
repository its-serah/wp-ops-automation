from typing import Optional

from playwright.sync_api import Browser, Page, sync_playwright

from .config import WPConfig


class WPBrowserSession:
    """
    Minimal Playwright-based browser session for WordPress admin.

    This is boilerplate you can expand with higher-level actions
    like publish_post, create_page, manage_plugins, etc.
    """

    def __init__(self, config: WPConfig, headless: bool = True) -> None:
        self._config = config
        self._headless = headless
        self._playwright = None
        self._browser: Optional[Browser] = None
        self._page: Optional[Page] = None

    def __enter__(self) -> "WPBrowserSession":
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch(headless=self._headless)
        self._page = self._browser.new_page()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()

    @property
    def page(self) -> Page:
        if not self._page:
            raise RuntimeError("Browser session not started. Use as a context manager.")
        return self._page

    def login(self) -> None:
        """
        Basic WordPress login flow.

        This assumes the standard WP login form; customize selectors
        as needed for your installation or plugins.
        """
        login_url = f"{self._config.base_url}/wp-login.php"
        self.page.goto(login_url)
        self.page.fill('input#user_login', self._config.username)
        self.page.fill('input#user_pass', self._config.password)
        self.page.click('input#wp-submit')
        self.page.wait_for_load_state("networkidle")


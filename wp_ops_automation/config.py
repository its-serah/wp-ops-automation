import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class WPConfig:
    base_url: str
    username: str
    password: str


def load_config() -> WPConfig:
    """
    Load configuration from environment variables (.env recommended).
    """
    base_url = os.getenv("WP_BASE_URL", "").rstrip("/")
    username = os.getenv("WP_USERNAME", "")
    password = os.getenv("WP_PASSWORD", "")

    if not base_url or not username or not password:
        raise RuntimeError(
            "Missing WordPress configuration. "
            "Please set WP_BASE_URL, WP_USERNAME and WP_PASSWORD "
            "in your environment or .env file."
        )

    return WPConfig(base_url=base_url, username=username, password=password)


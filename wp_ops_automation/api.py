from typing import Any, Dict

import requests

from .config import WPConfig


class WPApiClient:
    """
    Minimal WordPress REST API client.

    This is intentionally simple boilerplate that you can extend
    with authenticated routes, pagination helpers, etc.
    """

    def __init__(self, config: WPConfig) -> None:
        self._config = config
        self._session = requests.Session()
        self._session.auth = (config.username, config.password)

    @property
    def base_url(self) -> str:
        return f"{self._config.base_url}/wp-json/wp/v2"

    def get(self, path: str, **params: Any) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self._session.get(url, params=params)

    def post(self, path: str, payload: Dict[str, Any]) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self._session.post(url, json=payload)


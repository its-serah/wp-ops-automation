from .typing import TaskResult
from ..config import load_config
from ..browser import WPBrowserSession


def demo_login() -> TaskResult:
    """
    Example task that performs a login to WordPress admin.

    This is intended as a smoke test for configuration and
    browser automation wiring.
    """
    cfg = load_config()
    with WPBrowserSession(cfg) as session:
        session.login()
    return TaskResult(ok=True, message="Logged into WordPress admin successfully.")


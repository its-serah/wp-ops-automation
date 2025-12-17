from typing import Any, Dict

from .env import load_app_config
from .normalize import normalize_twilio_whatsapp
from .sheets import append_message_row


def handle_twilio_whatsapp_webhook(payload: Dict[str, Any]) -> None:
    """
    Entry point for a Twilio WhatsApp webhook JSON body.

    - Normalizes the payload.
    - Appends a row to Google Sheets.
    """
    cfg = load_app_config()
    msg = normalize_twilio_whatsapp(payload)
    append_message_row(cfg.sheets, msg)


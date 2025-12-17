import logging
from typing import Any, Dict

from .env import load_app_config
from .normalize import normalize_twilio_whatsapp
from .sheets import append_message_row


logger = logging.getLogger("whatsapp_agent")


def handle_twilio_whatsapp_webhook(payload: Dict[str, Any]) -> None:
    """
    Entry point for a Twilio WhatsApp webhook payload.

    - Normalizes the payload.
    - Appends a row to Google Sheets.
    """
    logger.info("Received Twilio WhatsApp payload with keys: %s", list(payload.keys()))

    cfg = load_app_config()
    msg = normalize_twilio_whatsapp(payload)

    logger.info(
        "Normalized message from %s to %s (provider=%s, message_id=%s)",
        msg.from_number,
        msg.to_number,
        msg.provider,
        msg.message_id,
    )

    append_message_row(cfg.sheets, msg)
    logger.info("Appended message to Google Sheets spreadsheet_id=%s", cfg.sheets.spreadsheet_id)

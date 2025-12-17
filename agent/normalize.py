from datetime import datetime
from typing import Any, Dict

from .models import IncomingMessage


def normalize_twilio_whatsapp(payload: Dict[str, Any]) -> IncomingMessage:
    """
    Normalize a classic Twilio WhatsApp webhook payload into IncomingMessage.

    Expected keys (among others):
    - From
    - To
    - Body
    - SmsMessageSid (or MessageSid)
    - Timestamp-like field (we will fall back to now() if missing)
    """
    from_number = str(payload.get("From", "")).replace("whatsapp:", "")
    to_number = str(payload.get("To", "")).replace("whatsapp:", "")
    body = str(payload.get("Body", ""))
    message_id = (
        str(payload.get("SmsMessageSid"))
        if payload.get("SmsMessageSid") is not None
        else str(payload.get("MessageSid", ""))
    )

    # Some Twilio payloads may include a timestamp; if not, use now()
    ts_raw = payload.get("Timestamp") or payload.get("SmsTimestamp")
    if ts_raw:
        try:
            timestamp = datetime.fromisoformat(str(ts_raw))
        except ValueError:
            timestamp = datetime.utcnow()
    else:
        timestamp = datetime.utcnow()

    return IncomingMessage(
        provider="twilio",
        raw=payload,
        from_number=from_number,
        to_number=to_number,
        body=body,
        timestamp=timestamp,
        message_id=message_id or None,
        contact_name=None,
    )


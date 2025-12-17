from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class IncomingMessage:
    """
    Normalized representation of an incoming WhatsApp message.

    This is provider-agnostic; different webhooks can be mapped into this
    structure (Twilio, WhatsApp Cloud API, etc.).
    """

    provider: str
    raw: Dict[str, Any]

    from_number: str
    to_number: str
    body: str
    timestamp: datetime
    message_id: Optional[str] = None
    contact_name: Optional[str] = None


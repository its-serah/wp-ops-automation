from datetime import datetime, timezone

from agent.normalize import normalize_twilio_whatsapp


def test_normalize_twilio_whatsapp_basic_fields():
    payload = {
        "From": "whatsapp:+12345550100",
        "To": "whatsapp:+12345550999",
        "Body": "Hello!",
        "MessageSid": "SM123",
        "SmsTimestamp": "2025-01-01T12:00:00",
    }

    msg = normalize_twilio_whatsapp(payload)

    assert msg.provider == "twilio"
    assert msg.from_number == "+12345550100"
    assert msg.to_number == "+12345550999"
    assert msg.body == "Hello!"
    assert msg.message_id == "SM123"
    assert isinstance(msg.timestamp, datetime)


def test_normalize_twilio_whatsapp_missing_optional_fields():
    payload = {
        "From": "whatsapp:+111",
        "To": "whatsapp:+222",
        "Body": "No message id or timestamp",
    }

    msg = normalize_twilio_whatsapp(payload)

    assert msg.message_id is None
    assert msg.body == "No message id or timestamp"
    # Timestamp should default to "now" (we just assert it is a datetime)
    assert isinstance(msg.timestamp, datetime)


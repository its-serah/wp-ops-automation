from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

from agent.handler import handle_twilio_whatsapp_webhook


app = FastAPI(title="WhatsApp -> Google Sheets Agent")


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/webhook/twilio-whatsapp")
async def twilio_whatsapp_webhook(request: Request) -> PlainTextResponse:
    """
    HTTP endpoint for a Twilio WhatsApp webhook.

    Twilio typically sends application/x-www-form-urlencoded by default,
    but can also send JSON. We handle both and pass the resulting payload
    into the core handler, which appends a row to Google Sheets.
    """
    content_type = request.headers.get("content-type", "")

    if "application/json" in content_type:
        payload: Dict[str, Any] = await request.json()
    else:
        form = await request.form()
        payload = dict(form)

    handle_twilio_whatsapp_webhook(payload)
    return PlainTextResponse("OK")



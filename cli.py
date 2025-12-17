import json
from typing import Optional

import typer

from agent.handler import handle_twilio_whatsapp_webhook

app = typer.Typer(help="Local utilities for the WhatsApp -> Sheets agent.")


@app.command()
def simulate_twilio_webhook(payload_path: str, pretty: Optional[bool] = True) -> None:
    """
    Simulate receiving a Twilio WhatsApp webhook by loading a JSON payload
    from a file and passing it through the handler.

    This is useful for local testing without actually calling the HTTP endpoint.
    """
    with open(payload_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    if pretty:
        typer.echo("Loaded payload:")
        typer.echo(json.dumps(payload, indent=2))

    handle_twilio_whatsapp_webhook(payload)
    typer.echo("Payload processed and appended to Google Sheets (if configured correctly).")


def main() -> None:
    app()


if __name__ == "__main__":
    main()


# WhatsApp → Google Sheets Agent

Automation agent that listens to WhatsApp messages and stores them as records in Google Sheets.

## Overview

The goal of this project is:

- Receive WhatsApp messages via a webhook (e.g. Twilio / WhatsApp Cloud API).
- Normalize the incoming payload into a simple schema.
- Append a row to a Google Sheet for every message.

This repo is framework-agnostic at the core (plain Python for the logic) so you can plug it into any HTTP entrypoint (Flask, FastAPI, Cloud Function, n8n, Make, Zapier, etc.).

## Getting started

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment:

- Create a `.env` (or export env vars) for:
  - `GCP_SERVICE_ACCOUNT_JSON` → absolute path to your Google service account JSON.
  - `SHEETS_SPREADSHEET_ID` → ID of the target Google Sheet.
  - `SHEETS_WORKSHEET_NAME` → sheet/tab name (e.g. `Sheet1`).

### Sheet schema

Rows are appended with the following columns, in order:

1. `timestamp_iso` – ISO 8601 timestamp of when the message was received/normalized.
2. `provider` – source provider identifier (e.g. `twilio`).
3. `from_number` – sender WhatsApp number (no `whatsapp:` prefix).
4. `to_number` – receiving WhatsApp number.
5. `body` – text content of the message.
6. `message_id` – provider-specific message ID (if present).
7. `contact_name` – optional contact name (currently `None` for Twilio).

4. Run the FastAPI webhook locally:

```bash
uvicorn web:app --reload --port 8000
```

5. Point your WhatsApp provider (e.g. Twilio) to the webhook:

- Webhook URL: `https://<your-host-or-ngrok>/webhook/twilio-whatsapp`
- HTTP method: `POST`
- Content type:
  - Twilio default (form-encoded) is supported, or
  - `application/json` if you enable JSON on Twilio.

Every incoming message hitting this endpoint is normalized and appended as a new row in your configured Google Sheet.

### Local simulation via CLI

You can test the entire pipeline without exposing an HTTP endpoint by simulating a Twilio webhook from a JSON file:

```bash
python cli.py simulate_twilio_webhook samples/twilio_message.json
```

This will:

- Load the sample Twilio-like payload.
- Pass it through the same handler used by the FastAPI endpoint.
- Append a row to Google Sheets using your configured environment.

## Architecture

At a high level, the flow is:

1. **Transport** – `web.py` exposes a FastAPI endpoint (`/webhook/twilio-whatsapp`) that accepts Twilio webhook calls (form or JSON).
2. **Handler** – `agent/handler.py` contains `handle_twilio_whatsapp_webhook`, which orchestrates:
   - loading configuration (`agent/env.py`),
   - normalizing the payload (`agent/normalize.py`),
   - appending to Google Sheets (`agent/sheets.py`).
3. **Domain model** – `agent/models.py` defines `IncomingMessage`, a provider-agnostic representation of a WhatsApp message.
4. **Tooling** – `cli.py` provides a local entry point to replay sample payloads through the same handler.

This separation keeps the HTTP layer thin and the core logic reusable in other environments (e.g. Cloud Functions, background workers).

## Development

### Running tests

Install dev dependencies (already in `requirements.txt`) and run:

```bash
pytest
```

This currently exercises the Twilio normalizer; you can extend it as the agent grows.

### Logging

The project uses Python's built-in `logging` module. To see logs during local development, run your app with a basic configuration, for example:

```bash
export LOGLEVEL=INFO
python -m uvicorn web:app --reload --port 8000
```

Or configure logging explicitly at process startup (e.g. in your process manager or entry script) to route logs to stdout or a log aggregation service.

## Status

- [x] Initial Python boilerplate and repo setup.
- [x] WhatsApp (Twilio-style) payload normalization.
- [x] Google Sheets append helper.
- [x] HTTP webhook example (FastAPI).
- [x] CLI helper to simulate webhook locally.
- [ ] Support for other WhatsApp providers (e.g. WhatsApp Cloud API).
- [ ] Basic tests.

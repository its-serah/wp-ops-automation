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

## Status

- [x] Initial Python boilerplate and repo setup.
- [x] WhatsApp (Twilio-style) payload normalization.
- [x] Google Sheets append helper.
- [x] HTTP webhook example (FastAPI).
- [x] CLI helper to simulate webhook locally.
- [ ] Support for other WhatsApp providers (e.g. WhatsApp Cloud API).
- [ ] Basic tests.

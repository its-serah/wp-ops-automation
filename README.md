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
  - WhatsApp verification token / secrets (if needed by your provider).
  - Google service account JSON path or credentials.
  - Target Google Sheet ID and sheet/tab name.

4. Use the core handler in your webhook:

- Import the core handler from the package (to be implemented) and call it with the incoming JSON body.
- The handler returns a normalized record and appends it to Google Sheets.

## Status

- [x] Initial Python boilerplate and repo setup.
- [ ] WhatsApp payload normalization.
- [ ] Google Sheets append helper.
- [ ] HTTP webhook example (FastAPI/Flask).
- [ ] Basic tests and CLI helpers.

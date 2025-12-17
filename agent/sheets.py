from dataclasses import dataclass
from typing import List, Sequence

import gspread
from google.oauth2.service_account import Credentials

from .models import IncomingMessage


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Column order used when writing rows to the sheet.
# Keep this in sync with the documentation in README.md.
COLUMNS: List[str] = [
    "timestamp_iso",
    "provider",
    "from_number",
    "to_number",
    "body",
    "message_id",
    "contact_name",
]


@dataclass
class SheetsConfig:
    service_account_json_path: str
    spreadsheet_id: str
    worksheet_name: str


def make_client(config: SheetsConfig) -> gspread.Client:
    credentials = Credentials.from_service_account_file(
        config.service_account_json_path, scopes=SCOPES
    )
    return gspread.authorize(credentials)


def append_message_row(config: SheetsConfig, message: IncomingMessage) -> None:
    client = make_client(config)
    spreadsheet = client.open_by_key(config.spreadsheet_id)
    worksheet = spreadsheet.worksheet(config.worksheet_name)

    row: List[str] = [
        message.timestamp.isoformat(),
        message.provider,
        message.from_number,
        message.to_number,
        message.body,
        message.message_id or "",
        message.contact_name or "",
    ]
    worksheet.append_row(row, value_input_option="USER_ENTERED")


def append_batch(config: SheetsConfig, messages: Sequence[IncomingMessage]) -> None:
    if not messages:
        return

    client = make_client(config)
    spreadsheet = client.open_by_key(config.spreadsheet_id)
    worksheet = spreadsheet.worksheet(config.worksheet_name)

    rows: List[List[str]] = [
        [
            msg.timestamp.isoformat(),
            msg.provider,
            msg.from_number,
            msg.to_number,
            msg.body,
            msg.message_id or "",
            msg.contact_name or "",
        ]
        for msg in messages
    ]
    worksheet.append_rows(rows, value_input_option="USER_ENTERED")

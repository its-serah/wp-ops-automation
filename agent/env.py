import os
from dataclasses import dataclass

from dotenv import load_dotenv

from .sheets import SheetsConfig


load_dotenv()


@dataclass
class AppConfig:
    sheets: SheetsConfig
    # You can add WhatsApp verification tokens etc. here later.


def load_app_config() -> AppConfig:
    service_account_json_path = os.getenv("GCP_SERVICE_ACCOUNT_JSON", "")
    spreadsheet_id = os.getenv("SHEETS_SPREADSHEET_ID", "")
    worksheet_name = os.getenv("SHEETS_WORKSHEET_NAME", "Sheet1")

    if not service_account_json_path or not spreadsheet_id:
        raise RuntimeError(
            "Missing Google Sheets configuration. "
            "Please set GCP_SERVICE_ACCOUNT_JSON and SHEETS_SPREADSHEET_ID."
        )

    sheets_cfg = SheetsConfig(
        service_account_json_path=service_account_json_path,
        spreadsheet_id=spreadsheet_id,
        worksheet_name=worksheet_name,
    )
    return AppConfig(sheets=sheets_cfg)


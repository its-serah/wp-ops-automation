from dataclasses import dataclass
from typing import Optional


@dataclass
class TaskResult:
    ok: bool
    message: str
    data: Optional[object] = None


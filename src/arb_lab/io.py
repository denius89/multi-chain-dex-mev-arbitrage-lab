from __future__ import annotations

import json
from pathlib import Path

from .models import Opportunity


def load_jsonl(path: str | Path) -> list[Opportunity]:
    records: list[Opportunity] = []
    with Path(path).open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                records.append(Opportunity.from_dict(json.loads(line)))
            except (json.JSONDecodeError, TypeError, ValueError) as exc:
                raise ValueError(f"{path}:{line_number}: {exc}") from exc
    return records

from __future__ import annotations

from collections import Counter
from decimal import Decimal

from .models import Opportunity


def summarize(records: list[Opportunity]) -> dict[str, object]:
    by_network = Counter(record.network for record in records)
    gross = sum((record.gross_profit_usd for record in records), Decimal("0"))
    costs = sum((record.execution_cost_usd for record in records), Decimal("0"))
    net = sum((record.net_profit_usd for record in records), Decimal("0"))
    return {
        "records": len(records),
        "by_network": dict(sorted(by_network.items())),
        "gross_profit_usd": str(gross),
        "execution_cost_usd": str(costs),
        "net_profit_usd": str(net),
    }

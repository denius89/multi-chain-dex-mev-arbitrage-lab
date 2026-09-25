from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any


REQUIRED_FIELDS = {
    "schema_version",
    "opportunity_id",
    "network",
    "observation_mode",
    "location",
    "route",
    "financials",
    "provenance",
    "confidence",
    "observed_at",
    "strategy_type",
    "status",
}


@dataclass(frozen=True)
class Opportunity:
    schema_version: str
    opportunity_id: str
    network: str
    observed_at: datetime
    strategy_type: str
    status: str
    gross_profit_usd: Decimal
    execution_cost_usd: Decimal
    net_profit_usd: Decimal
    evidence: dict[str, Any]

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Opportunity":
        missing = sorted(REQUIRED_FIELDS - raw.keys())
        if missing:
            raise ValueError(f"missing required fields: {', '.join(missing)}")

        financials = raw["financials"]
        if not isinstance(financials, dict):
            raise ValueError("financials must be an object")
        gross = Decimal(str(financials["gross_pnl"]))
        cost = Decimal(str(financials["execution_cost"]))
        net = Decimal(str(financials["net_pnl"]))
        if abs((gross - cost) - net) > Decimal("0.000001"):
            raise ValueError("net_profit_usd must equal gross_profit_usd - execution_cost_usd")

        observed_at = datetime.fromisoformat(str(raw["observed_at"]).replace("Z", "+00:00"))
        if observed_at.tzinfo is None:
            raise ValueError("observed_at must include a timezone")

        return cls(
            schema_version=str(raw["schema_version"]),
            opportunity_id=str(raw["opportunity_id"]),
            network=str(raw["network"]["name"]),
            observed_at=observed_at,
            strategy_type=str(raw["strategy_type"]),
            status=str(raw["status"]),
            gross_profit_usd=gross,
            execution_cost_usd=cost,
            net_profit_usd=net,
            evidence={
                "location": raw["location"],
                "route": raw["route"],
                "provenance": raw["provenance"],
                "confidence": raw["confidence"],
            },
        )

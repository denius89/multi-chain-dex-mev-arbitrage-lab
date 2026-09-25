import json
import unittest
from pathlib import Path

from arb_lab.analytics import summarize
from arb_lab.io import load_jsonl
from arb_lab.models import Opportunity


ROOT = Path(__file__).resolve().parents[1]


class OpportunityTests(unittest.TestCase):
    def test_sample_is_valid(self) -> None:
        records = load_jsonl(ROOT / "data/samples/opportunities.jsonl")
        self.assertEqual(len(records), 2)
        self.assertEqual(summarize(records)["net_profit_usd"], "1.30")

    def test_rejects_inconsistent_net(self) -> None:
        raw = json.loads((ROOT / "data/samples/opportunities.jsonl").read_text().splitlines()[0])
        raw["financials"]["net_pnl"] = "99"
        with self.assertRaisesRegex(ValueError, "must equal"):
            Opportunity.from_dict(raw)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import argparse
import json

from .analytics import summarize
from .io import load_jsonl


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Multi-chain arbitrage research utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("validate", "summarize"):
        child = subparsers.add_parser(command)
        child.add_argument("path", help="Path to an opportunity JSONL file")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    records = load_jsonl(args.path)
    if args.command == "validate":
        print(f"valid: {len(records)} records")
    else:
        print(json.dumps(summarize(records), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

# Decision log

Material decisions should be appended; do not rewrite history.

## 2026-09-25 — Research-first project

**Decision:** Start with historical replay and paper monitoring, not live trading.

**Reason:** A working bot can be implemented without proving that accessible profit exists. Economic validation must precede expensive infrastructure and capital allocation.

## 2026-09-25 — Expand beyond Solana

**Decision:** Compare Solana, Base, Robinhood Chain, and Ethereum.

**Reason:** The observed Solana case is informative but does not justify network lock-in. Different ordering and liquidity structures may reward different capabilities.

## 2026-09-25 — Shared core with adapters

**Decision:** Use one normalized opportunity model, shared analytics, and network-specific collection/execution adapters.

**Reason:** Cross-network comparison requires identical definitions of gross/net PnL, costs, latency, and evidence quality.

## 2026-09-25 — Separate recurring and tail economics

**Decision:** Report ordinary recurring opportunities separately from rare extreme events.

**Reason:** A jackpot can make an unprofitable continuous strategy appear attractive when averaged incorrectly.

## Open decisions

- First two networks for historical implementation.
- Primary storage: PostgreSQL only or PostgreSQL plus Parquet/ClickHouse.
- Python versus Rust boundary for collectors and simulation.
- Minimum evidence threshold for a tiny-live test.
- Whether CEX–DEX inventory and account dependencies remain in scope.

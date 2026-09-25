# Sprint recommendation — 2026-09-25

## Decision

Start the next research phase with **Base as the primary historical track** and **Robinhood Chain as the primary emerging-network discovery track**. Run Ethereum's narrow MEV-Share census only as a low-cost side experiment. Give Solana a short forensic gate before any broad collection or low-latency purchase.

This is a research allocation decision, not a claim that any network is profitable.

## Why this portfolio

1. **Base** has the best combination of public data, EVM replay tooling, diverse venues and published classifier work. Its decisive risk is regime mismatch: the strongest empirical paper predates Flashblocks, and Denim is targeted to change the interface again. BASE-HR-001 measures the current regime directly.
2. **Robinhood Chain** offers the highest information gain: live FCFS infrastructure, public AMMs, Morpho, Stock Token mechanics and a separate Lighter domain. The evidence supports discovery, not profit. The probe must first establish canonical pool/activity data, executable exits and ordinary-taker access.
3. **Ethereum** is technically mature but generic opportunities are highly competitive and private-flow coverage is incomplete. ETH-R1 is worth running only as a bounded, specialized hint census—not as a generic arbitrage build.
4. **Solana** remains strategically important, but the current project fixture has not yet been independently reconstructed from raw chain data. SOL-HR-001 is the cheapest honest gate before paying for faster feeds.

## Authorized work

| Track | Timebox | Spend ceiling before re-approval | Deliverable | Stop condition |
| --- | --- | ---: | --- | --- |
| Base BASE-HR-001 | 5–10 engineering days | $49 provider spend | post-Flashblocks population, trace-validated classifier sample, exact cost ledger | classifier/replay cannot be made reproducible or no candidates survive one later state transition |
| Robinhood discovery | 7 complete UTC days | $49 provider spend | verified registry, swap/Morpho event census, quote/depth matrix, rejection ledger | no reproducible public market population or no executable exit for any narrow strategy |
| Ethereum ETH-R1 | 7 days, optional | $49 provider spend | one-family hint census with simulation/reconstruction rates | hints cannot be reconstructed reliably or no residual survives conservative costs |
| Solana SOL-HR-001 | 1–3 engineering days | $0 initially | immutable raw fixture, balance/cost reconciliation, missing-state ledger | raw records unavailable or deltas require unobservable assumptions |

Provider costs are envelopes, not complete operating budgets. They exclude hosting, storage, redundancy, egress, taxes, extra regions/IPs and trade-level gas/tips/bids. No competitive infrastructure purchase is authorized.

## Gates before any executor

- One reproducible historical population that includes losers and undecodable cases.
- Exact or explicitly bounded accounting from gross opportunity to trade-net result.
- A 7–14 day paper monitor with end-to-end timestamps and delay-decay checkpoints.
- Two independent live sources for a shortlisted network, with measured gaps and costs.
- Evidence that positive residuals recur after failed attempts and allocated infrastructure.
- Separate security review and explicit approval for a guarded tiny-live test.

Until all gates pass: no funded key, no automated transaction broadcast, no node/colocation purchase, and no income forecast.

## Reading order

1. [Cross-network scorecard](cross-network-scorecard.md)
2. [Independent review](independent-review.md)
3. [Stage-2 preregistration](preregistration.md)
4. [Infrastructure cost screen](infrastructure-costs.md)
5. Individual reports in [network-screening/](network-screening/)

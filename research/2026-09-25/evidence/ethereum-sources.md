# Ethereum screening source register

Retrieval date for all links: **2026-09-25**.

This register supports `network-screening/ethereum.md`. Documentation describes interfaces as observed on the retrieval date. Papers support only their declared datasets and methods; their quantitative findings are not assumed to persist unchanged.

## Official documentation

### E1 — Ethereum.org: maximal extractable value

- URL: https://ethereum.org/developers/docs/mev/
- Supports: definitions of arbitrage/liquidation MEV; warning that common DEX arbitrage, liquidations, and sandwiches are unlikely to be profitable for new searchers; suggestion to explore the long tail.
- Evidence type: official ecosystem documentation.
- Limitation: qualitative guidance, not a profitability dataset or current opportunity count.

### E2 — Flashbots Auction overview

- URL: https://docs.flashbots.net/flashbots-auction/overview
- Supports: private communication channel and Flashbots Auction's PoS/mev-boost architecture.
- Evidence type: primary product documentation.
- Limitation: documents Flashbots interfaces, not all builders, relays, or private bilateral order flow.

### E3 — Flashbots: understanding bundles

- URL: https://docs.flashbots.net/flashbots-auction/advanced/understanding-bundles
- Supports: bundles are ordered transactions, can include pending user transactions, and target blocks.
- Evidence type: primary product documentation.
- Limitation: interface semantics do not establish inclusion rates or economics.

### E4 — Flashbots JSON-RPC endpoints

- URL: https://docs.flashbots.net/flashbots-auction/advanced/rpc-endpoint
- Supports: `eth_sendBundle`, `mev_sendBundle`, privacy hints, refunds, simulation fields, and the current one-backrun-transaction restriction dated in the documentation.
- Evidence type: primary API documentation.
- Limitation: mutable interface; pin client/schema version in any experiment.

### E5 — Flashbots MEV-Share introduction

- URL: https://docs.flashbots.net/flashbots-mev-share/introduction
- Supports: order-flow auction design, selective disclosure, partial bundles, simulation, permissionless searcher access, and documented default refund description.
- Evidence type: primary product documentation.
- Limitation: stated design/defaults may differ from event-specific privacy and refund configurations.

### E6 — Flashbots MEV-Boost overview

- URL: https://docs.flashbots.net/flashbots-mev-boost/introduction
- Supports: validators access a builder marketplace; builders create blocks containing order flow and a proposer payment.
- Evidence type: primary product documentation.
- Limitation: not a current builder-market-share dataset.

### E7 — Flashbots builder multiplexing

- URL: https://docs.flashbots.net/flashbots-auction/advanced/multiplexing
- Supports: transactions and bundles can be sent to multiple builders through supported APIs.
- Evidence type: primary product documentation.
- Limitation: available routing is not evidence of winning-builder coverage or favorable treatment.

### E8 — Aave v3 overview and advanced market operations

- URLs:
  - https://aave.com/docs/aave-v3/overview
  - https://aave.com/docs/aave-v3/markets/advanced
  - https://aave.com/docs/aave-v3/smart-contracts/pool
- Supports: health-factor threshold, permissionless liquidation flow, debt repayment/collateral receipt, and version-specific liquidation mechanics.
- Evidence type: official protocol documentation.
- Limitation: deployment addresses, reserve parameters, close factors, and bytecode must be pinned for each historical block range.

### E9 — Ethereum JSON-RPC and Geth tracing

- URLs:
  - https://ethereum.org/developers/docs/apis/json-rpc/
  - https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-debug
  - https://geth.ethereum.org/docs/developers/evm-tracing/built-in-tracers
- Supports: canonical block/receipt access and client-specific execution tracing used by the proposed replay design.
- Evidence type: official network/client documentation.
- Limitation: provider access, retention, throttling, and historical-state completeness vary; trace output is client/version dependent.

## Empirical papers and research

### P1 — Who Wins Ethereum Block Building Auctions and Why?

- URL: https://arxiv.org/abs/2407.13931
- Authors: Burak Öz, Danning Sui, Thomas Thiery, Florian Matthes.
- Study window: October 2023–March 2024.
- Supports: approximately 90% MEV-Boost use in the study context; three builders produced 80% of observed blocks; correlations between market share and order-flow diversity, and between profitability and exclusive order flow.
- Evidence type: empirical paper/preprint.
- Limitations: correlations do not prove causation; builder identities and shares can change; do not project the percentages to 2026 without a fresh dataset.

### P2 — Private Order Flows and Builder Bidding Dynamics: The Road to Monopoly in Ethereum's Block Building Market

- URL: https://arxiv.org/abs/2410.12352
- Authors: Shuzheng Wang, Yue Huang, Wenqin Zhang, Yuming Huang, Xuechao Wang, Jing Tang.
- Study window: January 2023–May 2024.
- Supports: the paper's estimate that private order flow contributed 54.59% of block value and its empirical/model analysis of reinforcing builder advantages.
- Evidence type: empirical/modeling preprint.
- Limitations: model-dependent attribution of private order flow; not a direct measure of private-flow accessibility to a new searcher.

### P3 — Non-Atomic Arbitrage in Decentralized Finance

- URL: https://arxiv.org/abs/2401.01622
- Authors: Lioba Heimbach, Vabuk Pahari, Eric Schertenleib.
- Study window: the Merge through 2023-10-31.
- Supports: classifier-derived estimate that more than one quarter of volume on five studied Ethereum DEXes was likely non-atomic arbitrage; 11 searchers accounted for more than 80% of identified non-atomic-arbitrage volume.
- Evidence type: empirical paper/preprint.
- Limitations: heuristic classification; volume is not PnL; off-chain legs and true operator boundaries are partially unobserved.

### P4 — Measuring CEX-DEX Extracted Value and Searcher Profitability: The Darkest of the MEV Dark Forest

- URL: https://arxiv.org/abs/2507.13023
- Authors: Fei Wu, Danning Sui, Thomas Thiery, Mallesh Pai.
- Study window: 2023-08-08–2025-03-08.
- Supports: 7,203,560 identified CEX–DEX arbitrages, estimated $233.8 million extracted by 19 major labeled searchers, roughly three-quarter concentration among three searchers, liquidity/return patterns, and evidence associating profitability with builder relationships.
- Evidence type: empirical preprint.
- Limitations: CEX execution is inferred; PnL depends on assumed execution horizon, price feeds, labels, fees, and builder/searcher attribution. The authors note that definitive proof of exclusivity would require relay-level evidence.

### P5 — An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities

- URL: https://arxiv.org/abs/2106.06389
- Authors: Kaihua Qin, Liyi Zhou, Pablo Gamito, Philipp Jovanovic, Arthur Gervais.
- Supports: historical liquidation-mechanism taxonomy, incentives, and participant risks across Aave, Compound, MakerDAO, and dYdX.
- Evidence type: empirical academic paper/preprint.
- Limitations: old protocol versions and market structure; use for methodology, not current profitability or market share.

### P6 — Searcher Competition in Block Building

- URL: https://collective.flashbots.net/t/searcher-competition-in-block-building/3659
- Supports: a competition model in which sufficiently overlapping searcher capabilities compete expected profit toward zero, validated against aggregated historical MEV-Share clash data.
- Evidence type: Flashbots research discussion linking the underlying paper.
- Limitations: theoretical assumptions and aggregated data; it does not measure the proposed contract-specific strategy.

### P7 — Flashbots Merge Anniversary: A Year in Review

- URL: https://collective.flashbots.net/t/merge-anniversary-a-year-in-review/2400
- Supports: historical `mev-inspect-py` analysis of atomic MEV and proposer share; comparison of atomic and non-atomic value capture.
- Evidence type: Flashbots retrospective research post.
- Limitations: historical, conservative classifier coverage, not peer-reviewed, and not current 2026 economics.

## Evidence not yet collected

- Current builder/relay market shares and per-builder inclusion performance.
- A reproducible current MEV-Share hint census.
- Project-original Ethereum blocks, traces, receipts, or transaction hashes.
- Current atomic-arbitrage and liquidation concentration.
- Provider quotes for archive state, traces, storage, egress, and live pending feeds.
- Actual searcher bundle submissions, rejection responses, or retained-value accounting.

These omissions are why the screen recommends a bounded data census rather than a trading implementation.

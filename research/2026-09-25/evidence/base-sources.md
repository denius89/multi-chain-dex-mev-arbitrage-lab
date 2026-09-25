# Base screening source register

Retrieval date for all links: **2026-09-25**.

This register supports [`../network-screening/base.md`](../network-screening/base.md). Official documentation describes interfaces as observed on the retrieval date. Papers support only their declared samples and methods; quantitative findings are not assumed to remain unchanged under Flashblocks or Denim.

## Base network documentation

### B1 — Transaction ordering

- URL: https://docs.base.org/specifications/transactions/transaction-ordering
- Supports: 200-ms priority-fee auctions; arrival time determines eligible Flashblock; ordering locks after broadcast; cumulative gas allocation; dynamic mempool behavior.
- Evidence type: official network documentation.
- Limitation: describes protocol/operator behavior, not provider-specific latency, inclusion probability, or searcher economics.

### B2 — Base RPC overview

- URL: https://docs.base.org/base-chain/api-reference/rpc-overview
- Supports: public endpoints are HTTP-only and rate-limited; Flashblocks `pending` state; standard EVM RPC; `eth_simulateV1`; transaction/log/full-Flashblock subscriptions; provider-dependent debug tracing.
- Evidence type: official API documentation.
- Limitation: methods and provider support are mutable. Presence of simulation methods is not a bundle-submission or adjacency guarantee.

### B3 — Flashblocks API

- URLs:
  - https://docs.base.org/base-chain/api-reference/flashblocks-api/flashblocks-api-overview
  - https://docs.base.org/base-chain/api-reference/flashblocks-api/newFlashblockTransactions
  - https://docs.base.org/base-chain/api-reference/flashblocks-api/pendingLogs
  - https://docs.base.org/base-chain/api-reference/flashblocks-api/newFlashblocks
  - https://docs.base.org/base-chain/api-reference/flashblocks-api/base_transactionStatus
- Supports: observable preconfirmation subscriptions, pending logs/state, and transaction-receipt checks at Flashblock cadence.
- Evidence type: official API documentation.
- Limitation: data is exposed after sequencer ordering into a Flashblock; it is not a public view of every transaction waiting in the sequencer's private mempool.

### B4 — Flashblocks engineering deep dive

- URL: https://blog.base.dev/flashblocks-deep-dive
- Supports: 2025-07-16 mainnet launch; ten 200-ms Flashblocks per two-second block; sequencer topology; private mempool route; builder fee ordering; RPC fan-out architecture; documented historical reliability work.
- Evidence type: primary Base engineering post.
- Limitation: architecture narrative and historical engineering measurements are not an SLA or current latency benchmark.

### B5 — Denim 200-ms native blocks

- URL: https://docs.base.org/upgrades/denim/200ms-blocks
- Supports: experimental Vibenet status; October 2026 target; five complete canonical blocks per second; per-block hash/state/receipts/finality lifecycle; BaseTime/`timestampMs` design; replacement of Flashblocks.
- Evidence type: official upgrade specification.
- Limitation: documentation says exact activation times and required client versions remain undecided; Vibenet behavior is not production behavior.

### B6 — Migrate from Flashblocks

- URL: https://docs.base.org/upgrades/denim/migrate-from-flashblocks
- Supports: Denim not yet active on Sepolia/mainnet on retrieval date; removal of Flashblocks subscriptions and pending preconfirmation state; migration mappings to canonical heads/logs/state.
- Evidence type: official migration documentation.
- Limitation: rollout plan is mutable and must be rechecked before any live experiment.

### B7 — Run a Base node

- URL: https://docs.base.org/specifications/node-operators/run-a-node
- Supports: official node deployment path, Flashblocks enablement, public mainnet/Sepolia endpoints, rate-limit warning, resource/cost warning, and snapshot availability.
- Evidence type: official node-operator documentation.
- Limitation: does not supply a fixed universal hardware or cost quote; configuration and chain growth change requirements.

## Protocol and venue documentation

### V1 — Uniswap v3 Base deployments

- URL: https://developers.uniswap.org/docs/protocols/v3/deployments/v3-base-deployments
- Supports: official Base v3 factory, router, quoter, position manager, Permit2, universal router, and WETH deployment mappings.
- Evidence type: primary protocol deployment registry.
- Limitation: v4 and other versions require their own manifests; individual pools must be enumerated from the factory or official index.

### V2 — Uniswap unified deployments

- URL: https://developers.uniswap.org/deployments
- Supports: current multi-version, multi-network deployment registry, including Base.
- Evidence type: primary protocol deployment registry.
- Limitation: large and mutable; save a dated machine-readable manifest before data collection.

### V3 — Aerodrome contracts and deployments

- URL: https://github.com/aerodrome-finance/contracts
- Supports: constant-product-style pool/router implementation and official Base deployment list for the repository's generation.
- Evidence type: primary source-code/deployment repository.
- Limitation: concentrated-liquidity/Slipstream generations and upgrades must be pinned separately; repository addresses are not a complete historical registry by themselves.

### V4 — PancakeSwap Infinity on Base

- URLs:
  - https://blog.pancakeswap.finance/articles/baseinfinity
  - https://github.com/pancakeswap/pancake-developer/blob/master/docs/pages/contracts/universal-router/addresses.md
- Supports: Infinity live on Base; CLAMM and LBAMM pool types; hooks/dynamic fees; routing across v2/v3/Infinity; Base router addresses.
- Evidence type: primary protocol announcement and developer repository.
- Limitation: marketing gas claims are not used as measured transaction costs; pool-manager/factory/hook addresses still require a dated manifest.

### V5 — Balancer Base deployments

- URL: https://docs.balancer.fi/developer-reference/contracts/deployment-addresses/base.html
- Supports: official Base page for active core contracts, routers, factories, hooks/peripherals, and deprecated deployments.
- Evidence type: primary protocol deployment documentation.
- Limitation: deployment state is mutable; bytecode/version and active/deprecated status must be preserved by block range.

### V6 — Aave Base address book and protocol docs

- URLs:
  - https://github.com/aave-dao/aave-address-book/blob/main/src/AaveV3Base.sol
  - https://aave.com/docs
- Supports: an official Base v3 deployment/address registry and market integration surface.
- Evidence type: primary DAO-maintained address book and protocol documentation.
- Limitation: reserve parameters, oracle configuration, liquidation rules, and addresses can change; use a block-specific generated version.

### V7 — Morpho developer resources

- URLs:
  - https://docs.morpho.org/developers/contracts/addresses/
  - https://docs.morpho.org/developers/api/get-started/
  - https://docs.morpho.org/developers/sdks/get-started/
- Supports: Base chain ID support, contract/address resources, API access to markets/positions, and low-level SDK primitives.
- Evidence type: primary protocol documentation.
- Limitation: API convenience data must be reconciled to on-chain market parameters for historical liquidation accounting.

## Historical-data documentation

### D1 — Dune Base raw transactions

- URL: https://docs.dune.com/data-catalog/evm/base/raw/transactions
- Supports: availability of the `base.transactions` raw table.
- Evidence type: primary data-provider documentation.
- Limitation: query plan, freshness, pricing, and export limits depend on the account/tier and can change.

### D2 — Dune Base logs

- URL: https://docs.dune.com/data-catalog/evm/base/raw/logs
- Supports: availability of the `base.logs` table.
- Evidence type: primary data-provider documentation.
- Limitation: event logs omit internal calls and do not replace trace or historical-state replay.

### D3 — Dune Base traces

- URL: https://docs.dune.com/data-catalog/evm/base/raw/traces
- Supports: availability of the `base.traces` raw table for internal call analysis.
- Evidence type: primary data-provider documentation.
- Limitation: validate trace semantics/completeness against independently fetched samples and record the data version.

### D4 — Dune Base decoded data and DEX trades

- URLs:
  - https://docs.dune.com/data-catalog/evm/base/decoded/overview
  - https://docs.dune.com/data-catalog/evm/base/curated-data/dex/dex-trades
- Supports: decoded contract tables and curated Base DEX-trade data used to bootstrap the public optimistic-MEV classifier.
- Evidence type: primary data-provider documentation.
- Limitation: labels and protocol coverage may omit new/custom/hook pools; they are candidate-generation inputs, not canonical financial truth.

## Empirical research

### P1 — Optimistic MEV in Ethereum Layer 2s: Why Blockspace Is Always in Demand

- URL: https://arxiv.org/abs/2506.14768 (v2, 2025-08-05; AFT 2025 extended paper).
- Authors: Ozan Solmaz, Lioba Heimbach, Yann Vonlanthen, Roger Wattenhofer.
- Observation window: August 2023–May 2025; Q1 2025 is used for several headline percentages.
- Supports: formalization and classification of optimistic MEV; open Dune/trace method; Base transaction outcomes, gas/fee shares, bot-contract examples, calldata reuse, and cross-L2 comparison.
- Key Base sample results used in the screen:
  - 6.3% of DEX-interacting calls to identified cyclic-arbitrage contracts executed trades in the broad comparison;
  - 51% of Base gas in Q1 2025 was attributed to cyclic-arbitrage contracts, 48% to interaction/probing;
  - 23% of Base transaction fees were attributed to these contracts despite their gas share;
  - top-contract sample: about 0.58% trade-execution rate and 0.005% EVM revert rate;
  - the top ten Base contracts by attributed bot gas cumulatively reached 24.56% of the identified bot set.
- Reproducibility fixtures reported by the paper:
  - contract: `0xF5fF765b0c1278E54281193d7019281e0e50A8C0`;
  - no-swap probe: `0x1d977d6867e2868b518a10803d64b414e428bd8e639d3c5054b2529cb55d18cb`;
  - successful two-swap cycle: `0xb67825a6fa60e4bd9892076ead93c41f631460a53b8219036a5ace051f139bd7`.
- Evidence type: peer-reviewed empirical conference paper/extended preprint.
- Critical limitation: its Base sample predates the 2025-07-16 Flashblocks mainnet launch. It cannot establish current 200-ms-regime economics. Classification is heuristic and operator ownership is not proven by contract address.

### P2 — Cross-Rollup MEV: Non-Atomic Arbitrage Across L2 Blockchains

- URL: https://arxiv.org/abs/2406.02172 (v2, 2024-10-17).
- Authors: Krzysztof Gogol, Johnnatan Messias, Deborah Miori, Claudio Tessone, Benjamin Livshits.
- Supports: methodology and estimates for potential cross-rollup/CEX–DEX price discrepancies; more than 500,000 unexplored opportunities; average 10–20-block persistence; estimated opportunity value of 0.03%–0.05% of volume for Arbitrum/Base/Optimism under the paper's assumptions.
- Evidence type: empirical/measurement research.
- Limitations: identifies potential non-atomic opportunities, not necessarily executed net-profitable trades; results use legacy block regimes and must not be converted directly into 200-ms latency expectations.

### P3 — Cross-Chain Arbitrage: The Next Frontier of MEV in Decentralized Finance

- URL: https://arxiv.org/abs/2501.17335 (v2, 2025-06-18).
- Authors: Burak Öz, Christof Ferreira Torres, Christoph Schlegel, Bruno Mazorra, Jonas Gebele, Filip Rezabek, Florian Matthes.
- Observation window: September 2023–August 2024 across nine chains.
- Supports: 242,535 identified executed cross-chain arbitrages and $868.64 million aggregate volume; comparison of inventory- and bridge-based execution; reported 66.96% pre-positioned-inventory share; 9-second versus 242-second settlement findings; high actor concentration.
- Evidence type: empirical preprint.
- Limitations: cross-chain aggregate rather than a current Base-only sample; clustering/classification/model assumptions apply; volume is not PnL; off-chain hedging and full operator economics remain partially unobservable.

## Evidence not yet collected

- Project-original post-Flashblocks Base transaction sample.
- Raw receipts/traces and checksums for the paper-reported fixtures.
- Post-Flashblocks bot contract list and current trade/no-trade/revert ratios.
- Current profit distribution, tail concentration, winner concentration, and failure cost.
- Provider quotes and measured completeness for archive state/traces.
- Dual-provider Flashblocks lag measurements.
- Evidence of a production Base interface guaranteeing private trigger/backrun adjacency.
- Denim mainnet activation block/client versions and post-activation measurements.
- Current contract manifests and bytecode hashes for every proposed venue.

These omissions are why the screen recommends a bounded regime-aware census rather than live execution.

# Robinhood Chain — network screening

> Research date: 2026-09-25  
> Network: Robinhood Chain mainnet (`chainId = 4663`)  
> Stage: Stage 1 screening; no profitability claim  
> Decision: **GO to a narrow, read-only historical/market-data probe; NO-GO for an executor**

## Short conclusion

Robinhood Chain is not merely an announced ecosystem. The chain is live, public endpoints and a sequencer feed are documented, Stock Token contracts are exposed through a live registry, Uniswap transactions are visible in the explorer, Lighter exposes a dedicated instance/API, and Morpho has measurable lending and liquidation activity.

It is nevertheless too early to call Robinhood Chain a profitable arbitrage target. The strongest public metrics describe aggregate TVL and volume, not accessible searcher PnL. The Stock Token registry proves issuance, not liquid two-sided markets. Rialto and RFQ integrations are documented or announced, but this screening did not establish firm public quotes, contract-level fill history, or sufficient depth for an ordinary taker. Lighter is a separate execution domain, so a Lighter/onchain spread is not atomic by default.

The cheapest credible next step is a **7-day read-only probe** covering (a) public Uniswap/aggregator routes, (b) Stock Token reference normalization, and (c) Morpho liquidations. Do not buy low-latency infrastructure or build transaction submission yet.

## Evidence standard used

- **Confirmed:** official Robinhood/venue documentation, official public API output, explorer transaction evidence, or current third-party aggregate data clearly labelled as such.
- **Derived:** calculation or screening judgment based on cited inputs.
- **Hypothesis:** a strategy that still needs historical replay or live paper data.
- A venue announcement, ecosystem listing, API support flag, or token deployment is **not** treated as proof of executable liquidity or profit.

## Confirmed network and ordering facts

- Robinhood Chain is a live, permissionless EVM-compatible Arbitrum L2 using ETH for gas.
- Ordering is documented as first-come, first-served at the sequencer. A later transaction cannot jump ahead of an already received transaction by paying a higher fee.
- Public, rate-limited RPC, WebSocket/sequencer-feed, and direct sequencer endpoints are documented. Robinhood recommends a production provider and archive access for historical indexing.
- Soft confirmation is sub-second; posting to Ethereum typically takes minutes; full L1 finality is documented at roughly 13 minutes after posting.
- The public sequencer feed is an Arbitrum low-latency feed of sequenced data. Nothing in the reviewed documentation proves pre-order/mempool visibility. Treat it as a faster observation path, not privileged order flow.

**Implication:** pure same-chain backrun/cyclic arbitrage is a latency race in which priority-fee bidding cannot repair late arrival. A public team may still compete on faster state ingestion, direct sequencer submission, precomputed routes, and neglected markets, but that remains unmeasured.

## Current activity snapshot

The following values are mutable, third-party DefiLlama snapshots retrieved on 2026-09-25. They establish that economic activity exists; they do not establish arbitrage profitability or independent data quality:

| Metric | Snapshot |
|---|---:|
| DeFi TVL | $1.016B |
| Stablecoin market cap | $1.038B |
| RWA active AUM | $291.27M |
| DEX volume, 24h | $1.339B |
| DEX volume, 7d | $10.018B |
| Perpetual volume, 24h | $633.76M |
| Perpetual volume, 7d | $4.356B |

DefiLlama also showed Uniswap with about $283.46M TVL on the chain and Lighter with about $102.04M TVL. These are protocol-level aggregates, not a list of Stock Token markets or executable depth. Recent Blockscout results show successful transactions touching Uniswap V2/V4 contracts, including a transaction containing both `PoolManager` and `Uniswap V2` transfers and another involving an ASML Stock Token and the Uniswap v4 position manager. This is enough to confirm live contract use, not enough to infer a profitable route.

## Venue-by-venue assessment

### Uniswap and public AMMs — **verified live; depth not yet measured**

Confirmed:

- Robinhood lists Uniswap as the public DEX; Uniswap states its apps/API support Robinhood Chain.
- 0x added Robinhood Chain to Swap/Gasless APIs and lists numerous native sources, including Uniswap V2/V3/V4, PancakeSwap, SushiSwap, Ramses, Ekubo and others.
- Explorer evidence shows successful Uniswap contract interactions.

Not established:

- exact active factories/pool managers and the complete pool registry;
- executable depth by pair and input size;
- whether multiple independent pools exist for the same liquid Stock Token pair;
- searcher profit, failed-attempt costs, and opportunity lifetime.

**Screening result:** best same-chain starting surface because it is public, atomic routes are technically possible, and historical logs are indexable. Start with verified factories and actual swap counts, not advertised protocol names.

### Rialto propAMM — **announced and accessible as an app; liquidity unverified here**

Rialto announced a Robinhood Chain spot venue and its Rivo Altus propAMM, initially describing 90+ Stock Tokens and major crypto assets. Robinhood lists Rialto as a propAMM/aggregator. Rialto documentation describes supported markets conceptually.

This screening did **not** independently obtain:

- canonical Robinhood Chain contract addresses and ABIs;
- public quote/API requirements;
- firm quote eligibility for an ordinary account;
- onchain fill events, volume, spreads, or depth.

**Screening result:** retain as a discovery task, but do not include Rialto in backtests until contracts and fills are reproducibly identified.

### RFQ / aggregators — **routing support confirmed; firm RFQ access unproven**

Robinhood documentation describes signed market-maker RFQ quotes through aggregators such as 0x RFQ, 1inch Fusion, and LI.FI. 0x officially supports chain ID 4663 in its Swap and Gasless APIs and exposes a source-list endpoint.

API support does not prove that a public taker receives a firm Stock Token RFQ. It may return only AMM routing, require an API key or commercial access, restrict the taker, or expose no maker for a requested pair. A valid test must preserve the signed quote, source breakdown, taker, expiry, input/output, settlement target, gas estimate, and revert outcome.

**Screening result:** test public quote coverage with a small fixed pair matrix; count RFQ fills separately from AMM routes. Do not model indicative quotes as executable liquidity.

### Lighter order book — **live separate domain; not atomically composable by assumption**

Confirmed:

- Robinhood documents a dedicated Lighter instance with its own contracts, sequencer, blockspace, and liquidity.
- The instance has a public UI, API base URL, market/order-book/trade endpoints, and a Robinhood Chain deposit contract.
- Direct deposits and fast/secure withdrawals are documented; DefiLlama records current Lighter TVL and perpetual volume on Robinhood Chain.

Not established:

- which Stock Token spot/perpetual books are currently live;
- public depth and fill history per market;
- deterministic deposit crediting and fast-withdraw latency under load;
- whether any hedge can be made atomically with a Robinhood Chain AMM transaction.

**Screening result:** promising for basis and inventory-based convergence, but treat cross-domain execution as two-legged and non-atomic until proven otherwise.

### Morpho — **deployment verified; activity indicated by third-party snapshots**

Morpho officially supports chain ID 4663 and publishes deployment/API support. The official address registry identifies the Robinhood Chain Morpho deployment (`0x9D53d5E3bd5E8d4Cbfa6DB1ca238AEA02E651010`), and Blockscout indexes it as `Morpho`.

Mutable DefiLlama snapshots on 2026-09-25 showed approximately:

- $563.9M Morpho Blue TVL on Robinhood Chain;
- $56.9K fees in 24h and $401.4K in 7d;
- collateral liquidated: $4.5K in 24h, $63.7K in 7d, and $188.2K in 30d.

Those liquidation totals demonstrate an active liquidation surface, not liquidator profit. We still need the market IDs, collateral types, oracle paths, borrower health, liquidation incentives, competition, and unwind liquidity.

**Screening result:** advance alongside AMM screening. It may be more falsifiable than Stock Token cross-venue arbitrage because market events and liquidations are onchain and historically replayable.

## Stock Tokens and price sources

### What is confirmed

- Stock Tokens are ERC-20 tokenized debt securities, not ownership of the underlying equity.
- The live `/rhj/assets` registry returns active chain-4663 deployments, multipliers, status, decimals, and per-session trading capabilities. A registry entry proves that a token contract is active; it does not prove a liquid market.
- Stock Tokens use a shares-per-token multiplier. Raw REST equity bid/ask data is **not** multiplier-adjusted, while the onchain Chainlink feed is already adjusted.
- The REST `/prices/{symbol}` endpoint is cached for 15 seconds and rate-limited to 60 requests/second. It is suitable as a reference/check, not as the sole source for a sub-second executor.
- Chainlink feeds provide onchain references; the integration requires timestamp/staleness and `oraclePaused()` checks.
- Chainlink Data Streams provide a separate sub-second, signed pull-data path and a Robinhood Chain verifier proxy, but access/coverage and cost must be established before it is included in an MVP budget.

### Critical accounting rule

For comparison with an executable token price:

```text
token_reference_price = raw_underlying_bid_or_ask * currentMultiplier
```

Never compare an AMM Stock Token price directly to the raw REST equity price. A visible difference may be entirely explained by a dividend/split multiplier. Also, a Chainlink/REST reference is not itself an executable exit.

## Trading windows and regime changes

- Authorized market makers can mint/burn from Monday 02:00 CET/CEST through Saturday 02:00 CET/CEST. Ordinary users cannot assume primary-market access; Robinhood states that direct issuance is limited to authorised participants after KYB.
- End users may trade Stock Tokens onchain outside that window.
- Per-asset market, extended-hours, fractional, and overnight capability must be read from the live asset registry and can vary.
- Corporate actions can change the multiplier and pause or stale an oracle.

**Hypothesis:** spreads/depth may change near US session open/close, at the weekly mint/burn boundary, over weekends, during halts, and around multiplier changes. Without an executable hedge or redemption, those are inventory-risk regimes, not risk-free arbitrage.

## Strategy shortlist

| Rank | Strategy | Evidence today | Atomic? | Cheapest falsification |
|---:|---|---|---|---|
| 1 | Public AMM cyclic/cross-pool | Live Uniswap/AMM use confirmed | Potentially yes, same chain | Enumerate verified pools; replay quotes around swaps |
| 2 | Morpho liquidations + AMM unwind | Deployment confirmed; activity indicated by third-party snapshots | Potentially yes | Index markets/liquidations; calculate realized seizure and unwind |
| 3 | RFQ vs AMM | Aggregator/RFQ plumbing documented | Only if firm quote settlement composes | Request fixed quote matrix; inspect source and settlement |
| 4 | Stock Token venue/reference divergence | Tokens and references confirmed | Usually no external hedge for public user | Normalize top tokens; measure executable AMM depth and persistence |
| 5 | Lighter spot/perp basis | Separate active domain confirmed | No, unless future proof/message path changes this | Pull market list, depth, funding and recent trades |
| 6 | Corporate-action/session boundary | Correct state variables exist | Generally inventory-based | Monitor predefined windows and multiplier events |
| Hold | Rialto propAMM convergence | Product announcement/listing only | Unknown | Resolve contracts/API and reproduce one fill |

## What can be tested without paid data

1. **Registry snapshot:** fetch `/rhj/assets`, `/prices/{symbol}`, and `/corporate-actions`; preserve retrieval timestamps and hashes.
2. **Live heads/logs:** use the rate-limited public RPC for a bounded proof and the public sequencer feed for connectivity/timestamp experiments.
3. **Pool discovery:** enumerate verified factory/pool-manager events using public RPC/Blockscout over a bounded range.
4. **Aggregator coverage:** query public/free-tier 0x routing for a fixed token/size matrix; label AMM and RFQ sources separately.
5. **Lighter discovery:** fetch public market metadata, books, recent trades, funding and candles from the dedicated API.
6. **Morpho discovery:** use the public Morpho API and onchain events to list markets, balances and liquidations.
7. **Reference normalization:** compare multiplier-adjusted REST and onchain oracle values; reject stale, paused, halted, or closed-reference observations.

Free/public data is enough to decide whether the candidate population exists and whether decoders work. It is **not** enough to make strong millisecond-latency or complete-failure-cost claims; archive traces, durable feed capture, and production RPC may be needed later.

## Proposed 7-day probe

### Scope

- 10 highest-activity Stock Tokens selected by observed swaps (not brand recognition), plus WETH/USDG.
- Verified Uniswap V2/V3/V4 contracts and at most one additional public AMM family.
- All Morpho markets with non-zero borrow and the top 20 borrowers by liquidation proximity.
- Lighter metadata/depth collection only; no assumption of atomic execution.
- 0x quote matrix at fixed notional sizes: $10, $100, $1,000 and $10,000 where routes exist.

### Required outputs

- canonical contract/market registry with provenance;
- counts of pools, swaps, quotes, RFQ-sourced quotes, Morpho markets and liquidations;
- executable depth and price impact at fixed sizes;
- normalized reference divergence with freshness flags;
- same-chain simulated net PnL including gas/L1 data component;
- rejection reasons: no route, stale reference, multiplier mismatch, insufficient depth, non-atomic leg, restricted quote, revert;
- pipeline timestamps for public RPC vs sequencer feed.

### Pass gate

Advance to historical reconstruction only if at least one narrowly defined strategy has:

- reproducible inputs and verified contracts;
- multiple candidate events, not one outlier;
- a real executable exit;
- measurable costs and simulation support;
- an entry path that does not require authorised-participant mint/burn or undisclosed private order flow.

## Screening score

Scale: 1 (poor) to 5 (strong). Scores are recommendations, not facts.

| Criterion | Score | Rationale |
|---|---:|---|
| Public data accessibility | 4 | Public RPC/feed, explorer, registries and venue APIs; archive/production quality may cost money |
| Historical replay feasibility | 4 | EVM logs/traces and public protocol APIs; cross-domain Lighter replay adds complexity |
| Demonstrated economic activity | 5 | Large third-party aggregate DEX/perps/TVL and reported Morpho liquidation activity; requires on-chain reconstruction |
| Public entry path | 3 | AMMs/Morpho are public; primary mint/burn is permissioned; RFQ eligibility unclear |
| Atomic execution surface | 3 | Strong on same-chain AMMs/Morpho, weak across Lighter/reference markets |
| Competition accessibility | 2 | FCFS rewards end-to-end latency; no measured searcher concentration yet |
| Unique structural hypotheses | 4 | Stock Token multipliers, sessions, corporate actions, lending and separate Lighter domain |
| Evidence of accessible profit | 1 | No searcher PnL reconstruction in this sprint |

**Overall recommendation:** keep Robinhood Chain on the shortlist, but the first implementation should be a registry/indexer plus AMM/Morpho classifier. Stock Token/RFQ/Lighter strategies remain discovery tracks until public executable depth is demonstrated.

## Unknowns that block a stronger conclusion

1. Verified live pool registry, depth and pair concentration by DEX.
2. Searcher addresses, realized PnL, failure costs and winner concentration.
3. Firm RFQ availability to an ordinary public taker and RFQ fill history.
4. Rialto contracts, public quote terms and onchain fills.
5. Current Lighter market list and Stock Token spot/perp depth.
6. Stock Token share of DEX volume after correct multiplier normalization.
7. Actual feed-to-RPC-to-sequencer latency from our deployment region.
8. Post-subsidy fee regime and whether headline activity is durable.

## Sources

Detailed source classification and retrieval notes are in [`../evidence/robinhood-sources.md`](../evidence/robinhood-sources.md).

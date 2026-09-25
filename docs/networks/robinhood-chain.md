# Robinhood Chain: research brief

> Status: research design, not a profitability claim
> Snapshot date: 2026-09-25
> Network: Robinhood Chain mainnet (`chainId = 4663`)

## Executive summary

Robinhood Chain is a live, permissionless, EVM-compatible Arbitrum Layer 2 focused on tokenized real-world assets. Its most important execution property for this project is **first-come, first-served (FCFS) sequencing**: a higher priority fee does not move a later transaction ahead of an earlier one already received by the sequencer. The chain publishes public RPC, WebSocket, sequencer, sequencer-feed, Blockscout, Stock Token metadata, price, and corporate-action endpoints.

The network is therefore interesting for two distinct research tracks:

1. **Latency-sensitive onchain arbitrage** among AMMs, RFQ liquidity, order books, and other venues.
2. **Information- and structure-driven arbitrage** around Stock Tokens: venue divergence, oracle/market divergence, trading-session boundaries, issuer mint/burn windows, corporate actions, lending liquidations, and spot/perpetual basis.

Only the network mechanics and advertised integrations are confirmed. **The existence, frequency, size, accessibility, and persistence of profitable opportunities are unproven.** The first deliverable should be a read-only monitor and historical classifier, not a trading executor.

## Confirmed facts

The statements in this section are taken from Robinhood Chain's current official documentation unless another primary source is linked.

### Network and execution

- Robinhood Chain is an Ethereum-compatible Layer 2 built on Arbitrum Dedicated Blockchains / Arbitrum Nitro.
- Mainnet chain ID is `4663`; ETH is the native gas token.
- Transaction data is posted to Ethereum using blobs.
- Transaction ordering is FCFS by arrival time at the sequencer. Robinhood's documentation explicitly says that paying a higher fee cannot jump ahead of transactions already in the queue.
- A transaction receives a sub-second soft confirmation from the sequencer. Posting to Ethereum typically takes minutes; full Ethereum finality is documented as roughly 13 minutes after posting.
- Fees consist of L2 execution cost and L1 data cost.
- The sequencer applies compliance screening; transactions associated with sanctioned addresses may be excluded.

Primary references:

- [About Robinhood Chain](https://docs.robinhood.com/chain/)
- [Connecting to Robinhood Chain](https://docs.robinhood.com/chain/connecting/)
- [Differences from Ethereum](https://docs.robinhood.com/chain/differences-from-ethereum/)
- [Gas and fees](https://docs.robinhood.com/chain/gas-and-fees/)
- [Transaction finality](https://docs.robinhood.com/chain/transaction-finality/)

### Public endpoints

| Purpose | Mainnet endpoint |
|---|---|
| Rate-limited RPC | `https://rpc.mainnet.chain.robinhood.com` |
| Sequencer submission | `https://sequencer.mainnet.chain.robinhood.com` |
| Sequencer feed | `wss://feed.mainnet.chain.robinhood.com` |
| Block explorer | `https://robinhoodchain.blockscout.com` |
| Stock Token asset registry | `https://api.robinhood.com/rhj/assets` |
| Stock Token quote by symbol | `https://api.robinhood.com/rhj/prices/{symbol}` |
| Corporate actions | `https://api.robinhood.com/rhj/corporate-actions` |

The public RPC is rate-limited and not recommended by Robinhood for production. Robinhood lists Alchemy as the recommended provider and also lists Chainstack, QuickNode, Blockdaemon, dRPC, Validation Cloud, and GlobalStake. Archive access is required for dependable historical reads. See [Connecting to Robinhood Chain](https://docs.robinhood.com/chain/connecting/).

A self-hosted full node can subscribe directly to the sequencer feed, but Robinhood documents substantial requirements: at least 8 CPU cores, 64 GB RAM (128 GB recommended), local NVMe, and several terabytes of storage. A full node also needs Ethereum execution and beacon endpoints. It is **not** required for the initial monitor. See [Run a full node](https://docs.robinhood.com/chain/run-a-full-node/).

### Liquidity and market surfaces

Robinhood's ecosystem documentation currently identifies the following surfaces:

| Surface | Advertised role | What must still be verified |
|---|---|---|
| Uniswap | Public AMM / DEX | Factory/router versions, pool addresses, TVL, active pairs, fee tiers, usable depth |
| Rialto | PropAMM / spot aggregator | Quote interface, contract addresses, fill rules, public accessibility, historical fills |
| RFQ via aggregators | Signed market-maker quotes; Robinhood names 0x RFQ, 1inch Fusion, and LiFi | API access, quote validity, taker eligibility, settlement contracts, failed-fill behavior |
| Lighter | Dedicated order-book venue for spot and perpetuals | Listed markets, live depth, fees, rate limits, fill history, withdrawal timing |
| Morpho | Lending and borrowing | Deployed markets, collateral parameters, oracle configuration, liquidation incentives, liquidity |
| Chainlink | Onchain price feeds and offchain Data Streams | Feed coverage, heartbeat, deviation threshold, access terms for Data Streams |

References:

- [Robinhood Chain ecosystem](https://docs.robinhood.com/chain/)
- [Building with Stock Tokens — liquidity sources](https://docs.robinhood.com/chain/building-with-stock-tokens/)
- [Robinhood Chain Lighter Domain](https://docs.robinhood.com/chain/lighter-domains/)

The Robinhood Chain Lighter instance is a dedicated domain with its **own execution, sequencer, blockspace, and liquidity**; it is not simply another contract sharing Robinhood Chain's FCFS ordering. Its official page lists the settlement/deposit contract, API base URL, and API documentation. This separation matters: cross-venue strategies must model deposit, withdrawal, crediting, and inventory latency rather than assume atomic composability with Robinhood Chain AMMs.

### Stock Tokens

- Stock Tokens are ERC-20 tokenized debt securities issued by Robinhood Assets (Jersey) Limited. They provide economic exposure to underlying shares or ETFs but do not grant ownership rights in the underlying security.
- Tokens use 18 decimals and implement ERC-8056-style UI scaling through `uiMultiplier()`.
- Each Stock Token has a Chainlink price feed. The onchain feed price is already multiplier-adjusted.
- Robinhood's REST `/prices` endpoint returns the raw underlying-equity bid/ask and is **not** multiplier-adjusted. Combining REST and onchain prices without applying `currentMultiplier` creates a false discrepancy.
- REST prices are documented with a 15-second cache and a 60-request-per-second limit. They are unsuitable as the only source for sub-second execution decisions.
- Chainlink Stock Token feeds update 24/5. A feed can pause during a corporate action; code must check timestamps, heartbeat, sequencer uptime, and `oraclePaused()`.
- Direct mint/burn is available only to authorized participants / market makers after KYB. A normal searcher cannot assume access to primary-market conversion.
- Stock Tokens can still trade onchain outside the mint/burn window, subject to venue liquidity.

References:

- [Stock Tokens overview](https://docs.robinhood.com/chain/stock-tokens/)
- [Building with Stock Tokens](https://docs.robinhood.com/chain/building-with-stock-tokens/)
- [Stock Token APIs](https://docs.robinhood.com/chain/stock-token-apis/)
- [Oracles and price feeds](https://docs.robinhood.com/chain/oracles-and-price-feeds/)
- [Canonical token contracts](https://docs.robinhood.com/chain/contracts/)

## Time windows that change market behavior

All times below follow Robinhood's documentation and are subject to daylight-saving schedules.

### Tokenization window

Authorized market makers can mint and burn Stock Tokens from **Monday 02:00 CET/CEST through Saturday 02:00 CET/CEST**. Mint/burn is unavailable outside that window. Secondary onchain trading may continue.

This creates a researchable boundary:

- during the window, authorized participants can in principle anchor secondary prices through creation/redemption;
- outside the window, inventory cannot be refreshed through issuer mint/burn, so spreads and inventory premia may behave differently;
- this does **not** prove that public traders can capture the divergence, because they lack direct mint/burn access and may face shallow or one-sided liquidity.

### Per-asset trading sessions

The `/rhj/assets` response exposes per-asset trading capabilities for regular, extended, fractional, and 24/5 sessions. These capabilities vary by asset and can change. The monitor must ingest them as state, not hardcode a single market calendar.

### Weekends, halts, and corporate actions

- Stock Token balances remain transferable and onchain venues may remain open while the reference equity market or oracle feed is closed.
- `/prices/{symbol}` includes `isTradingHalt` and `generatedAt`.
- Corporate actions can schedule a future multiplier through `newUIMultiplier()` and `effectiveAt()` and emit `UIMultiplierUpdated`.
- A stale, paused, or closed-market reference is **not executable external liquidity**. Mark-to-oracle profit must never be presented as realizable profit without a valid exit venue.

## Strategy classes to investigate

These are **hypotheses**, not confirmed profit sources. Each must be tested net of fees, price impact, fill risk, inventory requirements, and latency.

### H1 — AMM-to-AMM cyclic arbitrage

Examples:

- `USDG -> Stock Token -> USDG` across two pools;
- triangular routes such as `USDG -> Stock A -> Stock B -> USDG`;
- crypto/stablecoin routes on public AMMs.

Research questions:

- Are there multiple independent pools for the same pair?
- Is pool depth sufficient after fees?
- Can the full route execute atomically in one EVM transaction?
- How quickly does FCFS competition remove the opportunity?

### H2 — RFQ versus AMM

Compare a firm signed RFQ with the executable output of an AMM route. This can be atomic only if the quote's settlement contract can be called within the same transaction and the quote remains valid for the caller, amount, and block/time conditions.

Do not compare indicative UI quotes. Store the complete signed quote, expiry, maker, taker restrictions, requested input, actual output, gas, and revert reason.

### H3 — Stock Token venue convergence

Compare executable Stock Token prices across Uniswap, Rialto/RFQ, Lighter spot, and any other verified venue. Normalize every price into token-equivalent USD using the current multiplier.

Potential edge: fragmented liquidity can reprice at different speeds. Main risk: venues may not be atomically composable, so the strategy becomes inventory-based market making rather than risk-free arbitrage.

### H4 — Onchain venue versus reference price

Compare executable AMM/RFQ/order-book prices with:

- the multiplier-adjusted Robinhood REST bid/ask;
- the Chainlink onchain feed;
- Chainlink Data Streams where access is available.

This is initially a **mispricing detector**, not an arbitrage claim. A reference price is not necessarily tradable, and ordinary users cannot directly mint/burn with the issuer.

### H5 — Session-boundary and closed-window dislocations

Measure spreads, depth, and reversion around:

- US regular-market open and close;
- extended/overnight transitions;
- start/end of the weekly mint/burn window;
- weekends and holidays;
- trading halts;
- oracle pauses and corporate actions.

The goal is to learn whether dislocations widen predictably and whether an accessible venue exists on both sides. Holding inventory through a closed reference market is directional risk, not atomic arbitrage.

### H6 — Lighter spot/perpetual basis

Measure spot-perpetual basis, funding, order-book depth, and cross-venue hedge cost. Because the Lighter domain has separate execution and liquidity, assume non-atomic execution until its APIs and settlement semantics prove otherwise.

### H7 — Morpho liquidation and oracle-lag opportunities

If live Morpho markets accept Stock Tokens or related assets as collateral, index:

- market parameters and LLTV;
- oracle source and freshness rules;
- borrower health factors;
- liquidation incentive;
- available collateral liquidity and hedge route.

This track only exists if relevant markets and meaningful borrow balances are verified onchain. An advertised integration is not proof of deployed, liquid markets.

### H8 — Corporate-action normalization failures

Search for venues, indexers, or contracts that temporarily use inconsistent multipliers around dividends or splits. Correct accounting requires:

```text
token_reference_price = raw_underlying_price * currentMultiplier
underlying_share_units = raw_token_amount * uiMultiplier / 1e18
```

This is an analytical hypothesis. Trading on a suspected discrepancy requires confirming the official event state, oracle freshness, venue behavior, and executable unwind.

## Why FCFS changes the design

On Robinhood Chain, bidding a larger priority fee cannot overtake an already-received transaction. For pure AMM backruns, likely advantages are therefore:

- seeing the relevant state change earlier;
- calculating the route faster;
- sending directly to the sequencer with lower network latency;
- maintaining prebuilt calldata, approvals, balances, and route state;
- identifying opportunities ignored by generic searchers.

This is partly an inference from the documented ordering model. The research must measure actual arrival-to-inclusion behavior and must not assume the public sequencer feed is a mempool containing future transactions. Arbitrum feeds normally distribute sequenced transaction data for low-latency following; they do not automatically grant privileged pre-order visibility.

For strategies based on market structure, corporate actions, or cross-domain inventory, raw latency may matter less than correct normalization, venue coverage, and inventory placement.

## Data acquisition plan

### Phase A — canonical registry

Build a versioned registry containing:

- active Stock Tokens from `/rhj/assets`;
- verified token contract address and chain ID;
- `currentMultiplier`, pending multiplier, and effective time;
- trading capabilities and asset status;
- Chainlink feed proxy, decimals, heartbeat, and latest update;
- verified venues, pools, fee tiers, routers, and settlement contracts;
- Lighter market identifiers;
- Morpho market identifiers and parameters;
- first and last observed block for every contract.

Never trust symbols as identifiers. Key assets by chain ID and contract address; also preserve Robinhood's stable asset `id` for cross-chain deduplication.

### Phase B — historical chain extraction

Use an archive RPC or indexed dataset to extract:

1. factory/pool creation events for verified DEX deployments;
2. swaps, liquidity changes, and transfers for relevant assets;
3. RFQ settlement fills where contracts and event ABIs are available;
4. Lighter deposits/withdrawals on Robinhood Chain plus API fills if obtainable;
5. Morpho market creation, supply, borrow, repay, and liquidation events;
6. Chainlink price updates and sequencer uptime events;
7. multiplier and corporate-action events;
8. gas used, L1 fee component, status, block, transaction index, and traces.

Suggested initial sample:

- all blocks from mainnet launch to the current tip if the dataset is still small;
- otherwise, 14 ordinary days plus windows around market open/close, weekends, halts, and corporate actions;
- extend only after event counts and data costs are known.

### Phase C — opportunity reconstruction

For every state transition:

1. reconstruct the pre-transaction state;
2. calculate executable quotes at several input sizes;
3. include all venue fees, gas, L1 data cost, slippage, and quote expiry;
4. simulate the complete atomic route where possible;
5. scan the same and following blocks for searcher transactions;
6. attribute visible profit from token balance deltas, not nominal quote difference;
7. separate atomic profit from inventory revaluation;
8. record competing transactions and whether the opportunity remained after delays of 0, 50, 100, 250, 500, and 1,000 ms where replay resolution permits.

### Phase D — searcher and concentration analysis

Cluster only on defensible evidence:

- repeated sender or executor contract;
- identical bytecode or calldata shape;
- common funding source, fee recipient, or settlement pattern;
- repeated route fingerprint.

Do not state that addresses share an owner unless ownership is proven. Report top-3/top-10 profit concentration, success rate, failed execution cost, route concentration, capital deployed, and dependence on outlier trades.

## Minimal read-only monitor MVP

### Objective

Determine whether Robinhood Chain produces recurring, executable opportunities before paying for low-latency infrastructure or deploying capital.

### Inputs

- WebSocket heads/logs from a production RPC;
- public sequencer feed, initially consumed directly or through a lightweight Nitro follower;
- canonical Stock Token registry and REST metadata;
- Chainlink feeds and sequencer-uptime feed;
- verified Uniswap pools and other public onchain liquidity;
- RFQ quotes only when official/public access is obtained;
- Lighter market data API;
- verified Morpho markets.

### Components

1. **Registry sync** — refresh assets, multipliers, trading capabilities, venues, ABIs, and oracle metadata.
2. **State ingestor** — subscribe to blocks/logs and maintain pool/order-book/reference-price state with timestamps from each source.
3. **Normalizer** — convert raw balances, multipliers, decimals, and prices to consistent token and USD units.
4. **Quote engine** — calculate executable AMM paths and ingest firm RFQ/order-book quotes.
5. **Opportunity detector** — evaluate H1–H8 and reject routes without a real exit.
6. **Simulator** — run `eth_call` or local EVM simulation against the exact state and estimate both L2 and L1-data fees.
7. **Recorder** — persist observations, opportunities, route snapshots, source latency, and realized subsequent outcomes.
8. **Reporter** — daily summary of opportunity count, lifetime, size, costs, venue coverage, false-positive reason, and theoretical net PnL.

### Recommended MVP scope

Start with:

- 10–20 liquid Stock Tokens selected by measured onchain activity, not brand recognition;
- USDG and ETH/WETH as settlement assets where pools exist;
- Uniswap plus one accessible second source (firm RFQ or Lighter spot);
- Chainlink and Robinhood REST references;
- no key management and no transaction submission.

Do **not** run a full node initially. Upgrade from provider WebSockets to a feed-connected node only if measurements show that data latency is the binding constraint.

### Observation schema

At minimum, persist:

```text
network, chain_id, observed_at_ns, source, source_sequence,
block_number, block_hash, tx_hash, venue, market, base_token, quote_token,
side, amount_in, amount_out, effective_price, venue_fee,
gas_estimate, l1_data_fee_estimate, reference_price, reference_timestamp,
multiplier, oracle_updated_at, oracle_paused, sequencer_up,
tokenization_window_open, trading_session, is_halted,
strategy_class, gross_edge_usd, estimated_net_usd,
atomic, executable, rejection_reason
```

### Acceptance criteria before an executor

Run continuously for at least 14 days and cover at least two weekends/session transitions. Proceed only if:

- prices and balance changes reconcile against explorer data;
- multiplier and raw/reference-price conversions pass fixtures;
- every reported opportunity has a reproducible route and timestamped source data;
- gas and L1-data fees are included;
- simulated calls succeed at the recorded block/state;
- results distinguish atomic opportunities from inventory-based spreads;
- positive net opportunities recur after realistic delay assumptions;
- no single outlier accounts for the entire result;
- venue access requirements and quote eligibility are documented.

If those conditions fail, the correct result is a documented rejection or narrower hypothesis—not an executor.

## Research outputs

The Robinhood Chain workstream should produce:

1. `registry-robinhood-chain.json` — canonical contracts, feeds, markets, ABIs, and provenance.
2. A reproducible extractor with block-range checkpoints.
3. Parquet/CSV event and opportunity datasets using the repository-wide schema.
4. A notebook or script reconstructing at least ten candidate opportunities end to end.
5. A 14-day paper-monitor report.
6. A scorecard comparing opportunity frequency, net value, lifetime, concentration, and implementation cost with Solana, Base, and Ethereum.
7. A go/no-go decision for a narrowly scoped executor.

## Material risks and failure modes

### Market and execution

- FCFS favors the lowest end-to-end latency; gas bidding does not compensate for slow arrival.
- Shallow pools can display large theoretical spreads that disappear at executable size.
- RFQ quotes may be indicative, restricted, expired, or unavailable to the proposed taker.
- Lighter's separate domain prevents assuming atomic cross-venue settlement.
- Non-atomic routes carry leg, inventory, funding, and withdrawal risk.
- Soft confirmations depend on the sequencer until data is posted to Ethereum.

### Data and accounting

- REST quotes are cached and may lag; their multiplier semantics differ from onchain feeds.
- Oracle feeds can be stale or paused, especially around corporate actions.
- `block.number` in contracts reflects an estimate of the Ethereum L1 block; use the Arbitrum L2 block number where needed.
- Stock Token symbol collisions are possible; use verified contract addresses.
- Dividends and splits alter `uiMultiplier()` without changing raw ERC-20 balances.
- A reference-price discrepancy is not profit unless a matching executable hedge or redemption exists.

### Infrastructure

- Public endpoints are rate-limited and unsuitable for production execution.
- Archive history, traces, and sequencer-feed retention may require separate providers or local storage.
- A self-hosted node is resource intensive and also depends on L1 execution/beacon access.
- Network, sequencer, protocol, contract, and API behavior can change; registries must be versioned.

### Protocol and counterparty

- Smart-contract, bridge, oracle, market-maker, stablecoin, and lending risks remain.
- The sequencer can exclude screened transactions.
- Primary-market mint/burn is permissioned and cannot be treated as a universally available arbitrage leg.
- Governance and validator arrangements are not equivalent to Ethereum L1 decentralization.

## Open questions to resolve first

1. Which exact Uniswap deployments and pool factories are live, and what is their real depth?
2. What are Rialto's public contracts, interfaces, quote eligibility, and historical fill events?
3. Can this project obtain firm RFQ quotes from 0x, 1inch, or LiFi without privileged market-maker relationships?
4. Which Stock Tokens and spot/perpetual markets are live on the Robinhood Chain Lighter domain?
5. Which Morpho markets are deployed and economically active?
6. What is the measured delay among sequencer feed, provider WebSocket, RPC state, and Blockscout?
7. Does the sequencer endpoint support any submission method materially faster than standard RPC for public users?
8. How do spreads and executable depth change around session and tokenization-window boundaries?
9. What fraction of apparent opportunities survives multiplier normalization and realistic fees?
10. Is profit concentrated in permissioned market makers or also visible to ordinary public addresses?

## Source quality and update policy

Contract addresses, feeds, markets, endpoints, and trading capabilities are mutable operational data. The monitor should obtain them from official registries or verified deployment events and record `source_url`, `retrieved_at`, and the block at which each value was verified.

Primary sources used for this brief:

- [Robinhood Chain documentation](https://docs.robinhood.com/chain/)
- [Network endpoints](https://docs.robinhood.com/chain/connecting/)
- [Stock Tokens](https://docs.robinhood.com/chain/stock-tokens/)
- [Building with Stock Tokens](https://docs.robinhood.com/chain/building-with-stock-tokens/)
- [Stock Token APIs](https://docs.robinhood.com/chain/stock-token-apis/)
- [Oracles and price feeds](https://docs.robinhood.com/chain/oracles-and-price-feeds/)
- [Chainlink Data Streams](https://docs.robinhood.com/chain/data-streams/)
- [Lighter domain](https://docs.robinhood.com/chain/lighter-domains/)
- [Full-node guide](https://docs.robinhood.com/chain/run-a-full-node/)
- [Protocol contracts](https://docs.robinhood.com/chain/protocol-contracts/)

Re-verify this document before implementing or funding an executor. The research date is intentionally prominent because Robinhood Chain and its ecosystem are new and can change quickly.

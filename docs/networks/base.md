# Base research dossier

Status date: **2026-09-25**. This document is a research plan, not evidence that any strategy is profitable. Network behavior must be re-verified before live use, especially around the planned Denim upgrade.

## Executive view

Base is an EVM rollup with a sequencer and sub-second transaction ordering. Today, Base uses Flashblocks: ten roughly 200 ms preconfirmation windows are built inside a normal two-second block. Transactions compete primarily by priority fee within each window, but arrival time also matters because ordering becomes locked when a Flashblock is committed. A later, higher-fee transaction cannot move into an earlier Flashblock.

This makes Base suitable for testing atomic DEX arbitrage, backruns, liquidations, and externally triggered DEX trades. It does **not** make any of them easy. A historical block shows the final ordering, but it does not fully reveal network arrival times or all failed/private attempts. Live measurement is therefore mandatory before drawing conclusions about latency advantage.

## Execution and ordering

### Current production model: Flashblocks

- Base's sequencer uses `base-builder` and runs priority-fee auctions approximately every 200 ms.
- Each Flashblock commits part of a two-second block. Once committed and broadcast, its ordering is locked.
- The builder accepts transactions continuously. Selection is fee-ordered at the moment of selection, so apparent fee inversions can occur when a high-fee transaction arrives after an earlier Flashblock has closed.
- Flashblock gas capacity grows cumulatively through the full block. Base documents that the per-transaction gas maximum is below the first Flashblock's capacity, so inclusion delay is normally driven by fee and arrival time rather than transaction size.
- Flashblocks-aware RPC endpoints expose `newHeads` about every 200 ms plus `newFlashblockTransactions`, `pendingLogs`, and `newFlashblocks`. The raw infrastructure stream is intended for node operators; applications should use a compatible RPC provider.

Primary references:

- [Base transaction ordering](https://docs.base.org/specifications/transactions/transaction-ordering)
- [Flashblocks reference](https://docs.base.org/specifications/flashblocks)
- [Flashblocks API overview](https://docs.base.org/base-chain/api-reference/flashblocks-api/flashblocks-api-overview)
- [Base RPC overview](https://docs.base.org/base-chain/api-reference/rpc-overview)
- [Run a Base node](https://docs.base.org/base-chain/node-operators/run-a-base-node)

### Planned model: Denim

Denim is planned to replace Flashblocks with **canonical 200 ms blocks**. Each interval will have its own block number, block hash, state root, receipts, fork-choice update, and unsafe/safe/finalized lifecycle. Flashblocks subscriptions and `pending` preconfirmation state will no longer have direct equivalents; applications will consume ordinary canonical block, log, and RPC streams at the faster cadence.

As of the status date:

- canonical 200 ms blocks are experimental on Vibenet;
- Base targets Sepolia and Mainnet for October 2026;
- exact activation timestamps and required client versions are not final.

Consequences for this project:

1. Keep the market-state engine independent of Flashblocks-specific message types.
2. Implement a `BaseHeadSource` interface with a Flashblocks adapter now and a canonical-200-ms adapter later.
3. Tag every observation with the active ordering regime; do not merge pre-Denim and post-Denim latency statistics.
4. Treat the announced schedule as planning information, not a production guarantee.

Primary references:

- [Denim: 200 ms native blocks](https://docs.base.org/upgrades/denim/200ms-blocks)
- [Migrate from Flashblocks](https://docs.base.org/upgrades/denim/migrate-from-flashblocks)
- [Base upgrades overview](https://docs.base.org/upgrades/overview)

## Initial protocol surface

Start from verified deployment registries rather than copied addresses. Pin every contract address and ABI to a dated manifest committed to the repository.

Suggested first set:

- Uniswap v3 and v4 pools;
- Balancer pools and routers;
- the largest additional Base AMMs after their official deployment manifests and ABIs are verified;
- Aave positions for liquidation research.

Official registries:

- [Uniswap v3 Base deployments](https://developers.uniswap.org/docs/protocols/v3/deployments/v3-base-deployments)
- [Uniswap v4 deployments](https://developers.uniswap.org/docs/protocols/v4/deployments)
- [Balancer Base deployment addresses](https://docs.balancer.fi/developer-reference/contracts/deployment-addresses/base.html)
- [Aave developer documentation](https://aave.com/docs)

## Strategy classes to test

### 1. Atomic DEX-to-DEX arbitrage

Execute two or more swaps in one transaction and revert unless the ending balance exceeds the starting balance plus all modeled costs. Candidate routes include same-pair price differences, stablecoin loops, and three-token cycles.

Research questions:

- Is the quoted edge still positive at executable size after pool fees and price impact?
- How often is the route still profitable at the next 200 ms state update?
- How concentrated are wins among sender or executor-contract clusters?
- Does a route require temporary inventory or can it use a flash-liquidity source?

### 2. Backrun of state-changing transactions

A large swap or another protocol action can move one pool away from related venues. The research bot should detect the resulting state, compute a price-restoring trade, and submit only an atomic transaction with a strict minimum final balance.

Base's public documentation describes fee-and-arrival ordering, not an Ethereum-style Flashbots bundle guarantee for this workflow. Do not assume private atomic bundles or exact adjacency unless a supported production interface is independently confirmed.

### 3. Liquidations

Monitor lending positions, oracle updates, interest accrual, and protocol parameter changes. A liquidation candidate is only viable when the liquidation bonus minus swap slippage, gas, financing, and failed-attempt cost remains positive. Aave documents liquidations as permissionless and highly competitive; health factor below one is the eligibility trigger in its current public explanation.

Reference: [Aave health factor and liquidations](https://aave.com/help/borrowing/liquidations).

### 4. CEX-to-DEX / DEX-to-CEX dislocations

Compare executable onchain prices with authenticated exchange order books. This is not atomic across venues. It requires prefunded inventory on both sides, order-book depth modeling, exchange API timestamping, transfer/withdrawal status monitoring, and explicit inventory limits.

Historical onchain data alone cannot prove this strategy's realizable PnL. The study must retain contemporaneous offchain order-book snapshots and distinguish:

- theoretical midpoint spread;
- executable spread at size;
- hedge fill and latency;
- inventory mark-to-market;
- deposits, withdrawals, and rebalancing cost.

## Data sources

### Historical

- An archive-capable Base RPC for blocks, transactions, receipts, logs, historical `eth_call`, and traces.
- Official protocol ABIs and deployment manifests, versioned by block range.
- Token metadata obtained from contracts, with explicit handling for proxies, rebasing, fee-on-transfer behavior, and non-standard decimals.
- External prices only for reporting or inventory valuation, never as a substitute for reconstructing actual swap amounts.

Base exposes Ethereum-compatible JSON-RPC methods; use the canonical [Ethereum JSON-RPC specification](https://ethereum.org/developers/docs/apis/json-rpc/) plus the [Base API reference](https://docs.base.org/base-chain/api-reference/rpc-overview). For trace semantics, document the chosen client and version because debug APIs are client-specific.

### Live

- Two independent Flashblocks-aware WebSocket providers, timestamped at receipt with a monotonic local clock.
- Optional self-hosted Base node to compare provider lag and capture the upstream stream under Base's node-operator guidance.
- Ordinary RPC endpoints for state checks, receipts, and transaction submission.
- Authenticated CEX market-data streams only when evaluating cross-venue strategies.

Never commit RPC keys, exchange credentials, wallet keys, or raw signed transactions.

## Historical research method

1. **Freeze a manifest.** Record chain ID, date, block interval, protocol versions, pool factories, routers, lending contracts, token metadata, and pricing sources.
2. **Use stratified windows.** Analyze at least 14 ordinary days plus separately labeled volatility/event windows. Do not select only known profitable blocks.
3. **Collect canonical evidence.** Store block headers, full transaction order, receipts, logs, gas fields, traces, and contract bytecode hashes. Preserve raw responses or content hashes so results are reproducible.
4. **Decode state changes.** Convert swaps, transfers, liquidations, flash loans, direct ETH movements, and internal calls into a normalized event schema.
5. **Cluster conservatively.** Link senders and executor contracts only using explicit transaction relationships. Keep `actor_cluster_confidence`; do not assume all funding addresses have one owner.
6. **Calculate realized PnL.** Use net token balance changes for the controlled cluster, subtract L2 execution cost and any visible direct payments, and separate realized stablecoin/ETH profit from residual inventory.
7. **Reconstruct the opportunity.** Replay the pre-transaction state, quote the observed route at the observed size, and compare it with the executed result. For candidate routes not taken, label the result counterfactual.
8. **Test latency sensitivity.** Replay against the state after 200, 400, 600, 1,000, and 2,000 ms where live captures exist. Canonical historical data cannot recover exact arrival latency, so do not fabricate it.
9. **Account for failures.** Onchain reverted attempts are visible; dropped, private, and never-included attempts may not be. Report visible failure cost and the observability gap separately.
10. **Validate samples manually.** For every classifier version, manually inspect random positives, random negatives, the largest PnL observations, and apparent anomalies.

### Denim boundary

Store `ordering_regime = flashblocks | denim_200ms`. After activation, start a fresh baseline. Metrics based on a two-second canonical block are not directly comparable with metrics based on five canonical blocks per second.

## Required metrics

| Metric | Definition |
|---|---|
| Observed opportunities/day | Candidates profitable under the stated state snapshot and cost assumptions |
| Executed wins/day | Included transactions with positive realized PnL |
| Net PnL distribution | Median, P90, P99, maximum, and total after visible variable costs |
| Tail concentration | Share of total PnL from the largest 1, 5, and 10 events |
| Winner concentration | Share captured by top 3 and top 10 conservative actor clusters |
| Inclusion position | Flashblock index and transaction index; canonical block index after Denim |
| Time-to-observe | Provider receive time minus first receive time across controlled feeds |
| Opportunity decay | PnL at successive observed state updates, not invented millisecond estimates |
| Revert cost | Gas and other visible cost of reverted included attempts |
| Capital efficiency | Net realized PnL divided by peak capital actually at risk |
| Inventory exposure | Maximum unhedged token value and duration |
| Data completeness | Missing blocks, traces, logs, or offchain snapshots by interval |

Always publish both regular-return statistics and tail-event statistics. A single extreme event must not be presented as stable daily income.

## Principal risks and invalid assumptions

- **Sequencer and provider dependence:** the first state observed by our RPC may not be the first state observed by a competitor.
- **Ordering-regime change:** Denim will invalidate Flashblocks-specific ingestion and alter time-series interpretation.
- **Hidden competition:** private submissions and dropped attempts are not fully visible in canonical data.
- **Simulation mismatch:** incorrect block context, fee model, token behavior, hooks, or state overrides can create fictitious profit.
- **Reorg/finality:** preconfirmed or unsafe state is not equivalent to finalized state.
- **Smart-contract risk:** approvals, callbacks, hooks, reentrancy, unexpected token behavior, and upgradeable contracts require explicit defenses.
- **Fee undercounting:** total cost can include execution, L1 data-related charges, operator fees, direct payments, CEX fees, and rebalancing.
- **Adverse inventory:** CEX-DEX execution is non-atomic and can leave one side unhedged.
- **Selection bias:** starting from famous winning transactions overstates expected returns.

## Minimum research MVP

The first Base deliverable is a **paper system**, not an executor with capital:

1. Versioned manifest for Uniswap v3/v4, Balancer, and one lending market.
2. Historical collector for blocks, receipts, logs, traces, and bytecode hashes.
3. Decoders for swaps, transfers, and liquidations.
4. Exact pool math for a small whitelist of pools and atomic two-leg route replay.
5. Live dual-provider Flashblocks capture with local timestamps and feed-lag comparison.
6. Opportunity journal containing snapshot ID, route, size, gross edge, modeled costs, decay, and eventual winner.
7. Dashboard or report for the metrics above.
8. No transaction submission until replay tests agree with actual historical outcomes and at least 7–14 days of live paper monitoring are complete.

### Go/no-go gate for a tiny live test

Proceed only if the same implementation can reproduce multiple independent real transactions, live paper observations survive realistic delay and costs, data loss is measured, and the expected downside is bounded by hard transaction and daily limits. Passing this gate justifies an experiment; it does not imply expected profit.

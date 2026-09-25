# Ethereum research dossier

Status date: **2026-09-25**. This document defines a reproducible investigation, not an earnings claim. Ethereum's mature MEV market is highly competitive, and public-chain evidence is incomplete because substantial order flow is private.

## Executive view

Ethereum differs from a simple public-mempool latency race. Searchers compete through public transaction propagation, private order flow, block builders, relays, and proposer-builder separation. Flashbots Auction lets searchers submit ordered bundles privately to builders; MEV-Share exposes selected hints from private user transactions and currently accepts backruns.

For this project, the most credible research targets are:

- exact, atomic multi-DEX arbitrage;
- MEV-Share backruns;
- lending liquidations;
- event-driven or protocol-specific opportunities;
- CEX-DEX dislocations with explicit inventory and hedge risk.

Known, generic DEX arbitrage and liquidation strategies are mature and competitive. Ethereum.org explicitly warns that these common categories are unlikely to be profitable for new searchers and points toward a longer tail of less-obvious opportunities. That is a reason to measure carefully, not a reason to assume the long tail is profitable.

## Execution, ordering, and private flow

Ethereum validators propose canonical blocks, while specialized builders can construct execution payloads under proposer-builder separation. Searchers observe public or selectively disclosed order flow, simulate strategies, and send bids/bundles to builders. Builders optimize blocks from public transactions, private transactions, and searcher bundles, then compete to have their payload selected.

Important consequences:

- Final onchain ordering does not reveal when each participant first saw the opportunity.
- Public mempool capture is incomplete because transactions can be submitted privately.
- The visible priority fee is not necessarily the full inclusion payment; bundles can include direct conditional payments to the fee recipient.
- Builder coverage matters. A valid bundle sent to one builder may miss a slot won by another builder.
- A reverted public transaction pays gas when included. Flashbots describes sealed-bid bundles as avoiding payment for bids that are not included, but bundle design and allowed reverts still require careful simulation.

Primary references:

- [Ethereum.org: maximal extractable value](https://ethereum.org/developers/docs/mev/)
- [Flashbots Auction overview](https://docs.flashbots.net/flashbots-auction/overview)
- [Flashbots JSON-RPC endpoints](https://docs.flashbots.net/flashbots-auction/advanced/rpc-endpoint)
- [Ethereum proof of stake](https://ethereum.org/developers/docs/consensus-mechanisms/pos/)

## Flashbots and MEV-Share

### Flashbots Auction

`eth_sendBundle` submits an ordered array of signed transactions for a target block, with optional timestamp constraints, allowed reverts, replacement identity, and builder routing. `eth_callBundle`/simulation methods should be used with an explicit state block and target block context. Searchers authenticate relay requests with a separate signing key; this key should not hold trading funds.

The research implementation must track:

- target block and state block;
- builders selected;
- simulated gas, coinbase difference, and direct payment;
- submission time and response;
- inclusion outcome and realized token deltas;
- replacement/cancellation history.

### MEV-Share

MEV-Share is an order-flow auction. Users or applications submit private transactions and select which hints are disclosed, such as contract address, function selector, calldata, logs, or hash. Searchers construct partial bundles around the disclosed transaction. The MEV-Share node simulates candidates and forwards successful bundles with refund rules.

As documented on the status date:

- MEV-Share currently accepts backruns;
- `mev_sendBundle` is the submission method;
- a bundle is limited to one backrun transaction under the current documented format;
- `mev_simBundle` supports simulation against explicit block context;
- privacy hints determine what the searcher can reconstruct, so a strategy must tolerate incomplete information.

Primary references:

- [MEV-Share introduction](https://docs.flashbots.net/flashbots-mev-share/introduction)
- [MEV-Share searcher guide](https://docs.flashbots.net/flashbots-mev-share/searchers/getting-started)
- [Flashbots RPC: `mev_sendBundle` and `mev_simBundle`](https://docs.flashbots.net/flashbots-auction/advanced/rpc-endpoint)

## Initial protocol surface

Use official deployment registries and pin addresses, ABIs, and bytecode hashes by block range. A practical first set is:

- Uniswap v2/v3/v4 pools;
- Balancer Vault/pools;
- one Curve pool family only after its official registries and pool math are integrated;
- Aave positions for liquidation research.

References:

- [Uniswap protocol deployments](https://developers.uniswap.org/docs/protocols/deployments)
- [Uniswap v4 deployments](https://developers.uniswap.org/docs/protocols/v4/deployments)
- [Balancer Mainnet deployment addresses](https://docs.balancer.fi/developer-reference/contracts/deployment-addresses/mainnet.html)
- [Aave developer documentation](https://aave.com/docs)

Do not begin with every DEX. Correct handling of a small set of pool types is more valuable than wide but inaccurate route coverage.

## Strategy classes to test

### 1. Atomic multi-DEX arbitrage

Combine all swaps and repayment in one executor transaction or bundle and revert unless the final asset balance satisfies a minimum-profit invariant. Candidate paths include two-venue same-pair trades, stablecoin loops, three-token cycles, and routes involving flash liquidity.

The model must include:

- pool fees and exact integer rounding;
- price impact at size;
- gas used under the actual route;
- EIP-1559 base fee and priority component;
- direct builder/fee-recipient payments;
- flash-loan fees;
- residual token balances and approvals.

### 2. Backruns

Backruns restore price consistency after a user's swap or another state-changing transaction. MEV-Share is the preferred initial research surface because it offers an explicit, documented backrun flow and simulation API without relying only on public-mempool racing.

Measure gross arbitrage separately from:

- user refund;
- builder/proposer payment;
- gas and financing;
- searcher residual.

The final searcher residual, not the pre-bid opportunity, is the relevant result.

### 3. Liquidations

Monitor borrower state, oracle updates, accrued interest, asset prices, reserve configuration, and protocol events. Aave describes liquidation as permissionless once health factor is below one and notes that the field is highly competitive.

A liquidation simulator must model debt repaid, collateral received, liquidation bonus, flash liquidity, collateral-sale slippage, gas, builder bid, and partial/full liquidation rules current for the exact protocol version.

Reference: [Aave health factor and liquidations](https://aave.com/help/borrowing/liquidations).

### 4. CEX-to-DEX / DEX-to-CEX arbitrage

This is a cross-system market-making problem, not a purely atomic MEV transaction. The bot must hold inventory on both venues or accept transfer latency. Required evidence includes authenticated order-book updates, actual fill acknowledgements, onchain execution, venue fees, withdrawal/deposit availability, and rebalancing cost.

Key risks:

- one leg fills and the other fails;
- order-book data arrives late or differs from executable liquidity;
- withdrawals are paused or delayed;
- inventory moves against the strategy before rebalancing;
- API rate limits, account limits, or venue downtime break hedging.

Report inventory PnL and spread-capture PnL separately.

### 5. Protocol-specific and event-driven opportunities

Examples include unusual pool hooks, migrations, oracle update timing, peg mechanisms, auctions, redemptions, and newly deployed protocol interactions. These require contract-specific reasoning and often offer fewer observations. They should be researched only from public interfaces and normal protocol behavior; vulnerabilities or unintended fund extraction are outside this repository's scope.

## Data sources

### Canonical chain data

- Execution JSON-RPC for blocks, full transactions, receipts, and logs.
- Archive state for historical `eth_call` and deterministic replay.
- Client-specific traces such as Geth `debug_traceTransaction`, with client/version recorded.
- Consensus/beacon data when proposer, slot, or payload attribution is required.
- Official ABIs, source code, deployment manifests, and protocol parameter history.

Primary references:

- [Ethereum JSON-RPC API](https://ethereum.org/developers/docs/apis/json-rpc/)
- [Geth debug namespace](https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-debug)
- [Geth built-in tracers](https://geth.ethereum.org/docs/developers/evm-tracing/built-in-tracers)

### Live order-flow data

- A self-hosted execution node or multiple independent pending-transaction WebSocket feeds for the public mempool.
- MEV-Share event stream and hint payloads under the documented searcher interface.
- Flashbots relay responses and bundle simulation outputs.
- Builder/relay attribution data from official or open infrastructure, with source and coverage recorded.
- Authenticated CEX WebSocket feeds only for cross-venue research.

Never commit API secrets, wallet keys, exchange credentials, raw signed trading transactions, or full private order-flow payloads that are not intended for redistribution.

## Historical research method

1. **Freeze the scope.** Record UTC dates, block ranges, client/provider, protocol deployments, bytecode hashes, token metadata, oracle sources, and price conventions.
2. **Use representative samples.** Analyze at least 14 ordinary days and separately labeled stress/event windows. Pre-register event selection rules where possible.
3. **Collect raw canonical evidence.** Store headers, complete transaction order, receipts, logs, traces, base fee, gas used, effective gas price, fee recipient, and relevant internal ETH transfers.
4. **Decode economic actions.** Normalize swaps, transfers, flash loans, liquidations, refunds, direct builder payments, and token balance changes.
5. **Classify conservatively.** Label strategies from call structure and asset flows; retain classifier version and confidence. Avoid assigning ownership based only on funding proximity.
6. **Calculate realized PnL.** Compute net asset deltas across the conservatively defined actor cluster. Subtract gas, direct payments, financing, and user refunds. Mark residual inventory at an explicitly named conservative price.
7. **Reconstruct pre-state.** Replay at the parent state and reproduce the observed transaction. Compare computed outputs with actual receipts and traces before using the simulator for counterfactual routes.
8. **Model the auction.** Separate opportunity value, searcher retained value, builder/proposer payment, and user refund. Visible gas alone is not the searcher's full economic cost.
9. **Capture observability limits.** Canonical blocks omit non-included bundles and much private order flow. Historical estimates are lower bounds on competition and failure attempts.
10. **Validate manually.** Review random classified and unclassified transactions, the largest PnL cases, and all apparent negative-cost or impossible-profit observations.

### Counterfactual and latency analysis

Historical replay may answer, “Would this transaction have succeeded against this state?” It cannot answer, “Would our server have seen and won it?” without contemporaneous capture.

For live paper monitoring, record:

- first seen time on each public feed;
- first MEV-Share hint time;
- state/head used for simulation;
- simulation completion time;
- bundle submission time per builder;
- target block, inclusion outcome, and winning transaction position;
- opportunity value after 50, 100, 250, 500, 1,000, and 2,000 ms where the captured state permits it.

Do not infer millisecond arrival time from transaction index.

## Required metrics

| Metric | Definition |
|---|---|
| Candidates/day | Opportunities positive under the documented snapshot and full cost model |
| Included wins/day | Included actions with positive realized PnL |
| Net PnL distribution | Median, P90, P99, maximum, total, and confidence/coverage |
| Tail concentration | Share of PnL from the top 1, 5, and 10 events |
| Actor concentration | Share captured by top 3/top 10 conservative clusters |
| Searcher retention | Realized searcher PnL divided by pre-bid opportunity value |
| Bid intensity | Gas tip plus visible direct payment and refund as share of opportunity value |
| Inclusion rate | Included submissions divided by valid submissions, by builder and strategy |
| Simulation accuracy | Difference between simulated and realized asset/gas deltas |
| Opportunity decay | Value at successive captured states after first observation |
| Visible failure cost | Included reverted gas plus other observable failed execution cost |
| Inventory exposure | Peak unhedged value and time for non-atomic strategies |
| Data completeness | Missing blocks, traces, mempool intervals, hints, or CEX snapshots |

Publish regular-return and tail-event statistics separately. Never annualize a short, selectively sampled window without a clearly labeled sensitivity analysis.

## Principal risks and invalid assumptions

- **Private-order-flow blind spot:** public mempool data does not represent the full opportunity set or competition.
- **Builder/relay coverage:** submission to one endpoint does not guarantee access to the winning builder for a slot.
- **Bid leakage and trust:** builders and relays see private payloads; Flashbots itself advises evaluating builder behavior and relay connectivity.
- **Simulation divergence:** wrong parent state, timestamp, base fee, fee recipient, revert policy, or protocol version can invalidate a result.
- **False actor clustering:** executor, funder, beneficiary, and bundle signer may be different entities.
- **Token/accounting traps:** rebasing, fee-on-transfer, ERC-777 callbacks, unusual decimals, wrappers, and proxy upgrades can corrupt PnL.
- **Gas and payment undercounting:** effective gas cost is only one component of competitive inclusion cost.
- **CEX execution risk:** cross-venue paths are non-atomic and expose inventory and counterparty/operational risk.
- **Smart-contract risk:** the executor holds approvals and may interact with adversarial contracts; whitelists, balance assertions, and reentrancy protection are required.
- **Selection and survivorship bias:** starting from successful searchers omits failed operators and sunk infrastructure cost.

## Minimum research MVP

The first Ethereum deliverable should avoid live capital:

1. Versioned manifest for Uniswap v3/v4, Balancer, and one Aave market.
2. Historical collector for blocks, receipts, logs, traces, fee-recipient payments, and deployment bytecode hashes.
3. Normalized decoders for swaps, transfers, flash loans, and liquidations.
4. Exact two-leg and one three-leg route simulator with property tests and historical replay fixtures.
5. PnL accounting that separates opportunity value, gas, builder payment, refund, residual inventory, and retained searcher value.
6. Live public-mempool collector plus MEV-Share hint listener, both with monotonic receive timestamps.
7. Paper backrun builder using `mev_simBundle`; no signing with a funded key.
8. Seven to fourteen days of live paper monitoring before any tiny live test.

### Go/no-go gate for a tiny live test

Advance only when:

- several independent historical transactions reproduce exactly within stated tolerances;
- live opportunities remain positive after realistic auction, refund, gas, and latency assumptions;
- simulation error and missing-data rates are measured;
- the strategy does not depend on an unverified private interface;
- contract calls are whitelisted and protected by minimum-return assertions;
- per-transaction, per-hour, and per-day loss limits are enforced.

Passing the gate means the hypothesis is testable with bounded capital. It does not establish stable or expected profit.

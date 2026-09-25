# Base network screening — 2026-09-25

## Short conclusion

**Provisional decision: GO for a bounded historical screen; HOLD for a live execution MVP.**

Base is unusually researchable for a small team. It has standard EVM receipts and traces, public Dune tables for transactions/logs/traces/DEX trades, official deployment registries for several programmable AMMs, and a live preconfirmation interface that exposes sequencer-ordered state about every 200 ms. Published research also confirms that cyclic-arbitrage contracts and speculative on-chain pool probing were material on Base.

The strongest public empirical result is not current enough to establish 2026 economics. The optimistic-MEV study observed August 2023–May 2025; Base launched Flashblocks on mainnet on 2025-07-16. Its Base findings therefore describe the earlier two-second ordering regime, not today's 200-ms Flashblock auctions. Denim is intended to replace Flashblocks with canonical 200-ms blocks, with Base documentation targeting October 2026 but explicitly leaving exact activation details undecided. Base is therefore a good candidate for a **regime-aware historical study**, but a poor candidate for immediate optimization around one soon-changing ingestion interface.

The cheapest credible entry is to reproduce the published optimistic-MEV classifier on a small post-Flashblocks sample, validate several transactions against traces, and measure opportunity decay between observed Flashblocks. Do not start by operating a node, spamming probes, deploying capital, or assuming an Ethereum-style private bundle/adjacency guarantee.

This screen establishes testability and a falsifiable next experiment. It does not establish accessible profit, current opportunity frequency, or a competitive landing rate.

## Scope and evidence status

- Network: Base mainnet, chain ID `8453`.
- Status date: 2026-09-25.
- Strategy classes: atomic DEX cycles, optimistic on-chain probing, state-change backruns, lending liquidations, and non-atomic cross-rollup/CEX–DEX arbitrage.
- Evidence used: Base and protocol documentation retrieved on the status date; Dune data-catalog documentation; empirical papers with explicit observation windows.
- Not performed: original chain scan, fresh PnL reconstruction, provider-latency measurement, transaction submission, wallet clustering, or contract deployment.

Labels used below:

- **Confirmed fact** — directly supported by primary documentation or a cited empirical study for its declared sample.
- **Derived result** — arithmetic or comparison derived from cited inputs; the method is stated.
- **Inference** — interpretation for this project.
- **Hypothesis** — falsifiable proposition requiring our own data.
- **Recommendation** — proposed next action.

## 1. Ordering and execution regime

### 1.1 Current production: Flashblocks

**Confirmed facts**

1. Base currently documents block construction through `base-builder`, with a priority-fee auction approximately every 200 ms.
2. Ten incremental Flashblocks form a normal two-second Base block. Once a Flashblock is built and broadcast, its ordering is locked; a later high-priority-fee transaction cannot move into an earlier Flashblock.
3. The builder continuously accepts transactions and fee-orders the available set at selection time. Ordering is therefore a hybrid of arrival timing and priority fee, not one global two-second priority-gas auction.
4. The sequencer path uses a private mempool. The Base engineering description routes submitted transactions through `proxyd` to that private mempool and then to execution-layer builders.
5. Flashblocks-aware RPC can expose `pending` state, `newFlashblockTransactions`, `pendingLogs`, and full `newFlashblocks` payloads. The public Base endpoints are HTTP-only; WebSocket subscriptions require a compatible provider or a node.
6. `eth_simulateV1` can simulate multiple calls against current preconfirmed state. The official API reviewed here documents normal `eth_sendRawTransaction`; it does not document an Ethereum/Flashbots-style production bundle-submission method that guarantees trigger-plus-backrun adjacency.

**Inferences**

- A Base searcher competes on both observation/submission latency and priority fee. Seeing a transaction in a published Flashblock is seeing already ordered state, not a public pending transaction that can necessarily be placed immediately behind its trigger.
- Historical canonical blocks reveal final transaction order but not each transaction's arrival time, all private-mempool candidates, dropped attempts, or provider lag.
- An atomic multi-swap arbitrage inside one transaction is straightforward EVM engineering. A guaranteed backrun of another party's transaction is a different capability and must not be assumed from Flashblocks subscriptions or `eth_simulateV1`.

### 1.2 Planned production: Denim

**Confirmed facts as documented on 2026-09-25**

1. Denim's 200-ms native blocks are experimental on Vibenet and are not active on Base Sepolia or Base Mainnet.
2. Base targets Sepolia and mainnet for October 2026, while exact activation timestamps and required client versions remain undecided.
3. Denim replaces incremental Flashblocks with five complete canonical blocks per second. Each block has its own number, hash, state root, receipts, fork-choice update, and unsafe/safe/finalized lifecycle.
4. Flashblocks subscriptions and `pending` preconfirmation state are removed. Consumers migrate to ordinary canonical `newHeads`, logs, blocks, and state.
5. Base's normal seconds-based header timestamp remains; planned `timestampMs`/BaseTime metadata represents the sub-second component.

**Recommendation**

Every Base record must carry:

```text
ordering_regime = legacy_2s | flashblocks | denim_200ms
```

The collector should expose a regime-neutral head/state interface. Flashblocks and Denim results must not be silently pooled: they differ in canonical block numbering, state references, observable failure boundaries, and usable latency checkpoints.

## 2. Verified venue surface

The table lists venues whose Base deployments are supported by primary protocol documentation or repositories. It is an implementation inventory, **not a volume or profitability ranking**. Before collection, pin contract addresses, bytecode hashes, ABI versions, factory events, and active/deprecated status to a dated manifest.

| Venue | Confirmed Base surface | Initial research use | Important caveat |
| --- | --- | --- | --- |
| Uniswap | Official v3 Base deployment registry; unified registry also covers current deployments | Concentrated-liquidity quoting, two-venue cycles, trace fixtures | v3/v4 and hook behavior require separate decoders and exact integer math |
| Aerodrome | Official contracts repository publishes Base pool factory/router deployments and constant-product-style pool implementation; separate concentrated-liquidity deployments must be independently pinned | Base-native pool family, same-pair and triangular routes | Do not treat every Solidly-compatible pool as identical; fee and factory generations matter |
| PancakeSwap | Official documentation says v2, v3, and Infinity liquidity is live/routable on Base; official router registry lists Base routers | Multiple AMM generations and hook/bin-based pools | Infinity CLAMM/LBAMM/hooks require distinct state and fee models |
| Balancer | Official Base deployment page lists active core contracts, routers, pool factories, hooks, and deprecated contracts | Weighted/stable/custom pool routes and batch-router interactions | Registry is mutable; preserve active/deprecated status by block range |
| Aave v3 | Official Aave address book contains a Base v3 market and pool/oracle contracts | Liquidation classification and event-driven study | Eligibility and economics depend on reserve parameters and oracle state at the exact block |
| Morpho | Official API/docs support Base (`8453`) markets and positions | Alternative liquidation/market-state research | Market-specific oracle, loan, collateral, LLTV, and gate parameters must be reconstructed |

### Minimum DEX manifest for the first screen

Start with only:

1. Uniswap v3 factory and pools;
2. Aerodrome constant-product pools;
3. PancakeSwap v3 pools;
4. one explicitly selected concentrated-liquidity family after its deployment is pinned.

Balancer, Uniswap v4, PancakeSwap Infinity, and additional hook-based venues should enter only after the basic classifier reconciles. Broad venue coverage would increase decoder risk before it improves evidence quality.

## 3. Publicly confirmed MEV and arbitrage patterns

### 3.1 Optimistic cyclic arbitrage — strong historical evidence, current status unknown

**Confirmed facts for the cited study window**

The AFT 2025 paper *Optimistic MEV in Ethereum Layer 2s* analyzed Base, Optimism, Arbitrum, and Ethereum from August 2023 to May 2025. It defines optimistic MEV as speculative transactions that determine opportunity existence and trade parameters during execution, often by reading pool state on-chain and terminating without swaps when no profitable route exists.

For Base, the paper reports:

- only **6.3%** of DEX-interacting transactions sent to identified cyclic-arbitrage contracts executed a trade in the broad comparison;
- cyclic-arbitrage contracts consumed **51% of Base gas in Q1 2025**, with interaction/probing transactions contributing 48%;
- those contracts accounted for **23% of transaction fees** despite consuming more than half the gas;
- among the study's top Base bot contracts, only **0.58%** of calls executed an arbitrage, while the EVM revert rate was about **0.005%**; most losing probes returned successfully without swapping;
- the top ten Base contracts by bot-gas usage accounted cumulatively for only **24.56%** of gas attributed to the identified MEV-bot set, so gas usage in that sample was not dominated by just one or two contracts;
- a case-study contract `0xF5fF765b0c1278E54281193d7019281e0e50A8C0` repeatedly inspected pools at runtime. Transaction `0x1d977d6867e2868b518a10803d64b414e428bd8e639d3c5054b2529cb55d18cb` performed no swap, while `0xb67825a6fa60e4bd9892076ead93c41f631460a53b8219036a5ace051f139bd7` executed a two-swap `WETH → TYBG → WETH` cycle according to the paper.

These addresses and hashes are included as **paper-reported reproducibility fixtures**. This sprint did not independently fetch and checksum their receipts/traces.

**Derived result — regime mismatch**

The study ends in May 2025. Base states that Flashblocks launched on mainnet on 2025-07-16. Therefore the published Base sample ends before the current production ordering regime began. Its prevalence and success-rate figures cannot be treated as current measurements.

**Hypothesis BASE-A**

Optimistic cyclic-arbitrage probing remains detectable after Flashblocks, but its submission cadence, trade rate, fee strategy, and value capture changed materially under 200-ms locked ordering windows.

### 3.2 Atomic DEX-to-DEX cycles

**Confirmed fact**

Cyclic arbitrage can execute multiple swaps atomically in one EVM transaction, and the optimistic-MEV study identifies actual Base cycles from reconstructed swap paths and token balances.

**Inference**

The route mechanism is proven, but accessibility is not. Standard pool math and public factories lower implementation difficulty; the published volume of speculative bot traffic shows intense competition rather than available profit.

**Hypothesis BASE-B**

A narrow whitelist of pools with exact off-chain state tracking can outperform generic blind probing on fully loaded PnL by avoiding the very large number of no-trade calls, even if it detects fewer theoretical opportunities.

### 3.3 State-change backruns

**Confirmed fact**

The Flashblocks stream exposes sequencer-ordered transactions and logs after each sub-block is built. It therefore permits detection and quoting against the resulting preconfirmed state before the enclosing two-second block seals.

**Inference**

A later Flashblock may contain a price-restoring trade after a large earlier swap, but the official interfaces reviewed do not provide a documented adjacency guarantee. This is better described as **post-state arbitrage across Flashblocks** than an Ethereum-style bundle backrun.

**Hypothesis BASE-C**

Some dislocations created in Flashblock `i` remain profitable after conservative costs in Flashblock `i+1` or later, without requiring access to the private mempool before `i` is published.

### 3.4 Liquidations

**Confirmed facts**

Aave and Morpho expose Base markets and on-chain position state. Permissionless liquidation is possible when protocol-specific eligibility conditions are satisfied. Exact profitability requires the contemporaneous oracle value, debt/collateral state, liquidation incentive, gas, financing, and collateral-exit route.

**Inference**

Liquidations are historically reproducible, but monitoring eligibility is not an execution edge. Sequencer arrival/fee competition, oracle timing, and routing still matter. This is a secondary research track, not the first Base MVP.

### 3.5 Cross-rollup and CEX–DEX arbitrage

**Confirmed facts for cited historical samples**

- A 2024 cross-rollup study estimated more than 500,000 unexplored non-atomic opportunities and estimated opportunity value of 0.03%–0.05% of trading volume across Arbitrum, Base, and Optimism in its methodology. It found average persistence of 10–20 blocks.
- A later one-year cross-chain study identified 242,535 executed arbitrages across nine chains, found 66.96% used pre-positioned inventory, and reported high actor concentration. These are cross-chain aggregate findings, not Base-only current profitability estimates.

**Limitations**

- “Potential opportunity” is not an executed fill or net PnL.
- Legacy block persistence is not comparable across two-second Base blocks, 200-ms Flashblocks, and Denim's 200-ms canonical blocks.
- CEX fills, fees, rebates, hedge failures, inventory transfer, and account constraints are not visible in Base chain history.

**Recommendation**

Keep non-atomic activity in the classifier so it is not mistaken for atomic DEX arbitrage. Do not select it for the first executor without contemporaneous off-chain order-book and fill data.

## 4. Historical and live data availability

### 4.1 Historical

| Data need | Available path | Confirmed limitation | Screen result |
| --- | --- | --- | --- |
| Blocks, transactions, receipts, logs | EVM JSON-RPC; Dune `base.transactions` and `base.logs` | Public Base RPC is rate-limited; provider retention varies | Good for bounded research |
| Internal calls/traces | Provider `debug_trace*`; Dune `base.traces` | Debug method availability/rate limits are provider-specific; trace semantics depend on client/version | Feasible; pin source/version |
| DEX swap classification | Dune `dex.trades` on Base plus official ABIs | Curated coverage/labels can lag or omit custom pools | Good bootstrap, not sole truth |
| Historical contract calls/decoded events | Dune decoded tables and protocol manifests | ABI/proxy/version history must be validated | Feasible with manifest |
| Historical pre-state | Archive-capable RPC or deterministic replay from a known earlier state | Ordinary receipts/logs do not provide arbitrary historical storage | Likely paid for exact replay |
| Flashblock index/arrival timing | Contemporaneous captured Flashblocks | Canonical historical block alone cannot recover provider arrival time or all incremental states | Major historical blind spot |
| Dropped/private attempts | Not present in canonical chain | Private-mempool rejected/dropped submissions are invisible | Unresolved lower-bound bias |

Base documentation exposes `debug_traceTransaction`, `debug_traceBlockByHash`, and `debug_traceBlockByNumber`, but explicitly says availability and rate limits vary by provider. Dune documentation confirms raw Base transactions, logs, creation traces, traces, decoded data, and curated DEX trades. Together these are sufficient to build a low-cost candidate census before purchasing bulk archive access.

### 4.2 Live

**Confirmed facts**

- Public Base endpoints support HTTP but not WebSocket subscriptions and are rate-limited.
- Flashblocks-compatible providers can expose new heads, individual preconfirmed transactions, pending logs, full Flashblocks, and pending-state calls.
- A self-hosted Base node can consume Flashblocks, but Base warns that node operation is time-consuming, resource-expensive, and potentially costly; snapshots can shorten initial sync.

**Inference**

Two provider feeds with local monotonic timestamps are needed to measure provider lag. A single feed can run a functional paper monitor but cannot distinguish network latency from provider latency.

## 5. Cheap-start conditions

### Tier 0 — documentary and query reproduction

- Use the open optimistic-MEV methodology as the starting classifier.
- Query a bounded post-Flashblocks sample in Dune: one ordinary UTC day plus one declared high-activity day.
- Identify calls to known/paper-reported cyclic-arbitrage contracts and independently derive new candidate contracts from swap cycles.
- Pull a small random sample of receipts/traces through public or existing RPC access.
- No wallet, node, WebSocket, or paid low-latency service is required.

**Budget conclusion:** can begin with zero marginal infrastructure spend, subject to existing query/RPC quotas. “Free” does not mean unlimited; bytes scanned, export limits, and trace throttling must be recorded.

### Tier 1 — bounded historical replay

- Buy archive/tracing access only after fixing exact block ranges and estimating calls/bytes.
- Decode four whitelisted venue families at most.
- Preserve raw responses or content hashes, provider/client version, contract bytecode hash, and query text.
- Reproduce 100–300 candidates only if the initial sample establishes adequate classifier precision.

### Tier 2 — live paper monitor

- Use two Flashblocks-aware WebSocket feeds if the provider budget permits; one feed plus public HTTP can bootstrap functionality but not comparative latency.
- Timestamp receive, decode, quote, simulation-ready, and hypothetical-send stages.
- Do not self-host a node until measurements show provider lag is the limiting variable.
- Implement both `FlashblocksHeadSource` and `CanonicalHeadSource`; exercise the latter on Denim Vibenet before mainnet migration.

### Not justified at screening stage

- a funded executor;
- a custom sequencer/node colocated deployment;
- repeated live speculative probing;
- all-venue graph search;
- assuming private order-flow or guaranteed bundles;
- treating gas price alone as total execution cost.

## 6. Competition and accessibility

### Confirmed evidence

- Base's legacy regime supported very large-scale speculative probing: the cited study observed tens of millions of non-reverted calls to individual top contracts and a very low trade-execution rate.
- The current Flashblocks builder fee-orders each available 200-ms batch, while arrival time determines which batch a transaction can enter.
- The private mempool prevents a public-mempool observer from seeing all candidate transactions before ordering.
- The published study provides open classification logic and identified contract fixtures, lowering research entry cost.

### Inferences

- Cheap gas makes experimentation affordable but also makes brute-force competition affordable. It is not itself a moat.
- A small team can compete first on measurement quality and narrow venue math, not on broad coverage.
- Post-state opportunities observable after a published Flashblock are the most credible permissionless latency path; pre-order trigger backruns likely require information not exposed by the public preconfirmation stream.
- Denim may make event boundaries easier to reason about because every 200-ms state becomes canonical, but it will also remove the current pending/Flashblocks interface and may change bot behavior.

## 7. Provisional screen score

Scores use 1 = poor and 5 = strong. They assess research accessibility, not expected profit.

| Criterion | Score | Rationale |
| --- | ---: | --- |
| Data access | 5 | Public RPC plus raw/decoded/curated Dune Base tables; exact archive state and live WSS may be paid |
| Historical reproducibility | 4 | EVM receipts/traces and open classifier; exact Flashblock timing is not recoverable from canonical blocks alone |
| Opportunity diversity | 4 | Multiple AMM generations, lending markets, cross-domain paths, and hook/custom-pool surface |
| Execution access | 3 | Public transaction submission and atomic EVM execution; no documented adjacency/private-bundle guarantee in reviewed Base APIs |
| Prototype cost | 4 | Bounded classifier/replay can start cheaply; two live feeds/archive traces add cost later |
| Competition accessibility | 2 | Documented large bot activity, private mempool, and 200-ms fee/arrival competition |
| Implementation simplicity | 3 | Standard EVM base, offset by concentrated liquidity, hooks, proxy/version history, and regime migration |
| Evidence confidence | 4 | Strong official interfaces and peer-reviewed historical evidence, but no fresh project sample and a major regime mismatch |
| **Total** | **29/40** | Suitable for bounded historical research; not enough evidence for execution selection |

## 8. Unknown metrics

No project-original opportunity sample was collected, so the following remain unknown:

- post-Flashblocks opportunities/day;
- profitable opportunities/day after L2 execution, L1 data-related, operator, and failed-attempt costs;
- trade-net PnL distribution;
- recurring versus tail contribution;
- opportunity survival by successive Flashblock;
- current winner concentration and actor clustering;
- current no-trade/revert cost per realized win;
- minimum competitive priority fee and provider-latency distribution;
- fully loaded infrastructure break-even;
- how Denim changes any of the above.

The historical 2025 paper values are not substituted for these metrics.

## 9. Recommended next test

### BASE-HR-001 — post-Flashblocks optimistic-MEV census

**Question**

Did optimistic cyclic arbitrage remain economically and operationally relevant after Base changed from two-second blocks to 200-ms Flashblock auctions, and is any subset reproducible without private-mempool access?

**Pre-registered sample**

1. Two complete ordinary UTC days after 2025-07-16, selected by a deterministic hash-derived rule before viewing profitability.
2. One post-Flashblocks stress day selected using an external, predeclared ETH-volatility threshold, not DEX profit.
3. The two paper-reported transactions above as legacy-regime classifier fixtures.
4. A later Denim sample must be a separate experiment after mainnet activation.

**Phase A — zero/low-cost census**

- Reimplement the paper's Dune logic: swap-cycle reconstruction, router/aggregator exclusion, first-callee contract attribution, and `trade | interaction | residual` plus `success | revert` labels.
- Compare paper-reported contracts with contracts derived independently in the new sample.
- Report calls, swaps, transaction status, gas used, effective gas price, unique calldata reuse, venue touches, and conservative actor-cluster confidence.
- Manually validate random positives, random negatives, highest-gas calls, and every alleged profitable cycle in the small sample.

**Phase B — exact replay for a narrow venue set**

- Fetch canonical block/receipt/log/trace evidence and exact historical bytecode for 30–50 representative trades and no-trade probes.
- Reconstruct token deltas and all visible fees in base units.
- Re-quote observed routes using exact pool state and compare output to the executed amounts.
- Do not estimate sub-200-ms arrival latency from canonical history.

**Phase C — live paper observation only if A/B pass**

- Capture `newFlashblocks`, `newFlashblockTransactions`, and `pendingLogs` from two providers for seven complete days.
- For every pool-changing event, quote whitelisted cycles at the observed state and at the next observed Flashblocks.
- Record decay by observed state transition: same received state, next Flashblock, +2, +3, +5, and sealed two-second block. Keep wall-clock receipt deltas separately.
- Simulate an independent atomic transaction; do not assume trigger adjacency.

**Go gate**

Advance Base to the two-network live-paper shortlist only if:

1. the classifier reconciles across Dune and independently fetched traces;
2. multiple post-Flashblocks cycles have exact, positive realized accounting after visible variable costs;
3. some independently detectable post-state candidates remain positive at the next observable Flashblock;
4. provider gaps and lag are measured rather than assumed;
5. results are not dominated by one event or an unpriced residual token;
6. the implementation has a tested Denim-compatible canonical-head adapter.

**Stop/hold conditions**

- profitable candidates require seeing the private mempool before ordering;
- opportunities disappear before the next observable state;
- exact integer replay reverses apparent profits;
- current activity is almost entirely no-trade probing with negative fully loaded economics;
- trace/archive cost exceeds the approved research budget;
- Denim activation occurs before a comparable baseline is completed, in which case freeze the Flashblocks dataset and restart the live baseline under Denim.

## 10. Principal uncertainties and contradictory evidence

1. **Temporal mismatch:** the strongest Base MEV paper predates Flashblocks and cannot answer the current economics question.
2. **Denim schedule:** one official page targets October 2026, while the migration guide stresses that activation time and client versions remain undecided. Treat the month as a target, not a commitment.
3. **No public pre-order view:** Flashblocks expose ordered preconfirmations, not all transactions waiting in the private sequencer mempool.
4. **Failure undercount:** canonical data captures included reverts and successful no-trade probes, but not dropped/rejected/unsubmitted attempts.
5. **Profit reconstruction:** a cyclic token path is not sufficient; controlled-address balance deltas, wrapped/native ETH, gas, L1 data-related fees, operator fees, flash-loan fees, residual inventory, and external hedges must be reconciled.
6. **Curated-data coverage:** Dune accelerates discovery but custom pools, proxies, hooks, and new deployments may be missing or mislabeled.
7. **Contract ownership:** a callee address is not automatically one independent operator; clustering remains an inference.
8. **Venue ranking:** official deployments prove availability, not liquidity depth or accessible opportunity.

## 11. Artifacts and source register

The detailed source register, evidence scope, and limitations are in [`../evidence/base-sources.md`](../evidence/base-sources.md).

No project-original raw chain dataset, provider quote, or independently verified address cluster was produced in this screening sprint.

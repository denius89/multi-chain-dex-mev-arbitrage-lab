# Ethereum network screening — 2026-09-25

## Short conclusion

**Provisional decision: HOLD as a primary generic-arbitrage MVP; GO for one bounded research track.**

Ethereum has unusually good canonical-chain observability, mature simulation tooling, atomic EVM execution, and a documented permissionless entry point to private order flow through MEV-Share. Those properties make historical reconstruction and paper execution feasible for a small team.

The accessible strategy is not generic public-mempool speed racing. Official Ethereum guidance says common DEX arbitrage and liquidations are unlikely to be profitable for new searchers. Public empirical work also shows strong concentration in block building and CEX–DEX arbitrage, with differentiated or exclusive order flow associated with winning builders and searchers. A small team should therefore test one narrowly scoped **MEV-Share backrun or protocol/event-specific route**, while treating generic atomic arbitrage, generic Aave liquidation, and CEX–DEX as benchmarks rather than the initial production thesis.

This screen establishes technical testability, not accessible profit. It contains no fresh on-chain PnL sample and therefore does not populate profit, frequency, latency, or failure-cost fields in the project scorecard.

## Scope and evidence status

- Network: Ethereum mainnet.
- Status date: 2026-09-25.
- Strategy classes: atomic multi-DEX arbitrage, MEV-Share backruns, lending liquidations, multi-protocol/event-driven routes, and CEX–DEX arbitrage.
- Evidence used: official Ethereum, Flashbots, and Aave documentation; public empirical papers/preprints with declared observation windows.
- Not performed in this sprint: archive-node replay, mempool capture, MEV-Share event capture, bundle submission, wallet clustering, or original PnL calculation.

Labels used below:

- **Confirmed fact** — directly supported by official documentation or by a cited paper for its stated sample.
- **Inference** — an interpretation of the cited facts for this project.
- **Hypothesis** — a falsifiable proposition requiring our own data.
- **Recommendation** — a proposed next action.

## Market structure and execution

### Confirmed facts

1. MEV-Boost gives validators access to blocks built by a marketplace of builders. Builders combine transaction order flow with a payment offered to the proposing validator. This separates proposing from block construction but adds builders and relays to the execution path.
2. Flashbots bundles are ordered groups of one or more transactions submitted for a target block. A bundle may include a searcher's transactions and other pending user transactions.
3. Flashbots supports multiplexing transactions or bundles to multiple builders. Submission to a single builder is therefore not the only documented route, but builder coverage remains an execution variable.
4. MEV-Share is an order-flow auction. Users choose privacy hints, searchers submit partial bundles, the node simulates candidates, and successful candidates can be forwarded to builders subject to refund rules.
5. The documented MEV-Share hint surface includes transaction hash, contract address, function selector, calldata, logs, and `default_logs`. The last discloses partial swap information for Curve, Balancer, and Uniswap-v2/v3-style trades.
6. As documented on the status date, a `mev_sendBundle` bundle can contain only one backrun transaction. The documented private-transaction `fast` preference sends to all registered builders and sets MEV-Share revenue share to 50%; the MEV-Share introduction describes a default 90% user refund. A research implementation must record the exact configuration rather than assume one universal split.
7. Canonical block data cannot reveal non-included private bundles or the time at which each searcher first observed an opportunity.

### Inferences

- Ethereum execution quality depends on more than RPC latency: hint completeness, simulation correctness, builder routing, bid/refund policy, and target-block timing all affect inclusion and retained value.
- Historical block replay can validate route math and realized accounting, but it cannot reconstruct the full competitive set or produce credible millisecond win probabilities without contemporaneous private/public order-flow capture.
- The existence of a permissionless MEV-Share interface lowers the access barrier compared with strategies requiring bilateral private-order-flow deals. It does not remove auction competition.

## Strategy assessment

### 1. Generic atomic multi-DEX arbitrage

**Confirmed facts**

- Ethereum.org identifies DEX arbitrage as a well-known MEV class and says it is unlikely to be profitable for new searchers.
- Atomic EVM execution can combine swaps, financing, repayment, and a minimum-profit assertion in one reverting transaction or ordered bundle.
- Post-Merge Flashbots analysis based on `mev-inspect-py` reported that, in its observed period, proposers captured the majority of atomic MEV profits and at times 80–95%. This is historical, methodology-limited evidence, not a current universal rate.

**Inference**

Plain two-pool routing over the largest venues is a useful simulator correctness benchmark but a weak initial business thesis. The route is legible, widely implemented, and much of the available value can be competed into builder/proposer payments.

**Hypothesis ETH-A**

A narrow pool family or contract interaction that established generic routers model poorly may leave reproducible atomic opportunities after gas and competitive bids.

**Falsification test**

Pre-register one pool family and 14 baseline days plus two stress days. Replay all state changes that touch the chosen contracts; compare the best exact route against included arbitrages and calculate value remaining after observed gas/direct payments and a conservative builder bid. Reject the hypothesis if positive cases are isolated, disappear under exact integer math, or require unavailable order flow.

### 2. MEV-Share backruns

**Confirmed facts**

- MEV-Share selectively discloses private transaction information and is permissionless for searchers according to Flashbots documentation.
- Searchers may receive incomplete hints and build a single backrun transaction around the private transaction under the current documented bundle format.
- The MEV-Share node simulates candidate bundles and attaches refund conditions before forwarding successful candidates.
- Flashbots documentation exposes `mev_sendBundle` and simulation functionality. The privacy configuration determines what a searcher can reconstruct.

**Inference**

MEV-Share is the cleanest bounded Ethereum entry point for this project because the interface, hint stream, simulation path, and backrun role are explicit. The principal research problem is not merely speed; it is whether a specialized decoder and route model can turn partial hints into sufficiently accurate bids while retaining value after refunds and builder competition.

**Hypothesis ETH-B — preferred Ethereum test**

For one under-covered swap or oracle-triggered contract family, a specialized decoder can produce valid backruns from MEV-Share hints with materially better simulation acceptance than a generic blind strategy, leaving positive paper residual after refund, gas, and bid assumptions.

**Falsification test**

Capture the public MEV-Share event stream for 7–14 days with monotonic receive timestamps. Limit scope to one declared contract family. For every usable hint, persist decode completion, candidate route, simulation result, assumed refund/bid, and value at 50/100/250/500/1,000/2,000 ms. Reject if hint coverage is inadequate, accepted candidates are too rare, or conservative residual is non-positive.

### 3. Lending liquidations

**Confirmed facts**

- Aave v3 positions become eligible for liquidation when their health factor falls below one. A liquidator repays debt and receives collateral with a liquidation incentive under version- and reserve-specific rules.
- Ethereum.org identifies liquidations as well-known MEV and unlikely to be profitable for new searchers.
- The 2021 empirical liquidation study covers Aave, Compound, MakerDAO, and dYdX and documents both liquidation incentives and participant risks. Its market shares and economics are historical and must not be projected to 2026.

**Inference**

Monitoring health factors alone is not an edge. A production competitor needs timely oracle state, accurate accrued debt and close-factor logic, collateral-sale routing, financing, and builder delivery. Generic Aave liquidation is therefore a good accounting fixture but a poor first execution target.

**Hypothesis ETH-C**

Liquidation-adjacent backruns around fully hinted oracle updates may be more accessible than winning the liquidation itself, because the specialized opportunity occurs after a known state transition.

**Falsification test**

Without attempting live liquidation, classify fully hinted oracle-update events and simulate a fixed list of allowed downstream routes. Measure hint sufficiency and residual after refund/gas. Do not infer viability from historical liquidation bonuses alone.

### 4. CEX–DEX / non-atomic arbitrage

**Confirmed facts from declared historical samples**

- A 2024 paper analyzing Ethereum from the Merge through 2023-10-31 estimated that more than one quarter of volume on the five studied large DEXes was likely non-atomic arbitrage; 11 searchers accounted for more than 80% of the identified non-atomic arbitrage volume. These are classifier-derived results for that window.
- A 2025 preprint analyzing 2023-08-08 through 2025-03-08 identified 7,203,560 CEX–DEX arbitrages by 19 major labeled searchers and estimated $233.8 million of extracted value. Three searchers captured about three quarters of both volume and extracted value.
- The same 2025 study reports that leading high-volume strategies commonly operated at single-digit-basis-point gross returns, that nearly 90% of trades for one major pattern earned below 20 bps gross, and that searcher profitability was linked to builder integration/exclusive relationships.
- The off-chain hedge leg, actual CEX fee tier, rebates, internal inventory transfer, and failed hedge attempts are not fully observable from Ethereum blocks.

**Inference**

CEX–DEX contains substantial measured activity but has the highest practical entry barrier in this screen: exchange accounts and limits, low-latency authenticated feeds, inventory on both sides, hedge execution, reconciliation, and potentially builder integration. On-chain revenue estimation alone is insufficient to reproduce net economics.

**Recommendation**

Keep CEX–DEX in the historical classifier so it is not mistaken for atomic arbitrage, but do not select it for the first Ethereum executor. Revisit only if the project gains reliable CEX execution data and can measure both legs.

### 5. Multi-protocol and event-driven routes

**Confirmed facts**

- Ethereum.org explicitly points new searchers toward a long tail of less-known MEV opportunities rather than common arbitrage/liquidation categories.
- Ethereum's contracts and receipts allow deterministic replay when the correct historical bytecode, state, transaction context, and protocol parameters are available.

**Inference**

This is where “ingenuity rather than pure speed” is most plausible: migrations, auctions, redemptions, peg mechanisms, hook-specific state transitions, or combinations across protocols can reward exact contract modeling. The trade-off is sparse data and higher model/audit effort.

**Hypothesis ETH-D**

A public, intended protocol mechanism with a complex or infrequent state transition can support a narrow deterministic strategy that generic routers do not price correctly.

**Guardrail**

The scope is normal public protocol behavior. Vulnerability exploitation, unintended fund extraction, compromised keys, and manipulation of users are excluded.

## Empirical evidence on concentration and entry barriers

### Confirmed facts for the cited samples

1. **Builder concentration:** the 2024 “Who Wins Ethereum Block Building Auctions and Why?” study reports that MEV-Boost accounted for approximately 90% of blocks in its study context and that three builders produced 80% of blocks from October 2023 through March 2024. It finds builder market share correlated with order-flow diversity and profitability correlated with exclusive order-flow access.
2. **Private-flow contribution:** a separate 2024 preprint studying January 2023 through May 2024 estimates private order flow contributed 54.59% of block value in its model/sample and describes a reinforcing relationship between private flow and builder wins.
3. **Non-atomic concentration:** the 2024 non-atomic arbitrage paper reports 11 searchers above 80% of identified volume through 2023-10-31.
4. **CEX–DEX concentration:** the 2025 CEX–DEX study reports three searchers at roughly 75% of both volume and extracted value in its 19-month dataset.
5. **Common-strategy warning:** Ethereum.org says well-known DEX arbitrage and liquidations are unlikely to be profitable for new searchers.

### Limits

- These studies cover different windows, classifiers, economic quantities, and actor definitions. Their percentages must not be combined into a single “Ethereum concentration score.”
- Builder market shares and private-flow relationships may have changed after the study windows.
- Searcher labels and clusters are inferences; one operator may use multiple addresses, and one address may serve multiple roles.
- Included-chain analysis omits losing private bundles and can understate competition and total search cost.

### Project inference

The combined evidence is strong enough to reject the assumption that a small team can enter Ethereum by implementing a generic route scanner and buying a faster RPC. It does **not** prove that all Ethereum strategies are inaccessible. It redirects the search toward differentiated order interpretation and contract-specific state transitions.

## What a small team can test without relying only on latency

Ranked in recommended order:

1. **Specialized MEV-Share paper backrunner.** One contract family, partial-hint decoder, exact simulation, no funded key. Differentiation: decoding and pricing quality.
2. **Protocol/event-specific historical replay.** One public mechanism such as redemption, auction, migration, or hook behavior. Differentiation: contract understanding and complete accounting.
3. **Constrained multi-protocol route search.** Two or three audited venue types with exact math and a route invariant. Differentiation: route construction; use primarily to validate the shared simulator.
4. **Liquidation-adjacent event study.** Observe oracle-triggered state changes and downstream backruns without trying to win generic liquidations.

Not recommended as the first Ethereum execution MVP:

- broad public-mempool two-pool arbitrage;
- generic Aave liquidation racing;
- blind spam/probing transactions;
- CEX–DEX without authenticated fill and inventory data;
- builder operation or acquisition of exclusive order flow.

## Access, cost, and observability screen

| Dimension | Finding | Evidence class |
|---|---|---|
| Canonical historical data | Blocks, receipts, logs, traces, and historical state are technically accessible through an archive-capable node/provider | Confirmed capability; provider completeness/cost not measured |
| Atomic replay | EVM transactions and bundles can be simulated against explicit state when context is reproduced correctly | Confirmed capability |
| Public live flow | Public pending transactions can be captured, but this excludes private flow | Confirmed limitation |
| Private-flow entry | MEV-Share offers permissionless hints and bundle APIs | Confirmed capability |
| Full private-flow coverage | No; hint selection and private bilateral flow create blind spots | Confirmed limitation/inference |
| Competitive delivery | Builder multiplexing is documented, but winning coverage and bidding remain empirical questions | Confirmed capability plus unknown performance |
| Historical failure visibility | Included reverts are visible; rejected/non-included private submissions generally are not | Confirmed limitation |
| Initial capital | Historical replay and paper backrun require no funded trading wallet | Confirmed by proposed design |
| Prototype fixed cost | Not estimated in this sprint; quote archive RPC/storage/compute only after fixing the block window and retention policy | Unknown |

## Provisional score

Scores use 1 = poor and 5 = strong. They assess research accessibility, not profit potential.

| Criterion | Score | Rationale |
|---|---:|---|
| Historical data/replay access | 4 | Strong RPC/tracing/tool surface; archival completeness and cost remain provider-specific |
| Atomic execution/simulation | 5 | Mature EVM and documented bundle/simulation paths |
| Live opportunity observability | 2 | Significant private-flow blind spot; MEV-Share exposes only selected hints |
| Permissionless execution access | 4 | Public chain plus Flashbots/MEV-Share APIs; no guarantee of competitive inclusion |
| Small-team differentiation potential | 3 | Plausible in specialized/event-driven niches, weak for generic strategies |
| Generic-strategy competition | 1 | Official warning plus strong empirical concentration evidence |
| Net-economics measurability | 3 | Strong for atomic included trades; weak for non-included bundles and CEX legs |
| Evidence confidence | 4 | Strong official docs and several empirical samples, but no project-original dataset yet |

## Uncertainties and missing data

1. Current usable MEV-Share hint volume by contract family and the fraction that yields reproducible simulations.
2. Current builder routing/inclusion distribution for small independent searchers.
3. Actual retained searcher value after refunds, gas, direct bids, and failed/replaced submissions in 2026.
4. Cost and completeness of the selected archive/tracing provider for the declared block windows.
5. Which contract families are under-modeled by existing searchers; this cannot be established from documentation alone.
6. Whether MEV-Share event history is sufficiently complete for historical frequency estimates; live capture is safer for latency and coverage.
7. Current protocol deployments, bytecode versions, and parameter histories for any selected strategy.

## Recommended next test

### ETH-R1: bounded MEV-Share hint census

**Purpose:** decide whether Ethereum deserves one of the two historical/paper-monitoring slots without building an executor.

**Scope:**

- duration: seven complete UTC days, extend to 14 only if uptime and decode coverage are acceptable;
- one predeclared contract family, not all DEXes;
- no funded key, no bundle broadcast required;
- public MEV-Share event stream plus canonical blocks/receipts for later outcome matching;
- monotonic timestamps at receipt, decode completion, route completion, and simulation completion.

**Persist per event:**

- hint fields and privacy mode, with redistribution restrictions respected;
- target contracts and classifier confidence;
- whether the trigger could be reconstructed;
- candidate route and optimized input;
- simulation state/block and result;
- gross opportunity value;
- gas estimate, configured refund, conservative builder bid, and retained residual;
- value after 50/100/250/500/1,000/2,000 ms where captured states permit;
- canonical inclusion/outcome match and rejection reason.

**Gate:** proceed to deeper historical reconstruction only if the collector has measured uptime, the chosen hints are reconstructible at a useful rate, several independent simulations reconcile to canonical outcomes, and some paper residual remains positive under declared conservative costs. Otherwise stop or select a different contract family; do not compensate by widening blindly.

## Screening decision

- **Generic Ethereum arbitrage:** no-go for first MVP.
- **Generic liquidation racing:** no-go for first MVP.
- **CEX–DEX execution:** hold; research/classification only.
- **Specialized MEV-Share backrun:** go to bounded paper-data census.
- **Protocol/event-specific strategy:** go to hypothesis discovery and historical replay only after selecting one explicit mechanism.

Ethereum should remain in the comparative project, but its candidature for the first executor depends on ETH-R1 data. The project must not interpret mature tooling or large historical extracted value as evidence that profit is accessible to this team.

## Sources

The source register, retrieval dates, scope notes, and limitations are in [`../evidence/ethereum-sources.md`](../evidence/ethereum-sources.md).

# Independent review checklist — research sprint 2026-09-25

Status: **review protocol**  
Reviewer role: independent evidence and reproducibility review  
Applies to: `network-screening/*.md` and `infrastructure-costs.md` produced in this sprint

## Review outcomes

Each file receives exactly one overall outcome:

- **PASS** — every critical check passes; remaining issues are editorial or explicitly bounded and do not change the ranking or recommendation.
- **CONDITIONAL** — no known fatal error, but one or more material claims require correction, stronger evidence, or a narrower conclusion before use in a network-selection decision.
- **FAIL** — a critical check fails, the central result cannot be reproduced, or unsupported claims materially drive the conclusion.

A file cannot pass merely because it contains many citations. Sources must support the exact claims, be current for the stated status date, and permit the claimed inference.

## 1. Scope and epistemic labeling

- [ ] The file states network, venue set, strategy class, observation/status date, and intended decision.
- [ ] Confirmed facts, derived results, hypotheses, and recommendations are distinguishable.
- [ ] A network overview is not presented as evidence of accessible profit.
- [ ] Claims are falsifiable and scoped; terms such as “fast”, “cheap”, “profitable”, “dominant”, and “live” have measurable meanings.
- [ ] Unknowns and data blind spots are listed next to the affected conclusions.
- [ ] The report does not silently narrow or broaden the project scope.

**Critical failure:** a recommendation is primarily supported by unlabeled speculation or by a single exceptional transaction.

## 2. Source quality and claim-level traceability

- [ ] Every material mutable claim has an inline source or an evidence record.
- [ ] Network mechanics, ordering, fees, APIs, contract/program addresses, and product availability use primary sources where available.
- [ ] Secondary sources are used only for independent research, context, or discovery, and are clearly identified.
- [ ] Each citation resolves to the exact relevant page/section rather than a homepage or search result.
- [ ] The cited source actually entails the nearby claim; stronger wording than the source is not used.
- [ ] Announcements, forum posts, roadmaps, and marketing pages are not treated as proof of production behavior.
- [ ] Conflicting sources are disclosed and resolved or left explicitly unresolved.
- [ ] Every source has a retrieval date; mutable pages should also have a preserved snapshot, quoted version, release, commit, or checksum where practical.
- [ ] Links and cited contract/program identifiers were checked independently.

**Critical failure:** a core ordering, atomicity, live-availability, or cost claim depends only on an unsourced statement, a secondary summary where primary documentation exists, or an inaccessible citation.

## 3. Freshness and temporal consistency

- [ ] The status date is explicit and no later facts are implied.
- [ ] Current production state is separated from announced, testnet, experimental, deprecated, or future state.
- [ ] Upgrade schedules are labeled as targets until activation is verified from production evidence.
- [ ] Pricing and plan limits include retrieval date, billing unit, overages, taxes/credits exclusions, and any negotiated/enterprise ambiguity.
- [ ] DEX/protocol support is verified against current official deployments and, where material, current on-chain code/account activity.
- [ ] Historical claims use the rules, fee model, and software version active during the sampled block/slot range.
- [ ] Findings that may become stale include a re-verification trigger.

**Critical failure:** a testnet/future feature or announced integration is treated as available on mainnet, or a superseded execution/ordering model drives the score.

## 4. Announced versus live integrations

For every named venue, feed, relay, RFQ system, order book, oracle, or sequencer interface:

- [ ] Official announcement/documentation is recorded.
- [ ] Exact network and chain ID are recorded.
- [ ] Deployed contract/program address or production endpoint is recorded where applicable.
- [ ] Code exists at that address/endpoint and matches the claimed product/version.
- [ ] Recent production transactions, events, liquidity, or responses establish actual activity.
- [ ] “Deployed”, “available”, “integrated”, “liquid”, and “usable by an external searcher” are evaluated separately.
- [ ] Permissioning, allowlists, authentication, rate limits, geofencing, and commercial access requirements are stated.
- [ ] Inactive or zero-liquidity deployments do not improve the network score without an explicit caveat.

**Critical failure:** an announced but unverified integration materially supports opportunity count, data accessibility, or MVP feasibility.

## 5. On-chain reproducibility

- [ ] Exact chain ID, block/slot range, UTC range, finality level, RPC/indexer provider, retrieval timestamp, and query/command are given.
- [ ] Transaction hashes, relevant contract/program/pool addresses, and raw-data paths are included for representative claims.
- [ ] Raw inputs are immutable or checksummed.
- [ ] Collector commit/version, decoder version, schema version, and dependencies are recorded.
- [ ] Inclusion, exclusion, deduplication, and error-handling rules are explicit.
- [ ] A second researcher can reproduce the sample and summary without private credentials, or credential requirements are clearly documented.
- [ ] Missing blocks/slots, archival gaps, RPC pruning, reorgs/finality, provider disagreement, and decode failures are quantified.
- [ ] Representative transactions are reconciled from raw chain data through normalized legs to the reported result.
- [ ] Historical pre-state is available or reconstructed; if not, results are labeled balance reconstruction rather than exact replay.
- [ ] Counts and durations accompany percentages; small samples avoid false precision.

**Critical failure:** claimed empirical results have no block/slot/transaction identifiers, no preserved inputs, or no executable reproduction path.

## 6. Sampling and survivorship bias

- [ ] Baseline windows were predeclared before inspecting profitability: at least 14 complete ordinary UTC days unless a justified screening-only exception is stated.
- [ ] Stress/event windows are defined by an external trigger and kept separate from baseline economics.
- [ ] Known jackpot/event cases validate decoding but do not estimate frequency.
- [ ] The candidate-search procedure includes losing, reverted, expired, and zero-profit outcomes where observable.
- [ ] The sample is not restricted to known winning wallets or transactions.
- [ ] Wallet discovery rules are reproducible and do not rank only by observed profit before estimating market-wide distributions.
- [ ] Selection changes made after viewing results are versioned and disclosed.
- [ ] The report distinguishes full population, deterministic sample, random sample, and convenience sample.
- [ ] Coverage denominator is defined; unclassified and undecodable transactions remain in coverage statistics.
- [ ] Results are reported with and without the largest event and, when useful, largest 1% of trades.
- [ ] Median day/trade, active-day ratio, trimmed mean, tail shares, and longest no-profit/loss streak are considered before claiming recurrence.
- [ ] Off-chain rejected submissions and invisible private attempts are identified as an unmeasured blind spot, not assumed zero.

**Critical failure:** a conclusion about stable or recurring returns is inferred from selected winners, a known profitable wallet, or one/few tail events without a denominator.

## 7. Gross, trade-net, and fully loaded PnL

- [ ] `gross_pnl`, variable `execution_cost`, `trade_net_pnl`, and `fully_loaded_pnl` are separately defined.
- [ ] All legs, internal transfers, wrapped/native conversions, token decimals, flash loans, inventory changes, and residual balances reconcile.
- [ ] Protocol fees embedded in swap outputs are not double-counted.
- [ ] Base gas/network fee, priority fee, relay/builder/Jito tip, flash-loan fee, non-refunded rent, and measured hedging/settlement costs are included where applicable.
- [ ] Failed/reverted attempt costs are attributed consistently and reported per successful trade.
- [ ] USD valuation names price source, timestamp, quote convention, and treatment of illiquid or depegged assets.
- [ ] Stablecoin-denominated cycles are not assumed equal to USD without noting depeg exposure when material.
- [ ] Infrastructure costs are allocated by declared period and method; engineering expense is kept separate unless explicitly modeled.
- [ ] Rebates, private payments, refunds, builder transfers, or off-chain hedges are included if observed and otherwise listed as unknown.
- [ ] Reported precision matches price, attribution, and decoding uncertainty.
- [ ] Core identities reconcile: `trade_net_pnl = gross_pnl - variable_execution_cost`; `fully_loaded_pnl = trade_net_pnl - allocated_infrastructure_cost`.

**Critical failure:** the recommendation relies on gross spread/profit, token balance deltas, or successful trades without observable fees and failure costs.

## 8. Latency and executability

- [ ] Latency is end-to-end: source publication → receipt → decode → route calculation → simulation → signed-ready payload → delivery/landing where measured.
- [ ] RPC ping is not used as a proxy for end-to-end latency.
- [ ] Historical mathematical opportunity, observable opportunity, simulated opportunity, submitted attempt, and landed execution are distinct states.
- [ ] Delay checkpoints include 0/50/100/250/500/1,000 ms or justified chain-native equivalents.
- [ ] Millisecond claims use actual timestamps/telemetry; final block order alone is not treated as arrival time.
- [ ] When sub-block timing or historical state is unavailable, estimates are labeled model-dependent and chain-state transitions are used instead of invented precision.
- [ ] Ordering rules, auction/tip mechanics, sequencing windows, account/contention locks, reorg/finality, and simulation staleness are included.
- [ ] Network location claims are supported by measured RTT/end-to-end tests from named regions, not geographic intuition.
- [ ] Opportunity lifetime and profit-decay curves state sample size and assumptions.
- [ ] The score reflects whether the required feed and delivery path are actually accessible within budget.

**Critical failure:** executable PnL is inferred from end-of-block state or best-case quotes without a latency/order model.

## 9. Wallet attribution and competition

- [ ] Address-level observations are separated from entity/team attribution.
- [ ] Wallet clustering rules are documented, deterministic where possible, and assigned confidence levels.
- [ ] Similar routes, timing, or fee patterns alone are not treated as proof of common ownership.
- [ ] Funding links, authority relationships, program deployment, shared settlement, and repeated coordinated behavior are evaluated as evidence—not certainty.
- [ ] Alternative explanations such as shared infrastructure, public SDK defaults, routers, custodians, or relayers are considered.
- [ ] Top-1/top-3/top-10 shares use a stated denominator and are reported both by address and, only when defensible, inferred entity.
- [ ] HHI is calculated only when attribution and coverage are adequate; unidentified share is retained.
- [ ] Profit attribution accounts for capital transfers and does not mistake deposits/withdrawals for trading PnL.
- [ ] Competitor counts distinguish independent actors, addresses, and attempts.

**Critical failure:** wallet ownership/entity claims are asserted as fact without direct evidence, or concentration results rely on undisclosed clustering.

## 10. Infrastructure cost and access audit

- [ ] Each component has provider/product/tier, quoted currency, billing cadence, included usage, overage, region/IP limits, and retrieval date.
- [ ] Free, developer, business, enterprise, negotiated, and waitlisted access are not conflated.
- [ ] One-time setup, recurring fixed, usage-variable, and trading-variable expenses are separate.
- [ ] Taxes, data egress, storage, observability, redundancy, archival access, extra IPs/regions, and required companion plans are included or explicitly excluded.
- [ ] The minimum research stack is separated from paper-monitor, tiny-live, and competitive/low-latency stacks.
- [ ] A lower/expected/upper scenario is shown without pretending enterprise quotes are known.
- [ ] “Free” endpoints are tested against history depth, rate limits, WebSocket/subscription support, and production terms.
- [ ] Server-region recommendations follow accessible feed/delivery endpoints and measured latency.
- [ ] Break-even calculations state observation period, PnL basis, uptime, and amortization assumptions.
- [ ] Promotional credits and temporary discounts are not embedded in steady-state economics.

**Critical failure:** a major required service is omitted, or advertised entry pricing is used despite insufficient features/limits for the proposed test.

## 11. Cross-network comparability and scoring

- [ ] Every network is evaluated with the same core questions and explicit chain-specific additions.
- [ ] Score definitions, weights, and evidence thresholds are fixed before final ranking or changes are disclosed.
- [ ] Unknown is not scored as favorable; lack of evidence is distinct from a negative finding.
- [ ] Scores separate research feasibility, paper-monitor feasibility, and expected trading attractiveness.
- [ ] Network volume is not used as a proxy for accessible arbitrage profit.
- [ ] Different finality, fee, private-flow, failure-visibility, and data-access models are normalized or stated as non-comparable.
- [ ] Tail-event potential and recurring economics are scored separately.
- [ ] Rankings include sensitivity to uncertain inputs and do not imply precision unsupported by evidence.
- [ ] No network is shortlisted solely because implementation is familiar or a dramatic public case exists.

**Critical failure:** the rank is produced from inconsistent definitions or assigns favorable values to missing evidence.

## 12. Conclusions, red flags, and next test

- [ ] Conclusions are no stronger than the evidence and identify the decisive facts.
- [ ] Recommendations state assumptions, expected information gain, cost ceiling, and stop condition.
- [ ] The smallest falsifiable next test is proposed; live execution is not recommended before historical and paper gates pass.
- [ ] Security-sensitive details, private keys, credentials, or exploitable user-targeting instructions are absent.
- [ ] Material limitations are visible in the executive conclusion, not buried.

### Mandatory red-flag scan

Mark every observed red flag in the independent review:

- [ ] Profitability inferred from DEX volume, TVL, spread screenshots, quoted routes, or one jackpot.
- [ ] Only successful transactions or known winning wallets sampled.
- [ ] Gross PnL presented as take-home profit.
- [ ] Failed attempts, tips, priority fees, hedging, or infrastructure ignored.
- [ ] Current mainnet capability inferred from roadmap/testnet/announcement.
- [ ] Explorer label treated as verified wallet ownership.
- [ ] “Atomic” treated as risk-free or as guaranteeing landing.
- [ ] Historical final ordering treated as proof of mempool visibility or arrival sequence.
- [ ] Millisecond latency claimed without timestamp provenance.
- [ ] Free/public RPC assumed suitable for competitive execution without measurement.
- [ ] Private order flow, rebates, off-chain hedges, or rejected bundles assumed absent.
- [ ] Inactive deployment or nominal integration treated as usable liquidity.
- [ ] Unsupported precision, annualized tail profit, or guaranteed daily-return language.
- [ ] Transaction hashes, addresses, raw evidence, retrieval dates, or reproduction commands missing.
- [ ] Network score/rank precedes evidence or changes methodology after results are seen.

## Review recording format

For each reviewed file, record:

1. **Outcome:** PASS / CONDITIONAL / FAIL.
2. **Decision use:** usable now / usable after named fixes / not usable.
3. **Critical findings:** numbered, each tied to a claim or section.
4. **Non-critical findings:** corrections that do not alter the decision.
5. **Claims independently verified:** exact source or on-chain evidence checked.
6. **Claims not verified:** reason and consequence.
7. **Reproduction attempted:** command, inputs, result, and mismatch if any.
8. **Required fixes:** owner-neutral and testable.
9. **Effect on shortlist:** none / uncertain / changes rank, with explanation.

## Minimum pass gate by file type

### Network-screening report

To pass, it must at minimum satisfy Sections 1–4, identify a reproducible historical test under Section 5, avoid the biases in Section 6, distinguish PnL levels in Section 7, and provide an honest latency/access assessment under Sections 8–9. It need not already contain a 14-day empirical study, but it must not make empirical profitability or concentration claims without one.

### Infrastructure-cost report

To pass, it must satisfy Sections 2–3 and 10, show dated primary pricing/access evidence, separate research/paper/tiny-live stacks, state exclusions, and avoid using unknown enterprise prices as exact figures.

### Comparative recommendation

To pass, all input reports must be at least CONDITIONAL with no unresolved critical failure affecting rank; Section 11 must pass; and the shortlist must be framed as candidates for historical reconstruction or paper monitoring, not as proven profitable networks.

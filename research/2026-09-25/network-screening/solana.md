# Solana network screening — 2026-09-25

## 1. Question and falsifiable hypothesis

**Question.** Can a small research team reconstruct and then paper-test atomic DEX arbitrage on Solana without first buying validator-grade infrastructure or a proprietary historical dataset?

**Falsifiable hypothesis.** A bounded universe of 2–3-leg cycles across Meteora, Raydium and Orca can be reconstructed from public transaction data, quoted locally from preserved pool state, and observed live with commodity infrastructure. The hypothesis fails for the first sprint if we cannot (a) reproduce several real routes and all visible costs, or (b) obtain the historical pre-state needed to distinguish a real opportunity from a post-hoc balance pattern.

This is a **network screen**, not a profitability study. No opportunity-frequency, latency-decay or PnL-distribution result is claimed here.

## 2. Short conclusion

**Decision: HOLD, with a bounded go-to-reconstruction experiment.**

Solana passes the basic feasibility screen: atomic multi-instruction execution exists; the target AMM implementations and SDK/source repositories are public; confirmed transactions expose messages, metadata and balance changes; Jito exposes an open bundle-submission path and publishes its auction mechanics. A public, formerly maintained Jito backrun bot also demonstrates the concrete architecture for circular backruns across Raydium and Orca. These facts establish technical feasibility, not accessible profit.

The main blocker is historical state. A transaction receipt is enough to reconstruct observed asset deltas, fees and program calls, but not necessarily the exact pool pre-state at an arbitrary slot. Public RPC is rate-limited and is not intended for production. Free bulk archives exist, but the free archive reviewed for this sprint had incomplete transaction-day coverage and did not cover the May 2026 ANB event. A broad 14-day replay therefore cannot yet be promised at zero data cost.

The smallest defensible next step is to reproduce the three named ANB-event transactions from raw RPC responses, identify every pool/program account, and determine whether the required pre-state can be recovered by replaying the complete set of writes in a narrowly bounded slot window. No additional wallet or transaction should be asserted until its raw record is preserved.

## 3. Scope and sample

- Network: Solana mainnet-beta.
- Venues screened: Meteora DLMM and DAMM v2; Raydium CPMM/CLMM/AMM v4; Orca Whirlpools; Jupiter as routing/control-quote infrastructure rather than a liquidity venue.
- Execution path screened: normal Solana transactions and Jito transactions/bundles.
- Strategy classes screened: two-venue cyclic arbitrage, triangular arbitrage, post-swap backruns, launch/liquidity-migration anomalies, and (as a later track) liquidations/oracle divergence.
- Historical event fixture: the ANB/ANX dislocation already recorded in `docs/project-context.md`.
- Retrieval date for mutable documentation: 2026-09-25.
- Excluded from this screen: live market scan, private order flow, CEX inventory, sandwich strategies, production submission and any profitability extrapolation.

No bounded block sample was downloaded during this screen. Consequently, all market-economics fields remain `unknown`.

## 4. Confirmed evidence

### 4.1 Execution and observable transaction data

1. **Confirmed fact — atomic execution is available at both transaction and Jito-bundle level.** Solana transaction instructions execute as one transaction; Jito documents bundles of at most five transactions that execute sequentially and atomically within one slot. A received `bundle_id` does not guarantee landing, and status must be checked separately.
2. **Confirmed fact — the public RPC surface is sufficient for bounded transaction forensics.** `getTransaction` returns the confirmed transaction, slot, version and metadata. Together with `getBlock` and `getSignaturesForAddress`, this supports transaction discovery, instruction ordering, logs, fees and pre/post balance reconstruction where the provider retains the requested history.
3. **Confirmed fact — public RPC is a research bootstrap, not a competitive live feed.** Solana's official mainnet endpoint is rate-limited (documented at 100 requests per 10 seconds per IP and 40 per single RPC method per 10 seconds) and explicitly not intended for production applications.
4. **Confirmed fact — low-latency delivery is an auction, not merely a faster RPC call.** Jito runs parallel auctions at 50 ms ticks. Conflicting account-lock patterns compete in the same local auction and are ranked by tip relative to requested compute units. The documented minimum bundle tip is 1,000 lamports, but Jito explicitly says the minimum may be insufficient in competitive periods.
5. **Confirmed fact — bundle atomicity has an operational edge case.** Jito warns that transactions from an uncled/skipped block may be rebroadcast through the normal banking stage without bundle atomicity. State assertions and placing the tip with the strategy (or guarding a separate tip transaction) are therefore required even for a later experimental executor.
6. **Confirmed fact — the low-latency feed landscape is changing.** The Jito ShredStream documentation reviewed on 2026-09-25 recommends migration to DoubleZero Edge before a stated shutdown. Any implementation plan that treats legacy Jito ShredStream as a durable dependency is already stale.

### 4.2 DEX and strategy implementation evidence

1. **Confirmed fact — the target venues expose program/SDK material suitable for deterministic quoters.** Meteora publishes a DLMM SDK and documentation for DLMM/DAMM products; Raydium publishes protocol documentation and SDK v2; Orca publishes Whirlpools SDKs and the Whirlpools repository. This is enough to start reference implementations and golden-vector tests. It does not prove that a locally written quoter matches every deployed program version.
2. **Confirmed fact — circular backrun arbitrage has a public implementation precedent.** The public `jito-labs/mev-bot` repository describes 2- and 3-hop circular routes across Raydium, Raydium CLMM and Orca, a Geyser-updated pool cache, Jupiter AMM calculators, Solend flash loans and Jito bundle submission. The repository explicitly states that it is no longer maintained and is not for production.
3. **Confirmed fact — observable competition is material.** Jito's epoch-414 analysis (published in 2023) reported that arbitrage transactions consumed 60% of block compute and that more than 98% of classified arbitrage transactions failed in that specific epoch. This is dated evidence and cannot be used as a 2026 failure-rate estimate, but it strongly rejects the assumption that cheap fees make landing easy.
4. **Confirmed fact — current public research artifacts exist.** A 2026 empirical bot study reports a dataset of 200 Solana bot addresses and more than 44 million on-chain transactions; a separate public Solana-MEV toolkit contains collectors and modules for atomic arbitrage, liquidations and sandwich detection. These sources support classifier design and replication, but their labels and attribution rules must be audited before reuse.

### 4.3 Historical-data access without a paid subscription

1. **Confirmed fact — Google BigQuery carries Solana archival data.** The Solana Foundation announced Solana data in Google's public dataset program. BigQuery is queryable without operating an archive node, but compute/scan cost and current table coverage must be measured; “public dataset” is not the same as unlimited free analysis.
2. **Confirmed fact — free downloadable Parquet data exists.** `solarchive.org` publishes no-key, CC-BY-4.0 Parquet partitions sourced from Solana Foundation BigQuery exports, with schemas and checksums. On the page inspected on 2026-09-25, the readiness table showed transaction partitions for only parts of the advertised history (including November–December 2025), while account/token snapshots were more broadly marked. The site itself says the complete archive exceeds 700 TB. It is useful for narrow, predicate-pushed experiments, not an invitation to download the chain.
3. **Confirmed fact — public RPC availability is provider-dependent.** `getTransaction` can return `null` when a record is not found, and `minimumLedgerSlot` exists because nodes may purge older ledger data. A free replay must therefore record the endpoint and its first available/minimum ledger boundary rather than assuming archive retention.
4. **Inference — a narrow event reconstruction is likely possible for little or no provider spend.** Three known signatures and a small surrounding slot window should fit public/explorer/bootstrap access if the records are retained. This inference is not yet confirmed because raw RPC responses were not collected in this sprint.
5. **Inference — a statistically useful 14-day all-venue scan is unlikely to be operationally free.** Even when the source dataset is public, query bytes, storage, egress and local compute are real costs. Address-first or program-first filtering can keep the first experiment small; a full-chain brute-force scan cannot.

## 5. Proven strategy classes and what “proven” means

| Strategy class | Evidence available | What remains unproven |
| --- | --- | --- |
| Two-venue atomic cycle | Public Jito bot design; DEX programs; project ANB fixture | 2026 frequency, net PnL, accessible landing rate |
| 3-hop triangular cycle | Public Jito bot explicitly evaluates 2/3-hop routes | Search-space economics after tips and state decay |
| Backrun after a large swap | Jito bot architecture and bundle ordering mechanics | Availability of trigger flow to a small independent team |
| Launch/migration dislocation | Meteora product surface and ANB-style project hypothesis | Recurrence, token-risk-adjusted returns, classifier precision |
| Liquidation | Jito's MEV documentation and public 2026 research toolkit | Scope, protocol-specific race mechanics and economics for this project |

Here “proven” means the mechanism and at least one implementation/research artifact are public. It does **not** mean profitable for this project.

## 6. ANB case as a fixture

The project currently records:

- arbitrage signature: `J8TY8VkjZpAAm78GwbnEE1xkBwGdheQ4C1VsZA7Cwcv1AyDw3PxTQJ3eWh9YZmZyLQnLD3fuHBsihXbX4sTATi8`;
- signer: `ESuvjvsQtjuxC4XGsDeMhx8Wp5yjQcCFGncGhupcJbg8`;
- slot: `416936448`;
- route: `0.227 USDC → 72,793.511082 ANX → 50,011,673.082571 ANB → 696,194.449401 USDC`;
- project-observed signer USDC delta: approximately `+696,194.222401 USDC`;
- project-observed SOL delta: approximately `-2.300174466 SOL`, described as mainly a Jito tip;
- trigger signature: `5wY3V7v8ALqB5hGj1vkqttLy4T65awaeTkm6G4oxt4xfvndrqFA7kLwqQq4VJzw8338B1YZyPFHooueCMyujxkFK`;
- earlier intermediate arbitrage: `5oiBGWFxs87reNtQSH2ZCmqyp9bcVgFp78FgCjPq7zaW4m1JXsfNPFGK3qeUCcYj4c7MpsEAWerHa68b2HfiVHor`.

**Deterministic arithmetic from the recorded route:**

```text
696,194.449401 USDC - 0.227000 USDC = 696,194.222401 USDC
```

This reconciles the stated USDC delta, but it is not yet an independent chain reproduction. The USD value of the SOL cost is intentionally not calculated without an explicit price source and timestamp. The fixture must remain marked `provisional` until raw `getTransaction`/`getBlock` responses are preserved and the following are independently reconciled:

1. all account keys including Address Lookup Tables;
2. outer and inner instructions in execution order;
3. token decimals and pre/post token balances for the signer-controlled accounts;
4. SOL fee, priority fee, Jito-tip transfer, rent debits and rent refunds;
5. concrete Meteora pool accounts and deployed program versions;
6. trigger/arbitrage ordering within the slot and neighboring slots;
7. whether any residual ANX/ANB inventory remained;
8. failed and successful competing attempts touching the same writable pool state.

No additional transaction or wallet is added by this screen because none was independently verified from a preserved raw record.

## 7. Competition and access assessment

### Confirmed

- Landing competition is sensitive to both account-lock conflicts and tip/CU efficiency; it is not a single global highest-tip queue.
- Jito provides regional Block Engine endpoints, including Amsterdam, Dublin, Frankfurt and London, so physical/network placement is measurable rather than abstract.
- Jito's own documentation says ShredStream can save hundreds of milliseconds. That is a vendor statement about its service, not a measured advantage for this project.
- The old public Jito bot recommends a multicore Linux host near the RPC and Block Engine, a Geyser feed, simulation support and 16 GB RAM for its four-worker configuration. This is implementation evidence from an obsolete reference bot, not a current minimum specification.

### Unknown

- Number of active independent searchers for our exact venue/token universe.
- Top-1/top-3/top-10 realized-profit concentration.
- Current landed-to-submitted ratio and off-chain rejection cost.
- Tip-to-gross distribution for successful cycles.
- Whether normal account/program subscriptions are fast enough for any positive candidates after 100/250/500 ms.
- Whether DoubleZero Edge or another shred/geyser path is required before paper monitoring.

### Screening implication

Buying low-latency infrastructure before measuring candidate decay is not justified. Conversely, a profitable zero-latency historical quote would not be evidence of accessibility. The paper monitor must timestamp source receipt, decode, route calculation and signed-ready simulation separately.

## 8. Historical replay feasibility matrix

| Need | Free/low-cost path | Limitation | Screen result |
| --- | --- | --- | --- |
| Known transaction receipt | Public RPC / official explorer | Retention, rate limits, explorer rendering | Feasible for fixtures; verify |
| Slot transaction order | `getBlock` on retained history | Large response; provider retention | Feasible for narrow windows |
| Address/program history | `getSignaturesForAddress` | Pagination and address-selection bias | Feasible for targeted collection |
| Broad transaction scan | BigQuery public dataset | Bytes scanned and schema/coverage checks | Feasible but not guaranteed free |
| Downloadable bulk history | solarchive Parquet | Very large; incomplete readiness table; lag | Useful only where partition exists |
| Exact historical pool pre-state | Replay writes or historical account-state source | Hardest requirement; snapshots may be insufficient | Unresolved blocker |
| Live basic observation | RPC WebSocket subscriptions | Provider gaps and latency | Feasible for paper bootstrap |
| Competitive low-latency observation | DoubleZero/shred or provider Geyser | Commercial/access/ops requirements | Defer until decay evidence |

## 9. Screening metrics

No empirical opportunity sample was collected. Required metrics therefore remain explicitly unknown:

- opportunities/day: `unknown`;
- profitable opportunities/day after costs: `unknown`;
- trade-net PnL distribution: `unknown`;
- recurring versus tail contribution: `unknown`;
- failure cost per success: `unknown`;
- opportunity lifetime and delay curve: `unknown`;
- winner concentration: `unknown`;
- fully loaded infrastructure break-even: `unknown`.

The report deliberately does not substitute DEX volume, Jito tip volume or an exceptional ANB route for these metrics.

## 10. Findings by confidence

### High confidence

- Atomic multi-leg execution and Jito bundles can represent the target cycles.
- Meteora/Raydium/Orca have public documentation or SDK/source artifacts sufficient to begin deterministic decoder/quoter work.
- Jito's 50 ms account-lock-aware auction makes tip bidding, requested CU and landing status first-class variables.
- Public RPC can support bounded forensics but is rate-limited and not a production data path.

### Medium confidence

- Known-signature and narrow-slot reconstruction can likely begin without paid data.
- A small team can build the offline decoder/quoter before buying a low-latency feed.
- The ANB event is an appropriate decoder and accounting fixture after independent raw-data reproduction.

### Low confidence / hypothesis

- A recurring positive edge survives at latency available to a small independent searcher.
- ANB-like tail events occur often enough to cover continuous operating cost.
- The old public Jito-bot architecture remains competitively relevant in 2026.

## 11. Decision and next bounded experiment

**Decision: HOLD.** Do not shortlist Solana for live paper monitoring yet; do proceed with a narrow historical reconstruction because the unresolved questions are measurable.

### Experiment SOL-HR-001 — ANB raw reconstruction

- Duration: 1–3 engineering days after an archival endpoint/dataset is selected.
- Data budget: start with public RPC/explorer and public BigQuery metadata; authorize paid archival calls only after recording the exact missing records and estimated bytes/requests.
- Inputs: the three signatures above; slot `416936448`; complete transactions for the slot and minimally necessary neighboring slots; all touched account/program identifiers.
- Deliverables: immutable raw JSON with hashes; manifest; decoded instruction/transfer ledger; cost ledger; provisional pool registry; list of missing historical account states.
- Success criterion: reproduce signer USDC and SOL deltas exactly in base units and attribute every material debit/credit to swap output, fee, priority fee, tip, rent or residual inventory.
- Failure criterion: required raw transactions are unavailable from all zero/low-cost sources, or balance changes cannot be reconciled without an unobservable assumption.
- Gate to SOL-HR-002: only after SOL-HR-001, test whether exact pool pre-state can be reconstructed and whether the quote engine matches each observed swap output to the smallest token unit or a documented tolerance.

## 12. Contradictory or missing evidence

- `solarchive.org` describes an eventual/target complete archive, while its inspected readiness table showed materially incomplete transaction partitions. Use the readiness index, not the marketing summary, when planning a date range.
- Jito's 2023 epoch-414 failure statistics demonstrate intense historical competition but are too old and too narrowly sampled to estimate 2026 performance.
- Public implementation repositories prove that strategies were implementable; they do not prove current profitability, current order-flow access or maintenance quality.
- The project-level ANB route reconciles arithmetically, but raw chain data was not preserved in this sprint. It must not yet become an asserted test vector in code.
- Off-chain rejected bundles and unsubmitted losing quotes are not observable from chain history, so on-chain failure cost is a lower bound.

## 13. Artifacts and source register

The detailed source register, evidence type and limitations are in [`../evidence/solana-sources.md`](../evidence/solana-sources.md). No raw chain dataset or new address list was produced in this screen.


# Infrastructure cost screen: Solana, Base, Robinhood Chain, Ethereum

Status date: **2026-09-25**  
Scope: research infrastructure for historical replay, live paper monitoring, and eventual competitive submission.  
Currency: USD, excluding tax. Prices are monthly unless stated otherwise.

This is a dated infrastructure screen, not a profitability estimate or a procurement quote. Provider prices, chain requirements, traffic, data retention, and auction costs can change. Recheck every price and capability before purchase.

## Short conclusion

**Confirmed:** a bounded prototype does not require a node or expensive low-latency feed. Existing hardware plus free RPC tiers can support registry work and small samples. Helius offers 1M credits and standard LaserStream WebSockets for $0; Alchemy offers 30M compute units and 25 requests/second for $0; QuickNode offers a one-month $0 trial with 10M credits and 15 requests/second.

**Recommendation:** start with provider APIs and local storage. Do not buy a dedicated node, raw shreds, or custom capacity until a 7–14 day paper monitor shows that feed or submission latency—not pool math, missing market access, or insufficient edge—is the binding constraint.

**Confirmed:** Solana is the only network in this screen with a clearly published retail-priced path from ordinary RPC to a low-latency trading stack. Helius Business plus raw shreds is **$1,499/month** before server, storage, traffic add-ons, tips, and transactions. Helius Professional plus raw shreds is **$1,799/month**. A dedicated Helius Solana node starts at **$2,900/month**.

**Unknown:** no official public source establishes a complete fixed monthly price for a competitive Base, Robinhood Chain, or Ethereum searcher. Provider usage can be priced, but dedicated endpoints, peering, relay coverage, server colocation, and high-throughput agreements are commonly custom-priced. Any single dollar total for those stacks would therefore be an estimate, not a confirmed fact.

## Cost taxonomy

| Cost class | Examples | Treatment in research economics |
|---|---|---|
| One-time | Purchased server/NVMe, setup, data backfill, snapshot download | Amortize separately; no official market-wide price is assumed here |
| Monthly fixed | RPC plan, dedicated node, stream subscription, server rental | Period cost; allocate to fully loaded PnL, not per-trade PnL |
| Usage-variable | API credits, stream TB, egress, object storage, L1-provider calls | Record from invoices/telemetry by experiment |
| Execution-variable | gas/base fee, priority fee, Jito tip, builder payment, reverted included attempts | Include in trade net PnL |
| Capital/risk | inventory, gas balance, bridge/rebalancing float | Not an infrastructure expense; report separately as capital at risk |

No labor, external audit, legal, tax, or trading capital is included.

## Published provider price anchors

These are useful planning anchors, not interchangeable products.

| Provider / product | Free or entry | Paid self-serve | Low-latency / dedicated | Important boundary |
|---|---:|---:|---:|---|
| Helius, Solana | $0: 1M credits, 10 RPS, standard LaserStream WSS | Developer $49: 10M credits, 50 RPS | Business $499 includes LaserStream WSS/gRPC; Professional $999; dedicated node from $2,900 | Mainnet gRPC begins at Business. Raw shreds cost separately: $1,000/IP on Free/Developer/Business, $800/IP on Professional |
| Helius stream add-on | Included allowance depends on plan | Additional 5 TB $400; 10 TB $750; 25 TB $1,750; 50 TB $3,250; 100 TB $6,000 | Enterprise custom | Add-ons are for LaserStream WSS/gRPC; do not treat them as node rental |
| Alchemy, multi-chain | $0: 30M CU, 25 RPS | PAYG $0.525 per 1M CU; 300 RPS / 10,000 CU/s included | Enterprise custom; capacity above included throughput can add $160/month per 5,000 CU/s block | Method mix determines CUs. Trace/debug availability and chain support must be checked per network |
| Alchemy Solana gRPC | None on Free | Starts at $75/TB on PAYG | Enterprise custom | A usage charge, not a fixed subscription |
| QuickNode, multi-chain | One-month $0 trial: 10M credits, 15 RPS | Build $49 month-to-month ($34/month billed annually): 80M credits, 50 RPS; Accelerate $249; Scale $499 | Dedicated and enterprise are custom; Solana gRPC is plan/add-on dependent | Credit multipliers and retention differ by method/product; model from the actual workload |

### Why the published tiers do not prove competitiveness

RPS and included credits measure capacity, not first-observation latency, state freshness, geographic proximity, landing probability, builder coverage, or sequencer access. A higher tier can remove rate-limit failures without improving the part of the pipeline that loses a trade. Any upgrade must be tied to measured `source -> receipt -> decode -> quote -> simulate -> submit` latency and missed-opportunity attribution.

## Network comparison

### Solana

#### Prototype / historical replay

Recommended minimum:

- Helius Free or QuickNode trial for bounded discovery and small transaction samples;
- Helius Developer ($49/month) when the free quota or RPS blocks reproducible collection;
- local compressed raw responses/Parquet and a checkpointed collector;
- Jito endpoints only for read-only integration and later paper submission modeling.

Helius lists archival data across its plan comparison. Historical **account state at an arbitrary slot** is still a separate capability question: archival transactions do not automatically provide exact historical account snapshots. Confirm the chosen replay method before bulk backfill.

Expected fixed provider spend: **$0–49/month** for the initial bounded study, excluding compute/storage. This is a planning range derived from the published free and Developer tiers, not a guarantee that a full 14-day all-pool backfill fits the quota.

#### Live paper monitor

- Helius Developer ($49) can support a narrow allowlist over standard WSS.
- Mainnet LaserStream gRPC is published from Business ($499).
- Extra LaserStream volume begins at $400 for 5 TB.
- A second independent provider is recommended for latency and gap measurement, but its cost depends on chosen tier and usage.

Practical fixed-provider envelope: **$49–899/month** before host/storage, using Developer for narrow WSS at the low end or Business plus the smallest published data add-on at the high end. The $899 figure is arithmetic (`$499 + $400`), not a packaged plan.

#### Competitive path

- Helius Business + raw shreds: **$1,499/month** (`$499 + $1,000/IP`).
- Helius Professional + raw shreds: **$1,799/month** (`$999 + $800/IP`).
- Helius dedicated node: **from $2,900/month**; exact configuration and colocation cost can be higher.
- Jito Block Engine access has a default **1 request/second per IP per region** and documents a **1,000-lamport minimum bundle tip**. No subscription price is published in the cited Jito docs. Competitive tips are auction-dependent and must be modeled as variable execution cost.
- Helius Sender is included with all Helius plans and documents a 0.000005 SOL minimum tip; that minimum is not evidence of a competitive bid.

Running an Agave RPC node oneself is not a budget shortcut. Official recommendations are 16 cores / 32 threads or more for an RPC node, 512 GB RAM for all account indexes, separate high-IOPS NVMe for accounts and ledger, and at least 1 Gbit/s symmetric networking for an unstaked node. Hardware/server pricing is not published by Anza and is therefore left **unpriced**.

**Recommendation:** do not self-host Solana in Stage 1 or 2. First quantify whether standard WSS loses otherwise valid opportunities. If it does, A/B test LaserStream gRPC before buying raw shreds or a dedicated node.

### Base

#### Prototype / historical replay

- Base public RPC is free but rate-limited, HTTP-only, and explicitly unsuitable for production traffic.
- All Base public endpoints are Flashblocks-enabled; `pending` state is updated roughly every 200 ms.
- WebSocket subscriptions require a compatible provider.
- Alchemy Free or the QuickNode free trial can cover bounded calls; archive reads and traces should be validated on the selected plan before collection.

Expected fixed provider spend: **$0** while bounded work fits a free tier. PAYG archive/trace workloads are usage-variable; with Alchemy the published unit is **$0.525 per 1M CU**. A request count alone cannot determine the bill because methods consume different CUs.

#### Live paper monitor

- use two independent Flashblocks-aware WSS providers;
- preserve raw Flashblock/preconfirmation timestamps and ordinary canonical blocks;
- use a separate archive/trace path if the live provider does not retain sufficient history.

No official source supplies a defensible universal monthly total for this dual-provider arrangement. A low-traffic monitor may remain within free/PAYG tiers; a full feed plus traces may not. Instrument CUs/credits and set provider spend caps.

#### Competitive path

Base documents normal transaction submission through `eth_sendRawTransaction`; it does not document an Ethereum-style public bundle relay that guarantees adjacency for this use case. Costs are therefore:

- provider/dedicated capacity: **custom or usage-based**;
- server close to the chosen provider/sequencer ingress: **unpublished**;
- L2 execution plus L1 data-related transaction fee: **variable**;
- reverted included attempts: **variable and paid**.

A self-hosted Base node requires at least an 8+ core modern CPU, 32 GB RAM (64 GB recommended), locally attached NVMe, and storage of approximately `2 x current chain size + snapshot size + 20%`. The official guide publishes requirements, not a server price. Self-host only to measure/control feed lag after provider evidence justifies it.

### Robinhood Chain

#### Prototype / historical replay

- official public RPC, sequencer feed, and sequencer endpoint are available without a published access fee, but are rate-limited and not recommended for production;
- Robinhood recommends Alchemy and explicitly says to use an archive endpoint for historical reads;
- Alchemy Free (30M CU, 25 RPS) is the natural first test; QuickNode and other named providers are alternatives.

Expected fixed provider spend: **$0** for a bounded registry and event sample if free quotas suffice. Archive, traces, and larger backfills become PAYG/custom.

#### Live paper monitor

- consume the public sequencer feed and a provider WSS simultaneously;
- compare receive time and gaps rather than assuming the feed is a pre-mempool advantage;
- use archive RPC for reconstruction;
- retain L1 fee components and Ethereum parent-chain dependencies.

No public official price is listed for the sequencer feed or sequencer endpoint. Availability without a listed fee must not be interpreted as a production SLA.

#### Competitive path

Robinhood Chain's FCFS ordering makes end-to-end arrival latency central. The public direct sequencer endpoint is documented, but the official terms provide no uptime/latency guarantee. A credible competitive stack may require:

- a feed-connected local Nitro node;
- direct sequencer submission;
- a production RPC/archive provider;
- Ethereum execution and beacon endpoints for the node;
- geographically suitable compute/networking.

Official node requirements: modern 8+ core CPU, 64 GB RAM (128 GB recommended), locally attached NVMe, and `(2 x current chain size) + 20%` with several TB of data. Archive requires substantially more. Initial sync can consume significant L1 request quota.

The complete competitive monthly cost is **unknown** because node hosting, archive storage, L1 endpoints, and production provider terms are not published as one package. Do not insert an invented estimate into the network scorecard; obtain measured traffic plus vendor quotes after the monitor validates a strategy.

### Ethereum

#### Prototype / historical replay

- Alchemy Free or QuickNode trial can support bounded block/receipt/log sampling;
- Alchemy PAYG is $0.525 per 1M CU when archive/trace usage exceeds free eligibility;
- `debug_trace*` / trace availability must be verified for the chosen plan and client;
- Flashbots relay can be integrated for simulation/submission research without a published subscription fee.

Expected fixed provider spend: **$0** for a small sample; historical trace-heavy work is usage-variable.

#### Live paper monitor

- at least two public-mempool feeds because any one feed is incomplete;
- MEV-Share event stream for private-flow hints;
- Flashbots bundle simulation and outcome tracking;
- ordinary canonical RPC/archive/traces for reconciliation.

Public mempool monitoring still cannot observe all private order flow. Paying for more RPC capacity does not remove this structural blind spot.

#### Competitive path

- Flashbots `relay.flashbots.net` supports `eth_sendBundle` and publishes a rate limit of 10,000 requests/second/IP; the cited docs publish no access subscription fee.
- The economic bid is embedded in priority fees/direct fee-recipient payments/refunds and is **variable**.
- Multi-builder/relay coverage, dedicated RPC, high-throughput mempool access, and colocated compute may be necessary; official self-serve prices for a complete stack are not published.
- Included reverted public transactions pay gas; losing private bundles may not land, but submission/simulation infrastructure and opportunity bids still need measurement.

A reference Ethereum full node profile recommends 4 TB NVMe, 32 GB RAM, 4 cores / 8 threads, and 50/15 Mbps download/upload. A local block builder profile rises to 64 GB, 8 cores / 16 threads, and 100/50 Mbps. These are hardware recommendations, not hosted-node prices. An arbitrage searcher does not need to become a validator or local block builder merely to use Flashbots.

## One-time, monthly, and variable matrix

| Network | One-time | Prototype monthly | Competitive monthly | Execution-variable |
|---|---|---:|---:|---|
| Solana | Optional local storage; self-host hardware unpriced | $0–49 provider tier | Published provider floor $1,499 with Business + one raw-shred IP; dedicated starts $2,900 | base fee, priority fee, Jito/Sender tip, paid failed attempts |
| Base | Optional local storage; self-host hardware unpriced | $0 plus PAYG overflow | Unknown: PAYG/custom provider + host/node | L2 execution, L1 data fee, priority fee, reverts |
| Robinhood Chain | Optional local storage; several-TB node if later justified | $0 plus PAYG archive/trace overflow | Unknown: Nitro node + L1 endpoints + provider/archive + compute | L2 execution, L1 data fee, failed attempts |
| Ethereum | Optional local storage; 4-TB-class node if later justified | $0 plus PAYG archive/trace overflow | Unknown: node/feed/provider/relay-builder coverage is not sold as one public package | base fee, priority/direct builder payment, refunds, included reverts |

The Solana $1,499 number is not a complete operating budget: it excludes host, storage, redundancy, extra stream data, and execution bids. The $0 entries mean “no fixed provider invoice within a free quota,” not zero total cost.

## Recommended staged procurement

### Stage 1 — network screen and bounded history

1. Use existing compute and free tiers.
2. Put a hard cap on block ranges and methods.
3. Record request count, CU/credit use, bytes received, and missing methods.
4. Upgrade only the provider that blocks a declared dataset.

Procurement trigger: the dataset cannot be completed reproducibly under free quotas/rate limits.

### Stage 2 — 7–14 day paper monitor

1. Narrow to at most two networks.
2. Use two independent live sources per shortlisted network.
3. Retain provider receive timestamps, disconnects, gaps, and invoice units.
4. Compare standard versus faster feeds on the same events.

Procurement trigger: opportunities remain positive after costs and decay, and feed delay is measurably responsible for missed executable candidates.

### Stage 3 — competitive infrastructure experiment

1. Buy the smallest low-latency upgrade that addresses the measured bottleneck.
2. Run an A/B paper test before enabling funded submission.
3. Allocate fixed infrastructure separately from trade-level variable costs.
4. Require an incremental PnL estimate to exceed incremental infrastructure spend under conservative assumptions.

Procurement trigger: a guarded tiny-live test is approved under the repository's research and security gates.

## Missing data and next test

Material unknowns:

- actual CU/credit/TB consumption for this repository's collector filters;
- provider-specific latency from the intended server region;
- exact archive/trace availability for Robinhood Chain on each paid plan;
- Base and Robinhood dedicated-node/peering quotes;
- complete Ethereum builder/relay coverage and commercial terms;
- current chain/snapshot sizes and therefore real node disk cost;
- execution bid distributions during the selected strategy windows.

**Recommended next test:** implement a 24-hour read-only traffic probe for one narrow market set on each network. Record requests, bytes, reconnects, p50/p95/p99 receive lag, missing data, archive/trace success, and simulated provider cost. Use that output—not generic monthly plans—to price the 14-day monitor.

## Evidence and provenance

All factual claims and official URLs are registered in [`evidence/infrastructure-sources.md`](evidence/infrastructure-sources.md). Retrieval date: 2026-09-25.

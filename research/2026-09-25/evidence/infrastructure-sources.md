# Infrastructure source register

Retrieval date: **2026-09-25**  
Scope: official documentation and official provider pricing used by `research/2026-09-25/infrastructure-costs.md`.

No third-party comparison, affiliate page, social-media post, or unsourced hosting estimate is used as primary evidence. Prices are mutable; preserve this retrieval date and recheck before procurement.

## E1 — Helius plans, archive, streams, shreds, Sender, dedicated nodes

**Claim:** Helius publishes Free ($0), Developer ($49), Business ($499), Professional ($999), raw-shred prices by IP, LaserStream data add-ons, Sender minimum tip, and dedicated nodes from $2,900/month.

**Classification:** Confirmed fact.

**Scope:** Solana; RPC, archive, WSS/gRPC, raw shreds, submission, dedicated node.

**Primary evidence:**

- https://www.helius.dev/pricing
- Retrieval date: 2026-09-25

**Relevant published values:**

- Free: 1M credits, 10 RPS, 1 `sendTransaction`/s, standard LaserStream WSS.
- Developer: $49/month, 10M credits, 50 RPS, 5 `sendTransaction`/s, staked connections.
- Business: $499/month, 100M credits, 200 RPS, 50 `sendTransaction`/s, 5 `sendBundle`/s, LaserStream WSS/gRPC.
- Professional: $999/month, 200M credits, 500 RPS.
- Raw shreds: $1,000/month/IP on Free, Developer, Business; $800/month/IP on Professional.
- LaserStream add-ons: 5 TB $400; 10 TB $750; 25 TB $1,750; 50 TB $3,250; 100 TB $6,000.
- Sender: included with all plans; 0.000005 SOL minimum tip.
- Dedicated nodes: starting at $2,900/month.
- The comparison table marks archival data as available across listed plans.

**Limitations:** plan inclusion does not establish latency from our deployment, adequate throughput for our filters, or a competitive tip. Enterprise and optimized configurations are custom.

## E2 — Alchemy multi-chain pricing

**Claim:** Alchemy publishes a 30M-CU free tier, PAYG at $0.525/1M CU, 300 RPS/10,000 CU/s included on PAYG, extra capacity at $160 per 5,000 CU/s block, and Solana gRPC from $75/TB.

**Classification:** Confirmed fact.

**Scope:** multi-chain provider; Ethereum, Base, Robinhood Chain, Solana where supported.

**Primary evidence:**

- https://www.alchemy.com/pricing
- Retrieval date: 2026-09-25

**Relevant published values:**

- Free: 30M CU/month, 25 RPS, five apps and five webhooks.
- PAYG: $0.525/1M CU, starting from 300 RPS; 10,000 CU/s included.
- Additional capacity: $160/month per additional 5,000 CU/s block; self-serve capacity ends at 30,000 CU/s.
- Solana gRPC: starting at $75/TB on PAYG.
- Full archive and premium/debug/trace capabilities vary by tier and chain.

**Limitations:** CUs vary by method. The price does not prove every method/product is available on every chain. Confirm archive, trace, WebSocket, and Robinhood Chain coverage in the account before collection.

## E3 — QuickNode plans and multi-chain coverage

**Claim:** QuickNode publishes a one-month $0 trial, Build at $49 month-to-month, higher self-serve tiers, credit overage rates, and supports all four project networks.

**Classification:** Confirmed fact.

**Scope:** multi-chain RPC/streams.

**Primary evidence:**

- https://www.quicknode.com/pricing
- https://www.quicknode.com/chains/solana
- https://www.quicknode.com/chains/robinhood
- Retrieval date: 2026-09-25

**Relevant published values:**

- Free trial: one month, 10M API credits, 15 RPS, no overage.
- Build: $49 month-to-month or displayed as $34/month billed annually, 80M credits, 50 RPS; $0.62/additional 1M credits.
- Accelerate: $249 month-to-month, 450M credits, 125 RPS.
- Scale: $499 month-to-month, 950M credits, 250 RPS.
- Dedicated/Enterprise: custom.
- Pricing page lists Solana, Ethereum, Base, and Robinhood Chain among supported chains.

**Limitations:** archive, traces, stream retention, gRPC, and add-ons differ by tier. Credit count is not request count; calculate from actual methods and payloads.

## E4 — Jito low-latency submission and ShredStream

**Claim:** Jito documents regional Block Engine endpoints, atomic bundles, a 1,000-lamport minimum bundle tip, a default 1 request/second/IP/region limit, and ShredStream as a low-latency block update path.

**Classification:** Confirmed fact.

**Scope:** Solana; submission relay and low-latency data.

**Primary evidence:**

- https://docs.jito.wtf/lowlatencytxnsend/
- https://docs.jito.wtf/lowlatencytxnfeed/
- Retrieval date: 2026-09-25

**Relevant published details:**

- Bundles contain up to five transactions and execute sequentially and atomically in one slot.
- A received bundle ID does not guarantee landing.
- Default limit: 1 request/second per IP per region; higher limits require a ticket.
- Minimum tip: 1,000 lamports; competitive tip depends on auction demand.
- Jito runs parallel auctions on 50 ms ticks and prioritizes conflicting bundles by tip/CU efficiency.
- ShredStream is positioned as the lowest-latency shred feed.

**Limitations:** the cited docs do not publish a ShredStream or Block Engine subscription price. Tip floors are not winning-bid forecasts.

## E5 — Solana fees and Agave node requirements

**Claim:** Solana charges a base fee plus optional prioritization fee; an Agave RPC node has materially higher official hardware recommendations than a normal application server.

**Classification:** Confirmed fact.

**Scope:** Solana; variable transaction cost and self-hosting.

**Primary evidence:**

- https://solana.com/docs/core/fees
- https://docs.anza.xyz/operations/requirements
- Retrieval date: 2026-09-25

**Relevant published details:**

- Base fee: 5,000 lamports per signature.
- Prioritization fee: computed from CU price and requested CU limit.
- RPC node: 16 cores / 32 threads or more; 512 GB RAM for all account indexes.
- NVMe: accounts 1 TB+, ledger 1 TB+, snapshots 500 GB+; separate accounts/ledger disks recommended.
- Networking: 1 Gbit/s symmetric sufficient for an unstaked node; higher for staked nodes.

**Limitations:** Anza publishes specifications, not hardware or hosting prices. Requirements can grow with the network and index configuration.

## E6 — Base public RPC, Flashblocks and node requirements

**Claim:** Base public endpoints are free/rate-limited and HTTP-only, support Flashblocks pending state, while a self-hosted node requires 8+ CPU cores, 32/64 GB RAM, NVMe, and dynamically sized storage.

**Classification:** Confirmed fact.

**Scope:** Base; RPC, preconfirmation stream, submission, node.

**Primary evidence:**

- https://docs.base.org/base-chain/quickstart/connecting-to-base
- https://docs.base.org/base-chain/api-reference/rpc-overview
- https://docs.base.org/specifications/node-operators/performance-tuning
- https://docs.base.org/base-chain/node-operators/run-a-base-node
- Retrieval date: 2026-09-25

**Relevant published details:**

- Public endpoints are rate-limited and unsuitable for production.
- Public Base endpoints are HTTP-only; WSS requires a provider.
- `pending` state on Flashblocks endpoints updates approximately every 200 ms.
- Standard submission uses `eth_sendRawTransaction`.
- Node minimum: modern 8+ core CPU, at least 32 GB RAM (64 GB recommended), local NVMe.
- Storage formula: `2 x current chain size + snapshot size + 20% buffer`.

**Limitations:** Base does not publish a single production RPC/colocation price or a public bundle product equivalent to Ethereum Flashbots for this workflow. Current chain size and provider method availability are mutable.

## E7 — Robinhood Chain endpoints, archive guidance and node requirements

**Claim:** Robinhood Chain publishes rate-limited public RPC, sequencer feed, and sequencer endpoints; recommends Alchemy and archive endpoints for history; and documents substantial full-node requirements plus L1 endpoint dependencies.

**Classification:** Confirmed fact.

**Scope:** Robinhood Chain; RPC, stream, archive, submission, node.

**Primary evidence:**

- https://docs.robinhood.com/chain/connecting/
- https://docs.robinhood.com/chain/run-a-full-node/
- https://docs.robinhood.com/chain/terms-of-service/
- Retrieval date: 2026-09-25

**Relevant published details:**

- Public mainnet RPC: `https://rpc.mainnet.chain.robinhood.com`.
- Sequencer feed: `wss://feed.mainnet.chain.robinhood.com`.
- Sequencer: `https://sequencer.mainnet.chain.robinhood.com`.
- Public endpoints are rate-limited and not recommended for production.
- Alchemy is the recommended provider; historical reads should use archive access.
- Full node: modern 8+ core CPU, 64 GB RAM (128 GB recommended), local NVMe, several TB; archive requires more.
- Node requires Ethereum execution RPC and beacon endpoints; initial sync can consume significant L1 quota.
- The official terms disclaim uptime/latency guarantees for the public infrastructure.

**Limitations:** no fee or SLA is published for the public sequencer feed/endpoint. The complete production stack cannot be priced without provider/server quotes and measured L1 usage.

## E8 — Ethereum node requirements

**Claim:** a current Ethereum hardware recommendation specifies 4 TB NVMe and distinguishes ordinary full-node requirements from validator/local-builder requirements.

**Classification:** Confirmed fact.

**Scope:** Ethereum; self-hosted execution + consensus node.

**Primary evidence:**

- https://eips.ethereum.org/EIPS/eip-7870
- https://ethereum.org/developers/docs/nodes-and-clients/run-a-node/
- Retrieval date: 2026-09-25

**Relevant published details:**

- Full node: 4 TB NVMe, 32 GB RAM, 4 cores / 8 threads, 50 Mbps down / 15 Mbps up.
- Local block builder: 4 TB NVMe, 64 GB RAM, 8 cores / 16 threads, 100/50 Mbps.
- An Ethereum node runs execution and consensus clients; staking is not required to run a node.

**Limitations:** EIP-7870 is a hardware recommendation, not a cloud price quote or a requirement to operate a searcher. Archive nodes can require different retention/storage.

## E9 — Flashbots relay and bundle economics

**Claim:** Flashbots exposes a public relay for Ethereum bundles, documents a 10,000 requests/second/IP limit, and uses economic bundle bids rather than a published access subscription.

**Classification:** Confirmed fact for endpoint/rate limit and auction mechanics; absence of a listed subscription is an observation of the cited documentation, not a guarantee of perpetual free access.

**Scope:** Ethereum; private bundle submission.

**Primary evidence:**

- https://docs.flashbots.net/flashbots-auction/advanced/rpc-endpoint
- https://docs.flashbots.net/flashbots-auction/advanced/troubleshooting
- https://docs.flashbots.net/flashbots-auction/overview
- Retrieval date: 2026-09-25

**Relevant published details:**

- Mainnet bundle relay: `https://relay.flashbots.net`.
- Rate limit: 10,000 requests/second per IP.
- `eth_sendBundle` accepts ordered signed transactions for a target block.
- Auction competitiveness is expressed through effective priority fee / direct economic payment; losing private bundles need not be included onchain.

**Limitations:** one relay does not imply all-builder coverage or inclusion. The cited pages publish no complete monthly price for multi-builder searcher infrastructure. Gas, builder payments, refunds, and opportunity bids remain variable.

## E10 — Derived price arithmetic

**Claim:** the published Helius Business + one raw-shred IP combination is $1,499/month, and Professional + one raw-shred IP is $1,799/month.

**Classification:** Derived result.

**Method:**

- Business: `$499 + $1,000 = $1,499`.
- Professional: `$999 + $800 = $1,799`.
- Source inputs: E1.

**Limitations:** these totals exclude host compute, storage, redundancy, extra LaserStream TB, taxes, and all transaction fees/tips. They are not complete trading budgets or evidence of profitability.

## Reproduction checklist

1. Open every primary URL above.
2. Record the new retrieval date and preserve screenshots/PDFs if procurement depends on the value.
3. Reconcile plan price, billing cadence, included quota, overage unit, RPS/CU/s, archive retention, trace/debug access, WSS/gRPC availability, regional endpoints, and support/SLA.
4. For node sizing, retrieve current chain and snapshot sizes rather than reusing this dated record.
5. Run a 24-hour traffic probe and calculate projected monthly units from actual method mix and bytes.
6. Treat tips, gas, builder payments, and failed attempts as execution-variable costs, not RPC subscription costs.

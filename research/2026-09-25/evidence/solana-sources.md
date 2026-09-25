# Solana screening source register — 2026-09-25

All mutable web sources were checked on 2026-09-25. “Primary” means protocol/network documentation, official source repository, raw chain identifier, or the authors' research artifact. It does not imply that every claim made by a vendor has been independently measured.

| ID | Source | Type | Used for | Limitation |
| --- | --- | --- | --- | --- |
| SOL-001 | [Solana: transactions](https://solana.com/docs/core/transactions) | Primary documentation | Transaction structure and atomic multi-instruction model | Does not establish market economics |
| SOL-002 | [Solana: fees](https://solana.com/docs/core/fees) | Primary documentation | Base/priority fee and compute-budget model | Fee market changes; recheck before implementation |
| SOL-003 | [Solana RPC: `getTransaction`](https://solana.com/docs/rpc/http/gettransaction) | Primary documentation | Confirmed transaction, slot, metadata and version retrieval | May return `null`; retention is endpoint-dependent |
| SOL-004 | [Solana RPC: `getBlock`](https://solana.com/docs/rpc/http/getblock) | Primary documentation | Transaction order and full slot context | Large responses and provider limits |
| SOL-005 | [Solana RPC: `getSignaturesForAddress`](https://solana.com/docs/rpc/http/getsignaturesforaddress) | Primary documentation | Targeted address/program discovery | Address-first sampling bias; pagination required |
| SOL-006 | [Solana RPC: `minimumLedgerSlot`](https://solana.com/docs/rpc/http/minimumledgerslot) | Primary documentation | Evidence that nodes may retain only a ledger suffix | Not the same as a guarantee for every history method |
| SOL-007 | [Solana: clusters and public RPC endpoints](https://solana.com/docs/references/clusters) | Primary documentation | Public mainnet endpoint, rate limits, non-production warning | Limits may change without notice |
| SOL-008 | [Solana RPC WebSocket methods](https://solana.com/docs/rpc/websocket) | Primary documentation | Basic live subscription surface | Availability and latency vary by provider |
| SOL-009 | [Jito: low-latency transaction send](https://docs.jito.wtf/lowlatencytxnsend/) | Primary vendor documentation | Max-five atomic bundles, landing caveat, 50 ms local auctions, tip/CU ranking, regional endpoints, uncled-block warning | Vendor mechanics; actual project latency/landing must be measured |
| SOL-010 | [Jito: low-latency block updates](https://docs.jito.wtf/lowlatencytxnfeed/) | Primary vendor documentation | Shred feed function and 2026 migration warning to DoubleZero Edge | “Hundreds of milliseconds” is a vendor claim, not our benchmark |
| SOL-011 | [Jito Foundation: Solana MEV epoch-414 analysis](https://www.jito.network/blog/solving-the-mev-problem-on-solana-a-guide-for-stakers/) | Primary ecosystem analysis | Historical 60% compute / >98% failed arbitrage figures | Single 2023 epoch; classifier and raw dataset not reviewed here |
| SOL-012 | [Jito Labs `mev-bot`](https://github.com/jito-labs/mev-bot) | Primary source repository | Concrete circular-backrun architecture, 2/3 hops, Geyser cache, flash loan and bundle path | Explicitly unmaintained and not production-ready |
| SOL-013 | [Meteora documentation](https://docs.meteora.ag/get-started) | Primary protocol documentation | Product/venue inventory | Product overview, not a transaction decoder |
| SOL-014 | [Meteora DLMM SDK](https://github.com/MeteoraAg/dlmm-sdk) | Primary source repository | Reference DLMM quote/decoder implementation | Deployed version compatibility must be checked |
| SOL-015 | [Raydium documentation](https://docs.raydium.io/) | Primary protocol documentation | CPMM/CLMM/AMM venue inventory | Recheck program IDs and fee configs on-chain |
| SOL-016 | [Raydium SDK v2](https://github.com/raydium-io/raydium-sdk-V2) | Primary source repository | Reference discovery/quote implementation | SDK output is not proof of landing |
| SOL-017 | [Orca developer documentation](https://docs.orca.so/developers/overview) | Primary protocol documentation | Whirlpools development surface | Recheck deployed program/version registry |
| SOL-018 | [Orca Whirlpools repository](https://github.com/orca-so/whirlpools) | Primary source repository | CLMM decoder/quoter reference | Needs golden tests against raw transactions |
| SOL-019 | [Jupiter developer platform](https://developers.jup.ag/) | Primary protocol documentation | Route discovery/control quote and transaction-building reference | Jupiter quote is not an executable-profit observation |
| SOL-020 | [Solana Foundation: data live on BigQuery](https://solana.com/news/solana-data-live-on-google-cloud-bigquery) | Primary network announcement | Archival public-dataset availability | Query cost, current schema and freshness require measurement |
| SOL-021 | [solarchive.org](https://solarchive.org/) | Public data distribution | Free CC-BY-4.0 Parquet, schemas, checksums and readiness table | Not official; inspected transaction coverage was incomplete; total archive is very large |
| SOL-022 | [Yellowstone Old Faithful](https://github.com/rpcpool/yellowstone-faithful) | Public archival source project | Alternative verifiable/content-addressed historical access | Operational complexity and indexes must be evaluated |
| SOL-023 | [Solana MEV empirical-analysis toolkit](https://github.com/wangjianyeART/solana-mev) | Authors' research artifact | Classifier/collector reference for atomic arbitrage and liquidations | Requires Helius key; labels and methodology not yet audited |
| SOL-024 | [Demystifying Solana Bots: From GitHub Blueprints to On-Chain Fingerprints](https://arxiv.org/abs/2607.28424) | Research preprint | 2026 implementation/on-chain bot taxonomy; reported 586 repositories, 200 addresses and >44M transactions | Preprint; address labels and reproducibility package require review |
| SOL-025 | [Project ANB arbitrage transaction](https://solscan.io/tx/J8TY8VkjZpAAm78GwbnEE1xkBwGdheQ4C1VsZA7Cwcv1AyDw3PxTQJ3eWh9YZmZyLQnLD3fuHBsihXbX4sTATi8) | Chain identifier via explorer | Provisional event fixture | Explorer page is not preserved raw RPC evidence |
| SOL-026 | [Project ANB trigger transaction](https://solscan.io/tx/5wY3V7v8ALqB5hGj1vkqttLy4T65awaeTkm6G4oxt4xfvndrqFA7kLwqQq4VJzw8338B1YZyPFHooueCMyujxkFK) | Chain identifier via explorer | Provisional trigger fixture | Explorer page is not preserved raw RPC evidence |
| SOL-027 | [Project ANB intermediate arbitrage](https://solscan.io/tx/5oiBGWFxs87reNtQSH2ZCmqyp9bcVgFp78FgCjPq7zaW4m1JXsfNPFGK3qeUCcYj4c7MpsEAWerHa68b2HfiVHor) | Chain identifier via explorer | Provisional neighboring fixture | Explorer page is not preserved raw RPC evidence |

## Evidence notes

- The ANB amounts and signer deltas in the screening report come from `docs/project-context.md`; only the subtraction of input USDC from output USDC is independently deterministic in this sprint.
- No owner identity is attributed to any address.
- No transaction other than the three already recorded by the project is introduced as a confirmed arbitrage.
- Vendor and protocol documentation establishes interfaces and mechanics, not profitability.
- The source register should be revised when SOL-HR-001 preserves raw RPC responses and hashes.

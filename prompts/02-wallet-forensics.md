# Prompt: wallet and transaction forensics

Analyze the following wallet(s), transaction(s), or block range in the context of this repository: `<REPOSITORY_URL>`.

Inputs:

- Network: `<NETWORK>`
- Wallet(s): `<WALLETS_OR_NONE>`
- Transaction(s): `<TRANSACTIONS_OR_NONE>`
- Block/slot and date range: `<RANGE>`
- Initial hypothesis: `<HYPOTHESIS>`

## Read first

Read `README.md`, the project brief, research plan, methodology, transaction schema, evidence ledger, findings, sources, and the relevant file under `docs/networks/`. Inspect existing collectors/decoders in `src/` and samples in `data/samples/` before duplicating work.

## Method

Build a reproducible evidence trail. Preserve raw identifiers and record the RPC/indexer endpoint, query parameters, retrieval time, chain state/finality, decoder version, and pricing source/timestamp. Normalize results to the repository schema.

For every candidate transaction, reconstruct where possible:

- starting and ending asset balances, including wrapped/native assets;
- transfers, swaps, pool fees, gas/base fee, priority fee, validator/builder/Jito tip, and failed/reverted attempts;
- route, pools, protocols, position in block/bundle, and nearby competing transactions;
- gross token delta and net result in native units;
- USD valuation using an explicit timestamp and source;
- inventory retained before/after the measured window;
- uncertainty caused by unidentified transfers, internal calls, address clusters, off-chain hedges, or missing data.

Do not assume all addresses in a route have one owner. Do not label a transaction as arbitrage merely because it contains multiple swaps. Do not report net profit when material inventory or costs remain unresolved.

## Deliverable

Return:

1. scope and data provenance;
2. transaction-level reconstruction;
3. classification of each result: confirmed arbitrage, probable arbitrage, ambiguous, or not arbitrage;
4. PnL reconciliation with known and unknown components;
5. recurring route/behavior patterns;
6. competing searchers and failure-cost observations, when supported;
7. conclusions, alternative explanations, and confidence levels;
8. exact reproduction commands or queries;
9. recommended next sample and stop condition.

Never infer future or stable profit from the sample. When write access exists, add normalized non-sensitive samples, a dated evidence record and source register entry, plus regression fixtures/tests for decoded transactions. Otherwise provide patch-ready updates.

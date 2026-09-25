# Stage-2 preregistration — v1

Status: frozen before opportunity/PnL queries.  
Freeze date: 2026-09-25.

This file closes the sampling ambiguities identified by independent review. Changing a rule after inspecting results requires a new version and an explicit deviation note; the original result must remain reproducible.

## Shared rules

- Use finalized/canonical data only for outcome accounting; retain the network-specific preconfirmation state separately.
- Store provider, endpoint class, request time, exact block/slot range, missing ranges, raw-response hashes and collector commit.
- Keep all decoded candidates, including zero-profit, reverted, no-route and undecodable records.
- Never select wallets or days by observed project profit.
- Report full population counts before drawing validation samples.

## BASE-HR-001

### Day selection

- Candidate ordinary-day universe: all complete UTC days from 2026-08-01 through 2026-08-31.
- Seed: UTF-8 string BASE-HR-001|ordinary|v1|2026-08.
- Compute SHA-256 of seed|counter, interpret the first eight bytes as an unsigned big-endian integer, and map modulo the remaining chronologically sorted dates. Select two dates without replacement, starting at counter 0.
- The stress day is the date in the same universe with the largest absolute Coinbase Exchange ETH-USD UTC daily open-to-close return from the public candles endpoint. Ties select the earlier date. Missing or duplicate daily candles stop selection; they are not imputed.
- Exclude the stress day from the ordinary-day draw. If it was selected, continue the hash counter until two ordinary dates remain.
- All selected dates are post-Flashblocks and pre-Denim. A later Denim sample is a separate experiment.

### Transaction sampling

- Candidate population: every transaction on the three selected days calling either a preregistered paper-reported contract or a contract independently classified from a completed same-transaction swap cycle.
- Freeze the contract list, bytecode hash, event signatures, venue manifest and classifier commit before classification counts are viewed.
- Validation strata: classifier-positive, classifier-negative, and undecodable. Within each stratum order records by SHA-256 of BASE-HR-001|validation|v1|tx_hash; inspect the first 25 or the whole stratum when smaller.
- Independently inspect every alleged profitable cycle in the bounded sample, but do not use that winner census to estimate classifier precision.

## Robinhood seven-day discovery probe

### Population and ranking

- Discovery lookback: 14 complete UTC days, 2026-09-10T00:00:00Z through 2026-09-24T00:00:00Z (end exclusive), leaving two complete days before the sprint snapshot.
- Token universe: contracts returned as active for chain ID 4663 in the first /rhj/assets snapshot captured at or after 2026-09-25T00:00:00Z; preserve response bytes and SHA-256.
- Pool universe: only factories/pool managers whose address, deployment source, bytecode hash and event signatures are frozen in the manifest before swap counts are aggregated.
- Activity metric: count successfully decoded canonical swap events touching each Stock Token during the lookback. Do not use USD volume or token amount for ranking.
- Select the ten highest counts. Ties sort by lower-case token contract address ascending. A token with zero decoded swaps cannot enter the top ten.
- Block coverage is the first canonical block with timestamp at or after the start through the last canonical block before the end. Any missing block or unresolved reorg/finality disagreement stops ranking until repaired.

### Probe window and outputs

- Run seven consecutive complete UTC days after the manifest and token ranking are frozen.
- Retain every route/quote request and its result: AMM, RFQ, no route, restricted, stale, expired, revert and decode failure.
- Morpho population is every market with non-zero borrow in the frozen API/on-chain snapshot; verify events on-chain before describing activity as project-confirmed.
- Lighter is metadata/depth observation only. Do not merge its candidates with atomic same-chain routes.

## Ethereum and Solana

- ETH-R1: choose and commit one contract family before capture; pin MEV-Share schema/API version, privacy handling, simulation state, refund/bid assumptions and builder route configuration.
- SOL-HR-001: pin commitment level, endpoint list, canonical JSON/hash procedure and an initial slot range of 416936447..416936449. Expand one neighboring slot per side only when a referenced account/state transition requires it, recording each reason.

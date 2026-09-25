# Roadmap

## Phase 0 — repository and methodology

- [x] Define multi-chain scope.
- [x] Define evidence and normalized opportunity contracts.
- [x] Add AI onboarding and reusable research prompts.
- [ ] Review network documents with a second researcher.

Exit condition: another researcher can reproduce the plan from the repository alone.

## Phase 1 — four-network screen

- [ ] Inventory venues, contracts, feeds, and historical-data access.
- [ ] Define network-specific transaction classifiers.
- [ ] Estimate fixed infrastructure cost at prototype and competitive tiers.
- [ ] Identify candidate searcher wallets without assuming common ownership.
- [ ] Populate `scorecards/network-screening.csv`.

Exit condition: two networks are shortlisted using documented scoring, not intuition.

## Phase 2 — historical replay

- [ ] Reproduce the Solana ANB route and balance deltas.
- [ ] Sample ordinary and high-volatility periods.
- [ ] Normalize 100–300 candidate transactions per shortlisted network.
- [ ] Calculate gross/net PnL, failure costs, winner concentration, and latency decay.
- [ ] Version all decoders and pricing inputs.

Exit condition: multiple independent opportunities are reproduced with conservative costs.

## Phase 3 — live paper monitor

- [ ] Run collectors continuously for 7–14 days.
- [ ] Timestamp receipt, detection, simulation, and hypothetical send.
- [ ] Replay at 0/50/100/250/500/1000 ms delay.
- [ ] Produce daily machine-generated summaries.
- [ ] Compare measured results with historical estimates.

Exit condition: at least one strategy has positive evidence after realistic latency and variable costs.

## Phase 4 — guarded tiny-live test

Prerequisites:

- explicit go decision in `docs/decision-log.md`;
- reviewed executor contract/program;
- isolated wallet and non-production funds;
- destination allowlist and maximum trade/tip/gas/day limits;
- simulation and min-profit assertion;
- circuit breakers and operator kill switch;
- monitoring and incident runbook.

Exit condition: a bounded trial produces auditable realized results without breaching limits.

## Phase 5 — scale or stop

Scale only the measured bottleneck: data latency, computation, submission, coverage, or capital. Stop or redesign if net evidence remains negative.

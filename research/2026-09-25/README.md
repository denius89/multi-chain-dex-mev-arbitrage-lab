# Research sprint 01 — network screening

**Snapshot date:** 2026-09-25  
**Scope:** Solana, Base, Robinhood Chain, Ethereum  
**Stage:** complete — desk research and data-access validation  
**Trading:** none

## Decision this sprint supports

Select the two networks that deserve historical transaction collection and a 7–14 day paper monitor.

This sprint does **not** attempt to estimate guaranteed revenue or prove that a strategy is executable. It determines whether the evidence, data access, market structure, and prototype cost justify a deeper quantitative phase.

## Required outputs

- `network-screening/solana.md`
- `network-screening/base.md`
- `network-screening/robinhood-chain.md`
- `network-screening/ethereum.md`
- `infrastructure-costs.md`
- `cross-network-scorecard.md`
- `independent-review.md`
- `recommendation.md`

## Sprint result

- Primary Stage-2 tracks: **Base historical replay** and **Robinhood Chain read-only discovery**.
- Optional low-cost side track: **Ethereum MEV-Share hint census**.
- Narrow gate only: **Solana raw reconstruction** before any paper monitor.
- No network is approved for funded execution.

Start with the [recommendation](recommendation.md), then the [cross-network scorecard](cross-network-scorecard.md) and [independent review](independent-review.md). Sampling rules are frozen in [preregistration.md](preregistration.md).

## Common questions

Each network report must answer:

1. Which strategy classes are technically possible and publicly evidenced?
2. Which venues and data feeds are confirmed live?
3. What ordering and submission mechanism controls execution?
4. Can historical opportunities be reconstructed without paid or exclusive data?
5. What evidence exists for competition and winner concentration?
6. Which important facts remain unobservable from public chain data?
7. What is the cheapest useful next experiment?
8. What would falsify the case for continuing?

## Evidence discipline

- Prefer primary protocol/network documentation and on-chain records.
- Use empirical papers for market-wide measurements when their dataset and period are explicit.
- Treat third-party dashboards as leads unless their methodology and raw data are reproducible.
- Record the retrieval date for mutable documents and pricing.
- Separate announced integrations from confirmed deployment, confirmed liquidity, and confirmed opportunity.
- Never present gross extracted value as searcher net income.
- Do not merge recurring economics with rare tail events.

## Scoring

The synthesis scores each network from 0 to 5 on:

- public data access;
- historical reproducibility;
- opportunity diversity;
- accessible execution;
- prototype cost;
- competition accessibility;
- implementation complexity;
- evidence confidence.

Scores are prioritization aids, not forecasts. Every score must link to evidence and list the main uncertainty.

## Go/Hold/Stop interpretation

- **Go:** sufficient evidence and data access for historical implementation now.
- **Conditional:** promising, but a named uncertainty must be tested first.
- **Hold:** monitor changes; do not allocate implementation effort yet.
- **Stop:** current public evidence or economics do not justify the next phase.

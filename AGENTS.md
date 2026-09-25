# Agent onboarding and repository rules

This file is the canonical entry point for ChatGPT, Codex, Claude, or another research/coding agent working in this repository.

## Mission

Determine whether a small, research-led team can build a reproducibly profitable DEX arbitrage or adjacent MEV system without assuming that a single exceptional transaction represents ordinary returns.

The networks currently in scope are Solana, Base, Robinhood Chain, and Ethereum. Do not silently narrow the project to Solana.

## Required reading order

Before proposing a strategy or changing code, read:

1. `README.md`
2. `docs/project-context.md`
3. `docs/research-methodology.md`
4. `docs/architecture.md`
5. the relevant file in `docs/networks/`
6. `docs/decision-log.md`
7. `docs/roadmap.md`

For a new ChatGPT conversation, also use `prompts/00-project-onboarding.md`.

## Epistemic rules

Every material claim must be labeled implicitly or explicitly as one of:

- **Confirmed fact:** supported by an on-chain record, primary documentation, or deterministic calculation.
- **Derived result:** calculated from preserved inputs; method and version must be stated.
- **Hypothesis:** plausible but not yet tested.
- **Recommendation:** a proposed action based on stated evidence and assumptions.

Do not:

- promise daily profit or extrapolate from a jackpot;
- use DEX volume as a proxy for accessible arbitrage profit;
- ignore failed transaction fees, tips, gas, hedging costs, or infrastructure;
- present a simulated opportunity as an executable one;
- invent transaction hashes, wallet ownership, latency, prices, or sources;
- request or commit private keys or seed phrases.

## Research workflow

Use the funnel in `docs/research-methodology.md`:

1. Network screen.
2. Historical replay.
3. Paper execution with measured latency.
4. Guarded tiny-live test only after a go decision.

Bulk data work belongs in deterministic code. Use the model to design, review, debug, and interpret. Save normalized outputs using `schemas/opportunity.schema.json`.

## Change protocol

- Keep research inputs and transformations reproducible.
- Add evidence records using `docs/evidence-template.md`.
- Record material scope/strategy decisions in `docs/decision-log.md`.
- Add or update tests for schema and calculation changes.
- Do not add live execution by default. A live executor requires an explicit decision, threat model, wallet isolation, allowlists, spend caps, simulation, and circuit breakers.
- Preserve source links and retrieval dates for mutable documentation.

## Expected response format for research tasks

1. Short conclusion.
2. Confirmed evidence.
3. Derived metrics and calculation method.
4. Uncertainties and missing data.
5. Recommended next test.
6. Files changed or artifacts produced.

## Current priority

The current priority is comparative evidence, not production trading:

- reproduce the Solana ANB case;
- screen Solana, Base, Robinhood Chain, and Ethereum consistently;
- build historical collectors and a normalized dataset;
- shortlist two networks for a 7–14 day paper monitor;
- select the first execution MVP only after measured results.

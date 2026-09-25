# Prompt: network screening

Using this repository: `<REPOSITORY_URL>`, conduct or extend the comparative screening of **Solana, Base, Robinhood Chain, and Ethereum** for a small-team DEX/MEV arbitrage project.

## Read first

Read `README.md`, `AGENTS.md`, `docs/project-context.md`, `docs/research-methodology.md`, the latest dated folder under `research/`, the relevant standing files under `docs/networks/`, and `schemas/opportunity.schema.json` before proposing data collection.

## Research rules

- Use the same questions, measurement window, units, and scoring scale for every network.
- Prefer primary sources: protocol/network documentation, repositories, explorer/API documentation, and reproducible on-chain queries.
- Record URL, publisher, retrieval date, claim supported, and scope/limitations for each source.
- Separate protocol capability from observed opportunity and observed opportunity from capturable profit.
- Flag measurements that are not comparable across chains.
- Do not use DEX volume, low gas, or a single profitable transaction as a proxy for strategy profitability.
- Never fabricate revenue, success rate, opportunity lifetime, competition, or infrastructure cost.

Evaluate at minimum:

- relevant AMMs, CLMMs, RFQ systems, order books, lending/liquidation venues, and tokenized-asset venues;
- transaction ordering, block/slot cadence, mempool or sequencer visibility, private order flow, bundles, atomicity, simulation, and reorg/finality behavior;
- available historical/live data and realistic entry-level infrastructure;
- visible searcher activity, failed-attempt cost, winner concentration, and barriers to entry;
- suitable strategy families: cyclic/cross-pool arbitrage, backruns, liquidations, oracle/venue divergence, inventory arbitrage, and protocol-specific edge;
- implications of 0/50/100/250/500/1000 ms detection-to-submission delays where measurable.

## Deliverable

Produce:

1. a compact comparison with claim-level citations;
2. a scored ranking with explicit weights and confidence levels;
3. the two best candidates for the next research phase;
4. the strongest argument against each recommended candidate;
5. a bounded data-collection plan and stop conditions;
6. a list of facts that could not be verified.

When repository write access is available, create or update a dated sprint folder with network reports, source registers, a common-rubric scorecard and an independent review record. Do not overwrite earlier evidence: append or supersede it with a dated explanation. Run available validation/tests and summarize changed files. If write access is unavailable, return a patch-ready change list.

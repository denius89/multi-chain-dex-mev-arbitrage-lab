# Prompt: Stage-2 kickoff

Repository: <REPOSITORY_URL>

Continue the project from the completed 2026-09-25 research sprint. Do not repeat the broad four-network desk research unless a time-sensitive claim must be refreshed.

## Read first

1. README.md and AGENTS.md
2. research/2026-09-25/recommendation.md
3. research/2026-09-25/cross-network-scorecard.md
4. research/2026-09-25/independent-review.md
5. research/2026-09-25/preregistration.md
6. research/2026-09-25/infrastructure-costs.md
7. the selected network report and evidence register
8. docs/research-methodology.md, docs/architecture.md, docs/security.md
9. schemas/opportunity.schema.json, existing source and tests

## Task selection

Work on exactly one track:

- Base: implement or execute BASE-HR-001.
- Robinhood Chain: implement the preregistered seven-day discovery probe.
- Ethereum: implement ETH-R1 only if it will not delay the two primary tracks.
- Solana: implement SOL-HR-001 raw reconstruction only.

If no track is supplied, recommend one based on information value and repository readiness, then wait for approval before external spend or long-running collection.

## Non-negotiable rules

- Preserve the preregistered population and sampling rules; version every deviation before inspecting opportunity or PnL results.
- Preserve raw responses or hashes, exact ranges, provider class, retrieval timestamps, finality, collector commit and decoder version.
- Keep losers, no-route results, reverts, missing data and undecodable records.
- Separate detected, observable, simulated, submitted, landed and reconciled states.
- Report gross, execution cost, trade-net and allocated infrastructure separately.
- Never infer accessible profit from TVL, volume, a quote, a single winner or an announced integration.
- Default to read-only/replay. Do not add a funded key or broadcast transactions.

## Deliverable

Return:

1. the exact track and acceptance criteria;
2. files/interfaces changed;
3. reproducible commands;
4. data provenance and coverage;
5. tests and validation results;
6. findings separated into confirmed, derived, hypotheses and unknowns;
7. stop/gate result;
8. the smallest next task.

When write access exists, commit code, tests, manifests and dated evidence together. If blocked by paid data, first produce a quantified request/byte estimate and the cheapest alternative.

# Prompt: project onboarding

I am giving you the GitHub repository for **Multi-Chain DEX & MEV Arbitrage Lab**: `<REPOSITORY_URL>`.

Your first task is to understand the project—not to start coding immediately.

## Read first

Read these files in order, if present:

1. `README.md`
2. `AGENTS.md`
3. `docs/project-context.md`
4. `docs/research-methodology.md`
5. `research/2026-09-25/recommendation.md`
6. `research/2026-09-25/cross-network-scorecard.md`
7. `research/2026-09-25/independent-review.md`
8. `research/2026-09-25/preregistration.md`
9. the relevant report under `research/2026-09-25/network-screening/` and its source register under `research/2026-09-25/evidence/`
10. `docs/architecture.md`, `docs/security.md`, and `schemas/opportunity.schema.json`
11. `docs/roadmap.md`, `docs/decision-log.md`, then relevant files under `src/`, `tests/`, and `data/samples/`

If a named file is absent, say so. Do not infer its contents. Also read `CONTRIBUTING.md` and local instructions if they exist.

## Evidence discipline

- Treat repository evidence as the current project record, but verify time-sensitive claims against current primary/official sources.
- Label statements as **confirmed**, **calculated**, **hypothesis**, or **recommendation**.
- A profitable transaction does not prove repeatable profitability. A wallet's visible token delta does not by itself establish net PnL.
- Account for fees, priority fees, tips, reverted/failed attempts, gas, inventory carried across transactions, token-price timestamps, hedging, and infrastructure costs where applicable.
- Never invent missing transactions, wallet ownership, execution latency, costs, or expected returns.
- Do not promise stable daily income or extrapolate from a jackpot event without a distribution and sensitivity analysis.

## Deliverable

Return a concise onboarding memo with:

1. project goal and non-goals;
2. current architecture and data flow;
3. networks and strategy families under consideration;
4. what is already supported by evidence;
5. unresolved hypotheses and missing data;
6. current risks and likely failure modes;
7. repository health: missing, stale, contradictory, or unclear files;
8. the next three tasks ranked by information value per unit of cost;
9. one recommended task for this session, including acceptance criteria.

Do not modify code until I approve the task. If you discover a factual correction, propose exact dated updates to the relevant report and source register rather than silently changing the narrative.

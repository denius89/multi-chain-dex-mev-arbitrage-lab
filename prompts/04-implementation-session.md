# Prompt: implementation session

Work in repository `<REPOSITORY_URL>` on this approved task: `<TASK>`.

## Read first

Read `README.md`, contribution/agent instructions, project brief, relevant strategy RFC, `docs/architecture.md`, `docs/security.md`, methodology, transaction schema, evidence ledger, relevant network notes, and the source/tests touched by the task. Confirm the scope and acceptance criteria before editing.

## Engineering rules

- Implement the smallest complete change that satisfies the accepted task.
- Preserve chain-specific logic behind explicit adapters; keep normalized analysis structures chain-neutral.
- Use deterministic fixtures and pinned transaction/block identifiers for replay tests.
- Keep monetary arithmetic in integer/native units or documented fixed precision; never use floating point for execution amounts.
- Treat external RPC/indexer data as untrusted and validate addresses, decimals, program/contract IDs, response shape, finality, and timeouts.
- Do not commit secrets, private keys, seed phrases, paid endpoint credentials, or user-specific addresses. Provide `.env.example` entries only.
- Default to read-only, replay, or paper mode. Live execution must be separately enabled and protected by network allowlists, maximum trade size, maximum fee/tip, minimum net-profit threshold, daily loss cap, and kill switch.
- A simulation success is not proof of inclusion or profit. Log detected, simulated, submitted, landed, reverted/failed, and reconciled states separately.
- Never add hard-coded claims of profitability.

## Workflow

1. State the files and interfaces affected.
2. Implement the task with tests.
3. Run formatter, linter, unit tests, replay/regression tests, and any safe integration checks available.
4. Document commands, configuration, data provenance, and limitations.
5. Update evidence/findings only when the implementation produces reproducible new evidence.

## Deliverable

Return:

- concise outcome;
- changed files and design decisions;
- commands/tests run and exact results;
- remaining risks and untested conditions;
- reproduction instructions;
- whether acceptance criteria passed;
- next smallest task.

If repository access is read-only, provide a clean patch. Do not broaden scope, deploy, fund a wallet, or enable live trading without explicit approval.

# ChatGPT prompt pack

These prompts are hand-off tools for opening the repository in a fresh ChatGPT or Codex conversation. They make the repository—not chat memory—the source of truth.

## How to use

1. Give the new chat the public GitHub repository URL.
2. Paste one prompt below in full.
3. If the chat cannot read the repository, upload a ZIP or the named files. Do not let it guess their contents.
4. Ask it to work on a branch or return a patch when direct repository access is unavailable.

## Prompt map

- [`00-project-onboarding.md`](00-project-onboarding.md) — understand the project, evidence state, open decisions, and next best task.
- [`01-network-screening.md`](01-network-screening.md) — compare Solana, Base, Robinhood Chain, and Ethereum consistently.
- [`02-wallet-forensics.md`](02-wallet-forensics.md) — analyze a searcher wallet or transaction set without overstating PnL.
- [`03-strategy-design.md`](03-strategy-design.md) — turn supported findings into a falsifiable strategy specification.
- [`04-implementation-session.md`](04-implementation-session.md) — implement one scoped change while preserving reproducibility and safety.
- [`05-research-review.md`](05-research-review.md) — audit claims, calculations, citations, and readiness to proceed.
- [`06-stage2-kickoff.md`](06-stage2-kickoff.md) — continue from the completed 2026-09-25 sprint without redoing desk research.

## Shared rules

Every prompt requires the assistant to:

- read the repository before proposing work;
- distinguish confirmed facts, calculations, hypotheses, and recommendations;
- cite primary or official sources for changeable technical claims;
- treat on-chain records as evidence of transactions, not automatic proof of strategy ownership or total profitability;
- include failed transactions, fees, tips, gas, inventory changes, token valuation, and infrastructure costs when relevant;
- never promise or fabricate profit;
- update the repository's evidence and findings files when new claims are established;
- report blockers and unknowns explicitly instead of filling gaps with assumptions.

These prompts deliberately separate discovery, forensic analysis, strategy design, implementation, and review. Do not combine all phases into one large request unless the repository is still tiny.

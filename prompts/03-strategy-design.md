# Prompt: strategy design

Using repository `<REPOSITORY_URL>`, design a testable strategy from the current evidence. The target network or thesis is: `<TARGET_OR_OPEN>`.

## Read first

Read the project brief, research plan, methodology, findings, evidence ledger, sources, network scorecard, relevant network notes, transaction schema, `docs/architecture.md`, `docs/security.md`, existing code, tests, and samples. Identify which claims are confirmed versus hypothesized before designing anything.

## Constraints

- The strategy must follow from recorded evidence; do not retrofit evidence to a preferred strategy.
- Separate detection edge, pricing/model edge, execution edge, and capital/inventory edge.
- Model fees, price impact, failed attempts, tips/priority fees, stale state, adverse selection, inventory, infrastructure, and opportunity cost.
- Do not assume quoted output equals executable output.
- Do not claim expected or stable profit without an out-of-sample dataset and sensitivity analysis.
- Prefer a narrow, falsifiable MVP over a broad multi-protocol bot.
- Avoid manipulative strategies, user-targeted sandwiching, unauthorized access, or reliance on deceptive behavior.

## Required specification

Define:

1. market inefficiency and why it may persist;
2. precise opportunity trigger and required data;
3. route construction and sizing algorithm;
4. transaction/bundle construction and atomic failure condition;
5. profitability equation in native and USD terms;
6. latency model and delay sensitivity;
7. capital requirements and inventory policy;
8. risk limits, kill switches, and key-management boundary;
9. paper-trading protocol and historical replay design;
10. falsification criteria and explicit stop conditions;
11. staged path: replay → live observation → paper execution → tiny live test;
12. observability metrics and post-trade reconciliation.

## Deliverable

Produce a strategy RFC with assumptions marked, equations defined, required interfaces listed, tests/acceptance criteria specified, and an evidence-to-design traceability section. Include the cheapest experiment capable of disproving the thesis.

When write access exists, add the RFC under `docs/strategies/` and update the evidence ledger only for genuinely new verified claims. Add hypotheses to findings as hypotheses, never as confirmed results. Otherwise return a patch-ready RFC. Do not implement the executor until the RFC and acceptance criteria are approved.

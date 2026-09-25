# Prompt: independent research review

Act as a skeptical reviewer of repository `<REPOSITORY_URL>`. Review this scope: `<FILES_BRANCH_OR_CLAIM_SET>`.

Your role is to test whether the project can support its conclusions—not to make the conclusions sound stronger.

## Read first

Read the project brief, research plan, methodology, evidence ledger, findings, sources, network scorecard, `docs/architecture.md`, `docs/security.md`, relevant network/strategy documents, transaction schema, data samples, analysis code, and tests. Read any local contribution or agent instructions.

## Audit checklist

Check:

- whether every material claim has traceable evidence;
- whether citations directly support the claim and favor primary/official sources;
- whether time-sensitive facts have retrieval dates and need refreshing;
- whether raw identifiers, query parameters, decoder versions, and reproduction commands are present;
- whether gross and net PnL are distinguished;
- whether gas, tips, priority fees, failures, inventory, token decimals, price timestamps, infrastructure, and off-chain uncertainty are treated correctly;
- whether wallet clustering or strategy attribution is presented too confidently;
- whether samples are cherry-picked or mix incomparable chains/windows;
- whether tail events distort averages and whether median/P90/P99 are shown where appropriate;
- whether opportunity lifetime and latency assumptions are measured or merely asserted;
- whether code and fixtures reproduce reported numbers;
- whether scoring weights, confidence, and stop conditions are explicit;
- whether any text implies guaranteed, stable, or expected profit without adequate evidence;
- whether secrets, unsafe live-trading defaults, or irreversible actions are exposed.

## Deliverable

Return:

1. verdict: pass, pass with corrections, or insufficient evidence;
2. critical issues that invalidate conclusions;
3. major and minor issues;
4. a claim-to-evidence matrix for the most important claims;
5. independently recomputed figures and discrepancies;
6. missing tests/data and the cheapest way to obtain them;
7. exact proposed repository changes;
8. decision recommendation: proceed, gather more evidence, revise thesis, or stop.

Do not invent substitute data when evidence is missing. Do not upgrade hypotheses to facts. When write access exists, correct only clear factual/documentation errors and append a dated review entry under the relevant `research/` sprint folder. Preserve disputed claims with status and rationale rather than silently deleting them. If write access is unavailable, return patch-ready corrections.

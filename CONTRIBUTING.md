# Contributing

## Research contributions

A research change should include:

- a falsifiable claim;
- primary sources or on-chain identifiers;
- retrieval dates for mutable sources;
- reproducible query, script, or calculation;
- gross and net results with cost assumptions;
- limitations and alternative explanations;
- an evidence record based on `docs/evidence-template.md`.

Do not submit screenshots as the only evidence when a transaction hash, API response, query, or primary document is available.

## Code contributions

1. Keep collectors separate from normalization and strategy detection.
2. Use the shared opportunity schema.
3. Preserve raw integer token amounts and decimals; avoid floating-point financial arithmetic.
4. Make timezones explicit and store canonical times in UTC.
5. Add tests for decoders and PnL calculations.
6. Run `python -m unittest discover -s tests -v`.

## Security

Never open an issue or commit containing credentials, wallet exports, private RPC URLs, seed phrases, or private keys. See `docs/security.md`.

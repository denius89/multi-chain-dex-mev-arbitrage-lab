# Security

## Scope and operating principle

This project analyzes public blockchain activity and may eventually support limited live execution. Treat the live executor as financial infrastructure: **deny by default, minimize authority, cap every loss path, and make every decision auditable**.

The public repository must remain safe to clone, inspect, and run in research or paper mode without access to funds. Live trading is never enabled by cloning the repository or setting a single undocumented flag.

## Non-negotiable rules

- Never commit seed phrases, private keys, keystore files, API keys, access tokens, webhook secrets, database credentials, signed transactions, or production endpoint URLs containing credentials.
- Never ask contributors or users to paste wallet secrets into an issue, pull request, chat, log, screenshot, prompt, or configuration file.
- Use a dedicated low-balance trading wallet. Never use a personal wallet, treasury, exchange deposit wallet, or wallet holding unrelated assets.
- Research collectors, detectors, simulators, notebooks and dashboards must not have signing authority.
- Paper mode is the default. Live mode requires explicit configuration, policy approval, and a separate secret-bearing deployment.
- Assume all third-party RPC, indexer, relayer, bundle and price services can be stale, unavailable, compromised, or inconsistent.
- A profitable quote is not authorization to trade.

## Secrets management

### Local development

- Store non-production secrets in an ignored `.env` file or OS credential store.
- Commit only `.env.example` with placeholder names and safe defaults.
- Run secret scanning in pre-commit hooks and CI.
- Rotate a credential immediately if it appears in git history, build logs, screenshots, an issue, or chat. Deleting the visible line is not sufficient.

### Deployed environments

- Inject secrets from a managed secret store at runtime; do not bake them into images or user-data scripts.
- Separate research, staging and live credentials and provider accounts.
- Scope API keys by service, network, endpoint, IP and permission where supported.
- Prefer short-lived workload identity over static cloud credentials.
- Restrict secret access to the live executor process and its deployment identity.
- Record secret metadata and rotation dates, never secret values, in the operational inventory.

### Signing keys

Prefer an external signer, hardware-backed key, KMS/HSM, or tightly permissioned local signing service. If a raw private key is unavoidable for an early tiny-live experiment, store it encrypted outside the repository, mount it only into the isolated executor, restrict filesystem/process access, and plan its replacement before increasing capital.

Do not expose a general-purpose signing RPC. The signer should accept a constrained intent or validate the complete transaction against policy before signing.

## Wallet and fund isolation

Use separate wallets for:

- paper mode: no key and no funds;
- staging/devnet/testnet: test assets only;
- tiny-live tests: minimal disposable capital;
- any later scaled deployment: separate strategy and network wallets.

Fund the live wallet with only the amount required for the current risk window. Sweep realized profits to a non-executor wallet through an explicit operational process. Avoid unlimited token approvals; set exact or narrowly bounded allowances and revoke obsolete approvals.

Never let one compromised adapter, network, or strategy access funds allocated to another.

## Transaction policy

Before signing, the executor must validate the fully constructed transaction rather than trusting detector output.

Required controls:

- network and chain-ID allowlist;
- recipient, program/contract, venue, pool and token allowlists;
- explicit instruction/function selector allowlist;
- rejection of proxy upgrades or unknown contract bytecode/program versions until reviewed;
- maximum input and temporary exposure per transaction;
- maximum token approval and prohibition of unlimited approvals;
- minimum output, maximum slippage and minimum expected net profit;
- maximum gas, priority fee, tip and total execution cost;
- transaction expiry, nonce or recent-blockhash freshness;
- expected number and order of route legs;
- post-route asset and balance constraints;
- prohibition of arbitrary calls supplied by external APIs.

Allowlists are versioned configuration reviewed like code. A newly discovered token or pool is not automatically safe to trade.

## Simulation and stale-state protection

Every live intent must pass a recent simulation using the exact payload or bundle intended for submission. The executor should reject when:

- the simulation fails or produces unclassified warnings;
- the simulation state is older than the configured limit;
- expected balance deltas differ from the detector estimate beyond tolerance;
- any unexpected token, account, contract, program or instruction appears;
- estimated net profit falls below the safety threshold after all modeled costs;
- oracle or reference prices are missing, stale or mutually inconsistent;
- the route depends on unfinalized state beyond the strategy's approved risk.

Simulation reduces risk but does not guarantee execution outcome. Re-check invariant conditions on-chain where atomic contracts/programs support it, and set conservative minimum output constraints.

## Spending limits and circuit breakers

Limits must be enforced locally by the live executor and, where possible, by the signer or smart contract/program as a second layer.

At minimum configure:

- maximum notional and loss per transaction;
- maximum cumulative fees/tips per hour and day;
- maximum gross exposure per asset, venue, network and strategy;
- maximum consecutive failures and failure rate over a rolling window;
- maximum data lag, simulation latency and submission latency;
- maximum deviation between expected and realized output;
- daily drawdown and absolute wallet-balance floor.

Trip a circuit breaker on breached limits, unknown errors, abnormal reorgs, provider disagreement, repeated simulation/execution divergence, unexpected wallet balance changes, contract/program upgrades, or observability loss.

Circuit breakers fail closed. Automatic recovery should be limited to clearly transient data transport faults. Financial, policy, bytecode, balance or accounting faults require manual review. Maintain an authenticated kill switch that stops new signing and submission without depending on the same provider being investigated.

## Data and price integrity

- Bind each decision to an explicit block/slot/hash and observation timestamp.
- Detect gaps, reorganizations, duplicate events and out-of-order streams.
- Compare critical state through independent providers during live tests where feasible.
- Treat external token metadata and USD prices as untrusted annotations.
- Use integer base units and checked arithmetic; reject overflow, underflow, precision loss and unknown decimals.
- Define finality assumptions per network and strategy.
- Preserve source references and configuration hashes for forensic replay.

## Software supply chain

- Pin dependencies and commit lockfiles.
- Minimize dependencies in the signer and live executor.
- Verify official package names, repository ownership and checksums/signatures where available.
- Enable automated dependency and vulnerability scanning, but review upgrades before merging.
- Build release artifacts in CI from protected branches and record provenance/SBOM where practical.
- Use reproducible builds for the live executor where the ecosystem permits.
- Run static analysis, formatting, unit tests, property tests and replay fixtures in CI.
- Fuzz parsers, quote arithmetic, route construction and transaction-policy validation.
- Do not execute arbitrary third-party strategy code, downloaded scripts, notebook cells, or transaction payloads in a secret-bearing environment.
- Isolate development tools, AI agents and browser sessions from production credentials.

## Public repository hygiene

Before every push, ensure the repository contains none of the following:

- real `.env` files, wallet material or keystores;
- authenticated RPC/WebSocket URLs or provider account IDs;
- production IPs, hostnames, dashboards, alert endpoints or infrastructure state;
- full logs or database dumps containing sensitive identifiers;
- operational wallet inventories, balances, exact capital deployment or active strategy parameters;
- signed or still-valid transactions;
- proprietary data that cannot legally be redistributed.

Use synthetic/redacted examples and public transaction references. Sample configuration must default to read-only public endpoints or empty placeholders. Documentation may explain controls without publishing the exact live thresholds, infrastructure topology, latency measurements, active wallet addresses, or alpha-bearing detector parameters.

GitHub Actions triggered from forks or pull requests must never receive live secrets. Use protected environments and manual approval for any deployment workflow. Public CI must remain research-only.

## Testing before live execution

Promotion requires all of the following:

1. Known historical transactions are reproduced with documented assumptions.
2. Arithmetic and invariants pass unit, property and fuzz tests.
3. Paper mode runs continuously long enough to measure gaps, latency and false positives.
4. Expected-versus-observed outcomes are within defined tolerances.
5. Failure injection confirms that stale data, provider outages, reorgs, malformed events and signer failures stop execution safely.
6. Policy tests prove that unknown networks, tokens, venues, contracts/programs and excessive amounts cannot be signed.
7. A second person reviews the live transaction builder, policy layer and secret path.
8. The funded wallet contains only the pre-approved tiny-live budget.
9. Monitoring, alerting, kill switch and incident steps are tested.

A successful paper run is necessary but not sufficient for live deployment.

## Logging and privacy

Security logs should include decision IDs, policy versions, code/config hashes, state references, public transaction hashes, result classes and numeric exposure. They must not contain secrets, raw private material, authorization headers, full signed payloads before expiry, or unredacted provider URLs.

Sanitize errors from third-party SDKs before forwarding them to chat, issue trackers, telemetry or alert channels.

## Incident response

If compromise or unexpected asset movement is suspected:

1. Disable signing and submission with the independent kill switch.
2. If safe, move remaining funds using a clean environment and previously prepared recovery path.
3. Revoke token approvals and provider credentials.
4. Preserve logs, configuration hashes, binaries and relevant chain references.
5. Identify the affected wallet, strategy, network and time window.
6. Rotate all potentially exposed secrets; do not reuse the wallet for live execution.
7. Publish no sensitive forensic detail until containment is complete.
8. Add a regression test and document the root cause before re-enabling any live path.

## Reporting vulnerabilities

Do not open a public issue for a vulnerability involving funds, secrets, signing, transaction-policy bypass, or exploitable strategy execution. The repository maintainer should configure GitHub private vulnerability reporting or publish a dedicated security contact before accepting external reports.

Until that channel exists, do not claim that private vulnerability reporting is available; repository setup must include it as a pre-live requirement.

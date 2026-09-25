# Independent review — research sprint 2026-09-25

Review date: **2026-09-25**  
Reviewer: independent evidence/reproducibility reviewer  
Protocol: [`review-checklist.md`](review-checklist.md)

## Short conclusion

The four network screens are generally disciplined Stage-1 documents: they distinguish testability from profitability, disclose the absence of project-original PnL samples, and propose bounded read-only tests. None proves an accessible trading edge, and none should be used to authorize an executor.

| File | Outcome | Decision use |
| --- | --- | --- |
| `network-screening/solana.md` | **PASS** | Usable to authorize `SOL-HR-001`, not paper/live trading |
| `network-screening/base.md` | **PASS** | Usable to authorize `BASE-HR-001`, subject to preregistration details below |
| `network-screening/ethereum.md` | **PASS** | Usable to authorize `ETH-R1`, not a generic-arbitrage executor |
| `network-screening/robinhood-chain.md` | **CONDITIONAL** | Usable after source-link repair and narrower activity wording |
| `infrastructure-costs.md` | **CONDITIONAL** | Cost logic is usable after provenance-link repair; totals are not procurement quotes |

There is no FAIL among these five files. However, the sprint is **not yet ready for a defensible cross-network rank** from these files alone. The per-network scoring tables do not use one common rubric: Base follows the eight dimensions declared in the sprint README, Ethereum and Robinhood substitute different criteria, and Solana contains no comparable numeric row. A synthesis may score all networks itself, but it must freeze the common rubric and cite the underlying sections rather than copy the incomparable local totals.

## Post-review remediation

The synthesis owner addressed the review findings after this independent verdict:

- moved the Robinhood and infrastructure registers into the sprint evidence directory and repaired both links;
- narrowed the Morpho heading to distinguish verified deployment from activity indicated by third-party snapshots;
- created one centrally scored common-rubric comparison in [cross-network-scorecard.md](cross-network-scorecard.md);
- froze Base and Robinhood sampling rules in [preregistration.md](preregistration.md).

The original review outcomes above are preserved as an audit record; this note records remediation and does not retroactively claim a second independent review.

## Independent checks performed

- Read the repository rules, research methodology, evidence template, four standing network dossiers, all five sprint reports, and the accompanying sprint source registers.
- Checked all relative Markdown evidence links in the reviewed files against the repository filesystem.
- Independently reopened current primary documentation for Base Denim, Robinhood Chain ordering/endpoints, Jito bundle auctions, Flashbots MEV-Share, and Helius pricing.
- Recomputed the published Helius arithmetic: `$499 + $1,000 = $1,499`; `$999 + $800 = $1,799`.
- Did not reproduce any on-chain PnL because the sprint explicitly produced no raw chain dataset. This is acceptable for network screening but is a hard boundary on every economic conclusion.

Confirmed in the independent spot checks:

- Base documentation states that Denim is experimental on Vibenet, targets Sepolia/mainnet in October 2026, has no scheduled activation timestamp, and replaces Flashblocks with canonical 200-ms blocks.
- Robinhood documentation states chain ID `4663`, FCFS sequencing, and public RPC, sequencer feed, and direct sequencer endpoints.
- Jito documentation states up to five transactions per atomic bundle, 50-ms parallel auction ticks, account-lock-aware auctions, and tip/requested-CU ranking.
- Flashbots documentation describes MEV-Share as permissionless for searchers and confirms that refund/revenue-share behavior depends on the exact request/configuration.
- Helius' current pricing page displays Developer `$49`, Business `$499`, Professional `$999`, shreds at `$1,000/IP` for Business and `$800/IP` for Professional, and LaserStream add-ons starting at `$400`.

## Cross-cutting findings

### C1 — No profitability evidence yet

**Assessment: correctly disclosed; not a defect.**

All reports avoid substituting TVL, DEX volume, route quotes, or a jackpot transaction for trade-net PnL. They also retain private-flow and failed-attempt blind spots. The next phase must preserve this boundary: a screen can authorize data collection, not capital deployment.

### C2 — The local scores are not comparable

**Severity: material for synthesis, not fatal to the individual narrative reports.**

The sprint README defines eight common dimensions:

1. public data access;
2. historical reproducibility;
3. opportunity diversity;
4. accessible execution;
5. prototype cost;
6. competition accessibility;
7. implementation complexity;
8. evidence confidence.

Base uses these dimensions. Ethereum instead scores atomic execution, live observability, permissionless access, differentiation, generic competition, and net-economics measurability. Robinhood scores demonstrated activity, public entry, atomic surface, unique hypotheses, and accessible-profit evidence. Solana does not provide the common numeric row.

**Required before a shortlist:** populate `data/network-scorecard.csv` once, centrally, with the frozen README dimensions. Treat `unknown` as unknown rather than zero or favorable. Add a one-sentence evidence pointer and principal uncertainty for every cell. Do not average or compare the existing local score tables.

### C3 — Screening evidence is documentary, not on-chain reproduction

**Assessment: correctly disclosed.**

The reports cite transaction hashes, contracts, explorer examples, and empirical-paper fixtures, but no sprint report preserves raw RPC responses, checksums, exact decoder versions, or executed reproduction commands. Accordingly:

- transaction/accounting claims from the project context remain provisional;
- paper-reported addresses and rates remain facts about the cited study windows only;
- Blockscout/Solscan labels and rendered transfers prove neither ownership nor PnL;
- DefiLlama snapshots establish a third-party activity estimate, not canonical chain accounting.

This is sufficient for Stage 1 only. Stage 2 must use evidence records with immutable inputs and exact commands.

### C4 — Survivorship and invisible-failure risks are handled well

**Assessment: pass.**

Each report identifies at least one of the important missing populations: dropped submissions, rejected bundles, private attempts, no-trade probes, off-chain hedge failures, or inaccessible order flow. The proposed next experiments generally retain negatives and rejection reasons. No report annualizes a tail event.

### C5 — Gross versus net economics are handled conceptually, not measured

**Assessment: pass for screening.**

The reports correctly require gas/base fees, priority fees, Jito tips or builder payments, failed attempts, residual inventory, and infrastructure allocation. No network has an empirical trade-net or fully loaded PnL distribution in this sprint. The eventual scorecard must not award economic attractiveness points based on mechanism, activity, or low nominal fees.

## File review: Solana

**Outcome: PASS**  
**Decision use: authorize only the bounded `SOL-HR-001` raw reconstruction.**

### What passes

- The report explicitly says it is not a profitability study and leaves frequency, PnL, latency decay, failure cost, and concentration as `unknown`.
- The ANB arithmetic is presented as deterministic subtraction, while the transaction itself remains `provisional` until raw RPC data is preserved.
- Jito bundle atomicity, landing uncertainty, auction mechanics, regional endpoints, and uncled-block rebroadcast risk are separated rather than collapsed into “atomic means safe”.
- The 2023 Jito failure statistic and the 2026 preprint are bounded to their source windows/methods and are not projected as current rates.
- Wallet ownership is not attributed, and exact historical pool pre-state is correctly named as the principal blocker.
- The next experiment has named inputs, deliverables, a cost escalation rule, success/failure criteria, and a second gate before exact quote replay.

### Non-critical findings

1. The heading “Proven strategy classes” risks being read too strongly, although the following paragraph narrows “proven” to public mechanism/implementation evidence. Prefer “Publicly evidenced mechanism classes” in a future edit.
2. `SOL-HR-001` should pin commitment/finality, RPC endpoint(s), raw JSON canonicalization, checksum algorithm, and the exact neighboring-slot expansion rule before collection.
3. The source register records retrieval dates but not snapshots/commits for every mutable documentation page. Pin SDK commits and deployed program versions when implementation begins.
4. No common scorecard row is supplied in this report. This is acceptable only if the synthesis produces the row centrally under the frozen rubric.

### Claims not independently reproduced

- ANB signer-controlled balances, tip attribution, route legs, pool addresses, and competitor set.
- Availability of exact pre-state at slot `416936448`.
- 2026 opportunity frequency, current tip distribution, or current searcher concentration.

These omissions are disclosed and do not overturn the Stage-1 result.

### Effect on shortlist

Solana is eligible for a **historical reconstruction slot**, not yet for a live paper-monitor slot. The unresolved pre-state question can still stop the track cheaply.

## File review: Base

**Outcome: PASS**  
**Decision use: authorize `BASE-HR-001`; freeze its sampling rule before any profitability query.**

### What passes

- Current Flashblocks behavior is cleanly separated from the announced Denim regime.
- Independent review of Base documentation confirmed that Denim is not active on mainnet, that October 2026 is a target rather than a scheduled activation, and that Flashblocks APIs will be replaced by canonical streams.
- The strongest empirical MEV paper is explicitly bounded to a pre-Flashblocks sample; its percentages are not treated as current economics.
- The report distinguishes atomic self-contained cycles from adjacency-dependent backruns and does not infer private-mempool visibility from published Flashblocks.
- The venue table is correctly framed as deployment inventory rather than liquidity/profit evidence.
- Failure visibility, historical pre-state, private submissions, curated-data coverage, contract clustering, gross/net accounting, and the ordering-regime mismatch are visible in the conclusion and uncertainty sections.
- Its provisional score uses the common eight dimensions declared in the sprint README.

### Required preregistration before `BASE-HR-001`

These do not block the screening report, but they must be resolved before data is inspected:

1. “Selected by a deterministic hash-derived rule” is not yet reproducible. Record the candidate-day universe, seed/input string, hash function, mapping from hash to dates, exclusion rules, and collision/retry behavior.
2. Define the external ETH-volatility source, calculation interval, threshold, timezone, missing-data rule, and tie-breaker used to choose the stress day.
3. Define how random positives/negatives are sampled, including seed and population after exclusions.
4. Pin a specific post-Flashblocks date range that completes before Denim activation or explicitly freeze data by ordering regime.

### Claims not independently reproduced

- Paper-reported Base transaction traces and optimistic-MEV contract classifications.
- Post-Flashblocks activity, PnL, opportunity survival, or actor concentration.
- Dune coverage/completeness for every proposed custom/hook venue.

The report labels these gaps accurately.

### Effect on shortlist

Base is eligible for a **bounded historical screen**. It should not receive a live slot until post-Flashblocks cases survive exact accounting and at least one subsequent observable state transition.

## File review: Ethereum

**Outcome: PASS**  
**Decision use: authorize the bounded `ETH-R1` MEV-Share hint census only.**

### What passes

- Generic DEX arbitrage, generic liquidation, CEX–DEX, specialized MEV-Share, and event-specific strategies are assessed separately.
- Empirical concentration figures retain their study windows, quantities, and attribution limitations; they are not combined into a synthetic current market-share claim.
- The report distinguishes included-chain observability from rejected/non-included private bundles and off-chain CEX legs.
- MEV-Share permissionless access is not equated with full private-flow coverage or profitable inclusion.
- Refund/revenue-share configurations are not silently merged: the report warns that the exact API path and configuration must be recorded.
- ETH-R1 is read-only, time-bounded, scoped to one contract family, and records end-to-end timestamps, simulation results, cost assumptions, decay checkpoints, outcomes, and rejection reasons.
- No wallet ownership is asserted, and the report rejects generic strategy racing as the first MVP without claiming all Ethereum opportunities are inaccessible.

### Non-critical findings

1. Select and commit the one contract family before starting capture; “under-covered” is a hypothesis, not an observable label. Specify the selection rule independently of later profitability.
2. Pin the MEV-Share event schema/API version, privacy/redistribution rules, builder-routing configuration, simulation block/state, and exact refund calculation.
3. The local score does not match the sprint's common eight-dimensional rubric and must not be copied into the cross-network comparison.
4. “Canonical-chain observability” should always retain the existing private-flow caveat; canonical completeness is not competition completeness.

### Claims not independently reproduced

- Current hint volume, reconstruction rate, simulation acceptance, retained value, or builder inclusion distribution.
- Historical paper wallet clusters and CEX hedge/PnL estimates.
- Current protocol-specific deployment and parameter histories for any eventual target family.

These are correctly listed as unknown.

### Effect on shortlist

Ethereum qualifies for a **cheap seven-day discovery/paper-data census**, not a generic historical profitability claim and not an executor. Its value is high information gain about specialized flow, not demonstrated earnings.

## File review: Robinhood Chain

**Outcome: CONDITIONAL**  
**Decision use: the proposed read-only probe is sensible, but repair provenance and narrow two claims before relying on the report in synthesis.**

### What passes

- Independent primary-source checks confirmed mainnet chain ID `4663`, FCFS ordering, and documented RPC, sequencer-feed, and sequencer endpoints.
- The report carefully separates token deployment, protocol/API support, executable quotes, liquidity, and accessible profit.
- Rialto remains announced/unverified; RFQ routing support is not treated as firm maker access; Lighter is correctly treated as a separate, non-atomic execution domain by default.
- Stock Token multiplier normalization, oracle staleness/pauses, market sessions, primary-market permissions, and the difference between a reference price and an executable exit are explicit.
- The seven-day probe is read-only and records no-route, stale-reference, multiplier, depth, atomicity, restriction, and revert failures.

### Material findings requiring correction

1. **Broken evidence link.** From `research/2026-09-25/network-screening/robinhood-chain.md`, `../../../../evidence/robinhood-sources.md` resolves outside the repository. The existing register is `evidence/robinhood-sources.md`; the correct relative path from the report is `../../../evidence/robinhood-sources.md` (or move the register into the sprint evidence folder and link consistently).
2. **Activity wording is stronger than the evidence.** The heading “Morpho — deployment and material activity verified” relies for activity/liquidation amounts on mutable DefiLlama snapshots, while only deployment and explorer contract existence are primary/on-chain-identified in the sprint. Change to “deployment verified; activity indicated by third-party snapshots” until events and balances are reconstructed on-chain.
3. **The activity score is not comparable.** “Demonstrated economic activity = 5” is driven by aggregate TVL/volume and third-party liquidation totals. It must not enter the common shortlist as a substitute for opportunity diversity, trade-net evidence, or accessible profit.
4. **Probe population is underspecified.** “10 highest-activity Stock Tokens selected by observed swaps” needs a fixed lookback, verified contract universe, swap decoder/version, aggregation method, tie-breaker, finality, and missing-data rules before collection.

### Non-critical findings

- Preserve actual `/rhj/assets`, price, corporate-action, Lighter, 0x, and Morpho API responses with timestamps and hashes; a source URL alone cannot reproduce a changing registry.
- Independently verify explorer-labeled Uniswap transactions via bytecode, logs, and traces before calling a protocol interaction canonical.
- State the exact timezone treatment for CET/CEST windows across daylight-saving changes.

### Claims not independently reproduced

- DefiLlama TVL/volume/liquidation calculations.
- Firm public Stock Token RFQ access, Rialto fills, active Lighter markets/depth, Uniswap pool depth, or any searcher PnL.
- Feed-to-sequencer latency from the intended server region.

### Effect on shortlist

The report supports a **read-only discovery probe**, especially AMM registry and Morpho event reconstruction. It does not yet support ranking Robinhood above Base/Solana/Ethereum using its local numeric score.

## File review: Infrastructure costs

**Outcome: CONDITIONAL**  
**Decision use: usable as a dated provider-price screen after repairing the evidence link; not a complete operating budget.**

### What passes

- Fixed, usage-variable, execution-variable, one-time, and capital-at-risk categories are separated.
- Research, paper-monitor, and competitive stages are separated.
- Free tiers are described as quota-bounded rather than free total infrastructure.
- Server/node specifications are not converted into invented hosting prices.
- Base, Robinhood, and Ethereum competitive-stack totals remain `unknown` where public self-serve pricing is insufficient.
- Solana Helius arithmetic was independently recomputed and agrees with the report; exclusions are visible.
- Gas, priority fees, tips/builder payments, refunds, and paid failures remain trade-level variables rather than being hidden in RPC subscription totals.
- The recommended 24-hour traffic probe is the correct next pricing instrument because actual method mix and bytes determine provider usage.

### Material findings requiring correction

1. **Broken evidence link.** From `research/2026-09-25/infrastructure-costs.md`, `../../../evidence/infrastructure-sources.md` resolves outside the repository. The existing register is `evidence/infrastructure-sources.md`; the correct relative path is `../../evidence/infrastructure-sources.md` (or move the register into the sprint evidence folder).
2. **No procurement total should be inferred.** The `$0–49`, `$49–899`, `$1,499`, `$1,799`, and `$2,900+` numbers are provider components/envelopes, not total monthly stacks. The report says this, but any downstream recommendation must repeat the exclusion of host, storage, redundancy, egress, taxes, extra regions/IPs, and trading bids.
3. **Provider capability needs account-level verification.** Pricing pages do not prove that archive state, traces, WSS/gRPC, or Robinhood support is available under the named plan in the required region. Preserve a plan-capability test result before purchase.

### Non-critical findings

- Preserve pricing-page snapshots or PDFs when a purchasing decision is made; current links and retrieval dates are adequate for screening but not for audit of a later invoice.
- The recommendation for two independent live sources is a design recommendation, not a priced requirement. The final monitor budget must name the actual two products and avoid counting overlapping free allowances as an SLA.
- The 24-hour probe should report p50/p95/p99 **end-to-end receive lag**, gap duration, reconnect loss, request/CU/credit/TB use, storage growth, and projected monthly cost under explicit uptime.

### Claims not independently reproduced

- Alchemy and QuickNode method-level billing for the planned collectors.
- Archive/trace availability and retention for each exact plan and network.
- Node hosting, peering, colocation, L1 endpoint, or enterprise agreement prices.

### Effect on shortlist

Infrastructure cost currently differentiates only the **known public price surface**, not competitive feasibility. It can support a low-cost research shortlist, but it cannot rank expected profitability or prove that one provider stack wins latency races.

## Red-flag result

| Red flag | Result |
| --- | --- |
| Profit inferred from volume/TVL/jackpot | Not observed as a conclusion; Robinhood activity score must remain outside economic ranking |
| Winner-only sampling / survivorship bias | No completed sample yet; future preregistration required |
| Gross PnL presented as net | Not observed |
| Failure/tip/infrastructure costs omitted | Not observed conceptually; not yet measured |
| Announced/testnet feature treated as mainnet | Not observed; Denim and Rialto are explicitly qualified |
| Explorer label treated as ownership proof | Not observed |
| Atomicity treated as guaranteed landing/risk-free | Not observed |
| Final block order treated as arrival sequence | Not observed |
| Millisecond latency claimed without telemetry | Not observed as project measurement |
| Free RPC assumed competitive | Not observed |
| Private/off-chain flow assumed absent | Not observed |
| Inactive integration treated as liquid | Not observed as a profit claim; Robinhood activity language needs tightening |
| Guaranteed/annualized returns | Not observed |
| Reproduction artifacts missing for empirical claims | Expected at Stage 1 and disclosed; mandatory in Stage 2 |
| Ranking before common scoring method | **Open issue** — local score tables are incomparable |

## Required fixes before final sprint recommendation

1. Repair the two broken evidence links.
2. Normalize all four networks into the single eight-dimension scorecard declared in `research/2026-09-25/README.md`; ignore local non-common totals.
3. Change Robinhood's Morpho activity wording to reflect third-party rather than project/on-chain verification.
4. Record exact deterministic sample-selection rules before Base or Robinhood data collection.
5. Keep every shortlist statement at the level of **historical reconstruction/read-only paper research**, not expected income or executor selection.

Once those fixes are incorporated, the evidence supports starting the bounded next experiments. It does not support real trading, a daily-income estimate, or purchasing competitive infrastructure.

---

## Post-remediation reviewer recheck — 2026-09-25

Scope of this recheck was limited to the four remediation items named above. Original file outcomes and substantive assessments were not rescored.

| Remediation item | Recheck result | Evidence |
| --- | --- | --- |
| Evidence paths | **CLOSED** | Both links resolve inside the repository to `research/2026-09-25/evidence/robinhood-sources.md` and `research/2026-09-25/evidence/infrastructure-sources.md`. |
| Morpho wording | **PARTIALLY CLOSED** | The section heading now correctly says “deployment verified; activity indicated by third-party snapshots”, but two later statements still say activity/liquidations are confirmed. |
| Common scorecard | **CLOSED** | `cross-network-scorecard.md` and `data/network-scorecard.csv` use the frozen eight-dimension rubric for all four networks; totals recompute to Base 29, Robinhood 27, Ethereum 27, and Solana 22. Unknowns remain explicit and the scorecard states that it ranks research feasibility, not profit. |
| Preregistration | **CLOSED for starting bounded collection** | `preregistration.md` now fixes Base's date universe, seed, SHA-256 selection, stress-day rule, validation strata, and regime boundary; it also fixes Robinhood's lookback, token/pool universes, ranking metric, tie-breaker, coverage rule, and seven-day window. Ethereum and Solana required pins are recorded. |

### Reviewer status: REMAINING WORDING ISSUE

The remediation is not fully closed because `network-screening/robinhood-chain.md` still contains two stronger Morpho statements that conflict with its corrected evidence qualification:

1. In the strategy shortlist, “Active lending and liquidations confirmed” should say that deployment is confirmed and activity is indicated by third-party snapshots pending on-chain event reconstruction.
2. In the old local screening score, “active Morpho liquidations” should be labeled third-party-reported, or the obsolete local score table should be removed in favor of the central common scorecard.

The opening phrase “Morpho has measurable lending and liquidation activity” is acceptable only because the later report identifies the measurements as mutable DefiLlama snapshots; adding “third-party-reported” there would eliminate ambiguity.

This remaining issue does **not** block the read-only Robinhood probe, and the central scorecard already assigns evidence confidence `3` with the correct limitation. It does block declaring the evidence-language remediation completely finished. After the two phrases are narrowed, reviewer status becomes **READY FOR BOUNDED STAGE-2 DATA COLLECTION**. This status would still not authorize funded execution or imply profitability.

**Final recheck: READY FOR BOUNDED STAGE-2 DATA COLLECTION — both remaining Morpho statements now correctly identify the activity evidence as third-party-reported and pending on-chain reconstruction; no remediation blocker remains.**

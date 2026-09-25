# Cross-network scorecard — 2026-09-25

## Result

This scorecard ranks **research feasibility**, not expected profit. Base is the strongest first historical track. Robinhood Chain and Ethereum tie numerically but answer different questions: Robinhood offers a public emerging-market discovery track, while Ethereum offers a narrow permissionless MEV-Share census in a mature and highly competitive market. Solana stays in the project, but its next gate is one raw historical reconstruction rather than a broad paper monitor.

| Rank | Network | Score / 40 | Research decision | Next gate |
| ---: | --- | ---: | --- | --- |
| 1 | Base | **29** | GO for bounded historical work | BASE-HR-001 |
| 2= | Robinhood Chain | **27** | Conditional GO, read-only | seven-day AMM/Morpho discovery probe |
| 2= | Ethereum | **27** | Conditional GO, specialized only | ETH-R1 MEV-Share hint census |
| 4 | Solana | **22** | HOLD broad monitoring | SOL-HR-001 raw reconstruction |

The two recommended full data-collection slots are **Base and Robinhood Chain**. Ethereum's smaller MEV-Share census may run as a low-cost side experiment if it does not delay those slots. Solana receives a short forensic gate; it advances only if raw accounting and historical state access can be reproduced.

## Frozen rubric

All dimensions were fixed in the sprint README before synthesis and are scored from 0 to 5. A higher value is favorable for a small independent research team.

| Dimension | 0 | 3 | 5 |
| --- | --- | --- | --- |
| Public data access | no usable public path | bounded public path with gaps or paid expansion | broad documented public paths |
| Historical reproducibility | cannot reproduce | material gaps or provider dependence | exact replay is practical |
| Opportunity diversity | no supported class | several plausible classes | several publicly evidenced, testable classes |
| Accessible execution | closed or permissioned | public submission with material access caveats | public and documented competitive path |
| Prototype cost | prohibitive/unknown | modest paid dependency | useful test fits free/very-low-cost access |
| Competition accessibility | opaque/dominated | measurable but difficult | observable and realistically contestable |
| Implementation simplicity | major novel blockers | normal protocol-specific work | small, standard implementation surface |
| Evidence confidence | unsupported | credible documentary evidence, no original sample | fresh reproducible project evidence |

Unknown evidence is never scored as favorable. Scores are integer prioritization aids; a two-point gap is not a profitability estimate.

## Evidence-linked scoring

### Base — 29/40

| Dimension | Score | Evidence and principal uncertainty |
| --- | ---: | --- |
| Public data access | 5 | [RPC, Dune and trace paths](network-screening/base.md#4-data-access-and-reproducibility); exact archive state may be paid. |
| Historical reproducibility | 4 | EVM receipts/traces and an open classifier exist; canonical blocks do not recover exact Flashblock arrival timing. |
| Opportunity diversity | 4 | [Multiple AMM generations and lending venues](network-screening/base.md#2-verified-venue-surface); custom hooks increase decoder risk. |
| Accessible execution | 3 | Public atomic EVM transactions are available; no reviewed API guarantees trigger/backrun adjacency. |
| Prototype cost | 4 | A bounded classifier starts cheaply; archive traces and dual live feeds may add usage cost. |
| Competition accessibility | 2 | Private mempool plus roughly 200-ms fee/arrival competition; current actor concentration is unknown. |
| Implementation simplicity | 3 | Standard EVM tooling helps, but venue versions, hooks and the Flashblocks→Denim migration add work. |
| Evidence confidence | 4 | Strong official documentation and a historical paper; no fresh project sample and the paper predates Flashblocks. |

### Robinhood Chain — 27/40

| Dimension | Score | Evidence and principal uncertainty |
| --- | ---: | --- |
| Public data access | 4 | [Public RPC/feed, registries and venue APIs](network-screening/robinhood-chain.md#what-can-be-tested-without-paid-data); archive completeness is untested. |
| Historical reproducibility | 4 | EVM logs/traces and Morpho/venue APIs support bounded replay; Lighter is a separate domain. |
| Opportunity diversity | 4 | [AMMs, Morpho, RFQ discovery, Stock Tokens and Lighter](network-screening/robinhood-chain.md#strategy-shortlist); several remain hypotheses. |
| Accessible execution | 3 | AMMs/Morpho are public; primary issuance is permissioned and firm RFQ access is unproven. |
| Prototype cost | 4 | Registry and event discovery can start on public/free access; production archive/feed needs measurement. |
| Competition accessibility | 2 | FCFS makes end-to-end latency decisive; searcher concentration and feed advantage are unknown. |
| Implementation simplicity | 3 | EVM tooling helps, but multiplier normalization, sessions, multiple domains and incomplete manifests add risk. |
| Evidence confidence | 3 | Live network/deployments are well documented; activity totals are third-party snapshots and no PnL was reconstructed. |

### Ethereum — 27/40

| Dimension | Score | Evidence and principal uncertainty |
| --- | ---: | --- |
| Public data access | 4 | Mature blocks/receipts/logs/traces plus public flow; private flow remains invisible. |
| Historical reproducibility | 4 | [Atomic replay is mature](network-screening/ethereum.md#access-cost-and-observability-screen); rejected private submissions and CEX legs are incomplete. |
| Opportunity diversity | 4 | [Five distinct strategy classes are screened](network-screening/ethereum.md#strategy-assessment); generic classes are poor first-MVP choices. |
| Accessible execution | 4 | Permissionless chain and MEV-Share/bundle APIs; inclusion is not guaranteed. |
| Prototype cost | 3 | Read-only capture can start cheaply, but archive/tracing cost is not yet measured. |
| Competition accessibility | 1 | Official warnings and empirical concentration make generic strategies especially difficult. |
| Implementation simplicity | 3 | Mature tools offset bundle economics, privacy modes and contract-specific simulation complexity. |
| Evidence confidence | 4 | Strong primary docs and multiple bounded studies; no current project-original sample. |

### Solana — 22/40

| Dimension | Score | Evidence and principal uncertainty |
| --- | ---: | --- |
| Public data access | 3 | [Public RPC, BigQuery and Parquet paths](network-screening/solana.md#43-historical-data-access-without-a-paid-subscription); coverage/retention are uneven. |
| Historical reproducibility | 2 | Known transactions may be recovered, but exact historical pool pre-state is the unresolved blocker. |
| Opportunity diversity | 4 | [Atomic cycles, triangles, backruns and launch anomalies](network-screening/solana.md#5-proven-strategy-classes-and-what-proven-means) are publicly evidenced mechanisms. |
| Accessible execution | 3 | Normal transactions and Jito bundles are public, but bundle landing and auction competitiveness are uncertain. |
| Prototype cost | 4 | The narrow forensic fixture can begin with public/low-cost data before any feed purchase. |
| Competition accessibility | 1 | Jito auction dynamics and dated failure evidence point to intense competition; current distribution is unknown. |
| Implementation simplicity | 2 | Program-specific decoding, account locks, historical state and Solana execution semantics raise complexity. |
| Evidence confidence | 3 | Strong mechanism documentation, but the key ANB fixture lacks preserved raw chain data in this sprint. |

## Sensitivity

- If Robinhood's probe finds no reproducible pool registry, firm exits or material Morpho events, its evidence and diversity scores fall and Ethereum becomes the clear second slot.
- If ETH-R1 finds a useful reconstruction rate and positive conservative paper residuals, Ethereum advances despite the competition score.
- If SOL-HR-001 cannot recover raw records or reconcile balances, Solana stops before any live-feed spend.
- Base remains first unless post-Flashblocks sampling shows the classifier no longer captures a meaningful candidate population or Denim invalidates the planned interface before collection.

See the [independent review](independent-review.md) for audit outcomes and limitations. The machine-readable values are in [data/network-scorecard.csv](data/network-scorecard.csv).

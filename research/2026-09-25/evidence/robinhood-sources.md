# Robinhood Chain source register

> Retrieved: 2026-09-25  
> Purpose: Stage 1 network screening  
> Rule: mutable metrics are snapshots, not durable facts.

## Primary network and Stock Token sources

| Source | Supports | Does not prove |
|---|---|---|
| [About Robinhood Chain](https://docs.robinhood.com/chain/) | Live network; EVM/Arbitrum basis; ETH gas; FCFS ordering; ecosystem listings | Venue liquidity, searcher profit, pre-order visibility |
| [Connecting](https://docs.robinhood.com/chain/connecting/) | Chain ID 4663; public RPC, sequencer and feed; provider/archive guidance | Production reliability/latency from our region |
| [Transaction finality](https://docs.robinhood.com/chain/transaction-finality/) | Sub-second soft confirmation; L1 posting/finality stages | Irreversibility at soft confirmation |
| [Stock Tokens](https://docs.robinhood.com/chain/stock-tokens/) | Instrument type; ERC-20 model; tokenization window; permissioned primary issuance; multipliers | Secondary-market liquidity or accessible redemption |
| [Live assets registry](https://api.robinhood.com/rhj/assets) | Current token deployments/status/multipliers/session capability fields | Active pools, volume, holder distribution |
| [Stock Token APIs](https://docs.robinhood.com/chain/stock-token-apis/) | REST schemas; 15s price cache; raw-price multiplier semantics; corporate actions | Executable quotes or sub-second data |
| [Oracles and price feeds](https://docs.robinhood.com/chain/oracles-and-price-feeds/) | Chainlink feed integration; freshness and pause handling | Tradable external liquidity |
| [Data Streams](https://docs.robinhood.com/chain/data-streams/) | Sub-second signed pull-data architecture and verifier proxy | Free/public entitlement, Stock Token coverage, profitability |
| [Building with Stock Tokens](https://docs.robinhood.com/chain/building-with-stock-tokens/) | Documented liquidity-source patterns: AMM, propAMM, RFQ, Lighter | Actual depth or firm public RFQ availability |

## Primary venue sources

| Source | Supports | Does not prove |
|---|---|---|
| [Robinhood Chain Lighter Domains](https://docs.robinhood.com/chain/lighter-domains/) | Dedicated domain, contract/API, separate execution/liquidity, deposit/withdraw modes | Atomic AMM↔Lighter execution or current market depth |
| [Lighter API docs](https://apidocs.rh.lighter.xyz/docs/get-started) | Public market/order-book/trade API surface | Which markets are liquid today |
| [Morpho API supported networks](https://docs.morpho.org/developers/api/get-started/) | Robinhood Chain supported by Morpho data API | Specific active market balances |
| [Morpho addresses](https://docs.morpho.org/developers/contracts/addresses/) | Canonical Morpho deployment addresses | Active loans or profitable liquidations |
| [0x supported chains](https://docs.0x.org/docs/introduction/supported-chains) | Robinhood Chain Swap/Gasless/Cross-chain API support | RFQ maker response for a given public taker |
| [0x 2026-07-31 changelog](https://docs.0x.org/changelog/2026/7/31) | Native Robinhood Chain routing sources added | Source depth, availability in every quote, or profit |
| [Rialto launch announcement](https://blog.rialto.xyz/blog/introducing-rialto) | Announced propAMM and intended initial market coverage | Canonical contracts, fill history, depth, current operation |
| [Rialto supported markets](https://docs.rialto.xyz/overview/supported-markets) | Venue's stated market model | Independent onchain activity |
| [Uniswap Robinhood Chain launch](https://blog.uniswap.org/pools-trade) | First-party product/deployment claim | Pair-by-pair liquidity or arbitrage returns |

## Onchain/explorer observations

These are examples proving contract use only. They were surfaced through Blockscout's indexed transaction pages and must be decoded through RPC/API before use in a dataset.

| Evidence | Observation | Limitation |
|---|---|---|
| [Transaction `0x8e070c…5ee5`](https://robinhoodchain.blockscout.com/tx/0x8e070cd338558a0ef0b16f9236617cde051a751b6671f1f32e7935047ff55ee5) | Indexed token transfers mention `PoolManager` and `Uniswap V2` | Not classified as arbitrage; PnL not reconstructed |
| [Transaction `0x74c196…0382`](https://robinhoodchain.blockscout.com/tx/0x74c19617977e42c3819698a18e29c51cc7bdc699285105847e9ba76c994f0382) | Indexed interaction includes ASML Stock Token and Uniswap v4 position manager | Appears liquidity-related; not evidence of an executable spread |
| [Morpho contract](https://robinhoodchain.blockscout.com/address/0x9D53d5E3bd5E8d4Cbfa6DB1ca238AEA02E651010) | Explorer recognizes the canonical contract as `Morpho` | Does not enumerate market balances by itself |

## Secondary mutable metrics

DefiLlama is used as a discovery/triage source, not as the final accounting source. All figures below were displayed on pages retrieved 2026-09-25 and can change between requests.

| Source | Snapshot used | Required validation before decision |
|---|---|---|
| [Robinhood Chain page](https://defillama.com/chain/robinhood-chain) | TVL $1.016B; DEX volume $1.339B/24h and $10.018B/7d; perps $633.76M/24h; protocol rankings | Recompute from venue events/APIs for selected windows |
| [Robinhood Chain lending](https://defillama.com/protocols/lending/robinhood-chain) | Lending TVL $567.16M; Morpho is dominant | Enumerate Morpho markets and reconcile balances |
| [Morpho Blue](https://defillama.com/protocol/morpho-blue) | Robinhood Chain TVL ~$563.9M; fees and liquidation totals | Reconstruct liquidation events, costs and proceeds onchain |

## Evidence-quality notes

- Official documentation establishes intended mechanics and interfaces, but can describe capabilities before meaningful usage exists.
- Explorer search results establish that a transaction/contract exists, but human-readable labels can be incomplete or wrong. Historical work must verify bytecode, events, token addresses and traces.
- Aggregator support means a request can be routed on the chain. It does not mean an RFQ maker will respond or that every advertised source is active.
- TVL and volume are not proxies for accessible arbitrage PnL.
- REST/oracle prices are references, not exits. Profit requires an executable trade, redemption, or hedge.
- No source reviewed in this sprint establishes stable daily earnings for a public searcher.

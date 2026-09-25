# Project context

## Origin

The project began with an investigation of a Solana transaction:

- transaction: `J8TY8VkjZpAAm78GwbnEE1xkBwGdheQ4C1VsZA7Cwcv1AyDw3PxTQJ3eWh9YZmZyLQnLD3fuHBsihXbX4sTATi8`
- signer: `ESuvjvsQtjuxC4XGsDeMhx8Wp5yjQcCFGncGhupcJbg8`
- slot: `416936448`
- observed route: `0.227 USDC → 72,793.511082 ANX → 50,011,673.082571 ANB → 696,194.449401 USDC`
- observed signer USDC delta: approximately `+696,194.222401 USDC`
- observed SOL delta: approximately `-2.300174466 SOL`, dominated by a Jito tip

The route followed a large ANB sale that severely distorted liquidity across Meteora pools. Multiple searchers captured parts of the dislocation over three neighboring blocks, while many competing transactions failed.

This is a confirmed historical case study, not proof that the return is repeatable.

## Initial hypothesis

A continuously running searcher may collect small cyclic arbitrage opportunities and occasionally capture a rare liquidity dislocation. The economic test is:

```text
recurring net PnL
+ rare-event net PnL
- failed attempts
- data and server costs
- engineering and operational costs
```

## Scope expansion

The project now compares four networks:

- **Solana:** established case, fast state updates, Jito auction competition.
- **Base:** high-activity EVM L2 with sequencer-aware execution.
- **Robinhood Chain:** new EVM/Arbitrum chain combining public AMMs, proprietary liquidity, orderbooks, lending, and tokenized equities.
- **Ethereum:** mature, expensive and highly competitive; potentially better suited to private-orderflow, liquidation, CEX–DEX, and multi-protocol ideas than a simple latency race.

## Questions the project must answer

1. How many opportunities are visible per day after conservative costs?
2. How quickly does theoretical profit decay with delay?
3. How concentrated are successful executions among searchers?
4. What do failed attempts cost?
5. Which strategies are repeatable rather than tail events?
6. What data and infrastructure are needed for a fair test?
7. Can a small team reach positive net evidence before expensive infrastructure?

## Current non-goals

- promising a target income;
- custodying third-party money;
- shipping an unattended production trading system;
- implementing sandwich attacks or other user-harming strategies;
- treating paper profit as realized profit.

## Source transaction references

- Arbitrage transaction: https://solscan.io/tx/J8TY8VkjZpAAm78GwbnEE1xkBwGdheQ4C1VsZA7Cwcv1AyDw3PxTQJ3eWh9YZmZyLQnLD3fuHBsihXbX4sTATi8
- Triggering sale: https://solscan.io/tx/5wY3V7v8ALqB5hGj1vkqttLy4T65awaeTkm6G4oxt4xfvndrqFA7kLwqQq4VJzw8338B1YZyPFHooueCMyujxkFK
- Earlier intermediate arbitrage: https://solscan.io/tx/5oiBGWFxs87reNtQSH2ZCmqyp9bcVgFp78FgCjPq7zaW4m1JXsfNPFGK3qeUCcYj4c7MpsEAWerHa68b2HfiVHor

All figures should be independently reproduced before being used as fixtures or assertions in code.

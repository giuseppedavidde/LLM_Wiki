# Blockchain Technology

> Sources: Alan John & Jon Law, 2021
> Raw: [Crypto Technical Analysis](../../raw/crypto/crypto-technical-analysis-your-one-stop-guide-to-investing-trading-and-profiting.md)

## Overview

![Blockchain distributed ledger concept](images/crasht_p2_1.jpeg)

Blockchain is a distributed ledger technology (DLT) that enables trustless, decentralized transactions. Unlike centralized databases, blockchains store data across a network of computers (nodes), making them resistant to tampering, censorship, and single points of failure.

The core innovation of blockchain is solving the "double-spending problem" without a trusted intermediary. Every transaction is validated by network consensus, permanently recorded, and linked to all preceding transactions in an immutable chain.

## What Is a Blockchain?

A blockchain stores data in literal chains of blocks:

1. **Blocks** store digital information — time, date, amount, and participant digital keys for each transaction.
2. **Nodes** (computers in the network) validate each block. Bitcoin has tens of thousands of nodes; other networks may have more or fewer.
3. Once validated, the block is **appended to the public ledger** — a database recording every approved transaction in the network's history.
4. Each block is cryptographically linked to the block before and after it, forming a **chain**.

### Decentralization: The Jewelry Thief Analogy

Centralization (one vault, one security team) can be attacked from many angles — insiders, hackers, social engineering. Decentralization (assets constantly moving between unknown, distributed locations, protected by mathematical puzzles) removes the single point of failure. The network's rules are encoded in algorithms that cannot be changed once deployed, unlike centralized services that can raise fees, freeze accounts, or go bankrupt.

## Consensus Mechanisms

### Proof of Work (PoW)

Miners compete to solve complex mathematical problems. The first to solve the problem validates the block and receives a block reward. PoW is secure but energy-intensive. Bitcoin uses PoW, consuming significant computational resources in exchange for unparalleled network security.

### Proof of Stake (PoS)

Validators are chosen to create new blocks based on the amount of cryptocurrency they "stake" (lock up as collateral). PoS is far more energy-efficient than PoW. Ethereum transitioned from PoW to PoS. Cardano uses a modified PoS algorithm to improve scalability.

### Delegated Proof of Stake (DPoS)

Stakeholders vote for a small number of delegates who validate transactions on behalf of the network. DPoS is faster and more scalable than PoS but introduces some centralization risk.

### PBFT (Practical Byzantine Fault Tolerance)

A consensus mechanism designed for permissioned blockchains where validators are known. PBFT achieves consensus through multiple rounds of voting between nodes. It is highly efficient but less decentralized than PoW or PoS.

## Smart Contracts and dApps

**Smart contracts** are self-executing contracts with terms directly written into code. They run on blockchain networks and automatically execute when conditions are met. This removes the need for trust between parties. Smart contracts are irreversible, transparent, and untraceable.

**dApps** (decentralized applications) are applications that run on a blockchain network rather than a centralized server. Any app running on a peer-to-peer network without a centralized owner is a dApp.

**DAOs** (Decentralized Autonomous Organizations) are organizations run by computer code rather than humans. Governance tokens enable stakeholders to vote on protocol upgrades and decisions without centralized management.

## Layer 1 vs Layer 2

**Layer 1** is the base blockchain protocol — Bitcoin, Ethereum, Solana. Layer 1 handles security, consensus, and the core ledger. Scaling Layer 1 is difficult because every node must process every transaction.

**Layer 2** solutions build on top of Layer 1 to improve scalability and throughput. Examples include the Lightning Network (Bitcoin) and various Ethereum layer-2 rollups. Layer 2 processes transactions off the main chain and settles final results on Layer 1, dramatically increasing capacity.

The **scalability trilemma** (coined by Ethereum founder Vitalik Buterin) states that blockchain networks can only achieve two of three properties simultaneously: **decentralization**, **security**, and **scalability**. Most design tradeoffs involve choosing which property to deprioritize.

## Interoperability and Cross-Chain Bridges

Different blockchains operate in isolation by default. Cross-chain bridges enable assets and data to move between blockchains — for example, moving Bitcoin to Ethereum to use in DeFi applications. Bridges lock assets on the source chain and mint equivalent tokens on the destination chain. They are a critical infrastructure component for a multi-chain ecosystem but have been frequent targets for hacks.

## Blockchain Security

### 51% Attack

A group of miners controlling more than 50% of a network's hash rate (PoW) or staked assets (PoS) can manipulate the blockchain — reversing transactions, double-spending coins, and preventing new transactions from confirming. A successful 51% attack has never occurred on a major blockchain, but smaller networks with low hash rates are vulnerable.

### Double-Spending

The risk that a user spends the same coins twice. Blockchain prevents this through consensus — once a transaction is confirmed and added to a block, altering it would require re-mining all subsequent blocks, which becomes exponentially harder as the chain grows.

### Sybil Attack

An attacker creates multiple fake nodes to gain disproportionate influence over the network. PoW prevents Sybil attacks by requiring computational work; PoS requires staked economic value.

### Exchange Hacks

![Crypto security: blockchain vs exchanges](images/crasht_p5_1.jpeg)

The weakest link in crypto security is not the blockchain itself, but the centralized exchanges where most users trade. In 2019, 12 crypto exchanges were hacked, resulting in 510,000 stolen credentials and $293M in losses. Ironically, the centralization that blockchain was designed to eliminate is the primary attack vector.

## Types of Blockchains

- **Public blockchains**: Anyone can participate, read, and write. Bitcoin and Ethereum are public.
- **Private blockchains**: Access is restricted to approved participants.
- **Consortium blockchains**: Controlled by a group of organizations rather than a single entity.
- **Hybrid blockchains**: Combine elements of public and private blockchains.

Public blockchains are the most common and most relevant for cryptocurrency trading.

## Blockchain Origins

- **1991**: First conceptualization of cryptographically secured chains of blocks.
- **2000**: Stefan Konst published theory on cryptographic chains and practical implementation.
- **2008**: Satoshi Nakamoto released the Bitcoin whitepaper.
- **2009**: Nakamoto implemented the first blockchain as the public ledger for Bitcoin.
- **2014**: Blockchain use cases expanded beyond cryptocurrency.

The identity of Satoshi Nakamoto — the individual or group who created Bitcoin — remains unknown. Nakamoto holds approximately 1.1 million Bitcoins (worth over $50 billion), making the anonymous creator one of the wealthiest people on earth.

## See Also

- [Crypto Technical Analysis](crypto-technical-analysis.md)
- [Crypto Fundamental Analysis](crypto-fundamental-analysis.md)
- [Crypto Hype Analysis](crypto-hype-analysis.md)
- [Cryptocurrency Fundamentals](crypto-fundamentals.md)
- [Volume Profile](../trading/volume-profile.md)
- [Order Flow and Footprint](../trading/order-flow-footprint.md)
- [Contrarian Sentiment Analysis](../trading/contrarian-sentiment-analysis.md)
## 🔗 Graph Connections

| Concept | Relation | Source |
|---|---|---|
| Bitcoin (BTC) | Underpins | EXTRACTED |
| Ethereum (ETH) | Feature Of | EXTRACTED |
| Initial Coin Offering (ICO) | Funding Mechanism For | EXTRACTED |

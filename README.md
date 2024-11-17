# CryptoMPT

Modern Portfolio Theory (MPT) guides investors in balancing risk and return. It helps maximize returns for a specific risk level or minimize risk for a target return by diversifying investments. By combining assets with different risks and correlations, MPT aims to reduce overall portfolio risk and achieve optimal performance.

## Overview

Modern Portfolio Theory (MPT) is a foundational concept in finance that focuses on optimizing asset allocation to achieve the best trade-off between risk and reward. CryptoMPT applies this methodology to the volatile and diverse cryptocurrency market, providing portfolio recommendations that are stored on-chain for transparency and accessibility.

In this project, we:

1. __Analyze Historical Data__: Gather crypto pricing data using decentralized oracles (e.g., ChainLink).
2. __Optimize Portfolios__: Apply MPT to generate three portfolio strategies:
   - Minimized Risk: Prioritizes stability in a volatile market.
   - Maximized Returns: Focuses on growth potential.
   - Optimal Sharpe Ratio: Balances risk and reward effectively. 
3. __Store Allocations On-Chain__: Publish optimized allocations to a smart contract deployed on multiple blockchains, ensuring transparency and global accessibility.

## How it works

CryptoMPT is divided into 3 main sections. On the first one, primarily inside the ```./datasource``` folder, we retrieve historical data from ChainLink oracles. The second section, inside ```./mpt```, involves analyzing prices and generating exploring correlations between them to create portfolios with certain risk/rewards. Finally, using ```./contract```,we store the details of certain asset allocations on various chains for easy of use and to used as a building block for more advanced operations.


![CryptoMPT Explainer](CryptoMPT.webp "CryptoMPT Explainer")
Fig-1. Fairly accurate AI-Generated hallucination of how CryptoMPT works.



1. __Data Collection__:

   - Historical price data is gathered using ChainLink oracles. Example assets include Bitcoin, Ethereum, Solana, UniSwap, ChainLink, Aave, Dogecoin, Pepe, and Wif.

2. __Analysis and Optimization__:

   - Variance and covariance are calculated for the assets.
   - MPT is applied to generate three portfolio strategies: Min Risk, Max Return, and Optimal Sharpe Ratio.

3. __On-Chain Deployment__:

   - Optimized allocations are stored in a Solidity smart contract, CryptoMPT.sol.
   - Allocations are mapped to week numbers derived from timestamps for efficient data lookup.

4. __Accessing the Data__:
   - Anyone can query the smart contract to retrieve the latest portfolio allocations.

## Test deployments

This project's smart-contract was deployed, and __verified__, in number of chains including:


  * [BitKub](https://www.bitkub.com/) Testnet: [0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04](https://testnet.bkcscan.com/address/0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04?tab=contract)
  * [UniChain](https://www.unichain.org/) Sepolia: [0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04](https://sepolia.uniscan.xyz/address/0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04#code)
  * [Scroll](https://scroll.io/) Sepolia: [0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04](https://sepolia.scrollscan.com/address/0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04#code)
  * [Mantle](https://www.mantle.xyz/) Sepolia: [0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04](https://sepolia.mantlescan.xyz/address/0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04#code)
  * [Rootstock](https://rootstock.io/) Testnet: [0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04](https://explorer.testnet.rootstock.io/address/0xa1ac5bd954aa0857f15287ec67fee4d5587f6e04?__ctab=Code) 
  * [Morph](https://www.morphl2.io/) Holesky: [0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04](https://explorer-holesky.morphl2.io/address/0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04?tab=contract)
  * [Flare](https://flare.network/) Coston2: [0x18253170C3F5719E621Cc65330135032cBA33632](https://coston2-explorer.flare.network/address/0x18253170C3F5719E621Cc65330135032cBA33632?tab=contract)
  * [Base](https://www.base.org/) Sepolia: [0x72aCf8dB0e17D5A4bA9eB8176375D8F06eE3bfd0](https://base-sepolia.blockscout.com/address/0x72aCf8dB0e17D5A4bA9eB8176375D8F06eE3bfd0?tab=contract)
  * [Ethereum](https://www.base.org/) Sepolia: [0xbF31eC2eFBEeC6F5cfdbb3febc703BC1be0A8FE5](https://sepolia.etherscan.io/address/0xbF31eC2eFBEeC6F5cfdbb3febc703BC1be0A8FE5#code)
* 

Since all of these chains are EVM-compatible, deploying the smart contract was seamless and efficient, allowing us to quickly get up and running across all of them.

This project makes extensive use of [ChainLink](https://chain.link/), [ENS](https://ens.domains/), and [Blockscout](https://www.blockscout.com/)'s explorer.

## Presentation and Video

This [project's presentation](./CryptoMPT.pdf) is available as well as [video overview](./CryptoMPT.mp4).

### About the author

António Roldão is the creator of CryptoMPT. António is an entrepreneur and a passionate technologist with a Ph.D. in Electronics and Computer Engineering from Imperial College London. Antonio’s career spans diverse fields, including aerospace, finance, and artificial intelligence. He is the co-founder and CEO of [muse.ai](https://muse.ai), where he has pioneered advanced video search technology leveraging cutting-edge AI. Antonio combines deep technical expertise with a drive to create technologies that empower people and simplify complexity.

## Contributing
We welcome contributions to enhance CryptoMPT! Please submit issues or pull requests to this repository.

## License
This project is licensed under the MIT License.


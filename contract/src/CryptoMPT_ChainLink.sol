// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/shared/interfaces/AggregatorV3Interface.sol";

/**
 * @title CryptoMPT - A Solidity Implementation of Modern Portfolio Theory (MPT)
 *
 * @dev Modern Portfolio Theory (MPT) is a mathematical framework used to optimize
 * investments by balancing risk and return. MPT suggests how to allocate assets in
 * a portfolio to achieve maximum returns for a given level of risk or minimize risk
 * for a desired level of return. The Sharpe ratio is often used as a metric for
 * performance in this context, representing the return-to-risk efficiency of a portfolio.
 *
 * This smart contract enables storing and retrieving weekly portfolio data for multiple
 * crypto assets, allowing for a structured record of allocations and their associated
 * metrics like yield, volatility, and Sharpe ratio. The contract is open and transparent
 * making it suitable for decentralized financial (DeFi) applications.
 *
 * @author Antonio Roldao
 */

contract CryptoMPT {
    /**
     * @dev Struct to store weekly portfolio data.
     * Each entry contains the timestamp, yield, volatility, Sharpe ratio, and allocation
     * percentages for various crypto assets.
     */
    AggregatorV3Interface internal dataFeed;

    struct PortfolioData {
        uint256 ts;           // Timestamp of the data (seconds since Unix epoch).
        uint256 yield;        // Yield percentage (e.g., 1537 for 15.37%).
        uint256 volatility;   // Volatility percentage (e.g., 29 for 0.29%).
        uint256 sharpe;       // Sharpe ratio (scaled for precision, e.g., 5324 for 53.24).
        uint256 btc;          // BTC allocation percentage (e.g., 20 for 20%).
        uint256 eth;          // ETH allocation percentage.
        uint256 sol;          // SOL allocation percentage.
        uint256 uni;          // UNI allocation percentagev
        uint256 link;         // LINK allocation percentage.
        uint256 aave;         // AAVE allocation percentage.
        uint256 doge;         // DOGE allocation percentage.
        uint256 pepe;         // PEPE allocation percentage.
        uint256 wif;          // WIF allocation percentage.
        int btc_price;        // Value of BTC at update time.
    }

    // Mapping to store PortfolioData indexed by week number.
    mapping(uint256 => PortfolioData) private portfolioData;

    // Address of the contract owner, set during deployment.
    address public owner;

    // Event emitted whenever new portfolio data is added.
    event NewCryptoMPT(uint256 indexed weekNumber, PortfolioData data);

    /**
     * @dev Constructor to set the contract owner as the deployer.
     */
    constructor() {
        owner = msg.sender;

        /**
         * Network: Sepolia
         * Aggregator: BTC/USD
         * Address: 0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43
         */
        dataFeed = AggregatorV3Interface(
            0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43
        );

    }

    /**
     * @dev Modifier to restrict function execution to the owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Calculates the week number from a given timestamp.
     * @param timestamp The Unix timestamp in seconds.
     * @return The calculated week number.
     */
    function getWeekNumber(uint256 timestamp) public pure returns (uint256) {
        return timestamp / (7 * 24 * 60 * 60); // Total seconds in a week
    }

    /**
     * @dev Function to store weekly portfolio data.
     * Only the owner can call this function.
     *
     * @param values Array of 13 unsigned integers representing:
     *        [timestamp, yield, volatility, sharpe, btc, eth, sol, uni, link, aave, doge, pepe, wif]
     *        The values are stored as percentages scaled to integers for precision.
     */
    function setMPT(uint256[] calldata values) external onlyOwner {
        require(values.length == 13, "Values array must contain exactly 13 elements");

        // Extract the timestamp and calculate the corresponding week number.
        uint256 ts = values[0];
        uint256 weekNumber = getWeekNumber(ts);

        int btc_price = getChainlinkDataFeedLatestAnswer();

        // Create a new PortfolioData struct from the input values.
        PortfolioData memory data = PortfolioData(
            ts,
            values[1],  // Yield.
            values[2],  // Volatility.
            values[3],  // Sharpe ratio.
            values[4],  // BTC allocation.
            values[5],  // ETH allocation.
            values[6],  // SOL allocation.
            values[7],  // UNI allocation.
            values[8],  // LINK allocation.
            values[9],  // AAVE allocation.
            values[10], // DOGE allocation.
            values[11], // PEPE allocation.
            values[12],  // WIF allocation.
            btc_price    // Value of BTC at update time.
        );

        // Store the PortfolioData in the mapping, indexed by the week number.
        portfolioData[weekNumber] = data;

        // Emit an event to log the new data.
        emit NewCryptoMPT(weekNumber, data);
    }

    /**
     * @dev Function to retrieve portfolio data for a given timestamp.
     * The function converts the timestamp to a week number and retrieves the data.
     *
     * @param timestamp The Unix timestamp in seconds.
     * @return The PortfolioData associated with the week number derived from the timestamp.
     */
    function getMPT(uint256 timestamp) external view returns (PortfolioData memory) {
        uint256 weekNumber = getWeekNumber(timestamp);
        return portfolioData[weekNumber];
    }

    /**
     * Returns the latest answer for the price of Bitcoin.
     */
    function getChainlinkDataFeedLatestAnswer() public view returns (int) {
        // prettier-ignore
        (
            /* uint80 roundID */,
            int answer,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = dataFeed.latestRoundData();
        return answer;
    }
}

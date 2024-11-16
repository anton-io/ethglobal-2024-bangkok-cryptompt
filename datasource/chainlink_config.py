import os
import json

from web3 import Web3

DIR_THIS = os.path.abspath(os.path.dirname(__file__))

# Got this RPC from:
# https://chainlist.org/chain/1

# Ethereum:
# WEB3_PROVIDER = 'https://eth.llamarpc.com'

# Arbitrum:
WEB3_PROVIDER = 'https://arbitrum.llamarpc.com'
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))
print(f"Web3 provider: {WEB3_PROVIDER}")

# BTC/USD (Ethereum) | btc-usd.data.eth
# Got this Address/ABI from:
# https://data.chain.link/feeds/ethereum/mainnet/btc-usd

# Asset Name  |  ENS Shortcut  |   ARB ChainLink Contract Addr
chainlink_addrs = {
# L1:
 'btc': ['btc-usd.data.eth',   '0x6ce185860a4963106506C203335A2910413708e9'],
 'eth': ['eth-usd.data.eth',   '0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612'],
 'sol': ['sol-usd.data.eth',   '0x24ceA4b8ce57cdA5058b924B9B9987992450590c'],
# Apps:
 'uni': ['uni-eth.data.eth',  '0x9C917083fDb403ab5ADbEC26Ee294f6EcAda2720'],
'link': ['eth-usd.data.eth',  '0x86E53CF1B870786351Da77A57575e79CB55812CB'],
'aave': ['aave-usd.data.eth', '0xaD1d5344AaDE45F43E596773Bcc4c423EAbdD034'],
# Memes:
'doge': ['doge-usd.data.eth', '0x9A7FB1b3950837a8D9b40517626E11D4127C098C'],
'pepe': ['pepe-usd.data.eth', '0x02DEd5a7EDDA750E3Eb240b54437a54d57b74dBE'],
 'wif': ['wif-usd.data.eth',  '0xF7Ee427318d2Bd0EEd3c63382D0d52Ad8A68f90D'],
}

# Load the ChainLink ABI.
abi = json.load(open(f"{DIR_THIS}/chainlink_abi.json"))

# Choose the start and end dates for the timeseries:
DATE_TS_START = "04/11/2024 00:00:00"
DATE_TS_END   = "10/11/2024 23:59:59"
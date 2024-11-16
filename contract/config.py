#!/usr/bin/env python3

# Shared configuration.

import os
import eth_account
from web3 import Web3


DIR_THIS = os.path.abspath(os.path.dirname(__file__))

CONTRACT="CryptoMPT"

# Target Chain RPC (using Ganache for testing).
# WEB3_PROVIDER = 'HTTP://127.0.0.1:7545'
WEB3_PROVIDER = 'https://arb1.arbitrum.io/rpc'
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))


# Contract's ABI and BIN.
CONTRACT_BIN  = f"{DIR_THIS}/src/output/{CONTRACT}.bin"
CONTRACT_ABI  = f"{DIR_THIS}/src/output/{CONTRACT}.abi"

# Contract's address after it has been deployed:
CONTRACT_ADDR = f"0xa1AC5bD954aa0857F15287eC67Fee4d5587f6E04"

# Load private key (stored in .pkey).
try:
    PKEY = open(f"{DIR_THIS}/.pkey").read()
except Exception as _:
    print(f"Add private key to {DIR_THIS}/.pkey")
    exit(-1)

# Wallet address derived from the private key.
account = eth_account.Account.from_key(PKEY)
user_address = account.address

# # For POA
# from web3.middleware import geth_poa_middleware
# w3.middleware_onion.inject(geth_poa_middleware, layer=0)

if os.path.exists(CONTRACT_ABI):
    # Contract's ABI.
    contract_abi = open(CONTRACT_ABI, 'r').read()

    # Initialize the contract.
    contract = w3.eth.contract(address=CONTRACT_ADDR, abi=contract_abi)

#!/usr/bin/env python3

# Shared configuration.

import os
import eth_account
from web3 import Web3

DIR_THIS = os.path.abspath(os.path.dirname(__file__))

CONTRACT="CryptoMPT"

# Target Chain RPC (using Ganache for testing).
RPC_URL = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Contract's ABI and BIN.
CONTRACT_BIN  = f"{DIR_THIS}/src/output/{CONTRACT}.bin"
CONTRACT_ABI  = f"{DIR_THIS}/src/output/{CONTRACT}.abi"

# Contract's address after it has been deployed:
CONTRACT_ADDR = f"0x5bAdb2201d409E7887BAF43901ade77b038aba31"

# Load private key (stored in .pkey).
try:
    PKEY = open(f"{DIR_THIS}/.pkey").read()
except Exception as _:
    print(f"Add private key to {DIR_THIS}/.pkey")
    exit(-1)

# Wallet address derived from the private key.
account = eth_account.Account.from_key(PKEY)
user_address = account.address

if os.path.exists(CONTRACT_ABI):
    # Contract's ABI.
    contract_abi = open(CONTRACT_ABI, 'r').read()

    # Initialize the contract.
    contract = web3.eth.contract(address=CONTRACT_ADDR, abi=contract_abi)

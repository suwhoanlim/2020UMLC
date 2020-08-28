import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'HTTP://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/HelloWorld.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = web3.toChecksumAddress("0xB24921DB5bDB2955229d7e1f89eacc4c63B8B596")

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json["abi"]  # fetch contract's abi - necessary to call its functions
'''
abi = json.loads('[{"constant": true,"inputs": [],"name": "sayHello","outputs": [{"internalType": "string","name": "","type": "string"}],"payable": false,"stateMutability": "pure","type": "function"}]')
'''

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

# Call contract function (this is not persisted to the blockchain)
message = contract.functions.sayHello().call()

print(message)
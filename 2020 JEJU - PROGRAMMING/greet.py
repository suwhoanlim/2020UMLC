import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())
#account_1 = '0x09AE93c233Bf26b4f83824244d23c1A0EF61222D' # Fill me in
#account_2 = '0xE96E7286bDa0AD5a22FA12c9a8E71380f33E125E' # Fill me in
#private_key = '0x0ea6f4451dce5ab03185cdaf46b4bb66150720493ad97ba71f1319918b967af1' # Fill me in

web3.eth.defaultAccount = web3.eth.accounts[0] # already unlocked

abi = json.loads('[{"constant": false,"inputs": [{"name": "_greeting","type": "string"}],"name": "setGreeting","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"inputs": [],"payable": false,"stateMutability": "nonpayable","type": "constructor"},{"constant": true,"inputs": [],"name": "greet","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "greeting","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "view","type": "function"}]')
address = web3.toChecksumAddress("0x3b38F01D75827311Dd1F442043605127F7580e47")

contract = web3.eth.contract(address = address, abi = abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('hi').transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated gre: {}'.format(contract.functions.greet().call()))

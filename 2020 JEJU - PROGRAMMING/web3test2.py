from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())
print(web3.eth.blockNumber)


account_1 = '0x09AE93c233Bf26b4f83824244d23c1A0EF61222D' # Fill me in
account_2 = '0xE96E7286bDa0AD5a22FA12c9a8E71380f33E125E' # Fill me in
private_key = '0x0ea6f4451dce5ab03185cdaf46b4bb66150720493ad97ba71f1319918b967af1' # Fill me in
# PRkey of the 1st account

nounce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nounce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),	
    'gas': 200000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
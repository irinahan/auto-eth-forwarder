import os
from web3 import Web3

rpc_url = os.getenv("RPC_URL")
private_key = os.getenv("PRIVATE_KEY")
my_address = os.getenv("MY_ADDRESS")
destination_address = os.getenv("DESTINATION_ADDRESS")
gas_price_gwei = 20

web3 = Web3(Web3.HTTPProvider(rpc_url))

def send_all_eth():
    nonce = web3.eth.get_transaction_count(my_address)
    balance = web3.eth.get_balance(my_address)
    if balance == 0:
        print("No ETH to send.")
        return
    gas_price = web3.toWei(gas_price_gwei, 'gwei')
    gas_limit = 21000
    total_gas_cost = gas_price * gas_limit
    send_value = balance - total_gas_cost
    if send_value <= 0:
        print("Insufficient funds for gas.")
        return
    tx = {
        'nonce': nonce,
        'to': destination_address,
        'value': send_value,
        'gas': gas_limit,
        'gasPrice': gas_price,
    }
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Sent {web3.fromWei(send_value, 'ether')} ETH to {destination_address}. TX hash: {web3.toHex(tx_hash)}")

# Запуск скрипта
send_all_eth()

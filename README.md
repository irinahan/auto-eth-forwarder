README in English:

Automatic ETH Forwarder via GitHub Actions
This repository enables you to automatically forward all incoming ETH from your wallet to a specified address using GitHub Actions. The script is triggered on a schedule or manually and sends all available ETH (minus gas fee) to your main address.

Structure
auto_send_eth.py — main Python script handling ETH sending.

requirements.txt — dependencies list.

.github/workflows/auto_send_eth.yml — GitHub Actions workflow configuration.

Setup and Usage
Fork or create a repository with this structure.

Add Secrets in your repository settings (Settings → Secrets → Actions):

RPC_URL — your Ethereum RPC node endpoint (e.g., Infura/Alchemy)

PRIVATE_KEY — your wallet's private key (NEVER store it in public format!)

MY_ADDRESS — your sending ETH address

DESTINATION_ADDRESS — address to receive ETH

Run the workflow manually (Actions tab) or let it run every 30 minutes automatically.

The script checks the balance. If ETH is detected, it sends the full available amount (minus gas) to the recipient address.

Important!
Store private keys ONLY in secrets, never in your code!

Use with disposable wallets and small amounts for safety.

# main.py
# Entry point for ChainVault demo usage

import os
from dotenv import load_dotenv
from chainvault.wallet import Wallet
from chainvault.eth_client import EthereumClient


def main():
    """
    Demonstration of ChainVault functionality.
    """

    load_dotenv()

    rpc_url = os.getenv("ETH_RPC_URL")
    if not rpc_url:
        raise EnvironmentError("ETH_RPC_URL not found in environment variables.")

    # Initialize Ethereum client
    client = EthereumClient(rpc_url)

    # Generate new wallet
    wallet = Wallet.generate()

    print("=== New Wallet Generated ===")
    print(f"Address: {wallet.address}")
    print(f"Private Key: {wallet.private_key}")
    print()

    # Check balance
    balance = client.get_balance(wallet.address)
    print(f"Wallet Balance: {balance} ETH")

    # Sign message
    message = "Hello from ChainVault"
    signature = wallet.sign_message(message)

    print("\n=== Message Signed ===")
    print(f"Message: {message}")
    print(f"Signature: {signature}")


if __name__ == "__main__":
    main()

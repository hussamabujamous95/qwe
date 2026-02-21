# eth_client.py
# Ethereum blockchain interaction module

from web3 import Web3


class EthereumClient:
    """
    Handles communication with Ethereum blockchain.
    """

    def __init__(self, rpc_url: str):
        """
        Initialize Web3 connection.
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))

        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node.")

    def get_balance(self, address: str) -> float:
        """
        Get ETH balance for an address.
        Returns balance in Ether.
        """
        balance_wei = self.web3.eth.get_balance(address)
        return self.web3.from_wei(balance_wei, "ether")

    def get_nonce(self, address: str) -> int:
        """
        Get transaction count (nonce) for address.
        """
        return self.web3.eth.get_transaction_count(address)

    def build_transaction(self, from_address: str, to_address: str, value_eth: float):
        """
        Build raw transaction dictionary.
        Does not send transaction.
        """
        nonce = self.get_nonce(from_address)

        tx = {
            "nonce": nonce,
            "to": to_address,
            "value": self.web3.to_wei(value_eth, "ether"),
            "gas": 21000,
            "gasPrice": self.web3.eth.gas_price,
        }

        return tx

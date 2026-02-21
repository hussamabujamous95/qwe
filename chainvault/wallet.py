# wallet.py
# Module responsible for wallet creation and cryptographic operations

from eth_account import Account
import secrets


class Wallet:
    """
    Represents an Ethereum wallet with basic cryptographic features.
    """

    def __init__(self, private_key: str):
        """
        Initialize wallet with a private key.
        """
        self.account = Account.from_key(private_key)

    @staticmethod
    def generate():
        """
        Generate a new secure Ethereum wallet.
        Uses cryptographically secure randomness.
        """
        private_key = secrets.token_hex(32)
        return Wallet(private_key)

    @property
    def address(self):
        """
        Returns wallet public address.
        """
        return self.account.address

    @property
    def private_key(self):
        """
        Returns wallet private key as hex string.
        WARNING: Never expose this in production environments.
        """
        return self.account.key.hex()

    def sign_message(self, message: str):
        """
        Sign a text message with the wallet private key.
        """
        signed = self.account.sign_message(
            Account.signable_message_from_text(message)
        )
        return signed.signature.hex()

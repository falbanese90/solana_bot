import solana
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from config import encoded_keypair

from base58 import b58decode, b58encode

client = Client('https://api.devnet.solana.com')
keypair = b58decode(encoded_keypair)
private_key = keypair[:32]
public_key = keypair[32:]

kpair = Keypair.from_secret_key(private_key)

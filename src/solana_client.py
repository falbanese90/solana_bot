from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from config import encoded_keypair, receiver_public

from base58 import b58decode, b58encode

client = Client('https://api.devnet.solana.com')

## Sender
keypair = b58decode(encoded_keypair)
private_key = keypair[:32]
public_key = keypair[32:]

## Create Keypair object from decoded private key
kpair = Keypair.from_secret_key(private_key)

## Outline contents of transaction
txn = Transaction().add(transfer(TransferParams(
    from_pubkey=kpair.public_key,
    to_pubkey=PublicKey(receiver_public),
    lamports=200000
)))


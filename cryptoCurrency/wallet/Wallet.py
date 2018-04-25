from cryptoCurrency.blockChainVerifier import BlockChainVerifier
from cryptoCurrency.helper import BlockMaker


def main():
    print(str(make_wallet(example_block_chain)))


def get_balance(block_chain_string, account):
    wallet_store = make_wallet(block_chain_string)
    money = 0
    try:
        print(str(account) + " has ", end="")
        print(str(wallet_store[account]), end="")
        money = wallet_store[account]
    except KeyError:
        print("0", end="")
    print(" ICS-455-Cryptocurrency")
    return money


def make_wallet(block_chain_string):
    # make sure it is a valid block chain
    BlockChainVerifier.test_blocks(block_chain_string, False)

    wallet_store = {}

    block_chain = BlockMaker.separate_blocks(block_chain_string)

    if len(block_chain) > 0:
        for json_block in block_chain:
            block = BlockMaker.make_block(json_block)
            transaction = block["transactions"]
            receiver = transaction["receiver"]
            sender = transaction["sender"]
            amount = transaction["amount"]

            # zero out null values
            try:
                previous_receiver_value = wallet_store[receiver]
            except KeyError:
                previous_receiver_value = 0
            try:
                previous_sender_value = wallet_store[sender]
            except KeyError:
                previous_sender_value = 0

            # not checking for negative balances, maybe later
            wallet_store.update({receiver: previous_receiver_value + amount})
            wallet_store.update({sender: previous_sender_value - amount})
    else:
        print("Empty block chain")

    return wallet_store


example_block0 = """{
    "previous_hash": "",
    "timestamp": 1506057125.900785,
    "proof": 65,
    "index": 0,
    "transactions": [
        {
            "amount": 100,
            "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29",
            "receiver": "wvfYvNSFAwOFVV4B3o1kxsSY",
            "sender": "MIICWwIBAAKBgHztyBDR5al"
        }
    ]
}"""

example_block1 = """{
    "index": 1,
    "timestamp": 1606057125.900785,
    "transactions": [
        {
            "sender": "MIICWwIBAAKBgHztyBDR5al",
            "receiver": "wvfYvNSFAwOFVV4B3o1kxsSY",
            "amount": 100,
            "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29"
        }
    ],
    "proof": 1,
    "previous_hash": "48e3d46ceb2c56d8b33889601ee02651667b18b3763d503207177324e74cb840"
}"""

example_block2 = """{
    "index": 2,
    "timestamp": 1706057125.900785,
    "transactions": [
        {
            "sender": "MIICWwIBAAKBgHztyBDR5al",
            "receiver": "wvfYvNSFAwOFVV4B3o1kxsSY",
            "amount": 300,
            "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29"
        }
    ],
    "proof": 8,
    "previous_hash": "357a185c6f8da30504b8a36cb03587d0e98c3a89b69eeab904434ddccc6f4de1"
}"""

example_block_chain = "[" + example_block0 + "," + example_block1 + "," + example_block2 + "]"

if __name__ == "__main__":
    main()

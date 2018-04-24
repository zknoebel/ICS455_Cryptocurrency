import json

from src.Wallet import Wallet


# go through each block and check the hashes
def main():
    # test a transaction that should pass
    print("Test valid transaction:")
    print("Passes: " + str(verify_transaction(example_block_chain, valid_transaction)))

    print()

    # test a transaction that should fail
    print("Test invalid transaction:")
    print("Passes: " + str(verify_transaction(example_block_chain, invalid_transaction)))


def verify_transaction(block_chain_string, transaction_string):
    wallet_store = Wallet.make_wallet(block_chain_string)
    transaction = json.loads(transaction_string)

    try:
        if wallet_store[transaction["sender"]] > transaction["amount"]:
            return True
        else:
            return False
    except KeyError:
        return False


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
            "amount": 100,
            "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29"
        }
    ],
    "proof": 8,
    "previous_hash": "357a185c6f8da30504b8a36cb03587d0e98c3a89b69eeab904434ddccc6f4de1"
}"""

valid_transaction = """{
  "amount": 100,
  "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29",
  "receiver": "nwA6Sioun0wes7wASE2fo3i",
  "sender": "wvfYvNSFAwOFVV4B3o1kxsSY"
}
"""

invalid_transaction = """{
  "amount": 100,
  "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29",
  "receiver": "wvfYvNSFAwOFVV4B3o1kxsSY",
  "sender": "MIICWwIBAAKBgHztyBDR5al"
}
"""

example_block_chain = "[" + example_block0 + "," + example_block1 + "," + example_block2 + "]"

if __name__ == "__main__":
    main()

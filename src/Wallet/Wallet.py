from src.Helper import BlockMaker
from src.BlockChainVerifier import BlockChainVerifier

def main():
    print("Wallet Information\n", end="")
    make_wallet(example_block_chain)

def make_wallet(block_chain_string):

    # make sure it is a valid block chain
    BlockChainVerifier.test_blocks(block_chain_string)

    wallet_store = {}

    block_chain = BlockMaker.separate_blocks(block_chain_string)

    if len(block_chain) > 0:
        for json_block in block_chain:
            block = BlockMaker.make_block(json_block)

            previous_sender_value = wallet_store[block["transactions"]["sender"]]
            previous_receiver_value = wallet_store[block["transactions"]["receiver"]]

            if previous_sender_value != None:
                #todo throw error
            else:
                wallet_store.update(block["transactions"]["sender"], block["transactions"]["amount"] - previous_sender_value)

#todo add receiver

            print("Block at index " + str(block["index"]) + " has been verified.")
            index += 1
            hashed_value = BlockMaker.hash(block)

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

from hashlib import sha256
from src.Helper import BlockMaker
from src.BlockChainVerifier import BlockChainVerifier
import json

import json

example_block0 = """
{
    "previous_hash": "",
    "timestamp": 1506057125.900785,
    "proof": 0,
    "index": 0,
    "transactions": [
        {
            "amount": 100,
            "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29",
            "receiver": "wvfYvNSFAwOFVV4B3o1kxsSY",
            "sender": "MIICWwIBAAKBgHztyBDR5al"
        }
    ]
 }
"""

example_block1 = """
{
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
    "proof": 0,
    "previous_hash": "48e3d46ceb2c56d8b33889601ee02651667b18b3763d503207177324e74cb840"
}
"""

example_block2 = """
{
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
    "proof": 0,
    "previous_hash": "357a185c6f8da30504b8a36cb03587d0e98c3a89b69eeab904434ddccc6f4de1"
}
"""

example_block10 = """
{
    "index": 10,
    "timestamp": 1706057125.900785,
    "transactions": [
        {
            "sender": "MIICWwIBAAKBgHztyBDR5al",
            "receiver": "wvfYvNSFAwOFVV4B3o1kxsSY",
            "amount": 100,
            "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29"
        }
    ],
    "proof": 0,
    "previous_hash": "357a185c6f8da30504b8a36cb03587d0e98c3a89b69eeab904434ddccc6f4de1"
}
"""

example_block100 = """
{
    "index": 100,
    "timestamp": 1706057125.900785,
    "transactions": [
        {
            "sender": "MIICWwIBAAKBgHztyBDR5al",
            "receiver": "wvfYvNSFAwOFVV4B3o1kxsSY",
            "amount": 100,
            "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29"
        }
    ],
    "proof": 0,
    "previous_hash": "357a185c6f8da30504b8a36cb03587d0e98c3a89b69eeab904434ddccc6f4de1"
}
"""


def main():
    # hardness index of 2
    proof_example()

    # example block chain of length 3
    find_proof_of_work(example_block0)
    find_proof_of_work(example_block1)
    find_proof_of_work(example_block2)

    # example with hardness index of 2
    find_proof_of_work(example_block10)

    # example with hardness index of 3
    find_proof_of_work(example_block100)


# proof of work slide
def proof_example():
    r = {"proof": 0, "data": [1, 2, 3]}

    while sha256(json.dumps(r).encode()).hexdigest()[-2:] != "00":
        r["proof"] += 1
        print("last chars = " + sha256(json.dumps(r).encode()).hexdigest()[-2:])

    print("proof = " + str(r["proof"]))


def find_proof_of_work(json_block):
    block = BlockMaker.make_block(json_block)

    # the hardness will be the matching the index as the last two chars in the hash
    hardness = block["index"]
    hardness_index = -1 * len(str(hardness))

    if BlockMaker.hash(block)[hardness_index:] != str(hardness):
        block["proof"] = 0

    while BlockMaker.hash(block)[hardness_index:] != str(hardness):
        block["proof"] += 1

    print("proof of newly mined block = " + str(block["proof"]))
    print("hash of newly mined block = " + str(sha256(json.dumps(block).encode()).hexdigest()))
    return BlockMaker.make_json(block)


def mine_block(block_chain, timestamp, transactions):
    verified_tuple = BlockChainVerifier.test_blocks(block_chain)
    index = verified_tuple[0] + 1
    previous_hash = verified_tuple[1]
    proof = 0

    block = {"previous_hash": previous_hash, "timestamp": timestamp, "proof": proof, "index": index,
             "transactions": transactions}
    json_block = BlockMaker.make_json(block)

    # todo check for enough money in wallet when function is ready

    mined_block = find_proof_of_work(json_block)

    new_block_chain = BlockMaker.add_to_chain(block_chain, mined_block)

    return new_block_chain


if __name__ == "__main__":
    main()

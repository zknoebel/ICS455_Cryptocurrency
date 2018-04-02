from src.Helper import BlockMaker


# go through each block and check the hashes
def main():
    # test an example block chain
    print("Test correct block chain: ", end="")
    test_hashes(example_block_chain)

    print()

    # test an example that should fail
    print("Test incorrect block chain: ", end="")
    try:
        example_block_chain.reverse()
        test_hashes(example_block_chain)
    except ValueError as e:
        print(str(e))


def test_hashes(block_chain):
    hashed_value = ""

    for json_block in example_block_chain:
        block = BlockMaker.make_block(json_block)
        if hashed_value != block["previous_hash"]:
            raise ValueError("Hash does not match")

        hashed_value = BlockMaker.hash(block)

    print("All hashes have been verified")
    return True


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

example_block_chain = [example_block0, example_block1, example_block2]

if __name__ == "__main__":
    main()

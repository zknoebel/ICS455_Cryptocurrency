from cryptoCurrency.helper import BlockMaker


# go through each block and check the hashes
def main():
    # test an example block chain
    print("Test valid block chain:\n", end="")
    test_blocks(example_block_chain, True)

    print()

    # test an example that should fail
    print("Test invalid block chain:\n", end="")
    try:
        test_blocks(example_bad_block_chain, True)
    except ValueError as e:
        print(str(e))


def test_blocks(block_chain_string, debug):
    hashed_value = ""

    block_chain = BlockMaker.separate_blocks(block_chain_string)
    index = 0;
    if len(block_chain) > 0:
        for json_block in block_chain:
            block = BlockMaker.make_block(json_block)
            if hashed_value != block["previous_hash"] or index != block["index"]:
                raise ValueError("Hash does not match")

            if debug:
                print("Block at index " + str(block["index"]) + " has been verified.")
            index += 1
            hashed_value = BlockMaker.hash(block)

        if debug:
            print("All hashes have been verified")
    else:
        print("Empty block chain")
    return index - 1, hashed_value


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

example_block_chain = "[" + example_block0 + "," + example_block1 + "," + example_block2 + "]"
example_bad_block_chain = "[" + example_block0 + "," + example_block2 + "," + example_block1 + "]"

if __name__ == "__main__":
    main()

# ICS455_Cryptocurrency
    This repository is for the final project for ICS455 at the University of Hawaii at Manoa.
We chose to implement Blockchain protocols to create our own form of cryptocurrency. A Blockchain is
a data structure that consists of blocks that are linked sequentially and secured cryptographically. Every block
is easy to verify and append to an existing block. Each block contains a hash of its parent block, which is one
of the reasons why the modification of the blocks is difficult. If a change was made to a block, the following blocks
would also experience a change that would be witnessed during the verification of the Blockchain. The Blockchain data
structure therefore is in itself, a digital ledger. A ledger that is shared amongst a group of participants, or miners,
who record new blocks through the verification of transactions that were made before it. The miners compute this
proof of work function that makes double-spending impractical. Double-spending is a powerful obstacle to overcome
for digital currencies, as the ability to replicate the same token over and over for spending devalues the currency.
Our implementation currently utilizes a central authority without the use of a P2P network to mine. Foreseeable extensions
to the project includes the implementation of another cryptographic hash algorithm during the proof of work, the
implementation of a P2P network for validation, and the adjustment to our central authority by delegating some of its
duties in exchange for some type or reward.
    This project was developed in Python 3 and runs from the program `CmdLineRunner.py`. The user has the option to
find the `balance`, to `mine`, create a `transaction`, and to `verify`. An example run and a copy of the output can be
found below.
`
Show the options.

(CLR)help
Documented commands (type help <topic>):
========================================
balance  exit  help  mine  transaction  verify


Starting with the Genesis Block.

(CLR)help balance
Get the balance for a specific account

usage:
balance <block_chain_file> <account>

(CLR)balance sampleFiles/GenesisBlock.json wvfYvNSFAwOFVV4B3o1kxsSY
wvfYvNSFAwOFVV4B3o1kxsSY has 100000000000 ICS-455-Cryptocurrency

To make it easier to follow along we will use a name instead of a hash for sender and receiver

(CLR)help transaction
Create a transaction file

usage
transaction <sender> <receiver> <amount> <signature> <new_file_name>

Make a transaction
(CLR)transaction wvfYvNSFAwOFVV4B3o1kxsSY Abby 1000 2cf24dba5fb0a30e26e83b2ac5b9e29 sampleFiles/sample_transaction_file0
Make a transaction
(CLR)transaction wvfYvNSFAwOFVV4B3o1kxsSY Bob 1001 2cf24dba5fb0a30e26e83b2ac5b9e29 sampleFiles/sample_transaction_file1
Make a transaction
(CLR)transaction wvfYvNSFAwOFVV4B3o1kxsSY Charles 1002 2cf24dba5fb0a30e26e83b2ac5b9e29 sampleFiles/sample_transaction_file2
Make a transaction
(CLR)transaction wvfYvNSFAwOFVV4B3o1kxsSY Donna 1003 2cf24dba5fb0a30e26e83b2ac5b9e29 sampleFiles/sample_transaction_file3
Make a transaction
(CLR)transaction wvfYvNSFAwOFVV4B3o1kxsSY Edd 1004 2cf24dba5fb0a30e26e83b2ac5b9e29 sampleFiles/sample_transaction_file4


Now that we have some transactions, we can mine some blocks

(CLR)help mine
Mine a block

usage:
mine <current_block_chain_file> <transaction_file>
or
mine <current_block_chain_file> <transaction_file> <file_to_save_to>


Mine a block
(CLR)mine sampleFiles/GenesisBlock.json sampleFiles/sample_transaction_file0 sampleFiles/sample_block_chain
proof of newly mined block = 79
hash of newly mined block = 8e0c7b7ed06971d65d7d7f56b7387aa457c676300f116cb5ba36d250a8bd8501


Now a block has been mined and added to the block chain.
Lets verify this new block chain.


(CLR)help verify
Verify a block chain

usage:
verify <filename_to_verify>


(CLR)verify sampleFiles/sample_block_chain
Block at index 0 has been verified.
Block at index 1 has been verified.
All hashes have been verified

Now that we know that it works, lets mine a few more

Mine a block
(CLR)mine sampleFiles/sample_block_chain sampleFiles/sample_transaction_file0 sampleFiles/sample_block_chain
proof of newly mined block = 22
hash of newly mined block = e1ea222e556f950f49526741dbd5dd727a3fb92349e5f31d461b7f3ddd443902
Mine a block
(CLR)mine sampleFiles/sample_block_chain sampleFiles/sample_transaction_file1 sampleFiles/sample_block_chain
proof of newly mined block = 104
hash of newly mined block = 009ab3b4a9502f2275b786275d2af8aa4126a3c77b10ce3d2af3711ab5f18cf3
Mine a block
(CLR)mine sampleFiles/sample_block_chain sampleFiles/sample_transaction_file2 sampleFiles/sample_block_chain
proof of newly mined block = 28
hash of newly mined block = 81371fe42e86d79e1be1f490d098fc2b0738b3f2fef5efe241483054aa591dd4
Mine a block
(CLR)mine sampleFiles/sample_block_chain sampleFiles/sample_transaction_file3 sampleFiles/sample_block_chain
proof of newly mined block = 7
hash of newly mined block = 4254c3b1f9d357985365a475a70d0b3077787c9311f5fbf0c02ea28bc85fd835
Mine a block
(CLR)mine sampleFiles/sample_block_chain sampleFiles/sample_transaction_file4 sampleFiles/sample_block_chain
proof of newly mined block = 13
hash of newly mined block = bf8344b3fce0f3c8ea3d71dcf1ee8d114372f77871be545753add7adc8005c56

As you can see, the index of the end of the block's hash has to match the index of the block.
This automatically increases the hardness of the proof of work as more blocks are mined.

Now verify the entire chain
(CLR)verify sampleFiles/sample_block_chain
Block at index 0 has been verified.
Block at index 1 has been verified.
Block at index 2 has been verified.
Block at index 3 has been verified.
Block at index 4 has been verified.
Block at index 5 has been verified.
Block at index 6 has been verified.
All hashes have been verified

Show all of the balances
wvfYvNSFAwOFVV4B3o1kxsSY has 99999993990 ICS-455-Cryptocurrency
Abby has 2000 ICS-455-Cryptocurrency
Bob has 1001 ICS-455-Cryptocurrency
Charles has 1002 ICS-455-Cryptocurrency
Donna has 1003 ICS-455-Cryptocurrency
Edd has 1004 ICS-455-Cryptocurrency
`

## Blockchain
    The blocks of the Blockchain data structure will be stored in json format, as can be seen in our Genesis Block:
`
{
    "previous_hash": "",
    "timestamp": 1506057125.900785,
    "proof": 65,
    "index": 0,
    "transactions": [
        {
            "amount": 100000000000000000,
            "signature": "2cf24dba5fb0a30e26e83b2ac5b9e29",
            "receiver": "wvfYvNSFAwOFVV4B3o1kxsSY",
            "sender": "MIICWwIBAAKBgHztyBDR5al"
        }
    ]
}
`
    Each of our blocks contains the data (transactions), the block ID (index), the hash of the parent (previous_hash),
and the proof of work (proof). We start the Genesis Block, with the index of 0, with a substantial amount of our
currency to stimulate our economy. Further details on each characteristic of the blocks are detailed below.

### Transactions
    For now, each block will only have one transaction. Each transaction contains an amount to be sent,
the addresses of the sender and receiver, and the signature for the transaction.
`
{
	"amount": 1000,
	"signature": "2cf24dba5fb0a30e26e83b2ac5b9e29",
	"receiver": "Abby",
	"sender": "wvfYvNSFAwOFVV4B3o1kxsSY"
}
`
    As seen in the example run, the string for the receiver is only meant to be a placeholder for the actual public
key. The signature is the private key associated with the sender's public key. Through the command line runner, the user
is able to enter in the fields of the transaction.

    Now that the structure of the blocks has been described, the functionality of the Blockchain will discussed. To verify
that the transaction is valid, we must determine that the sender has enough funds to transfer.

### Proof of Work
    For our proof of work for the blocks, SHA-256 was our chosen Cryptographic Hash Algorithm, and our function maps to
the slide given.
```python
# proof of work slide
def proof_example():
    r = {"proof": 0, "data": [1, 2, 3]}

    while sha256(json.dumps(r).encode()).hexdigest()[-2:] != "00":
        r["proof"] += 1
        print("last chars = " + sha256(json.dumps(r).encode()).hexdigest()[-2:])

    print("proof = " + str(r["proof"]))
```
    During the `mine` option, the Blockchain and a given transaction file from the user has it's proof of work computed
in the following method.
```python
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
```

### Verification
    After the block has been mined, we can turn to the `verify` option to validate the new copy of the Blockchain.
As seen in the example run, the following method provides the user with verification that none of the blocks in the
Blockchain have been tampered with and is ready for another block to be mined.
```python
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
```

### Sources
Negrashov, Sergey. "Blockchains and Cryptocurrencies." University of Hawaii @ Manoa. 3/11/2018. PDF Presentation.

Wikipedia contributors, 'Blockchain,' Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 1 May. 2018.
    Web. 2 May. 2018

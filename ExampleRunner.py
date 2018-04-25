import sys

import CmdLineRunner

runner = CmdLineRunner.CmdLineRunner
runner.stdout = sys.stdout
people = {0: "Abby", 1: "Bob", 2: "Charles", 3: "Donna", 4: "Edd"}


def main():
    print("Show the options.")
    print()
    print("(CLR)help")
    print(
        "Documented commands (type help <topic>):\n========================================\nbalance  exit  help  mine  transaction  verify")
    print()
    print()

    print("Starting with the Genesis Block.")
    print()
    print("(CLR)help balance")
    runner.do_balance(runner, "")
    print()
    print("(CLR)balance sampleFiles/GenesisBlock.json wvfYvNSFAwOFVV4B3o1kxsSY")
    runner.do_balance(runner, "sampleFiles/GenesisBlock.json wvfYvNSFAwOFVV4B3o1kxsSY")

    print()
    print("To make it easier to follow along we will use a name instead of a hash for sender and receiver")
    print()
    print("(CLR)help transaction")
    runner.do_transaction(runner, "")
    print()

    for i in range(5):
        make_transaction("wvfYvNSFAwOFVV4B3o1kxsSY", people[i], 1000 + i, "2cf24dba5fb0a30e26e83b2ac5b9e29",
                         "sampleFiles/sample_transaction_file" + str(i))

    print()
    print()
    print("Now that we have some transactions, we can mine some blocks")
    print()
    print("(CLR)help mine")
    runner.do_mine(runner, "")
    print()

    mine_block("sampleFiles/GenesisBlock.json", "sampleFiles/sample_transaction_file0", "sampleFiles/sample_block_chain")

    print()
    print()
    print("Now a block has been mined and added to the block chain.")
    print("Lets verify this new block chain.")
    print()
    print()
    print("(CLR)help verify")
    runner.do_verify(runner, "")
    print()
    verify_chain()
    print()
    print("Now that we know that it works, lets mine a few more")
    print()
    for i in range(5):
        mine_block("sampleFiles/sample_block_chain", "sampleFiles/sample_transaction_file" + str(i), "sampleFiles/sample_block_chain")
    print()
    print("As you can see, the index of the end of the block's hash has to match the index of the block.")
    print("This automatically increases the hardness of the proof of work as more blocks are mined.")
    print()
    print("Now verify the entire chain")
    verify_chain()

    print()
    print("Show all of the balances")
    runner.do_balance(runner, "sampleFiles/sample_block_chain wvfYvNSFAwOFVV4B3o1kxsSY")
    for i in range(5):
        runner.do_balance(runner, "sampleFiles/sample_block_chain " + people[i])


def make_transaction(sender, receiver, amount, signature, new_file_name):
    print("Make a transaction")
    print("(CLR)transaction " + sender + " " + receiver + " " + str(amount) + " " + signature + " " + new_file_name)
    runner.do_transaction(runner, sender + " " + receiver + " " + str(amount) + " " + signature + " " + new_file_name)


def mine_block(current_block_chain, transaction, new_block_chain):
    print("Mine a block")
    print("(CLR)mine " + current_block_chain + " " + transaction + " " + new_block_chain)
    runner.do_mine(runner, current_block_chain + " " + transaction + " " + new_block_chain)


def verify_chain():
    print("(CLR)verify sampleFiles/sample_block_chain")
    runner.do_verify(runner, "sampleFiles/sample_block_chain")


if __name__ == '__main__':
    main()

import cmd
import json
import time

from src.BlockChainVerifier import BlockChainVerifier
from src.BlockMiner import BlockMiner
from src.Wallet import Wallet


class CmdLineRunner(cmd.Cmd):
    intro = "Use this tool to verify block chains or mine blocks.\n\nType help or ? to list commands.\nType help <command> to learn about the command\n"

    prompt = "(CLR) "

    def do_exit(self, arg):
        """Exit Command Line Runner."""
        print("Exiting now.")
        exit()

    def do_verify(self, arg):
        """Verify a block chain\n\nverify <filename_to_verify>\n"""

        if arg == '':
            print("""Verify a block chain\nusage\n\nverify <filename_to_verify>\n""")
        else:
            file = open(arg, 'r')
            block_chain = file.read()
            try:
                BlockChainVerifier.test_blocks(block_chain, True)
            except ValueError as e:
                print(str(e))

    def do_mine(self, arg):
        """Mine a block\n\nmine <current_block_chain_file> <transaction_file>\nor\nmine <current_block_chain_file> <transaction_file> <file_to_save_to>\n"""
        arguments = arg.split()
        if len(arguments) > 1:
            block_chain_file = open(arguments[0], 'r')
            transaction_file = open(arguments[1], 'r')
            timestamp = time.time()

            block_chain = block_chain_file.read()
            transactions = json.loads(transaction_file.read())
            new_block_chain = BlockMiner.mine_block(block_chain, timestamp, transactions)
            if (len(arguments) == 3):
                new_file = open(arguments[2], 'w')
                new_file.write(new_block_chain)
                new_file.close()
        else:
            print("""Mine a block\nusage\n\nmine <current_block_chain_file> <transaction_file>\nor\nmine <current_block_chain_file> <transaction_file> <file_to_save_to>\n""")


    def do_balance(self, arg):
        """Get the balance for a specific account\n\nbalance <block_chain_file> <account>"""
        arguments = arg.split()
        if len(arguments) == 2:
            block_chain_file = open(arguments[0], 'r')
            Wallet.get_balance(block_chain_file.read(), arguments[1])
        else:
            print("""Get the balance for a specific account\nusage\n\nbalance <block_chain_file> <account>""")




def parse(arg):
    """Convert a series of zero or more strings to an argument tuple."""
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    CmdLineRunner().cmdloop()

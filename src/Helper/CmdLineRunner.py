from src.BlockMiner import BlockMiner
from src.BlockChainVerifier import BlockChainVerifier
import cmd
import json

class CmdLineRunner(cmd.Cmd):
    intro = "Use this tool to verify block chains or mine blocks.\n\nType help or ? to list commands.\nType help <command> to learn about the command\n"

    prompt = "(CLR) "

    def do_exit(self, arg):
        """Exit Command Line Runner."""
        print("Exiting now.")
        exit()

    def do_verify(self, arg):
        """Verify a block chain\n\nverify <filename_to_verify>\n"""

        file = open(arg, 'r')
        block_chain = file.read()
        BlockChainVerifier.test_blocks(block_chain)

    def do_mine(self, arg):
        """Mine a block\n\nmine <current_block_chain_file> <transaction_file> <timestamp>\nor\nmine <current_block_chain_file> <transaction_file> <timestamp> <file_to_save_to>\n"""
        arguments = arg.split()
        block_chain_file = open(arguments[0], 'r')
        transaction_file = open(arguments[1], 'r')

        block_chain = block_chain_file.read()
        transactions = json.loads(transaction_file.read())
        new_block_chain = BlockMiner.mine_block(block_chain, arguments[2], transactions)
        if (len(arguments) == 4):
            new_file = open(arguments[3], 'w')
            new_file.write(new_block_chain)
            new_file.close()


def parse(arg):
    """Convert a series of zero or more strings to an argument tuple."""
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    CmdLineRunner().cmdloop()

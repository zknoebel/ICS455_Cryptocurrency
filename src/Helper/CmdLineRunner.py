from src.Helper import BlockMaker
from src.BlockMiner import BlockMiner
from src.BlockChainVerifier import BlockChainVerifier
import cmd


class CmdLineRunner(cmd.Cmd):
    intro = """Use this tool to verify block chains or mine blocks.
            Type help or ? to list commands.\n"""

    prompt = "(CLR) "

    def do_exit(self, arg):
        'Exit Command Line Runner.'
        print("Exiting now.")
        exit()

    def do_verify(self, arg):
        'Verify a block chain'
        file = open(arg, 'r')
        block_chain = file.read()
        BlockChainVerifier.test_hashes(file)

    def do_mine(self, arg):
        'Mine a block'
        arguments = arg.split()
        file = open(arguments[0], 'r')
        block = file.read()
        if (len(arguments) > 1):
            new_file = open(arguments[1], 'w')
            new_file.write(str(BlockMiner.find_proof_of_work(block)))
        else:
            BlockMiner.find_proof_of_work(block)


def parse(arg):
    'Convert a series of zero or more strings to an argument tuple.'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    CmdLineRunner().cmdloop()

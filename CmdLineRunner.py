import cmd
import json
import time

from cryptoCurrency.blockChainVerifier import BlockChainVerifier
from cryptoCurrency.blockMiner import BlockMiner
from cryptoCurrency.wallet import Wallet


class CmdLineRunner(cmd.Cmd):
    intro = "Use this tool to verify block chains or mine blocks.\n\nType help or ? to list commands.\nType help <command> to learn about the command\n"

    prompt = "(CLR) "

    def do_exit(self, arg):
        """Exit Command Line Runner."""
        print("Exiting now.")
        exit()

    def do_verify(self, arg):
        """Verify a block chain\n\nusage:\nverify <filename_to_verify>\n"""

        if arg == '':
            CmdLineRunner.do_help(self, "verify")
        else:
            try:
                file = open(arg, 'r')
                block_chain = file.read()
            except FileNotFoundError:

                block_chain = '{}'
            try:
                BlockChainVerifier.test_blocks(block_chain, True)
            except ValueError as e:
                print(str(e))

    def do_mine(self, arg):
        """Mine a block\n\nusage:\nmine <current_block_chain_file> <transaction_file>\nor\nmine <current_block_chain_file> <transaction_file> <file_to_save_to>\n"""
        arguments = arg.split()
        if len(arguments) > 1:
            try:
                block_chain_file = open(arguments[0], 'r')
                block_chain = block_chain_file.read()
            except FileNotFoundError:
                block_chain = "{}"

            try:
                transaction_file = open(arguments[1], 'r')
                transactions = json.loads(transaction_file.read())
            except FileNotFoundError:
                print("invalid transaction")
                return

            timestamp = time.time()

            try:
                new_block_chain = BlockMiner.mine_block(block_chain, timestamp, transactions)
            except ValueError as v:
                print("Invalid block chain: " + str(v))
                return

            if (len(arguments) == 3):
                new_file = open(arguments[2], 'w')
                new_file.write(new_block_chain)
                new_file.close()
        else:
            CmdLineRunner.do_help(self, "mine")

    def do_balance(self, arg):
        """Get the balance for a specific account\n\nusage:\nbalance <block_chain_file> <account>"""
        arguments = arg.split()
        if len(arguments) == 2:
            try:
                block_chain_file = open(arguments[0], 'r')
                block_chain = block_chain_file.read()
                Wallet.get_balance(block_chain, arguments[1])
            except FileNotFoundError:
                print("Empty block chain")

        else:
            CmdLineRunner.do_help(self, "balance")

    def do_transaction(self, arg):
        """Create a transaction file\n\nusage\ntransaction <sender> <receiver> <amount> <signature> <new_file_name>"""
        arguments = arg.split()
        if len(arguments) != 5:
            CmdLineRunner.do_help(self, "transaction")
            return

        transaction_string = '{"amount": ' + arguments[2] + ','
        transaction_string += '"signature": "' + arguments[3] + '",'
        transaction_string += '"receiver": "' + arguments[1] + '",'
        transaction_string += '"sender": "' + arguments[0] + '"}'

        file = open(arguments[4], 'w')
        file.write(transaction_string)
        file.close()


def parse(arg):
    """Convert a series of zero or more strings to an argument tuple."""
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    CmdLineRunner().cmdloop()

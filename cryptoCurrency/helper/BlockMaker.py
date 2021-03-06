import json
from collections import OrderedDict
from hashlib import sha256


def make_block(json_block):
    unordered_block = json.loads(json_block)

    # if left unordered the dicts will not hash the same way
    # order the transaction
    ordered_transaction = OrderedDict()
    ordered_transaction["sender"] = unordered_block["transactions"][0]["sender"]
    ordered_transaction["receiver"] = unordered_block["transactions"][0]["receiver"]
    ordered_transaction["amount"] = unordered_block["transactions"][0]["amount"]
    ordered_transaction["signature"] = unordered_block["transactions"][0]["signature"]

    # order the rest of the block
    block = OrderedDict()
    block["index"] = unordered_block["index"]
    block["timestamp"] = unordered_block["timestamp"]
    block["transactions"] = ordered_transaction
    block["proof"] = unordered_block["proof"]
    block["previous_hash"] = unordered_block["previous_hash"]

    return block


def hash(block):
    return sha256(json.dumps(block).encode()).hexdigest()


def make_json(block):
    string_block = '{\n\t"previous_hash": "' + str(block["previous_hash"]) + '",\n'
    string_block += '\t"timestamp": ' + str(block["timestamp"]) + ',\n'
    string_block += '\t"proof": ' + str(block["proof"]) + ',\n'
    string_block += '\t"index": ' + str(block["index"]) + ',\n'
    string_block += '\t"transactions": [\n'
    string_block += '\t\t{\n\t\t\t"amount": ' + str(block["transactions"]["amount"]) + ',\n'
    string_block += '\t\t\t"signature": "' + str(block["transactions"]["signature"]) + '",\n'
    string_block += '\t\t\t"receiver": "' + str(block["transactions"]["receiver"]) + '",\n'
    string_block += '\t\t\t"sender": "' + str(block["transactions"]["sender"]) + '"\n\t\t}\n\t]\n}'

    return string_block


def separate_blocks(block_chain_string):
    blocks = json.loads(block_chain_string)
    block_strings = []

    for block in blocks:
        block_strings.append(json.dumps(block))

    return block_strings


def add_to_chain(block_chain, block):
    last_occurence = block_chain.rfind('}')
    new_block_chain = block_chain[:last_occurence + 1] + ",\n" + block + "\n]"
    return new_block_chain

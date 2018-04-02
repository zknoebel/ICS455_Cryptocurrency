from collections import OrderedDict
from hashlib import sha256
import json


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
from hashlib import sha256
import json


def main():
    print("main")
    proof_example()


# proof of work slide
def proof_example():
    r = {"proof": 0, "data": [1, 2, 3]}

    while sha256(json.dumps(r).encode()).hexdigest()[-2:] != "00":
        r["proof"] += 1
        print("last chars = " + sha256(json.dumps(r).encode()).hexdigest()[-2:])

    print("proof = " + str(r["proof"]))


def find_proof_of_work(block, hardness):
    block["proof"] = 0;

    while sha256(json.dumps(block).encode()).hexdigest()[-1 * hardness:] != ("0" * hardness):
        block["proof"] += 1

        #just to show it works
        #get rid of this later
        print("last chars = " + sha256(json.dumps(block).encode()).hexdigest()[-2:])

        return block;

if __name__ == "__main__":
    main()

from hashlib import sha256
import json

#proof of work slide
""""

r = {'proof' : 0,
    'data' : [1, 2, 3]
    }
    
while sha256(json.dumps(r).encode()).hexdigest()[-1] != "0":
    r['proof'] += 1

print("proof=" + str(r['proof']))

"""
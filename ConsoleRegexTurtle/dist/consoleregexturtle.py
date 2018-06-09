import json
from pprint import pprint
from argparse import ArgumentParser

parse = ArgumentParser()
parse.add_argument('-d', dest='data', help='data file', required=True)
parse.add_argument('-w', dest='write', help='write json to file')
args = parse.parse_args()

data = {"examples": []}

with open(args.data, 'r') as f:
    strings = f.read().split()

for string in strings:
    data['examples'].append(
        {
            "string": string,
            "match": [
                {
                    "start": 0,
                    "end": len(string)
                }
            ]
        }
    )

# need to give it some data that it does not match against 
data['examples'].append({'string': 'GetProcess', 'match': []})
data['examples'].append({'string': 'abcdefgh', 'match': []})
data['examples'].append({'string': 'ABCDEFGH', 'match': []})
data['examples'].append({'string': '12345678', 'match': []})

if args.write:
    with open(args.write, 'w+') as r:
        r.write(data)
else:
    print(json.dumps(data))

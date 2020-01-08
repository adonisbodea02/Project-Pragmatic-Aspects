import json_lexer
import json_parser
from string_functions import to_json


def from_file(filename):
    tokens = []
    with open(filename) as f:
        for _, line in enumerate(f):
            line = line.strip('\n')
            tokens += json_lexer.lex(line)
    f.close()
    return json_parser.parse(tokens, is_root=True)[0]


def to_file(filename, obj):
    string = to_json(obj)
    with open(filename, 'w') as f:
        f.write(string)
    f.close()


# to_file('to_json.txt', {"foo": [1, None], "foo2": {"bar": [1, 2, None, 'three']}, "foo3": []})


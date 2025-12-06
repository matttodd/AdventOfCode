import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *
from functools import reduce

def solve(contents):
    ops = contents[-1].split()
    eqs = [[] for _ in range(len(ops))]
    # print(ops)
    for i in range(len(contents) - 1):
        # print(eqs)
        new = list(map(lambda x: int(x), contents[i].split()))
        for j in range(len(new)):
            eqs[j].append(new[j])
    tot = 0
    # print(ops, eqs)
    for i in range(len(ops)):
        if ops[i] == "*":
            res = reduce(lambda x, y: x * y, eqs[i], 1)
        elif ops[i] == "+":
            res = reduce(lambda x, y: x + y, eqs[i], 0)
        tot += res
    return str(tot)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()
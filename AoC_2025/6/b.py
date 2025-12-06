import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *
from functools import reduce

def solve(contents):
    contents = list(map(lambda x: x.strip("\n"), contents))
    max_line_len = len(max(contents, key=len))
    for i in range(len(contents)):
        if len(contents[i]) != max_line_len:
            contents[i] += " " * (max_line_len - len(contents[i]))
    # print(max_line_len)
    # for i in range(len(contents)):
    #     print(contents[i] + "X")
    ops = contents[-1].split()
    eqs = [[] for _ in range(len(ops))]
    scan = max_line_len - 1
    prob_c = len(ops) - 1
    while scan >= 0:
        # print(scan, prob_c, eqs)
        num = ""
        for j in range(len(contents) - 1):
            c = contents[j][scan]
            if c != " ":
                num += c
        if num == "":
            prob_c -= 1
        else:
            eqs[prob_c].append(int(num))
        scan -= 1
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
    contents = read_in(dont_strip=True)
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()
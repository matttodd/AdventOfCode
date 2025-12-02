from functools import reduce
from collections import defaultdict
from itertools import product


def solve(lines):
    levels = []
    tot = 0
    for i, line in enumerate(lines):
        items = list(line.strip().split())
        a = items[0]
        a = a[0:-1]
        a = int(a)
        vals = list(map(int, items[1:]))
        tot += answer(a, vals)
    # print(levels)
    return tot


def answer(a, vals):
    add = "+"
    mult = "*"
    possible = product("+*", repeat=len(vals)-1)
    # print(list(possible))
    for p in possible:
        cur = vals[0]
        for i, val in enumerate(vals[1:]):
            if p[i] == add:
                cur += val
            elif p[i] == mult:
                cur *= val
        if cur == a:
            print(a)
            return a
    return 0



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

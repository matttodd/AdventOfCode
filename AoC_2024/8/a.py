from functools import reduce
from collections import defaultdict
from itertools import product


def solve(lines):
    levels = []
    tot = 0
    nodes = defaultdict(list)
    for i, line in enumerate(lines):
        levels.append(list(line.strip()))
        for j, char in enumerate(line.strip()):
            if char != '.':
                nodes[char].append((i, j))
    # print(levels)
    # print(nodes)
    return answer(levels, nodes)


def answer(levels, nodes):
    tot = set()
    bx = len(levels)
    by = len(levels[0])
    for node, locs in nodes.items():
        for i, loc in enumerate(locs):
            for other in locs[i+1:]:
                print(node, loc, other)
                d1 = loc[0] - other[0] # -2
                d2 = loc[1] - other[1] # -1

                if 0 <= (loc[0] + d1) < bx and 0 <= (loc[1] + d2) < by:
                    tot.add((loc[0] + d1, loc[1] + d2))
                if 0 <= (other[0] - d1) < bx and 0 <= (other[1] - d2) < by:
                    tot.add((other[0] - d1, other[1] - d2))
    print(tot)
    return len(tot)



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

import sys
from collections import Counter

def solve(lines):
    tot = 0
    towels = set(lines[0].strip().split(', '))
    cache = Counter()
    for i, line in enumerate(lines[2:]):
        line = line.strip()
        design = line
        a = answer2(towels, design, cache)#, design in ['gbbr', 'rrbgbr'])
        tot += a
    return tot


def answer2(towels, design, cache):
    if design in cache:
        return cache[design]
    ways_to_pre = 0
    if design in towels:
        ways_to_pre += 1
    for t in towels:
        l = len(t)
        if t == design[:l]:
            ways_to_pre += answer2(towels, design[l:], cache)
    cache[design] = ways_to_pre
    return ways_to_pre


def answer(towels, design):
    # print(towels, design)
    q = []
    starting = True
    ways = 0
    while q or starting:
        # print(q)
        if starting:
            cur = ""
        else:
            cur = q.pop(0)
        # print(cur)
        starting = False
        if cur == design:
            ways += 1
        if len(cur) >= len(design):
            continue
        nxtc = design[len(cur):]
        # print(nxt)
        pos = list(filter(lambda x: nxtc[:len(x)] == x, towels))
        nxt = list(map(lambda x: cur + x, pos))
        # print(cur, nxtc, pos, nxt)
        # for p in nxt:
        #     q.append(p)
        # print(q)
        q.extend(nxt)
        # print(q)
    return ways


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

import sys
sys.setrecursionlimit(10000)
from itertools import combinations
from collections import defaultdict


def solve(lines):
    locks = []
    keys = []
    is_lock = False
    mid_lock = False
    running = [0, 0, 0, 0, 0]
    while len(lines):
        cur = lines.pop(0).strip()
        if cur == '#####' and mid_lock == False:
            is_lock = True
        if cur == "":
            if is_lock:
                locks.append(running.copy())
            else:
                keys.append(running.copy())
            is_lock = False
            mid_lock = False
            running = [0, 0, 0, 0, 0]
            continue
        mid_lock = True
        for i, c in enumerate(cur):
            if c == '#':
                running[i] += 1
    if is_lock:
        locks.append(running.copy())
    else:
        keys.append(running.copy())

    # print(comps)
    return answer(locks, keys)


def answer(locks, keys):
    mx = 7
    tot = 0
    # print(locks, keys)
    for l in locks:
        for k in keys:
            bad = False
            for i in range(5):
                if l[i] + k[i] > mx:
                    bad = True
            if not bad:
                tot += 1

    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

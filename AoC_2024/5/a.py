from functools import reduce
from collections import defaultdict


def solve(lines):
    levels = []
    ps = defaultdict(list)
    instrs = []
    pages = True
    for i, line in enumerate(lines):
        if line == "\n":
            pages = False
            continue
        if pages:
            a, b = map(int, line.strip().split("|"))
            levels.append((a, b))
            ps[a].append(b)
        else:
            instrs.append(list(map(int, line.strip().split(","))))
    # print(levels)
    return answer(levels, ps, instrs)


def answer(levels, ps, instrs):
    tot = 0
    for instr in instrs:
        broken = False
        needed = []
        for page in instr:
            for need in needed:
                if page not in ps[need]:
                    broken = True
            needed.append(page)
        if not broken:
            print(instr)
            tot += instr[len(instr) // 2]
    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

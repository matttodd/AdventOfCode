from functools import reduce
from collections import defaultdict
from itertools import permutations


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
        if broken:
            fixed = fix_it(instr, ps, [])
            print(fixed[len(fixed) // 2])
            tot += fixed[len(fixed) // 2]
    return tot


def fix_it(instr, ps, exist):
    if len(instr) == 0:
        return exist
    curr = instr.pop(0)
    if len(exist) == 0:
        exist.append(curr)
        return fix_it(instr, ps, exist)
    else:
        for i, e in enumerate(exist):
            if curr in ps[e]:
                continue
            else:
                exist.insert(i, curr)
                return fix_it(instr, ps, exist)
    exist.append(curr)
    return fix_it(instr, ps, exist)



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

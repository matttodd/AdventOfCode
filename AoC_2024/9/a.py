from functools import reduce
from collections import defaultdict
from itertools import product


def solve(lines):
    levels = [] # (index, length, id)
    tot = 0
    gaps = []
    run = 0
    for i, c in enumerate(lines[0].strip()):
        file = i % 2 == 0
        id = i // 2
        if file:
            levels.append((run, int(c), id))
            for j in range(int(c)):
                tot += id * (j + run)
        else:
            if int(c) == 0:
                continue
            gaps.append((run, int(c)))
        run += int(c)
    print(levels, gaps, tot)
    # print(nodes)
    return answer(levels, gaps, tot)


def answer(levels, gaps, tot):
    while True:
        to_move = levels.pop(-1)
        to_move_loc = to_move[0] + to_move[1] - 1
        to_move_v = to_move[2]
        gap = gaps.pop(0)
        loc = gap[0]
        if to_move_loc <= loc:
            return tot
        new_g = (gap[0] + 1, gap[1] - 1)
        if new_g[1] != 0:
            gaps.insert(0, new_g)
        tot -= to_move_loc * to_move_v
        tot += loc * to_move_v
        if to_move[1] > 1:
            levels.append((to_move[0], to_move[1] - 1, to_move[2]))



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

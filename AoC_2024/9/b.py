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
    return answer(levels, gaps)


def answer(levels, gaps):
    l_copy = levels.copy()
    for i in range(len(levels)-1, -1, -1):
        # start = len(levels)
        level = l_copy.pop(i)
        l_size = level[1]
        for j, gap in enumerate(gaps):
            # print(levels, gaps)
            # print(level, gap)
            g_size = gap[1]
            if gap[0] >= level[0]:
                break
            if g_size < l_size:
                continue
            # level placed
            for k, l in enumerate(levels):
                if l[0] < gap[0]:
                    continue
                if level in levels:
                    levels.pop(levels.index(level))
                levels.insert(k, (gap[0], l_size, level[2]))
                break
            # gap adjusted
            if g_size == l_size:
                gaps.pop(j)
            else:
                gaps[j] = (gap[0] + l_size, g_size - l_size)
            break
        # if start != len(levels):
        #     levels.insert(i, level)

    tot = 0
    for level in levels:
        for i in range(level[1]):
            tot += (level[0] + i) * level[2]

    return tot



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

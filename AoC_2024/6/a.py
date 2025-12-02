from functools import reduce
from collections import defaultdict


def solve(lines):
    levels = []
    v = (0, 0)
    for i, line in enumerate(lines):
        levels.append(list(line.strip()))
        if '^' in line:
            v = (i, line.index('^'))
    # print(levels)
    return answer(levels, v, 'U', {v}, None)


def answer(levels, v, dir, pos, prev):
    while v != prev:
        print(v, dir)
        next = ''
        next_dir = None
        if dir == 'U':
            next = (v[0]-1, v[1])
            next_dir = 'R'
        elif dir == 'D':
            next = (v[0]+1, v[1])
            next_dir = 'L'
        elif dir == 'L':
            next = (v[0], v[1]-1)
            next_dir = 'U'
        elif dir == 'R':
            next = (v[0], v[1]+1)
            next_dir = 'D'
        try:
            if levels[next[0]][next[1]] == '#':
                dir = next_dir
            else:
                v = next
                pos.add(v)
        except IndexError:
            return len(pos)
    return len(pos)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

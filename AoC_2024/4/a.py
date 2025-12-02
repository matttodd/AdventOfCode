from functools import reduce


def solve(lines):
    levels = []
    for i, line in enumerate(lines):
        levels.append(list(line.strip()))
    # print(levels)
    return answer(levels)

def answer(levels):
    tot = 0
    for i, line in enumerate(levels):
        for j, char in enumerate(line):
            if char == 'X':
                val = check_adj(levels, i, j, None, 'M')
                tot += val
                # print(i, j, val, tot)
    return tot


def check_adj(levels, i, j, a, char):
    # print(i, j, a, char)
    tot = 0
    adjs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]
    if a is not None:
        adjs = [a]
    for adj in adjs:
        try:
            ni = i + adj[0]
            nj = j + adj[1]
            if ni < 0 or nj < 0 or ni >= len(levels) or nj >= len(levels[0]):
                raise IndexError
            c = levels[ni][nj]
        except IndexError:
            continue
        if c == char:
            # print(i, j, c)
            if char == 'M':
                tot += check_adj(levels, i + adj[0], j + adj[1], adj, 'A')
            if char == 'A':
                return check_adj(levels, i + adj[0], j + adj[1], adj, 'S')
            if char == 'S':
                print(i, j, adj)
                return 1
    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

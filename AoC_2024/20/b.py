import sys
from collections import defaultdict
# sys.setrecursionlimit(10000)

def solve(lines):
    tot = 0
    board = []
    walls = set()
    start = None
    end = None
    for i, line in enumerate(lines):
        line = line.strip()
        board.append(list(line))
        if 'S' in line:
            start = (i, line.index('S'))
        if 'E' in line:
            end = (i, line.index('E'))
    return answer(board, start, end)


def answer(board, start, end):
    cost = {}
    pos = start
    count = 0
    while pos != end:
        # print(pos, cost)
        cost[pos] = count
        adjs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for adj in adjs:
            loc = (pos[0] + adj[0], pos[1] + adj[1])
            try:
                nxt = board[loc[0]][loc[1]]
                if nxt != '#' and loc not in cost:
                    pos = loc
                    break
            except IndexError:
                continue
        count += 1
    cost[end] = count

    tot = 0
    for loc, c1 in cost.items():
        # print(loc)
        for dest, c2 in cost.items():
            d = dist(loc, dest)
            if d > 20:
                continue
            if c1 - c2 - d >= 100:
                tot += 1
    return tot


def dist(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

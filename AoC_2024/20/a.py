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
    for i in range(1, len(board)-1):
        for j in range(1, len(board[0])-1):
            me = board[i][j]
            if me != '#':
                continue
            adjs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            mn = None
            mx = None
            for adj in adjs:
                loc = (i + adj[0], j + adj[1])
                nxt = board[loc[0]][loc[1]]
                if nxt == '#':
                    continue
                else:
                    if mn is not None and mx is not None:
                        mn = min(mn, cost[loc])
                        mx = max(mx, cost[loc])
                    else:
                        mn = mx = cost[loc]
            if mn != mx:
                # print((i, j), mn, mx, mx-mn - 2)
                if mx - mn - 2 >= 100:
                    tot += 1
    return tot



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

import sys
sys.setrecursionlimit(10000)

def solve(lines):
    tot = 0
    board = []
    for line in lines:
        board.append(list(line.strip()))
    a = [(0, i) for i in range(len(board[0]))]
    for ai in a:
        tot = max(tot, energize(board, set(), set(), ai, 'D'))
    a = [(len(board)-1, i) for i in range(len(board[0]))]
    for ai in a:
        tot = max(tot, energize(board, set(), set(), ai, 'U'))
    a = [(i, 0) for i in range(len(board[0]))]
    for ai in a:
        tot = max(tot, energize(board, set(), set(), ai, 'R'))
    a = [(i, len(board[0])-1) for i in range(len(board[0]))]
    for ai in a:
        tot = max(tot, energize(board, set(), set(), ai, 'L'))
    return tot


def energize(board, cache, been, loc, dir):
    if loc[0] < 0 or loc[0] >= len(board) or loc[1] < 0 or loc[1] >= len(board[0]):
        return
    if (loc, dir) in cache:
        return
    cache.add((loc, dir))
    been.add(loc)
    space = board[loc[0]][loc[1]]
    print(loc, space)
    if dir == 'R':
        if space == '|':
            energize(board, cache, been, (loc[0] + 1, loc[1]), 'D')
            energize(board, cache, been, (loc[0] - 1, loc[1]), 'U')
        elif space == '\\':
            energize(board, cache, been, (loc[0] + 1, loc[1]), 'D')
        elif space == '/':
            energize(board, cache, been, (loc[0] - 1, loc[1]), 'U')
        else:
            energize(board, cache, been, (loc[0], loc[1] + 1), dir)
    elif dir == 'L':
        if space == '|':
            energize(board, cache, been, (loc[0] + 1, loc[1]), 'D')
            energize(board, cache, been, (loc[0] - 1, loc[1]), 'U')
        elif space == '\\':
            energize(board, cache, been, (loc[0] - 1, loc[1]), 'U')
        elif space == '/':
            energize(board, cache, been, (loc[0] + 1, loc[1]), 'D')
        else:
            energize(board, cache, been, (loc[0], loc[1] - 1), dir)
    elif dir == 'U':
        if space == '-':
            energize(board, cache, been, (loc[0], loc[1] + 1), 'R')
            energize(board, cache, been, (loc[0], loc[1] - 1), 'L')
        elif space == '\\':
            energize(board, cache, been, (loc[0], loc[1] - 1), 'L')
        elif space == '/':
            energize(board, cache, been, (loc[0], loc[1] + 1), 'R')
        else:
            energize(board, cache, been, (loc[0] - 1, loc[1]), dir)
    else:
        if space == '-':
            energize(board, cache, been, (loc[0], loc[1] + 1), 'R')
            energize(board, cache, been, (loc[0], loc[1] - 1), 'L')
        elif space == '\\':
            energize(board, cache, been, (loc[0], loc[1] + 1), 'R')
        elif space == '/':
            energize(board, cache, been, (loc[0], loc[1] - 1), 'L')
        else:
            energize(board, cache, been, (loc[0] + 1, loc[1]), dir)
    return len(been)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

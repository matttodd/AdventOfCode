import sys
sys.setrecursionlimit(10000)


def solve(lines):
    commands = []
    for line in lines:
        direction, dist, color = line.strip().split()
        dist = int(dist)
        commands.append((direction, dist, color))
    maxx, maxy, start = min_max(commands)
    board = [['.' for i in range(maxx + 1)] for j in range(maxy + 1)]
    print(maxx, maxy, start)
    pop_board(board, commands, start)
    printb(board)
    tot = count_ditch(board)
    # printb(board)
    # print(tot)
    new_c = 0
    for i, row in enumerate(board):
        for j, ele in enumerate(row):
            if ele == '#' or ele == '.':
                new_c += 1
    # print(new_c)
    return new_c


def count_ditch(board):
    tot = len(board) * len(board[0])
    bad = set()
    begin = [(0, i) for i in range(len(board[0]))]
    begin.extend([(len(board) - 1, i) for i in range(len(board[0]))])
    begin.extend([(i, 0) for i in range(len(board))])
    begin.extend([(i, len(board[0]) - 1) for i in range(len(board))])
    # print(begin)

    while begin:
        cur = begin.pop(0)
        # print(cur)
        if cur in bad:
            continue
        if board[cur[0]][cur[1]] == '#':
            continue
        else:
            bad.add(cur)
            if not cur[0] < 0:
                begin.append((cur[0] - 1, cur[1]))
            if not cur[1] < 0:
                begin.append((cur[0], cur[1] - 1))
            if not cur[0] >= len(board) - 1:
                begin.append((cur[0] + 1, cur[1]))
            if not cur[1] >= len(board[0]) - 1:
                begin.append((cur[0], cur[1] + 1))

    for cur in bad:
        board[cur[0]][cur[1]] = 'X'

    return tot - len(bad)


def printb(board):
    for row in board:
        print("".join(row))


def pop_board(board, commands, start):
    cury = start[0]
    curx = start[1]
    board[cury][curx] = '#'
    for command in commands:
        d, dist, color = command
        for i in range(dist):
            if d == 'D':
                cury += 1
            elif d == 'U':
                cury -= 1
            elif d == 'L':
                curx -= 1
            else:
                curx += 1
            board[cury][curx] = '#'


def min_max(commands):
    curx = 0
    minx = 0
    maxx = 0
    cury = 0
    miny = 0
    maxy = 0
    for command in commands:
        d, dist, c = command
        if d == 'U':
            cury -= dist
            maxy = max(cury, maxy)
            miny = min(cury, miny)
        elif d == 'D':
            cury += dist
            maxy = max(cury, maxy)
            miny = min(cury, miny)
        elif d == 'L':
            curx -= dist
            maxx = max(curx, maxx)
            minx = min(curx, minx)
        elif d == 'R':
            curx += dist
            maxx = max(curx, maxx)
            minx = min(curx, minx)
    return maxx - minx, maxy - miny, (abs(miny), abs(minx))


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

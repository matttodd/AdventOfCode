import sys
sys.setrecursionlimit(10000)


NUM = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]
DIR = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]


def solve(lines):
    tot = 0
    for line in lines:
        line = line.strip()
        tot += answer(list(line))
    return tot


def answer(code):
    tot = 0
    locs = ['A', 'A', 'A']
    for c in code:
        tot += move_to_num(locs, c)
    print(tot)
    return int("".join(code)[:-1]) * tot


def move_to_dir(locs, end, ind):
    # print(locs)
    start = locs[ind]
    s = index_of(start, DIR)
    e = index_of(end, DIR)
    diff = (e[0] - s[0], e[1] - s[1])
    # print(ind, start, end, diff)
    instr = instrs(diff, locs[ind], DIR)
    if ind == len(locs) - 1:
        locs[ind] = end
        # print(instr)
        return len(instr[0])
    # print(ind, s, e, diff, instr)
    b = 99999
    for inst in instr:
        tot = 0
        for i in inst:
            tot += move_to_dir(locs, i, ind+1)
        b = min(b, tot)
    locs[ind] = end
    return b


def move_to_num(locs, end):
    # print(locs)
    start = locs[0]
    s = index_of(start, NUM)
    e = index_of(end, NUM)
    diff = (e[0] - s[0], e[1] - s[1])
    # print(0, start, end, diff)
    instr = instrs(diff, locs[0], NUM)
    # print(s, e, diff, instr)
    b = 99999
    for inst in instr:
        tot = 0
        for i in inst:
            tot += move_to_dir(locs, i, 1)
        b = min(b, tot)
    locs[0] = end
    return b


def index_of(c, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == c:
                return i, j


def instrs(diff, c, board):
    loc = index_of(c, board)
    q = [("", diff, loc)]
    all = []
    while q:
        res, d, loc = q.pop(0)
        # print(board[loc[0]][loc[1]])
        # print(res, d, c, loc, board)
        if d == (0, 0):
            all.append(res + 'A')
            continue
        if d[1] > 0:
            if board[loc[0]][loc[1]+1] is not None:
                q.append((res + ">", (d[0], d[1]-1), (loc[0], loc[1]+1)))
        if d[0] > 0:
            if board[loc[0]+1][loc[1]] is not None:
                q.append((res + "v", (d[0]-1, d[1]), (loc[0]+1, loc[1])))
        if d[1] < 0:
            if board[loc[0]][loc[1]-1] is not None:
                q.append((res + "<", (d[0], d[1]+1), (loc[0], loc[1]-1)))
        if d[0] < 0:
            if board[loc[0]-1][loc[1]] is not None:
                q.append((res + "^", (d[0]+1, d[1]), (loc[0]-1, loc[1])))
    return all


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

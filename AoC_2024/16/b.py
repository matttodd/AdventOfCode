import sys
# sys.setrecursionlimit(10000)
from bisect import insort

def solve(lines):
    tot = 0
    board = []
    start = None
    end = None
    for i in range(len(lines)):
        line = lines.pop(0).strip()
        if 'S' in line:
            start = (i, line.index('S'))
        if 'E' in line:
            end = (i, line.index('E'))
        board.append(list(line.strip()))
    ends = answer(board, start, end, '>')
    # print(len(path), len(set(path)), len(path) - len(set(path)))
    # print((1000 * (len(path) - len(set(path)))) + len(set(path)))
    # for p in path:
    #     board[p[0]][p[1]] = "o"
    # p_board(board)
    print(len(ends))
    s = set()
    for e in ends:
        p = e[3]
        s = s.union(set(p))
    return len(s) + 1


def answer(board, start, end, dir):
    cache = {}
    q = [(0, start, dir, [])]
    i = 0
    best = []
    tot = None
    while q:
        i += 1
        # if i < 30:
        #     print(q[:4])
        # print(q)
        cur = q.pop(0)
        cost = cur[0]
        loc = cur[1]
        move = cur[2]
        path = cur[3]
        if loc == end:
            if tot is None:
                tot = cost
                best.append(cur)
            else:
                if cost == tot:
                    best.append(cur)
            continue
        hash = f"{loc[0]}-{loc[1]}-{move}"
        if hash in cache and cache[hash] < cost:
            continue
        cache[hash] = cost
        d = (0, 0)
        if move == '^':
            d = (-1, 0)
        elif move == 'v':
            d = (1, 0)
        elif move == '<':
            d = (0, -1)
        elif move == '>':
            d = (0, 1)
        fwd = (loc[0] + d[0], loc[1] + d[1])
        if board[fwd[0]][fwd[1]] != '#':
            hash = f"{fwd[0]}-{fwd[1]}-{move}"
            if not (hash in cache and cache[hash] < cost + 1):
                insort(q, (cost + 1, fwd, move, path + [loc]))
        oth = other_dirs(move)
        hash = f"{loc[0]}-{loc[1]}-{oth[1]}"
        if not (hash in cache and cache[hash] < cost + 1000):
            insort(q, (cost + 1000, loc, oth[1], path + [loc]))
        hash = f"{loc[0]}-{loc[1]}-{oth[0]}"
        if not (hash in cache and cache[hash] < cost + 1000):
            insort(q, (cost + 1000, loc, oth[0], path + [loc]))
    return best


def other_dirs(move):
    if move == '^' or move == 'v':
        return '<', '>'
    else:
        return '^', 'v'


def p_board(board):
    print("\n".join(list(map(lambda x: "".join(x), board))))


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

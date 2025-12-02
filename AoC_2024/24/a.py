import sys
sys.setrecursionlimit(10000)
from itertools import combinations


def solve(lines):
    vals = {}
    board = []
    for i in range(len(lines)):
        line = lines.pop(0).strip()
        if line == "":
            break
        l, n = line.split()
        vals[l[:-1]] = int(n)
    for i in range(len(lines)):
        line = lines.pop(0).strip()
        x, op, y, _, out = line.split()
        board.append((x, y, op, out))
    return answer(vals, board)


def answer(vals, board):
    # print(vals, board)
    zs = []
    while len(board) != 0:
        x, y, op, out = board.pop(0)
        if x in vals and y in vals:
            if op == 'AND':
                vals[out] = vals[x] & vals[y]
            elif op == 'OR':
                vals[out] = vals[x] | vals[y]
            elif op == 'XOR':
                vals[out] = vals[x] ^ vals[y]
            if out[0] == 'z':
                zs.append((int(out[1:]), vals[out]))
        else:
            board.append((x, y, op, out))
    zs.sort()
    zs.reverse()
    nums = map(lambda x: str(x[1]), zs)
    n = "".join(nums)
    n = int(n, 2)
    return n


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

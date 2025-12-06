import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from AoC_2025.utils.read import *
from functools import reduce

def solve(contents):
    board = []
    h = len(contents)
    w = len(contents[0])
    board.append(["."] * (w + 2))
    for r in contents:
        r = list(r)
        r.insert(0, ".")
        r.append(".")
        board.append(r)
    board.append(["."] * (w + 2))
    # print(board)
    diffs = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),           (0, 1),
             (1, -1), (1, 0), (1, 1),]

    ans = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if board[i][j] == "@":
                c = reduce(lambda x, y: x + (0 if board[i+y[0]][j+y[1]] == "." else 1), diffs, 0)
                # print(i, j, c)
                if c < 4:
                    ans += 1
    return str(ans)

def setup():
    contents = read_in()
    ans = solve(contents)
    write_out(ans)
    print(ans)

setup()
from functools import reduce
from collections import defaultdict


def solve(lines):
    board = []
    heads = []
    for i, line in enumerate(lines):
        temp = list(map(int, line.strip()))
        for j, c in enumerate(temp):
            if c == 0:
                heads.append((i, j))
        board.append(temp)

    return answer(board, heads)


def answer(board, heads):
    tot = 0
    for head in heads:
        tot += sum(count_for_head(board, head, defaultdict(lambda: 0)).values())
    return tot


def count_for_head(board, loc, tot):
    val = board[loc[0]][loc[1]]
    if val == 9:
        tot[str(loc)] += 1
        return tot
    else:
        adjs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for adj in adjs:
            try:
                new_loc = (loc[0] - adj[0], loc[1] - adj[1])
                if new_loc[0] < 0 or new_loc[1] < 0:
                    raise IndexError
                c = board[new_loc[0]][new_loc[1]]
                if c == val + 1:
                    count_for_head(board, new_loc, tot)
                    # print(tot)
            except IndexError:
                continue
    return tot




with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

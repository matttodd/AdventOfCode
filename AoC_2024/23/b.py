import sys
sys.setrecursionlimit(10000)
from collections import defaultdict
from itertools import permutations

def solve(lines):
    tot = 0
    all = set()
    board = defaultdict(set)
    for ind, line in enumerate(lines):
        a, b = line.strip().split('-')
        all.add(a)
        all.add(b)
        board[a].add(b)
        board[b].add(a)
    return answer(board, all)


def answer(board, all):
    tot = all.copy()
    # print(board)
    while True:
        worst = min(board.items(), key=lambda x: len(x[1]))
        # print(worst)
        if len(worst[1]) == len(tot) - 1:
            ans = list(tot)
            ans.sort()
            return ",".join(ans)
        tot.remove(worst[0])
        board.pop(worst[0])
        for k in board.keys():
            if worst[0] in board[k]:
                board[k].remove(worst[0])


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

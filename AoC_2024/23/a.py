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
    tot = set()
    for k, v in board.items():
        if k[0] == 't' and len(v) >= 2:
            others = list(v)
            perms = list(permutations(others, 2))
            for p1, p2 in perms:
                if p2 in board[p1] and p1 in board[p2]:
                    t = [k, p1, p2]
                    t.sort()
                    tot.add(tuple(t))
    return len(tot)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

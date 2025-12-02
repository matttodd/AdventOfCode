import sys
sys.setrecursionlimit(10000)

def solve(lines):
    tot = 0
    board = []
    start = (0, 0)
    for ind, line in enumerate(lines):
        line = line.strip()
        if 'S' in line:
            start = (ind, line.index('S'))
        board.append(list(line))
    tot += how_many_plots(board, start)
    return tot


def how_many_plots(board, start):
    q = [(start, 0)]
    new_locs = set()
    while q:
        # print(q)
        cur = q.pop(0)
        # if cur[1] == 6:
        #     q.append(cur)
        #     return len(set(q))
        loc = cur[0]
        for poss in [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]:
            if poss[0] >= 0 and poss[0] < len(board) and poss[1] >= 0 and poss[1] < len(board[0]):
                if board[poss[0]][poss[1]] != '#':
                    new_locs.add((poss, cur[1] + 1))
        if len(q) == 0:
            if cur[1] == 64 - 1:
                return len(new_locs)
            else:
                q.extend(list(new_locs))
                new_locs = set()
    return 0


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

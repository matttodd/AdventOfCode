from functools import reduce

def solve(lines):
    tot = 0
    board = []
    empty_rows = set()
    empty_cols = set()
    for ind, line in enumerate(lines):
        board.append(list(line.strip()))
        if len(set(list(line.strip()))) == 1:
            empty_rows.add(ind)

    # print(board)

    i = 0
    while i < len(board[0]):
        if all(board[x][i] == '.' for x in range(len(board))):
            empty_cols.add(i)
        i += 1

    locs = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '#':
                locs.append((i, j))

    for i in range(len(locs) - 1):
        for j in range(i + 1, len(locs)):
            row_range = range(min(locs[i][0], locs[j][0]), max(locs[i][0], locs[j][0]))
            col_range = range(min(locs[i][1], locs[j][1]), max(locs[i][1], locs[j][1]))
            for k in col_range:
                if k in empty_cols:
                    tot += 10**6
                else:
                    tot += 1
            for k in row_range:
                if k in empty_rows:
                    tot += 10**6
                else:
                    tot += 1

    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

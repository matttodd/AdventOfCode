from functools import reduce

def solve(lines):
    tot = 0
    board = []
    for line in lines:
        board.append(list(line.strip()))
        if len(set(list(line.strip()))) == 1:
            board.append(list(line.strip()))

    # print(board)

    i = 0
    while i < len(board[0]):
        if all(board[x][i] == '.' for x in range(len(board))):
            for j in range(len(board)):
                board[j].insert(i, '.')
            i += 1
        i += 1

    locs = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '#':
                locs.append((i, j))

    for i in range(len(locs) - 1):
        for j in range(i + 1, len(locs)):
            tot += max(locs[i][0], locs[j][0]) - min(locs[i][0], locs[j][0])
            tot += max(locs[i][1], locs[j][1]) - min(locs[i][1], locs[j][1])

    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

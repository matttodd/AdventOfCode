from functools import reduce


def solve(lines):
    tot = 0
    boards = []
    board = []
    for line in lines:
        line = line.strip()
        if line == "":
            boards.append(board)
            board = []
        else:
            board.append(list(line))
    boards.append(board)
    for board in boards:
        tot += solve_board(board)
    return tot


def solve_board(board):
    for i in range(1, len(board)):
        if is_horiz(board, i):
            return (100 * i)
    for i in range(1, len(board[0])):
        if is_vert(board, i):
            return i
    # print(board)
    return None


def is_horiz(board, n):
    diff = 0
    for i in range(n):
        row_to_check = 2 * n - i - 1
        # print(board[row_to_check], board[i])
        if row_to_check >= len(board):
            continue
        diff += diffs(board[row_to_check], board[i])
    # print(n)
    return diff == 1


def is_vert(board, n):
    diff = 0
    for i in range(n):
        row_to_check = 2 * n - i - 1
        # print(board[row_to_check], board[i])
        if row_to_check >= len(board[0]):
            continue
        target = [board[x][row_to_check] for x in range(len(board))]
        source = [board[x][i] for x in range(len(board))]
        diff += diffs(target, source)
    # print(n)
    return diff == 1


def diffs(l1, l2):
    return sum(1 for i, j in zip(l1, l2) if i != j)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

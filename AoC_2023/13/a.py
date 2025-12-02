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
            return 100 * i
    for i in range(1, len(board[0])):
        if is_vert(board, i):
            return i
    # print(board)
    return None


def is_horiz(board, n):
    for i in range(n):
        row_to_check = 2 * n - i - 1
        # print(board[row_to_check], board[i])
        if row_to_check >= len(board):
            continue
        if board[row_to_check] != board[i]:
            return False
    # print(n)
    return True


def is_vert(board, n):
    for i in range(n):
        row_to_check = 2 * n - i - 1
        # print(board[row_to_check], board[i])
        if row_to_check >= len(board[0]):
            continue
        target = [board[x][row_to_check] for x in range(len(board))]
        source = [board[x][i] for x in range(len(board))]
        if target != source:
            return False
    # print(n)
    return True


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

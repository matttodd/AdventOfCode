from functools import reduce


def solve(lines):
    board = []
    for line in lines:
        line = line.strip()
        board.append(list(line))
    return load_board(board)


def load_board(board):
    count = 0
    for i in range(len(board[0])):
        highest_point = 0
        for j in range(len(board)):
            cur = board[j][i]
            if cur == '#':
                highest_point = j + 1
            elif cur == 'O':
                highest_point += 1
                count += (len(board) - highest_point + 1)
    return count


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

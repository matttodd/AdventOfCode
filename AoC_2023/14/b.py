from functools import reduce


def solve(lines):
    board = []
    for line in lines:
        line = line.strip()
        board.append(list(line))
    return load_board(board)


def load_board(board):
    cycles = 1_000_000_000
    cache = {0: board}
    diff = 0
    start = 0
    for i in range(1, cycles + 1):
        next_board(board)
        key = "\n".join(map(lambda x: "".join(x), board))
        if key in cache:
            print(i - cache[key])
            # print_board(board)
            diff = i - cache[key]
            start = cache[key]
            break
        cache[key] = i

    board_ind = ((cycles - start) % diff)
    print(cycles - start, diff, (cycles - start) % diff)
    for k, v in cache.items():
        if v == board_ind + start:
            board = list(map(list, k.split("\n")))
    print(board)
    print_board(board)

    return counts_for_board(board)


def counts_for_board(s_board):
    board = s_board.copy()

    count = 0
    for i in range(len(board[0])):
        for j in range(len(board)):
            cur = board[j][i]
            if cur == 'O':
                count += (len(board) - j)
    return count


def print_board(b):
    for row in b:
        print("".join(row))#.replace('+', " "))
    print()


def next_board(board):
    # north
    for i in range(len(board[0])):
        highest_point = 0
        for j in range(len(board)):
            cur = board[j][i]
            if cur == '#':
                highest_point = j + 1
            elif cur == 'O':
                board[highest_point][i] = "O"
                if j != highest_point:
                    board[j][i] = "."
                highest_point += 1
    # west
    for i in range(len(board)):
        highest_point = 0
        for j in range(len(board[0])):
            cur = board[i][j]
            if cur == '#':
                highest_point = j + 1
            elif cur == 'O':
                board[i][highest_point] = "O"
                if j != highest_point:
                    board[i][j] = "."
                highest_point += 1
    # south
    for i in range(len(board[0])):
        highest_point = len(board) - 1
        for j in range(len(board) - 1, -1, -1):
            cur = board[j][i]
            if cur == '#':
                highest_point = j - 1
            elif cur == 'O':
                if j != highest_point:
                    board[j][i] = "."
                    board[highest_point][i] = "O"
                highest_point -= 1
    # west
    for i in range(len(board)):
        highest_point = len(board[0]) - 1
        for j in range(len(board[0]) - 1, -1, -1):
            cur = board[i][j]
            if cur == '#':
                highest_point = j - 1
            elif cur == 'O':
                board[i][highest_point] = "O"
                if j != highest_point:
                    board[i][j] = "."
                highest_point -= 1


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

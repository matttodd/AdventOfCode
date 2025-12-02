import sys

sys.setrecursionlimit(10**6)


def main():
    print(solve())


def solve():
    board = []
    moves = []
    facing = 'R'
    max_width = 0
    has_loaded_board = False
    while True:
        try:
            inp = input()
            if has_loaded_board:
                temp = ""
                for cha in inp:
                    if cha == 'R':
                        moves.append(int(temp))
                        temp = ""
                        moves.append('R')
                    elif cha == 'L':
                        moves.append(int(temp))
                        temp = ""
                        moves.append('L')
                    else:
                        temp = temp + cha
                moves.append(int(temp))
            elif inp != '':
                max_width = max(max_width, len(list(inp)))
                board.append(list(inp))
            if inp == '':
                has_loaded_board = True
        except EOFError:
            for ind, row in enumerate(board):
                if len(row) < max_width:
                    board[ind] = row + [' ' for i in range(max_width - len(row))]
            # prnt(board)
            print(max(list(filter(lambda x: type(x) is int, moves))))
            start = (board[0].index('.'), 0)
            point, dir = get_resting_place(board, moves, facing, start)
            print(point, dir)
            return (point[1] + 1) * 1000 + (point[0] + 1) * 4 + num(dir)


def get_resting_place(board, moves, facing, current):
    while True:
        if len(moves) == 0:
            return current, facing
        if type(moves[0]) is int:
            if moves[0] == 0:
                moves = moves[1:]
                # print(moves[0:4], current, board[current[1]][current[0]])
            else:
                moves[0] = moves[0] - 1
                board, current = move_one(board, facing, current, current)
        else:
            facing = new_dir(facing, moves[0])
            moves = moves[1:]
    # return get_resting_place(board, moves, facing, current)


def num(dir):
    if dir == 'R':
        return 0
    elif dir == 'D':
        return 1
    elif dir == 'L':
        return 2
    else:
        return 3


def move_one(board, facing, current, prev):
    next_point = (0, 0)
    if facing == 'U':
        next_point = (current[0], current[1] - 1)
        if next_point[1] < 0:
            next_point = (current[0], len(board) - 1)
    elif facing == 'D':
        next_point = (current[0], current[1] + 1)
        if next_point[1] >= len(board):
            next_point = (current[0], 0)
    elif facing == 'L':
        next_point = (current[0] - 1, current[1])
        if next_point[0] < 0:
            next_point = (len(board[0]) - 1, current[1])
    elif facing == 'R':
        next_point = (current[0] + 1, current[1])
        if next_point[0] >= len(board[0]):
            next_point = (0, current[1])
    # print(next_point)
    if board[next_point[1]][next_point[0]] == ' ':
        return move_one(board, facing, next_point, prev)
    elif board[next_point[1]][next_point[0]] == '#':
        return board, prev
    else:
        return board, next_point


def new_dir(curr, r_or_l):
    if curr == 'U':
        return 'L' if r_or_l == 'L' else 'R'
    elif curr == 'D':
        return 'R' if r_or_l == 'L' else 'L'
    elif curr == 'L':
        return 'D' if r_or_l == 'L' else 'U'
    elif curr == 'R':
        return 'U' if r_or_l == 'L' else 'D'


def prnt(s):
    # print(s)
    rows = list(map(lambda x: "".join(x), s))
    # print(rows)
    print("\n".join(rows))


main()

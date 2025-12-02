import sys

sys.setrecursionlimit(10**6)

# appears the final spot in 92, 75 which when transformed back to the original coordinates
# should line up with 126, 42 and L should change to down when accounting for the rotation
# 58344 is too large so 126169 cannot be correct
# 36570 too low
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
            # print(max(list(filter(lambda x: type(x) is int, moves))))
            start = (board[0].index('.'), 0)
            point, dir = get_resting_place(board, moves, facing, start)
            print(point, dir)
            board[point[1]][point[0]] = 'O'
            prnt(board)
            return (point[1]), (point[0]), num(dir)


def get_resting_place(board, moves, facing, current):
    count = 10000
    while True:
        if len(moves) < 50:
            count = 0
        if len(moves) == 0:
            return current, facing
        if type(moves[0]) is int:
            if moves[0] == 0:
                moves = moves[1:]
                # board[current[1]][current[0]] = 'O'
            else:
                moves[0] = moves[0] - 1
                board, current, facing = move_one(board, facing, current, count)
                count += 1
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


def move_one(board, facing, current, count):
    # print(facing)
    og_facing = facing
    next_point = (0, 0)
    if facing == 'U':
        next_point = (current[0], current[1] - 1)
        if next_point[1] < 0 or board[next_point[1]][next_point[0]] == ' ':
            next_point, facing = new_pos_and_dir(current, facing)
            print(current, og_facing, next_point, facing)
    elif facing == 'D':
        next_point = (current[0], current[1] + 1)
        if next_point[1] >= len(board) or board[next_point[1]][next_point[0]] == ' ':
            next_point, facing = new_pos_and_dir(current, facing)
            print(current, og_facing, next_point, facing)
    elif facing == 'L':
        next_point = (current[0] - 1, current[1])
        if next_point[0] < 0 or board[next_point[1]][next_point[0]] == ' ':
            next_point, facing = new_pos_and_dir(current, facing)
            print(current, og_facing, next_point, facing)
    elif facing == 'R':
        next_point = (current[0] + 1, current[1])
        if next_point[0] >= len(board[0]) or board[next_point[1]][next_point[0]] == ' ':
            next_point, facing = new_pos_and_dir(current, facing)
            print(current, og_facing, next_point, facing)
    # if board[next_point[1]][next_point[0]] == ' ':
    #     return move_one(board, facing, next_point, prev)
    if board[next_point[1]][next_point[0]] == '#':
        # if count < 500:
        #     print(current, og_facing)
        return board, current, og_facing
    else:
        # if count < 500:
        #     print(next_point, facing)
        if count < 2000:
            if facing == 'L':
                board[next_point[1]][next_point[0]] = '<'
            elif facing == 'D':
                board[next_point[1]][next_point[0]] = 'V'
            elif facing == 'R':
                board[next_point[1]][next_point[0]] = '>'
            else:
                board[next_point[1]][next_point[0]] = '^'
        return board, next_point, facing


def new_pos_and_dir(curr, dir):
    DIM = 50
    if curr[0] < DIM:
        if dir == 'U':
            return ((3 * DIM) - curr[0] - 1, 0), 'D'
        elif dir == 'L':
            return ((4 * DIM) - (curr[1] - DIM) - 1, (3 * DIM) - 1), 'U'
        elif dir == 'D':
            return ((2 * DIM) + (DIM - curr[0] - 1), (3 * DIM) - 1), 'U'
    elif curr[0] < 2 * DIM:
        if dir == 'U':
            return (2 * DIM, curr[0] - DIM), 'R'
        elif dir == 'D':
            return (2 * DIM, (2 * DIM) + ((2 * DIM) - curr[0] - 1)), 'R'
    elif curr[1] < DIM:
        if dir == 'U':
            return (DIM - (curr[0] - (2 * DIM)) - 1, DIM), 'D'
        elif dir == 'L':
            return (DIM + curr[1], DIM), 'D'
        elif dir == 'R':
            return ((4 * DIM) - 1, (2 * DIM) + (DIM - curr[1]) - 1), 'L'
    elif curr[1] < 2 * DIM:
        if dir == 'R':
            return ((3 * DIM) + ((2 * DIM) - curr[1] - 1), 2 * DIM), 'D'
    elif curr[0] < 3 * DIM:
        if dir == 'L':
            return ((2 * DIM) - (curr[1] - (2 * DIM) + 1), (2 * DIM) - 1), 'U'
        elif dir == 'D':
            return (DIM - (curr[0] - (2 * DIM)) - 1, (2 * DIM) - 1), 'U'
    else:
        if dir == 'U':
            return ((3 * DIM) - 1, DIM + ((4 * DIM) - curr[0] - 1)), 'L'
        elif dir == 'R':
            return ((3 * DIM) - 1, DIM - (curr[1] - (2 * DIM) + 1)), 'L'
        elif dir == 'D':
            return (0, DIM + ((4 * DIM) - curr[0] - 1)), 'R'
    return dir


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

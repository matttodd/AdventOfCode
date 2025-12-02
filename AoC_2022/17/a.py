from collections import defaultdict
from copy import deepcopy


def main():
    print(solve())


def solve():
    total = 0
    board = [["." for _ in range(7)] for _ in range(5000000)]
    board.insert(0, ["_" for _ in range(7)])
    heights = {0: 1, 1: 3, 2: 3, 3: 4, 4: 2}
    len_wind = 0
    vals = []
    wind = ""
    height = 0
    while True:
        try:
            inp = input()
            wind = inp
        except EOFError:
            # print("hey look i started, FOOL")
            wind_count = 0
            len_wind = len(wind)
            for i in range(8000):
                if i % 5 == 0:
                    print(i, height, wind_count % len_wind)
                    # print(wind_count % len_wind)
                    vals.append(height)
                    # prnt(board, height)
                curr_height = height + 4
                bl = (2, curr_height)
                while True:
                    # draw_temp(board, i % 5, bl, height)
                    bl = move_side(board, i % 5, bl, wind[wind_count % len(wind)] == "<")
                    # draw_temp(board, i % 5, bl, height)
                    old_bl = (bl[0], bl[1])
                    bl = move_down(board, i % 5, bl)
                    # draw_temp(board, i % 5, bl, height)
                    wind_count += 1
                    if bl == old_bl:
                        break
                draw(board, i % 5, bl)
                height = max(height, bl[1] + heights[i % 5] - 1)
                # prnt(board, height)
            print(vals)
            diffs = []
            for i in range(len(vals) - 1):
                diffs.append(vals[i+1] - vals[i])
            print(diffs)
            return height


def draw(board, stype, bl):
    if stype == 0:
        board[bl[1]][bl[0]] = "#"
        board[bl[1]][bl[0] + 1] = "#"
        board[bl[1]][bl[0] + 2] = "#"
        board[bl[1]][bl[0] + 3] = "#"
    if stype == 1:
        board[bl[1]][bl[0] + 1] = "#"
        board[bl[1] + 1][bl[0]] = "#"
        board[bl[1] + 1][bl[0] + 1] = "#"
        board[bl[1] + 1][bl[0] + 2] = "#"
        board[bl[1] + 2][bl[0] + 1] = "#"
    if stype == 2:
        board[bl[1]][bl[0]] = "#"
        board[bl[1]][bl[0] + 1] = "#"
        board[bl[1]][bl[0] + 2] = "#"
        board[bl[1] + 1][bl[0] + 2] = "#"
        board[bl[1] + 2][bl[0] + 2] = "#"
    if stype == 3:
        board[bl[1]][bl[0]] = "#"
        board[bl[1] + 1][bl[0]] = "#"
        board[bl[1] + 2][bl[0]] = "#"
        board[bl[1] + 3][bl[0]] = "#"
    if stype == 4:
        board[bl[1]][bl[0]] = "#"
        board[bl[1] + 1][bl[0]] = "#"
        board[bl[1] + 1][bl[0] + 1] = "#"
        board[bl[1]][bl[0] + 1] = "#"


def draw_temp(sboard, stype, bl, height):
    board = deepcopy(sboard)
    if stype == 0:
        board[bl[1]][bl[0]] = "@"
        board[bl[1]][bl[0] + 1] = "@"
        board[bl[1]][bl[0] + 2] = "@"
        board[bl[1]][bl[0] + 3] = "@"
    if stype == 1:
        board[bl[1]][bl[0] + 1] = "@"
        board[bl[1] + 1][bl[0]] = "@"
        board[bl[1] + 1][bl[0] + 1] = "@"
        board[bl[1] + 1][bl[0] + 2] = "@"
        board[bl[1] + 2][bl[0] + 1] = "@"
    if stype == 2:
        board[bl[1]][bl[0]] = "@"
        board[bl[1]][bl[0] + 1] = "@"
        board[bl[1]][bl[0] + 2] = "@"
        board[bl[1] + 1][bl[0] + 2] = "@"
        board[bl[1] + 2][bl[0] + 2] = "@"
    if stype == 3:
        board[bl[1]][bl[0]] = "@"
        board[bl[1] + 1][bl[0]] = "@"
        board[bl[1] + 2][bl[0]] = "@"
        board[bl[1] + 3][bl[0]] = "@"
    if stype == 4:
        board[bl[1]][bl[0]] = "@"
        board[bl[1] + 1][bl[0]] = "@"
        board[bl[1] + 1][bl[0] + 1] = "@"
        board[bl[1]][bl[0] + 1] = "@"
    prnt(board, height)


def move_side(board, stype, bl, left):
    # print(stype, bl, left)
    if stype == 0:
        # shape 1
        if left:
            if bl[0] != 0 and board[bl[1]][bl[0] - 1] == ".":
                bl = (bl[0] - 1, bl[1])
        else:
            if bl[0] != 3 and board[bl[1]][bl[0] + 4] == ".":
                bl = (bl[0] + 1, bl[1])
    if stype == 1:
        # shape 2
        if left:
            if bl[0] != 0 and board[bl[1]][bl[0]] == "." and \
                    board[bl[1] + 1][bl[0] - 1] == "." and \
                    board[bl[1] + 2][bl[0]] == ".":
                bl = (bl[0] - 1, bl[1])
        else:
            if bl[0] != 4 and board[bl[1]][bl[0] + 2] == "." and \
                    board[bl[1] + 1][bl[0] + 3] == "." and \
                    board[bl[1] + 2][bl[0] + 2] == ".":
                bl = (bl[0] + 1, bl[1])
    if stype == 2:
        # shape 3
        if left:
            if bl[0] != 0 and board[bl[1]][bl[0] - 1] == "." and \
                    board[bl[1] + 1][bl[0] + 1] == "." and \
                    board[bl[1] + 2][bl[0] + 1] == ".":
                bl = (bl[0] - 1, bl[1])
        else:
            if bl[0] != 4 and board[bl[1]][bl[0] + 3] == "." and \
                    board[bl[1] + 1][bl[0] + 3] == "." and \
                    board[bl[1] + 2][bl[0] + 3] == ".":
                bl = (bl[0] + 1, bl[1])
    if stype == 3:
        # shape 4
        if left:
            if bl[0] != 0 and board[bl[1]][bl[0] - 1] == "." and \
                    board[bl[1] + 1][bl[0] - 1] == "." and \
                    board[bl[1] + 2][bl[0] - 1] == "." and \
                    board[bl[1] + 3][bl[0] - 1] == ".":
                bl = (bl[0] - 1, bl[1])
        else:
            if bl[0] != 6 and board[bl[1]][bl[0] + 1] == "." and \
                    board[bl[1] + 1][bl[0] + 1] == "." and \
                    board[bl[1] + 2][bl[0] + 1] == "." and \
                    board[bl[1] + 3][bl[0] + 1] == ".":
                bl = (bl[0] + 1, bl[1])
    if stype == 4:
        # shape 5
        if left:
            if bl[0] != 0 and board[bl[1]][bl[0] - 1] == "." and \
                    board[bl[1] + 1][bl[0] - 1] == ".":
                bl = (bl[0] - 1, bl[1])
        else:
            if bl[0] != 5 and board[bl[1]][bl[0] + 2] == "." and \
                    board[bl[1] + 1][bl[0] + 2] == ".":
                bl = (bl[0] + 1, bl[1])
    return bl


def move_down(board, stype, bl):
    if stype == 0:
        if board[bl[1] - 1][bl[0]] == "." and \
                    board[bl[1] - 1][bl[0] + 1] == "." and \
                    board[bl[1] - 1][bl[0] + 2] == "." and \
                    board[bl[1] - 1][bl[0] + 3] == ".":
            return bl[0], bl[1] - 1
    if stype == 1:
        if board[bl[1]][bl[0]] == "." and \
                    board[bl[1] - 1][bl[0] + 1] == "." and \
                    board[bl[1]][bl[0] + 2] == ".":
            return bl[0], bl[1] - 1
    if stype == 2:
        if board[bl[1] - 1][bl[0]] == "." and \
                    board[bl[1] - 1][bl[0] + 1] == "." and \
                    board[bl[1] - 1][bl[0] + 2] == ".":
            return bl[0], bl[1] - 1
    if stype == 3:
        if board[bl[1] - 1][bl[0]] == ".":
            return bl[0], bl[1] - 1
    if stype == 4:
        if board[bl[1] - 1][bl[0]] == "." and board[bl[1] - 1][bl[0] + 1] == ".":
            return bl[0], bl[1] - 1
    return bl


def prnt(board, height):
    rows = list(map(lambda x: "".join(x), board))[height - 15:height + 5]
    rows.reverse()
    out = "\n".join(rows)
    # print(rows)
    print(out)


main()


def solve(lines):
    total = 0
    board = []
    for line in lines:
        board.append(list(line.strip()))
    cur_num = ""
    is_cur_part_num = False
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if not val.isdigit():
                if is_cur_part_num:
                    print(cur_num)
                    total += int(cur_num)
                cur_num = ""
                is_cur_part_num = False
            else:
                if check_all_surrounding(x, y, board):
                    is_cur_part_num = True
                cur_num += val
        if is_cur_part_num:
            total += int(cur_num)
        cur_num = ""
        is_cur_part_num = False

    return total


def check_all_surrounding(x, y, board):

    def is_non_period(i, j):
        char = board[j][i]
        return not char.isdigit() and char != "."

    if x > 0:
        if is_non_period(x - 1, y):
            return True
        if y > 0:
            if is_non_period(x - 1, y - 1) or is_non_period(x, y - 1):
                return True
        if y < len(board) - 1:
            if is_non_period(x - 1, y + 1) or is_non_period(x, y + 1):
                return True
    # print(board[0], len(board))
    if x < len(board[0]) - 1:
        if is_non_period(x + 1, y):
            return True
        if y > 0:
            if is_non_period(x + 1, y - 1):
                return True
        if y < len(board) - 1:
            if is_non_period(x + 1, y + 1):
                return True
    return False


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

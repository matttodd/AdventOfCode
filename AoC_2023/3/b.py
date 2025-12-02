
def solve(lines):
    total = 0
    board = []
    gear_dict = {}
    for line in lines:
        board.append(list(line.strip()))
    cur_num = ""
    cur_gear = None
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if not val.isdigit():
                if cur_gear is not None:
                    print(cur_num)
                    if cur_gear in gear_dict:
                        gear_dict[cur_gear].append(int(cur_num))
                    else:
                        gear_dict[cur_gear] = [int(cur_num)]
                cur_num = ""
                cur_gear = None
            else:
                if cur_gear is None:
                    cur_gear = check_all_surrounding(x, y, board)
                cur_num += val
        if cur_gear is not None:
            if cur_gear in gear_dict:
                gear_dict[cur_gear].append(int(cur_num))
            else:
                gear_dict[cur_gear] = [int(cur_num)]
        cur_num = ""
        cur_gear = None
    for counts in gear_dict.values():
        if len(counts) == 2:
            total += counts[0] * counts[1]

    return total


def check_all_surrounding(x, y, board):

    def is_gear(i, j):
        char = board[j][i]
        return char == "*"

    if x > 0:
        if is_gear(x - 1, y):
            return x - 1, y
        if y > 0:
            if is_gear(x - 1, y - 1):
                return x - 1, y - 1
            if is_gear(x, y - 1):
                return x, y - 1
        if y < len(board) - 1:
            if is_gear(x - 1, y + 1):
                return x - 1, y + 1
            if is_gear(x, y + 1):
                return x, y + 1
    if x < len(board[0]) - 1:
        if is_gear(x + 1, y):
            return x + 1, y
        if y > 0:
            if is_gear(x + 1, y - 1):
                return x + 1, y - 1
        if y < len(board) - 1:
            if is_gear(x + 1, y + 1):
                return x + 1, y + 1
    return None


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

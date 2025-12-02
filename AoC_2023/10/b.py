from functools import reduce

def solve(lines):
    tot = 0
    board = []
    start = (0, 0)
    for i, line in enumerate(lines):
        temp = list(line.strip())
        board.append(temp)
        if 'S' in temp:
            s = temp.index('S')
            start = (i, s)

    return find_loop_length(board, start)


def connections(char):
        if char == '-':
            return [(0, -1), (0, 1)]
        elif char == '|':
            return [(-1, 0), (1, 0)]
        elif char == 'L':
            return [(-1, 0), (0, 1)]
        elif char == 'J':
            return [(-1, 0), (0, -1)]
        elif char == '7':
            return [(1, 0), (0, -1)]
        elif char == 'F':
            return [(1, 0), (0, 1)]
        elif char == 'S':
            return [(0, -1), (0, 1), (-1, 0), (1, 0)]


def find_loop_length(b, start):
    visitable = [start]
    been = set(visitable)
    while visitable:
        cur = visitable.pop(0)
        been.add(cur)
        char = b[cur[0]][cur[1]]
        cnc = connections(char)
        new_locs = map(lambda x: (cur[0] + x[0], cur[1] + x[1]), cnc)
        new_locs = filter(lambda x: x[1] >= 0 and x[1] < len(b[0]) and x[0] >= 0 and x[0] < len(b), new_locs)
        cnct = list(filter(lambda x: x not in been and b[x[0]][x[1]] != '.', new_locs))
        # print(cnct)
        if start == 'S':
            cnct = list(filter(lambda x:  b[x[0]][x[1]] != '.', cnct))
            fill = []
            for ct in cnct:
                ct_char = b[ct[0]][ct[1]]
                ct_connections = connections(ct_char)
                connections_connections = list(map(lambda x: (cur[0] + x[0], cur[1] + x[1]), ct_connections))
                if start in connections_connections:
                    fill.append(ct)
            cnct = fill

        visitable.extend(cnct)

    print_board(b)

    b = clear_wrong_pipes(b, been)

    print_board(b)

    ans = find_dots(b, been)

    print_board(b)

    return ans


def clear_wrong_pipes(board, been):
    new_board = []
    for i, row in enumerate(board):
        temp = []
        bonus = []
        for j, v in enumerate(row):
            if v == ".":
                temp += "@"
            else:
                temp += v if (i, j) in been else "@"
            if (v == '7' or v == 'F' or v == '|' or v == 'S') and (i, j) in been:
                bonus += '|'
            else:
                bonus += '+'
        new_board.append(temp)
        new_board.append(bonus)

    i = 0
    stop = len(board[0])
    while i < stop:
        col = [board[j][i] for j in range(len(board))]
        for k, item in enumerate(col):
            if (item == "L" or item == "F" or item == "-" or item == 'S') and (k, i) in been:
                new_board[2*k].insert(2*i + 1, "-")
            else:
                new_board[2*k].insert(2*i + 1, "+")
            new_board[2 * k + 1].insert(2 * i + 1, "+")
        i += 1

    return new_board


def print_board(b):
    for row in b:
        print("".join(row))#.replace('+', " "))


def find_dots(b, been):
    return bfs_from(b, (len(b)//2, len(b[0])//2))


def bfs_from(b, cur):
    queue = [cur]
    seen = set()
    counter = 0
    while queue:
        cur = queue.pop(0)
        if cur in seen:
            continue
        if cur[0] < 0 or cur[1] < 0 or cur[0] >= len(b) or cur[1] >= len(b[0]):
            # print(len(b), len(b[0]))
            # print(cur)
            return False
        seen.add(cur)
        # print(cur, queue)
        cur_char = b[cur[0]][cur[1]]
        if cur_char == '@':
            counter += 1
        if cur_char != "+" and cur_char != "." and cur_char != "@":
            continue
        queue.extend([(cur[0] - 1, cur[1]), (cur[0] + 1, cur[1]), (cur[0], cur[1] - 1), (cur[0], cur[1] + 1)])
    return counter


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

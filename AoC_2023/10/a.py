from functools import reduce

def solve(lines):
    tot = 0
    board = []
    start = (0, 0)
    for i, line in enumerate(lines):
        temp = list(line)
        board.append(temp)
        if 'S' in temp:
            s = temp.index('S')
            start = (i, s)

    return find_loop_length(board, start, None) // 2


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


def find_loop_length(b, start, prev):
    visitable = [start]
    been = set(visitable)
    while visitable:
        cur = visitable.pop(0)
        been.add(cur)
        # print(been)
        char = b[cur[0]][cur[1]]
        # print(char)
        cnc = connections(char)
        new_locs = list(map(lambda x: (cur[0] + x[0], cur[1] + x[1]), cnc))
        new_locs = list(filter(lambda x: x[0] >= 0 and x[0] < len(b[0]) and x[1] >= 0 and x[1] < len(b), new_locs))
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

    return len(been)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

import sys
sys.setrecursionlimit(10000)


def solve(lines):
    commands = []
    for line in lines:
        direction, dist, color = line.strip().split()
        color = color[2:-1]
        # dist = int(color[:-1], 16)
        # d_char = color[-1]
        # if d_char == '0':
        #     direction = 'R'
        # elif d_char == '1':
        #     direction = 'D'
        # elif d_char == '2':
        #     direction = 'L'
        # else:
        #     direction = 'U'

        dist = int(dist)
        commands.append((direction, dist))
    print(commands)
    verts, horiz = path_set(commands)
    verts.sort()
    horiz.sort()
    print(verts)
    print(horiz)
    return count_inner(verts, horiz)


def count_inner(verts, horiz):
    count = 0
    for i in range(1, len(horiz)):
        prev = horiz[i-1]
        cur = horiz[i]
        # if cur[0] == prev[0]:
        #     continue
        y_diff = cur[0] - prev[0]
        start = None
        for vert in verts:
            x = vert[0]
            y_max = vert[1]
            y_min = vert[2]
            if y_min <= prev[0] <= y_max:
                if start is None:
                    start = vert
                else:
                    # if
                    # print(prev, cur, start, vert)
                    print(cur[0], prev[0], vert[0], start[0], y_diff * (x - start[0] + 1))
                    count += y_diff * (x - start[0] + 1)
                    # count -=
                    start = None

    return count


def path_set(commands):
    x = 0
    y = 0
    verts = []
    horiz = []
    for command in commands:
        d, dist = command
        pre = (y, x)
        if d == 'D':
            y += dist
            verts.append((x, y, pre[0]))
        elif d == 'U':
            y -= dist
            verts.append((x, pre[0], y))
        elif d == 'L':
            x -= dist
            horiz.append((y, pre[1], x))
        else:
            x += dist
            horiz.append((y, x, pre[1]))
    return verts, horiz


# def count_ditch(board):
#     tot = len(board) * len(board[0])
#     bad = set()
#     begin = [(0, i) for i in range(len(board[0]))]
#     begin.extend([(len(board) - 1, i) for i in range(len(board[0]))])
#     begin.extend([(i, 0) for i in range(len(board))])
#     begin.extend([(i, len(board[0]) - 1) for i in range(len(board))])
#     print(begin)
#
#     while begin:
#         cur = begin.pop(0)
#         # print(cur)
#         if cur in bad:
#             continue
#         if board[cur[0]][cur[1]] == '#':
#             continue
#         else:
#             bad.add(cur)
#             if not cur[0] < 0:
#                 begin.append((cur[0] - 1, cur[1]))
#             if not cur[1] < 0:
#                 begin.append((cur[0], cur[1] - 1))
#             if not cur[0] >= len(board) - 1:
#                 begin.append((cur[0] + 1, cur[1]))
#             if not cur[1] >= len(board[0]) - 1:
#                 begin.append((cur[0], cur[1] + 1))
#
#     for cur in bad:
#         board[cur[0]][cur[1]] = 'X'


def printb(board):
    for row in board:
        print("".join(row))


# def pop_board(board, commands, start):
#     cury = start[0]
#     curx = start[1]
#     board[cury][curx] = '#'
#     for command in commands:
#         d, dist, color = command
#         for i in range(dist):
#             if d == 'D':
#                 cury += 1
#             elif d == 'U':
#                 cury -= 1
#             elif d == 'L':
#                 curx -= 1
#             else:
#                 curx += 1
#             board[cury][curx] = '#'


# def min_max(commands):
#     curx = 0
#     minx = 0
#     maxx = 0
#     cury = 0
#     miny = 0
#     maxy = 0
#     for command in commands:
#         d, dist, c = command
#         if d == 'U':
#             cury -= dist
#             maxy = max(cury, maxy)
#             miny = min(cury, miny)
#         elif d == 'D':
#             cury += dist
#             maxy = max(cury, maxy)
#             miny = min(cury, miny)
#         elif d == 'L':
#             curx -= dist
#             maxx = max(curx, maxx)
#             minx = min(curx, minx)
#         elif d == 'R':
#             curx += dist
#             maxx = max(curx, maxx)
#             minx = min(curx, minx)
#     return maxx - minx, maxy - miny, (abs(miny), abs(minx))


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

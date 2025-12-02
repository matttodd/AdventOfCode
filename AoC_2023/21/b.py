import sys
sys.setrecursionlimit(10000)

def solve(lines):
    tot = 0
    board = []
    start = (0, 0)
    for ind, line in enumerate(lines):
        line = line.strip()
        tot += line.count('.')
        if 'S' in line:
            tot += 1
            start = (ind, line.index('S'))
        board.append(list(line))
    print(tot)
    return how_many_plots(board, start, tot)


def how_many_plots(board, start, count):
    q = [(start, 0)]
    new_locs = set()
    full_board_odd = 0
    full_board_even = 0
    prev = None
    prevprev = 0
    while q:
        # print(q)
        cur = q.pop(0)
        loc = cur[0]
        for poss in [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]:
            if poss[0] >= 0 and poss[0] < len(board) and poss[1] >= 0 and poss[1] < len(board[0]):
                if board[poss[0]][poss[1]] != '#':
                    new_locs.add((poss, cur[1] + 1))
        if len(q) == 0:
            if len(new_locs) == prevprev:
                if (start[0] + start[1]) % 2 == 0:
                    full_board_even = len(new_locs)
                    full_board_odd = count - full_board_even
                else:
                    full_board_odd = len(new_locs)
                    full_board_even = count - full_board_odd
                print(len(new_locs))
                break
            prevprev = prev
            prev = len(new_locs)
            q.extend(list(new_locs))
            new_locs = set()
    print(full_board_even, full_board_odd)

    edges = [(0, i) for i in range(len(board[0]))]
    edges.extend([(len(board) - 1, i) for i in range(len(board[0]))])
    edges.extend([(i, 0) for i in range(1, len(board) - 1)])
    edges.extend([(i, len(board[0]) - 1) for i in range(1, len(board) - 1)])

    partial_fill = {}

    for edge in edges:
        is_odd = (edge[0] + edge[1]) % 2 == 1
        q = [(edge, 0)]
        new_locs = set()
        partial_fill[edge] = [1]
        while q:
            # print(q)
            cur = q.pop(0)
            loc = cur[0]
            for poss in [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]:
                if poss[0] >= 0 and poss[0] < len(board) and poss[1] >= 0 and poss[1] < len(board[0]):
                    if board[poss[0]][poss[1]] != '#':
                        new_locs.add((poss, cur[1] + 1))
            if len(q) == 0:
                q.extend(list(new_locs))
                partial_fill[edge].append(len(new_locs))
                new_locs = set()
                if len(partial_fill[edge]) > 1:
                    if partial_fill[edge][-2] == full_board_odd and partial_fill[edge][-1] == full_board_even:
                        break
                    elif partial_fill[edge][-2] == full_board_even and partial_fill[edge][-1] == full_board_odd:
                        break

    print(partial_fill)



    return 0


# def how_many_plots(board, start):
#     q = [(start, 0, 0, 0)]
#     new_locs = set()
#     odd_locs = set()
#     been = set()
#     while q:
#         cur = q.pop(0)
#         loc = cur[0]
#         for poss in [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]:
#             if poss[0] < 0:
#                 new_locs.add(((len(board) - 1, loc[1]), cur[1] + 1, cur[2] - 1, cur[3]))
#             elif poss[0] == len(board):
#                 new_locs.add(((0, loc[1]), cur[1] + 1, cur[2] + 1, cur[3]))
#             elif poss[1] < 0:
#                 new_locs.add(((loc[0], len(board[0]) - 1), cur[1] + 1, cur[2], cur[3] - 1))
#             elif poss[1] == len(board[0]):
#                 new_locs.add(((loc[0], 0), cur[1] + 1, cur[2], cur[3] + 1))
#             elif board[poss[0]][poss[1]] != '#':
#                 new_locs.add((poss, cur[1] + 1, cur[2], cur[3]))
#         if len(q) == 0:
#             if cur[1] == 100 - 1:
#                 return len(new_locs.union(odd_locs))
#             else:
#                 been.union(new_locs)
#                 if cur[1] % 2 == 0:
#                     odd_locs.union(new_locs)
#                 q.extend(list(new_locs - been))
#                 new_locs = set()
#     return 0


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

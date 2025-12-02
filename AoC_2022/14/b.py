import ast


def main():
    print(solve())


def solve():
    total = 0
    board = [["." for _ in range(1000)] for _ in range(200)]
    minx = 1000
    maxx = 0
    miny = 1000
    maxy = 0
    while True:
        try:
            # prnt(board)
            line = input().split(" -> ")
            line = list(map(lambda x: (int(x.split(',')[0]), int(x.split(',')[1])), line))
            # print(line)
            for i in range(len(line) - 1):
                minx = min(minx, line[i][0])
                maxx = max(maxx, line[i][0])
                miny = min(miny, line[i][1])
                maxy = max(maxy, line[i][1])
                if line[i][0] == line[i+1][0]:
                    for j in range(min(line[i][1], line[i+1][1]), max(line[i][1], line[i+1][1]) + 1):
                        board[j][line[i][0]] = '#'
                else:
                    for j in range(min(line[i][0], line[i+1][0]), max(line[i][0], line[i+1][0]) + 1):
                        board[line[i][1]][j] = '#'
            minx = min(minx, line[-1][0])
            maxx = max(maxx, line[-1][0])
            miny = min(miny, line[-1][1])
            maxy = max(maxy, line[-1][1])
        except EOFError:
            prnt(board, minx, maxx, 0, maxy)
            for i in range(1000):
                board[maxy + 2][i] = '#'
            new_source = 500
            prnt(board, minx, maxx, 0, maxy)
            while board[0][new_source] != 'o':
                # prnt(board, minx, maxx, 0, maxy)
                try:
                    place_in_board(board, (new_source, 0))
                    total += 1
                except IndexError:
                    return total
            # print(minx, maxx, miny, maxy)
            prnt(board, minx, maxx, 0, maxy)
            return total


def place_in_board(board, loc):
    # prnt(board, 494, 503, 0, 10)
    # print(loc)
    # print(board[loc[1] + 1][loc[0]], board[loc[1] + 1][loc[0] - 1], board[loc[1] + 1][loc[0] + 1])
    if board[loc[1] + 1][loc[0]] in ['#', 'o'] and board[loc[1] + 1][loc[0] - 1] in ['#', 'o'] and board[loc[1] + 1][loc[0] + 1] in ['#', 'o']:
        board[loc[1]][loc[0]] = 'o'
    elif board[loc[1] + 1][loc[0]] in ['#', 'o'] and board[loc[1] + 1][loc[0] - 1] in ['#', 'o']:
        place_in_board(board, (loc[0] + 1, loc[1] + 1))
    elif board[loc[1] + 1][loc[0]] in ['#', 'o']:
        place_in_board(board, (loc[0] - 1, loc[1] + 1))
    else:
        place_in_board(board, (loc[0], loc[1] + 1))


def prnt(s, minx, maxx, miny, maxy):
    # print(s)
    rows = list(map(lambda x: "".join(x[minx - 50:maxx+1+50]), s))
    # print(rows)
    print("\n".join(rows[miny:maxy+3]))


main()

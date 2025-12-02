import sys
sys.setrecursionlimit(10000)

def solve(lines):
    tot = 0
    start = stop = 0
    board = []
    for ind, line in enumerate(lines):
        line = line.strip()
        if ind == 0:
            start = (0, line.index('.'))
        elif ind == len(lines) - 1:
            stop = (len(lines) - 1, line.index('.'))
        board.append(list(line))
    return scenic(board, start, stop)


def scenic(board, start, stop):
    q = [(start, set())]
    m = 0
    while q:
        cur = q.pop(0)
        if cur[0] == stop:
            m = max(m, len(cur[1]))
        next = next_dirs(board, cur[0])
        for n in next:
            if n not in cur[1]:
                temp = cur[1].copy()
                temp.add(n)
                q.append((n, temp))
    return m



def next_dirs(board, cur):
    cur_col = cur[0]
    cur_row = cur[1]
    ans = []
    if board[cur_col][cur_row] == 'v':
        return [(cur_col + 1, cur_row)]
    elif board[cur_col][cur_row] == '<':
        return [(cur_col, cur_row - 1)]
    elif board[cur_col][cur_row] == '>':
        return [(cur_col, cur_row + 1)]
    elif board[cur_col][cur_row] == '^':
        return [(cur_col - 1, cur_row)]
    if cur_row < len(board[0]) - 1 and board[cur_col][cur_row + 1] != '#':
        ans.append((cur_col, cur_row + 1))
    if cur_row > 0 and board[cur_col][cur_row - 1] != '#':
        ans.append((cur_col, cur_row - 1))
    if cur_col < len(board) - 1 and board[cur_col + 1][cur_row] != '#':
        ans.append((cur_col + 1, cur_row))
    if cur_row > 0 and board[cur_col - 1][cur_row] != '#':
        ans.append((cur_col - 1, cur_row))
    return ans


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

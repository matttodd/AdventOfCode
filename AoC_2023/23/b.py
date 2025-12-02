import sys
sys.setrecursionlimit(10000)
from collections import defaultdict

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
    q = [(start, None, 0, set())]
    ints = defaultdict(set)
    dist_to_first = None
    first = None
    dist_to_last = None
    last = None
    while q:
        # print(len(q))
        cur = q.pop(0)
        prev = cur[1]
        step = cur[2] + 1
        temp = cur[3].copy()
        temp.add(cur[0])
        if cur[0] == stop and dist_to_last is None:
            dist_to_last = cur[2] + 1
            last = cur[1]
        # if cur[0] == stop:
        #     m = max(m, len(cur[1]))
        next = next_dirs(board, cur[0])
        if all(board[n[0]][n[1]] != '.' for n in next):
            if cur[1] is not None:
                ints[cur[0]].add((prev, cur[2] + 1))
                ints[prev].add((cur[0], cur[2] + 1))
                if len(ints[cur[0]]) == len(next):
                    continue
            else:
                dist_to_first = cur[2]
                first = cur[0]
            step = 0
            prev = cur[0]
        for n in next:
            if n not in temp:
                q.append((n, prev, step, temp))

    # print(ints)
    print(dist_to_first, dist_to_last)
    print(first, last)

    q = [(first, {first}, dist_to_first)]
    m = 0
    while q:
        # print(q)
        cur = q.pop(0)
        if cur[0] == last:
            m = max(m, cur[2])
            if m == cur[2]:
                print(m)
        for item in ints[cur[0]]:
            # print(item)
            temp = cur[1].copy()
            point = item[0]
            cost = item[1]
            if point not in temp:
                temp.add(point)
                insert_to(q, (point, temp, cur[2] + cost))
    return m + dist_to_last


def insert_to(q, ele):
    for ind, item in enumerate(q):
        if ele[2] // len(ele[1]) > item[2] // len(ele[1]):
            q.insert(ind, ele)
            return
    q.append(ele)



def next_dirs(board, cur):
    cur_col = cur[0]
    cur_row = cur[1]
    ans = []
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

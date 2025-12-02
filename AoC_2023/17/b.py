import sys
sys.setrecursionlimit(10000)

def solve(lines):
    tot = 0
    board = []
    for line in lines:
        board.append(list(map(int, list(line.strip()))))
    tot += shortest(board)
    return tot


def shortest(board):
    # col, row, cost, straight, last
    queue = [(0, 0, 0, 0, None)]
    # happy = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (4, 10), (4, 11), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)]
    been = {}
    ans = None
    while queue:
        cur = queue.pop(0)
        # print(cur)
        cur_col = cur[0]
        cur_row = cur[1]
        cost = cur[2]
        straight = cur[3]
        last_dir = cur[4]
        # path = cur[5]
        # if path == happy[:len(path)]:
        #     print(cur)
        if (cur_col, cur_row, straight, last_dir) in been and been[(cur_col, cur_row, straight, last_dir)] <= cost:
            continue
        been[(cur_col, cur_row, straight, last_dir)] = cost
        if cur_col == len(board) - 1 and cur_row == len(board[0]) - 1:
            if straight < 4:
                continue
            print(cur)
            if ans is None:
                ans = cost
                continue
            else:
                if cost < ans:
                    ans = cost
                    print(cur)
                return ans
                # else:
                #     return ans
        news = next_dirs(board, cur_col, cur_row, cost, straight, last_dir)
        for new in news:
            insert_to_queue(new, queue)
    return ans


def next_dirs(board, cur_col, cur_row, cost, straight, last_dir):
    ans = []
    if last_dir != 'R' and cur_row < len(board[0]) - 1 and ((last_dir == 'L' and straight < 10) or (last_dir != 'L' and straight >= 4) or last_dir is None):# and (cur_col, cur_row + 1) not in path:
        new_s = straight + 1 if last_dir == 'L' else 1
        # temp = path.copy()
        # temp.append((cur_col, cur_row + 1))
        ans.append((cur_col, cur_row + 1, cost + board[cur_col][cur_row + 1], new_s, 'L'))
    if last_dir != 'L' and cur_row > 0 and ((last_dir == 'R' and straight < 10) or (last_dir != 'R' and straight >= 4) or last_dir is None):# and (cur_col, cur_row - 1) not in path:
        new_s = straight + 1 if last_dir == 'R' else 1
        # temp = path.copy()
        # temp.append((cur_col, cur_row - 1))
        ans.append((cur_col, cur_row - 1, cost + board[cur_col][cur_row - 1], new_s, 'R'))
    if last_dir != 'D' and cur_col < len(board) - 1 and ((last_dir == 'U' and straight < 10) or (last_dir != 'U' and straight >= 4) or last_dir is None):# and (cur_col + 1, cur_row) not in path:
        new_s = straight + 1 if last_dir == 'U' else 1
        # temp = path.copy()
        # temp.append((cur_col + 1, cur_row))
        ans.append((cur_col + 1, cur_row, cost + board[cur_col + 1][cur_row], new_s, 'U'))
    if last_dir != 'U' and cur_col > 0 and ((last_dir == 'D' and straight < 10) or (last_dir != 'D' and straight >= 4) or last_dir is None):# and (cur_col - 1, cur_row) not in path:
        new_s = straight + 1 if last_dir == 'D' else 1
        # temp = path.copy()
        # temp.append((cur_col - 1, cur_row))
        ans.append((cur_col - 1, cur_row, cost + board[cur_col - 1][cur_row], new_s, 'D'))
    # print(cur_col, cur_row, cost, straight, last_dir, ans)
    return ans


def insert_to_queue(ele, queue):
    for ind, cur in enumerate(queue):
        if cur[0] == ele[0] and cur[1] == ele[1] and cur[2] <= ele[2] and cur[3] == ele[3] and cur[4] == ele[4]:
            return
        if ele[2] < cur[2]:
            queue.insert(ind, ele)
            return
    queue.append(ele)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

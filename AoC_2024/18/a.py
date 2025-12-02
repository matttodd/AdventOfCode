import sys
# sys.setrecursionlimit(10000)

WIDTH = 70
# WIDTH = 6
def solve(lines):
    board = [['.' for _ in range(WIDTH + 1)] for _ in range(WIDTH + 1)]
    falls = []
    for line in lines:
        line = line.strip()
        x, y = map(int, line.split(','))
        falls.append((x, y))
    return answer(board, falls)


def answer(board, falls):
    initial = set(falls[:1024])
    been = set()
    q = [(0, 0, {(0, 0)})]
    # loc = (0, 0)
    end = (WIDTH, WIDTH)
    while q:
        cur = q.pop(0)
        if (cur[0], cur[1]) == end:
            # print(cur)
            return len(cur[2]) - 1
        if (cur[0], cur[1]) in been:
            continue
        been.add((cur[0], cur[1]))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in dirs:
            newx = cur[0] + d[0]
            newy = cur[1] + d[1]
            if 0 <= newx <= WIDTH and 0 <= newy <= WIDTH:
                if (newx, newy) not in initial:
                    if (newx, newy) not in cur[2]:
                        news = cur[2].copy()
                        news.add((newx, newy))
                        q.append((newx, newy, news))
    return 0


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

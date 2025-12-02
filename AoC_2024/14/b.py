from functools import reduce
import time

width = 103
height = 101

# width = 11
# height = 7

def solve(lines):
    robs = []
    board = [[0 for i in range(height)] for i in range(width)]
    for line in lines:
        p, v = line.strip().split()
        py, px = map(int, p[2:].split(","))
        vy, vx = map(int, v[2:].split(","))
        board[px][py] += 1
        robs.append([px, py, vx, vy])
    return answer(robs, board)


def answer(robs, board):
    c = 0
    while True:
        p = pretty_rob(board, c)
        if "11111111" in p:
            print(p)
            return c
        c += 1
        for i in range(len(robs)):
            r = robs[i]
            # print(r)
            board[r[0]][r[1]] -= 1
            robs[i] = [(r[0] + r[2]) % width, (r[1] + r[3]) % height, r[2], r[3]]
            r = robs[i]
            board[r[0]][r[1]] += 1


    # return q1 * q2 * q3 * q4


def pretty_rob(robs):
    return "\n".join(list(map(lambda x: "".join(map(str, x)).replace("0", " "), robs)))


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

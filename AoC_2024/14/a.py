from functools import reduce

width = 101
height = 103

# width = 11
# height = 7

def solve(lines):
    robs = []
    for line in lines:
        p, v = line.strip().split()
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robs.append([px, py, vx, vy])
    return answer(robs)


def answer(robs):
    finals = []
    q1 = q2 = q3 = q4 = 0
    for r in robs:
        fin = ((r[0] + (100 * r[2])) % width, (r[1] + (100 * r[3])) % height)
        if fin[0] < width // 2 and fin[1] < height // 2:
            q1 += 1
        if fin[0] > width // 2 and fin[1] < height // 2:
            q2 += 1
        if fin[0] < width // 2 and fin[1] > height // 2:
            q3 += 1
        if fin[0] > width // 2 and fin[1] > height // 2:
            q4 += 1
        finals.append(fin)
    print(q1, q2, q3, q4)
    print(finals)

    return q1 * q2 * q3 * q4


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

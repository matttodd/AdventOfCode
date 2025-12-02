import sys
sys.setrecursionlimit(10000)
from itertools import combinations

# mn = 200000000000000
# mx = 400000000000000
mn = 7
mx = 27

def solve(lines):
    hails = []
    for line in lines:
        start, vel = line.strip().split('@')
        start.strip()
        vel.strip()
        x, y, z = map(lambda x: int(x.strip()), start.split(','))
        vx, vy, vz = map(lambda x: int(x.strip()), vel.split(','))
        hails.append(((x, y, z), (vx, vy, vz)))
    all_combos = combinations(hails, 2)
    return count_valid(all_combos)


def intersection(p1, p2, m1, m2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x = (y2 - y1 + m1x1 - m2x2) / (m1 - m2)


def count_valid(all_combos):
    cnt = 0
    for run in all_combos:
        # print(run)
        p1_start = run[0][0]
        p1_vel = run[0][1]
        p2_start = run[1][0]
        p2_vel = run[1][1]
        net_x = p1_start[0] - p2_start[0]
        net_y = p1_start[1] - p2_start[1]
        s1 = p1_vel[1] / p1_vel[0]
        s2 = p2_vel[1] / p2_vel[0]
        # x = (y2 - y1 + m1x1 - m2x2) / (m1 - m2)
        # y = m1(x - x1) - y1
        print(net_x, net_y, net_vx, net_vy)
        # y - y1 = m1(x - x1)
        # y - y2 = m2(x - x2)
        # m1(x - x1) = m2(x - x2) + y2 - y1
        # m1(x - x1) - m2(x - x2) = y2 - y1
        # m1x - m1x1 - m2x + x2m2 = y2 - y1
        # x(m1 - m2) = y2 - y1 + m1x1 - m2x2
    return cnt


def count_valid_ints(all_combos):
    cnt = 0
    for run in all_combos:
        # print(run)
        p1_start = run[0][0]
        p1_vel = run[0][1]
        p2_start = run[1][0]
        p2_vel = run[1][1]
        if p1_vel[0] == p2_vel[0] or p1_vel[1] == p2_vel[1]:
            continue
        tx = -(p1_start[0] - p2_start[0]) / (p1_vel[0] - p2_vel[0])
        ty = -(p1_start[1] - p2_start[1]) / (p1_vel[1] - p2_vel[1])
        # print(tx, ty)
        if tx >= 0 and ty >= 0:
            final_x = p1_start[0] + (tx * p1_vel[0])
            final_y = p1_start[1] + (ty * p1_vel[1])
            if mn <= final_x <= mx and mn <= final_y <= mx:
                print(run)
                print(tx, ty)
                print(final_x, final_y)
                cnt += 1
        # x1 + (t * vx1) = x2 + (t * vx2)
        # x1 - x2 = t (vx2 - vx1)
        # t = (x1 - x2) / (vx2 - vx1)
    return cnt


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

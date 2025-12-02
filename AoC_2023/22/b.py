import sys
sys.setrecursionlimit(10000)
from collections import defaultdict

def solve(lines):
    tot = 0
    bricks = []
    for line in lines:
        start, stop = line.strip().split('~')
        start = list(map(int, start.split(',')))
        stop = list(map(int, stop.split(',')))
        bricks.append((start, stop))
    bricks = sorted(bricks, key=lambda x: x[0][2])
    # board = [[[] for _ in range(10)] for _ in range(10)]
    # print(bricks, board)
    return process(bricks)


def process(bricks):
    leaning = defaultdict(set)
    arranged = []
    for ind, brick in enumerate(bricks):
        z = brick[0][2]
        bs = brick[0]
        be = brick[1]
        land_z = None
        if z == 1:
            arranged.append((brick[0], brick[1], ind))
            continue
        arr_copy = arranged.copy()
        for jnd in range(len(arranged)):
            lower_b = arr_copy[jnd]
            # print(brick, lower_b)
            bs = brick[0]
            be = brick[1]
            lbs = lower_b[0]
            lbe = lower_b[1]

            if land_z is not None and land_z != lbe[2]:
                break
            if not intersects(bs, be, lbs, lbe):
                continue
            else:
                # print(bs, be, lbs, lbe, "INTERSECT")
                if land_z is None:
                    land_z = lbe[2]
                    be[2] = (be[2] - bs[2]) + land_z + 1
                    bs[2] = land_z + 1
                    insert_by(arranged, (bs, be, ind))
                    # bricks[ind] = (bs, be)
                    leaning[ind].add(lower_b[2])
                else:
                    leaning[ind].add(lower_b[2])
        if land_z is None:
            be[2] = (be[2] - bs[2]) + 1
            bs[2] = 1
            insert_by(arranged, (bs, be, ind))
    #     print(arranged)
    # print(leaning)

    ans = set()
    for k, v in leaning.items():
        if len(v) == 1:
            for loc in v:
                ans.add(loc)
    # print(ans)
    # print(leaning)
    m = 0
    for an in ans:
        fall = {an}
        for k, v in leaning.items():
            temp = fall.copy()
            temp = temp.union(v)
            if len(fall) == len(temp):
                fall.add(k)
        m += len(fall) - 1

    return m



def insert_by(source, new):
    for i, ele in enumerate(source):
        if new[1][2] > ele[1][2]:
            source.insert(i, new)
            return
    source.append(new)


def intersects(a, b, c, d):
    rx1 = list(range(a[0], b[0] + 1))
    rx2 = list(range(c[0], d[0] + 1))
    combx = rx1.copy()
    combx.extend(rx2)
    ry1 = list(range(a[1], b[1] + 1))
    ry2 = list(range(c[1], d[1] + 1))
    comby = ry1.copy()
    comby.extend(ry2)
    return (len(rx1) + len(rx2) != len(set(combx))) and (len(ry1) + len(ry2) != len(set(comby)))


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

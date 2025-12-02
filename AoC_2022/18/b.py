from collections import defaultdict
from copy import deepcopy
import sys
sys.setrecursionlimit(10000)


def main():
    print(solve())


def solve():
    total = 0
    points = []
    minx = miny = minz = 100
    maxx = maxy = maxz = 0
    while True:
        try:
            inp = list(map(int, input().split(",")))
            point = (inp[0], inp[1], inp[2])
            minx = min(minx, inp[0])
            maxx = max(maxx, inp[0])
            miny = min(miny, inp[1])
            maxy = max(maxy, inp[1])
            minz = min(minz, inp[2])
            maxz = max(maxz, inp[2])
            # total += 6
            # total -= 2 * num_edges_with_bocks(point, points)
            points.append(point)
        except EOFError:
            minx -= 1
            maxx += 1
            miny -= 1
            maxy += 1
            minz -= 1
            maxz += 1
            # total -= remove_fully_enclosed(points, minx, maxx, miny, maxy, minz, maxz)
            return total_edges((minx, miny, minz), points, minx, maxx, miny, maxy, minz, maxz, set(), 0)


def total_edges(point, points, minx, maxx, miny, maxy, minz, maxz, air, total):
    # print(point, air, total)
    if point in points or point in air:
        return 0
    if point[0] < minx or point[0] > maxx:
        return 0
    if point[1] < miny or point[1] > maxy:
        return 0
    if point[2] < minz or point[2] > maxz:
        return 0
    i = point[0]
    j = point[1]
    k = point[2]
    air.add(point)
    neighbors = [(i - 1, j, k), (i + 1, j, k), (i, j - 1, k), (i, j + 1, k), (i, j, k - 1), (i, j, k + 1)]
    # new_total = total
    for neighbor in neighbors:
        if neighbor in air:
            # print("IS THIS HAPPENING")
            continue
        elif neighbor in points:
            # print("LOOK HERE", neighbor)
            total += 1
        else:
            total += total_edges(neighbor, points, minx, maxx, miny, maxy, minz, maxz, air, 0)
    print(total)
    return total


def num_edges_with_bocks(point, others):
    to_remove = 0
    for existing in others:
        if dist(point, existing) == 1:
            to_remove += 1
    return to_remove


def remove_fully_enclosed(points, minx, maxx, miny, maxy, minz, maxz):
    count = 0
    for i in range(minx, maxx):
        for j in range(miny, maxy):
            for k in range(minz, maxz):
                # if (i - 1, j, k) in points and (i + 1, j, k) in points and \
                #         (i, j - 1, k) in points and (i, j + 1, k) in points and \
                #         (i, j, k - 1) in points and (i, j, k + 1) in points and \
                #         (i, j, k) not in points:
                if is_surrounded((i, j, k), points, minx, maxx, miny, maxy, minz, maxz, []):
                    print(i, j, k)
                    print(num_edges_with_bocks((i,j,k), points))
                    count += (6 - num_edges_with_bocks((i, j, k), points))
    return count


def is_surrounded(point, points, minx, maxx, miny, maxy, minz, maxz, observed):
    if point in points:
        return False
    if point[0] < minx or point[0] > maxx:
        return False
    if point[1] < miny or point[1] > maxy:
        return False
    if point[2] < minz or point[2] > maxz:
        return False
    i = point[0]
    j = point[1]
    k = point[2]
    neighbors = [(i - 1, j, k), (i + 1, j, k), (i, j - 1, k), (i, j + 1, k), (i, j, k - 1), (i, j, k + 1)]
    res = True
    observed.append((i, j, k))
    for neighbor in neighbors:
        if neighbor not in points and neighbor not in observed:
            res = res and is_surrounded(neighbor, points, minx, maxx, miny, maxy, minz, maxz, observed)
    return res


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


main()

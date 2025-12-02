from collections import defaultdict
from copy import deepcopy


def main():
    print(solve())


def solve():
    total = 0
    points = []
    while True:
        try:
            inp = list(map(int, input().split(",")))
            point = (inp[0], inp[1], inp[2])
            total += 6
            total -= 2 * remove_edges(point, points)
            points.append(point)
        except EOFError:
            return total


def remove_edges(point, others):
    to_remove = 0
    for existing in others:
        if dist(point, existing) == 1:
            to_remove += 1
    return to_remove


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

main()

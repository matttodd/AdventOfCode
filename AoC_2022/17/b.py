from collections import defaultdict


def main():
    print(solve())


def solve():
    total = 0
    while True:
        try:
            continue
        except EOFError:
            return total


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


main()

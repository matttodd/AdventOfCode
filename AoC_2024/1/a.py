from functools import reduce


def solve(lines):
    l1 = []
    l2 = []
    for i, line in enumerate(lines):
        n1, n2 = map(int, line.split())
        l1.append(n1)
        l2.append(n2)

    return compare_lists(l1, l2)


def compare_lists(l1, l2):
    l1.sort()
    l2.sort()
    tot = 0
    for n1, n2, in zip(l1, l2):
        tot += abs(n1 - n2)
    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

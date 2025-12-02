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
    tot = 0
    for n1 in l1:
        tot += n1 * l2.count(n1)
    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

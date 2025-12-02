from functools import reduce

def solve(lines):
    tot = 0
    for line in lines:
        start = list(map(int, line.strip().split()))
        tot += recur(start)

    return tot


def recur(l):
    print(l)
    if all(a == 0 for a in l):
        return 0
    new_l = []
    for i in range(1, len(l)):
        new_l.append(l[i] - l[i-1])
    return l[-1] + recur(new_l)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

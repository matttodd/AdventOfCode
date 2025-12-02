from functools import reduce


def solve(lines):
    tot = 0
    runs = lines[0].strip().split(",")
    for run in runs:
        tot += hash(run)
    return tot


def hash(run):
    cur = 0
    for c in run:
        cur += ord(c)
        cur *= 17
        cur = cur % 256
    return cur


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

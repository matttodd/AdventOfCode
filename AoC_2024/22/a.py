import sys
# sys.setrecursionlimit(10000)
from collections import defaultdict


def solve(lines):
    tot = 0
    nums = []
    for line in lines:
        line = line.strip()
        nums.append(int(line))
        tot += answer(int(line))
    return tot


def answer(num):
    for i in range(2000):
        a = num * 64
        num = mix(a, num)
        num = prune(num)

        b = num // 32
        num = mix(b, num)
        num = prune(num)

        c = num * 2048
        num = mix(c, num)
        num = prune(num)
    return num


def mix(a, num):
    return a ^ num


def prune(num):
    return num % 16777216


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

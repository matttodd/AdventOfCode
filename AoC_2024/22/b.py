import sys
# sys.setrecursionlimit(10000)
from collections import defaultdict


def solve(lines):
    tot = 0
    nums = []
    for line in lines:
        line = line.strip()
        nums.append(int(line))
    return answer(nums)


def answer(nums):
    cache = {} # key = (4-tuple) find first occur -9,9
    for i in range(-9, 10):
        for j in range(-9, 10):
            for k in range(-9, 10):
                for l in range(-9, 10):
                    cache[(i, j, k, l)] = 0
    i = 0
    for num in nums:
        i += 1
        cpy = cache.copy()
        win = []
        for i in range(2000):
            t = int(str(num)[-1])
            prev = t
            a = num * 64
            num = mix(a, num)
            num = prune(num)

            b = num // 32
            num = mix(b, num)
            num = prune(num)

            c = num * 2048
            num = mix(c, num)
            num = prune(num)

            n = int(str(num)[-1])
            d = n - prev
            win.append(d)
            if len(win) > 4:
                win.pop(0)
            if len(win) == 4:
                tup = tuple(win)
                if cache[tup] == cpy[tup]:
                    cache[tup] += n
        # print(i)
    return max(cache.values())


def mix(a, num):
    return a ^ num


def prune(num):
    return num % 16777216


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

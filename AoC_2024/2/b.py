from functools import reduce


def solve(lines):
    levels = []
    for i, line in enumerate(lines):
        level = list(map(int, line.split()))
        levels.append(level)

    return is_safe(levels)


def is_safe(levels):
    tot = 0
    for level in levels:
        if check_up(level) or check_down(level):
            tot += 1
            continue
        for i in range(len(level)):
            l = level.copy()
            l.pop(i)
            if check_up(l) or check_down(l):
                tot += 1
                break
    return tot


def check_up(level):
    for n in range(len(level) - 1):
        if 1 <= level[n] - level[n+1] <= 3:
            continue
        else:
            return False
    return True


def check_down(level):
    for n in range(len(level) - 1):
        if 1 <= level[n+1] - level[n] <= 3:
            continue
        else:
            return False
    return True


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

from functools import reduce


def solve(lines):
    levels = []
    for i, line in enumerate(lines):
        levels.append(list(line.strip()))
    # print(levels)
    return answer(levels)


def answer(levels):
    tot = 0
    for i, line in enumerate(levels):
        for j, char in enumerate(line):
            if char == 'A':
                if check_adj(levels, i, j):
                    tot += 1
    return tot


def check_adj(levels, i, j):
    # print(i, j, a, char)
    tot = 0
    ops = [((-1, -1), (1, 1)), ((1, -1), (-1, 1))]
    for op in ops:
        try:
            ni1 = i + op[0][0]
            nj1 = j + op[0][1]
            ni2 = i + op[1][0]
            nj2 = j + op[1][1]
            if ni1 < 0 or nj1 < 0 or ni1 >= len(levels) or nj1 >= len(levels[0]):
                raise IndexError
            c1 = levels[ni1][nj1]
            c2 = levels[ni2][nj2]
            if (c1 == "S" and c2 == "M") or (c1 == "M" and c2 == "S"):
                continue
            else:
                return False
        except IndexError:
            return False
    return True


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

from functools import reduce


def solve(lines):
    levels = []
    tot = 0
    for i, line in enumerate(lines):
        tot += answer(line)

    return tot


def answer(line):
    tot = 0
    for i in range(line.count("mul")):
        start = line.index("mul")
        line = line[start:]
        # print(line)
        try:
            if line[3] == "(":
                close = line.index(")")
                nums = line[4:close]
                n1, n2 = map(int, nums.split(","))
                tot += n1 * n2
                # print(nums)
        except Exception as e:
            line = line[1:]
            continue
        line = line[1:]
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

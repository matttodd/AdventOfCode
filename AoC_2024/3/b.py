from functools import reduce


def solve(lines):
    levels = []
    tot = 0
    all = ""
    for i, line in enumerate(lines):
        all += line

    return answer(all)


def answer(line):
    tot = 0
    does = True
    while "mul" in line:
        # print(line)
        # print(does)
        start = 9999999999
        do = 9999999999
        dont = 9999999999
        if "mul" in line:
            start = line.index("mul")
        if "do" in line:
            do = line.index("do")
        if "don't" in line:
            dont = line.index("don\'t")
        if do < start and do != dont:
            does = True
            line = line[do+1:]
            continue
        elif dont < start:
            does = False
            line = line[dont+1:]
            continue
        if not does:
            line = line[start+1:]
            continue
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


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

from functools import reduce


def solve(lines):
    tot = 0
    runs = lines[0].strip().split(",")
    mp = {i: [] for i in range(256)}
    lb_loc = {}
    for run in runs:
        if '-' in run:
            lb = run[:-1]
            box = hash(lb)
            if lb in mp[box]:
                ind = mp[box].index(lb)
                mp[box].pop(ind)
        else:
            lb, fc = run.split("=")
            box = hash(lb)
            if lb in mp[box]:
                ind = mp[box].index(lb)
                mp[box][ind] = lb
            else:
                mp[box].append(lb)
            lb_loc[(box, lb)] = int(fc)

    # print(lb_loc)
    for box, lenses in mp.items():
        for ind, lens in enumerate(lenses):
            tot += (1 + box) * (1 + ind) * lb_loc[(box, lens)]
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

import math


def solve(lines):
    instr = lines[0].strip()
    starts = []
    l = {}
    r = {}
    for line in lines[2:]:
        s, _, d1, d2 = line.split()
        if s[-1] == "A":
            starts.append(s)
        d1 = d1[1:4]
        d2 = d2[:3]
        l[s] = d1
        r[s] = d2

    z_map = [[] for _ in range(len(starts))]

    locs = starts
    # print(len(starts))
    steps = 0
    while not are_all_zs(locs):
        dir = instr[steps % len(instr)]
        # print(locs)
        steps += 1
        for i, loc in enumerate(locs):
            if dir == "L":
                locs[i] = l[loc]
                if l[loc][-1] == 'Z':
                    is_multiple = False
                    for j in z_map[i]:
                        if steps % j == 0:
                            is_multiple = True
                            break
                    if not is_multiple:
                        z_map[i].append(steps)
            else:
                locs[i] = r[loc]
                if r[loc][-1] == 'Z':
                    is_multiple = False
                    for j in z_map[i]:
                        if steps % j == 0:
                            is_multiple = True
                            break
                    if not is_multiple:
                        z_map[i].append(steps)
        if len(list(filter(lambda x: len(x) == 1, z_map))) == len(z_map):
            return math.lcm(*list(map(lambda x: x[0], z_map)))
    return steps


def are_all_zs(locs):
    for loc in locs:
        if loc[-1] != "Z":
            return False
    return True


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

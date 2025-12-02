
def solve(lines):
    instr = lines[0].strip()
    first = "AAA"
    l = {}
    r = {}
    for line in lines[2:]:
        s, _, d1, d2 = line.split()
        if first is None:
            first = s
        d1 = d1[1:4]
        d2 = d2[:3]
        l[s] = d1
        r[s] = d2

    loc = first
    steps = 0
    print(instr, first, l, r)
    while loc != "ZZZ":
        dir = instr[steps % len(instr)]
        # print(steps, dir, loc)
        steps += 1
        if dir == "L":
            loc = l[loc]
        else:
            loc = r[loc]
    return steps


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

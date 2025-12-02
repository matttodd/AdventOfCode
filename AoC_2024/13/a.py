from functools import reduce


def solve(lines):
    tot = 0
    claws = []
    claw = []
    l = 0
    while lines:
        cur = lines.pop(0)
        cur = cur.strip()
        if cur == "":
            l = 0
            claws.append(claw)
            claw = []
            continue
        if l < 2:
            _, _, x, y = cur.split()
        else:
            _, x, y = cur.split()
        claw.append((int(x[2:-1]), int(y[2:])))
        l += 1
    claws.append(claw)
    print(claws)
    for c in claws:
        tot += answer(c)
    return tot


def answer(claw):
    ax, ay = claw[0]
    bx, by = claw[1]
    dx, dy = claw[2]
    i = 0
    good = None
    cost = None
    while ax * i <= dx:
        j = 0
        while (bx * j) + (ax * i) <= dx and (by * j) + (ay * i) <= dy:
            if (bx * j) + (ax * i) == dx and (by * j) + (ay * i) == dy:
                if cost is not None:
                    cost = min(cost, (i * 3) + j)
                    good = (i, j)
                else:
                    cost = (i * 3) + j
                    good = (i, j)
            j += 1
        i += 1
    print(cost, good)
    return 0 if cost is None else cost


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

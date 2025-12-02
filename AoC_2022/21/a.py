import sys
sys.setrecursionlimit(100000)


def main():
    print(solve())


def solve():
    ops = {}
    resolved = {}
    while True:
        try:
            inp = input().split()
            if len(inp) == 2:
                ops[inp[0][:-1]] = int(inp[1])
                resolved[inp[0][:-1]] = int(inp[1])
            else:
                ops[inp[0][:-1]] = (inp[1], inp[2], inp[3])
        except EOFError:
            return eval_monkey('root', ops, resolved)


def eval_monkey(monkey, ops, resolved):
    if monkey in resolved:
        return resolved[monkey]
    m1, operation, m2 = ops[monkey]
    val1 = eval_monkey(m1, ops, resolved)
    resolved[m1] = val1
    val2 = eval_monkey(m2, ops, resolved)
    resolved[m2] = val2
    if operation == "+":
        return val1 + val2
    elif operation == "-":
        return val1 - val2
    elif operation == "/":
        return val1 // val2
    else:
        return val1 * val2


def wrap(li, inds, leng):
    # print(len(li), len(set(li)))
    for i in range(leng):
        tracking = inds.index(i) # 0 index in li which has the i'th value from the original
        # print(li)
        # print(inds)
        li, inds = swap(li, inds, leng, tracking, li[tracking])
    return li


def swap(li, inds, leng, tracking, x):
    if x == 0:
        return li, inds
    if x < 0:
        # shift left
        if tracking == 0:
            t1 = li[tracking]
            t2 = inds[tracking]
            li[tracking] = li[-1]
            inds[tracking] = inds[-1]
            li[-1] = t1
            inds[-1] = t2
            new_tracking = leng - 1
        else:
            t1 = li[tracking]
            t2 = inds[tracking]
            li[tracking] = li[tracking - 1]
            inds[tracking] = inds[tracking - 1]
            li[tracking - 1] = t1
            inds[tracking - 1] = t2
            new_tracking = tracking - 1
        return swap(li, inds, leng, new_tracking, x + 1)
    if x > 0:
        # shift right
        if tracking == leng - 1:
            t1 = li[tracking]
            t2 = inds[tracking]
            li[tracking] = li[0]
            inds[tracking] = inds[0]
            li[0] = t1
            inds[0] = t2
            new_tracking = 0
        else:
            t1 = li[tracking]
            t2 = inds[tracking]
            li[tracking] = li[tracking + 1]
            inds[tracking] = inds[tracking + 1]
            li[tracking + 1] = t1
            inds[tracking + 1] = t2
            new_tracking = tracking + 1
        return swap(li, inds, leng, new_tracking, x - 1)




def geodes(bp, orbot, cbot, obbot, gbot, ore, clay, obs, geos, orenext, claynext, obsnext, geonext, t):
    # print(orbot, cbot, obbot, gbot, ore, clay, obs, geos, t)
    ore += orbot
    clay += cbot
    obs += obbot
    geos += gbot
    if t == 0:
        if geos > 0:
            print(geos)
        return geos
    options = []
    options.append(geodes(bp, orbot, cbot, obbot, gbot, ore, clay, obs, geos, orenext, claynext, obsnext, geonext, t - 1))
    if bp[0][0] <= ore and orenext:
        options.append(geodes(bp, orbot + 1, cbot, obbot, gbot, ore - bp[0][0], clay, obs, geos, True, False, False, False, t - 1))
        options.append(geodes(bp, orbot + 1, cbot, obbot, gbot, ore - bp[0][0], clay, obs, geos, False, True, False, False, t - 1))
        if cbot:
            options.append(geodes(bp, orbot + 1, cbot, obbot, gbot, ore - bp[0][0], clay, obs, geos, False, False, True, False, t - 1))
        if obbot:
            options.append(geodes(bp, orbot + 1, cbot, obbot, gbot, ore - bp[0][0], clay, obs, geos, False, False, False, True, t - 1))
    if bp[1][0] <= ore and claynext:
        options.append(geodes(bp, orbot, cbot + 1, obbot, gbot, ore - bp[1][0], clay, obs, geos, True, False, False, False, t - 1))
        options.append(geodes(bp, orbot, cbot + 1, obbot, gbot, ore - bp[1][0], clay, obs, geos, False, True, False, False, t - 1))
        if cbot:
            options.append(geodes(bp, orbot, cbot + 1, obbot, gbot, ore - bp[1][0], clay, obs, geos, False, False, True, False, t - 1))
        if obbot:
            options.append(geodes(bp, orbot, cbot + 1, obbot, gbot, ore - bp[1][0], clay, obs, geos, False, False, False, True, t - 1))
    if bp[2][0] <= ore and bp[2][1] <= clay and obsnext:
        options.append(geodes(bp, orbot, cbot, obbot + 1, gbot, ore - bp[2][0], clay - bp[2][1], obs, geos, True, False, False, False, t - 1))
        options.append(geodes(bp, orbot, cbot, obbot + 1, gbot, ore - bp[2][0], clay - bp[2][1], obs, geos, False, True, False, False, t - 1))
        if cbot:
            options.append(geodes(bp, orbot, cbot, obbot + 1, gbot, ore - bp[2][0], clay - bp[2][1], obs, geos, False, False, True, False, t - 1))
        if obbot:
            options.append(geodes(bp, orbot, cbot, obbot + 1, gbot, ore - bp[2][0], clay - bp[2][1], obs, geos, False, False, False, True, t - 1))
    if bp[3][0] <= ore and bp[3][2] <= obs and geonext:
        options.append(geodes(bp, orbot, cbot, obbot, gbot + 1, ore - bp[3][0], clay, obs - bp[2][2], geos, True, False, False, False, t - 1))
        options.append(geodes(bp, orbot, cbot, obbot, gbot + 1, ore - bp[3][0], clay, obs - bp[2][2], geos, False, True, False, False, t - 1))
        if cbot:
            options.append(geodes(bp, orbot, cbot, obbot, gbot + 1, ore - bp[3][0], clay, obs - bp[2][2], geos, False, False, True, False, t - 1))
        if obbot:
            options.append(geodes(bp, orbot, cbot, obbot, gbot + 1, ore - bp[3][0], clay, obs - bp[2][2], geos, False, False, False, True, t - 1))
    # print(options)
    if len(options) > 0:
        return max(options)
    else:
        return geos


main()

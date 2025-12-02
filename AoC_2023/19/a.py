import sys
sys.setrecursionlimit(10000)

def solve(lines):
    tot = 0
    wfs = {}
    xmas = []
    nld = False
    for line in lines:
        cur = line.strip()
        if cur == "":
            nld = True
            continue
        if not nld:
            name, rest = cur.split('{')
            rest = rest[:-1]
            steps = rest.split(',')
            wfs[name] = steps
        else:
            xms = cur[1:-1]
            xms = xms.split(',')
            xmas.append((int(xms[0][2:]), int(xms[1][2:]), int(xms[2][2:]), int(xms[3][2:])))
    print(wfs, xmas)
    tot += energize(wfs, xmas)
    return tot


def energize(wfs, xmas):
    tot = 0
    for xms in xmas:
        tot += follow_wf(wfs, xms, 'in')
    return tot


def follow_wf(wfs, xms, wf):
    for rule in wfs[wf]:
        if rule == 'A':
            return sum(xms)
        elif rule == 'R':
            return 0
        elif '<' in rule:
            eq, res = rule.split(':')
            char, amt = eq.split('<')
            if xms[char_to(char)] < int(amt):
                if res == 'A':
                    return sum(xms)
                elif res == 'R':
                    return 0
                else:
                    return follow_wf(wfs, xms, res)
        elif '>' in rule:
            eq, res = rule.split(':')
            char, amt = eq.split('>')
            if xms[char_to(char)] > int(amt):
                if res == 'A':
                    return sum(xms)
                elif res == 'R':
                    return 0
                else:
                    return follow_wf(wfs, xms, res)
        else:
            return follow_wf(wfs, xms, rule)


def char_to(char):
    if char == 'x':
        return 0
    elif char == 'm':
        return 1
    elif char == 'a':
        return 2
    else:
        return 3


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

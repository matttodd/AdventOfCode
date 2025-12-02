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
    tot += energize(wfs)
    return tot


def energize(wfs):
    tot = 0
    start = [1, 4000, 1, 4000, 1, 4000, 1, 4000, 'in']
    parts = [start]
    ans = []
    while parts:
        print(parts)
        cur = parts.pop(0)
        new_parts = get_parts(wfs, cur, ans)
        if new_parts:
            parts.extend(new_parts)
    print(ans)
    for a in ans:
        tot += (a[1] - a[0] + 1) * (a[3] - a[2] + 1) * (a[5] - a[4] + 1) * (a[7] - a[6] + 1)
    return tot


def get_parts(wfs, cur, ans):
    parts = []
    for rule in wfs[cur[-1]]:
        if rule == 'A':
            ans.append(cur)
            return parts
        elif rule == 'R':
            return parts
        elif '<' in rule:
            eq, res = rule.split(':')
            char, amt = eq.split('<')
            if cur[char_to(char) + 1] < int(amt):
                if res == 'A':
                    ans.append(cur)
                    return parts
                elif res == 'R':
                    return parts
                else:
                    temp = cur.copy()
                    temp[-1] = res
                    parts.append(temp)
                    return parts
            elif cur[char_to(char)] < int(amt):
                c1 = cur.copy()
                c2 = cur.copy()
                c1[char_to(char) + 1] = int(amt) - 1
                c1[-1] = res
                c2[char_to(char)] = int(amt)
                cur = c2
                print(c1, c2)
                if res == 'A':
                    ans.append(c1)
                elif res == 'R':
                    continue
                else:
                    c1[-1] = res
                    parts.append(c1)
        elif '>' in rule:
            eq, res = rule.split(':')
            char, amt = eq.split('>')
            if cur[char_to(char)] > int(amt):
                if res == 'A':
                    ans.append(cur)
                    return parts
                elif res == 'R':
                    return parts
                else:
                    temp = cur.copy()
                    temp[-1] = res
                    parts.append(temp)
                    return parts
            elif cur[char_to(char) + 1] > int(amt):
                c1 = cur.copy()
                c2 = cur.copy()
                c1[char_to(char) + 1] = int(amt)
                c2[char_to(char)] = int(amt) + 1
                c2[-1] = res
                cur = c1
                if res == 'A':
                    ans.append(c2)
                elif res == 'R':
                    continue
                else:
                    c2[-1] = res
                    parts.append(c2)
        else:
            temp = cur.copy()
            temp[-1] = rule
            parts.append(temp)
    return parts


def char_to(char):
    if char == 'x':
        return 0
    elif char == 'm':
        return 2
    elif char == 'a':
        return 4
    else:
        return 6


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

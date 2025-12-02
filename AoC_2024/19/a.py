import sys
import bisect
def solve(lines):
    tot = 0
    towels = lines[0].strip().split(', ')
    designs = []
    for line in lines[2:]:
        line = line.strip()
        design = line
        if answer(towels, design):
            tot += 1
    return tot


def answer(towels, design):
    # print(towels, design)
    q = []
    starting = True
    subs = set()
    while q or starting:
        # print(q)
        if starting:
            cur = ""
        else:
            cur = q.pop(0)
        if cur in subs:
            continue
        subs.add(cur)
        starting = False
        if cur == design:
            print('ya')
            return True
        if len(cur) >= len(design):
            continue
        nxtc = design[len(cur):]
        # print(nxt)
        pos = list(filter(lambda x: nxtc[:len(x)] == x, towels))
        nxt = list(map(lambda x: cur + x, pos))
        nxt = list(filter(lambda x: x not in subs, nxt))
        # print(cur, nxtc, pos, nxt)
        # for p in nxt:
        #     q.append(p)
        q.extend(nxt)
    return False


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

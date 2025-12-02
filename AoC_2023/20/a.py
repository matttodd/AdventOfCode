import sys
sys.setrecursionlimit(10000)

def solve(lines):
    tot = 0
    modules = {}
    ands = []
    for line in lines:
        cur = line.strip()
        lab, res = cur.split('->')
        lab = lab.strip()
        if lab[0] == '%':
            res = res.split(',')
            res = list(map(lambda x: x.strip(), res))
            modules[lab[1:]] = ['%', res, False]
        elif lab[0] == '&':
            res = res.split(',')
            res = list(map(lambda x: x.strip(), res))
            modules[lab[1:]] = ['&', res, []]
            ands.append(lab[1:])
        else:
            res = res.split(',')
            res = list(map(lambda x: x.strip(), res))
            modules['broadcaster'] = ['broadcaster', res]

    for a in ands:
        for k, v in modules.items():
            if a in v[1]:
                modules[a][2].append((False, k))

    high, low = count_pulse(modules)
    print(high, low)
    return high * low


def count_pulse(modules):
    high = low = 0
    cache = {}
    for i in range(1000):
        # initial = modules.copy()
        net_h = 0
        net_l = 0
        # if initial in cache:
        #     high += cache[initial][0]
        #     low += cache[initial][1]
        #     modules = cache[initial][2]
        #     continue
        q = [('low', 'broadcaster', 'button')]
        while q:
            cur = q.pop(0)
            net_h += 1 if cur[0] == 'high' else 0
            net_l += 1 if cur[0] == 'low' else 0
            target = [None]
            if cur[1] in modules:
                target = modules[cur[1]]
            # print(cur)
            # print(target)
            if target[0] == 'broadcaster':
                for t in target[1]:
                    q.append((cur[0], t, cur[1]))
            elif target[0] == '%':
                if cur[0] == 'low':
                    for t in target[1]:
                        if target[2]:
                            q.append(('low', t, cur[1]))
                        else:
                            q.append(('high', t, cur[1]))
                    modules[cur[1]][2] = not modules[cur[1]][2]
            elif target[0] == '&':
                # print(target)
                for ind, pair in enumerate(target[2]):
                    if pair[1] == cur[2]:
                        target[2][ind] = (True if cur[0] == 'high' else False, pair[1])
                        break
                same = True
                for pair in target[2]:
                    same &= pair[0]
                if same:
                    # print("LOW CON")
                    for t in target[1]:
                        q.append(('low', t, cur[1]))
                else:
                    # print("HIGH CON")
                    for t in target[1]:
                        q.append(('high', t, cur[1]))
                # print(target)
            # cache[initial] = (net_h, net_l, modules.copy())
        high += net_h
        low += net_l
        print(net_h, net_l)

    return high, low


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

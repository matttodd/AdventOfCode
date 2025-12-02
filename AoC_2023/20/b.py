import sys
import json
import time
from collections import defaultdict
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

    # configs = 1
    # for k, v in modules.items():
    #     if v[0] == '%':
    #         configs *= 2
    #     elif v[0] == '&':
    #         configs *= len(v[2])

    return count_pulse(modules)


def config(modules):
    conf = []
    for k, v in modules.items():
        if v[0] == '%':
            conf.append([v[2]])
        elif v[0] == '&':
            for pair in v[2]:
                conf.append(pair[0])
    return conf


def apply_config(modules, conf):
    c = 0
    for k, v in modules.items():
        if v[0] == '%':
            v[2] = conf[c]
            c += 1
        elif v[0] == '&':
            for i in range(len(v[2])):
                v[2][i] = (conf[c], v[2][i][1])
                c += 1


def count_pulse(modules):
    rx_l = 0
    rx_h = 0
    cache = defaultdict(list)
    count = 0
    # start = time.time()
    for _ in range(10):
    # while not (rx_l == 1 and rx_h == 0):
        count += 1
        if count % 1_000_000 == 0:
            print(count)
            # end = time.time()
            # print(end - start)
            # start = end
        rx_l = 0
        rx_h = 0
        q = [('low', 'broadcaster', 'button')]
        while q:
            cur = q.pop(0)
            # curfig = config(modules)
            # jsond = json.dumps([q, curfig])
            # if jsond in cache:
            #     apply_config(modules, cache[jsond])
            #     # print("cache hit")
            #     break
            target = [None]
            if cur[1] == 'rx' and cur[0] == 'low':
                rx_l += 1
            if cur[1] == 'rx' and cur[0] == 'high':
                rx_h += 1
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
                for ind, pair in enumerate(target[2]):
                    if pair[1] == cur[2]:
                        target[2][ind] = (True if cur[0] == 'high' else False, pair[1])
                        break
                same = True
                for pair in target[2]:
                    same &= pair[0]
                if same:
                    for t in target[1]:
                        q.append(('low', t, cur[1]))
                else:
                    for t in target[1]:
                        q.append(('high', t, cur[1]))
            # cache[jsond] = curfig
        for k, v in modules.items():
            if v[0] == '&':
                cache[k].append(list(map(lambda x: x[0], v[2])))
            elif v[0] == '%':
                cache[k].append(v[2])
    # print(cache)
    for k,v in cache.items():
        print(f"{k}: with hist: {v}")

    return count


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

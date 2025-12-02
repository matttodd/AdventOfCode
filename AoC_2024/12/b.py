from functools import reduce


def solve(lines):
    tot = 0
    plants = set()
    area = []
    for line in lines:
        r = list(line.strip())
        for c in r:
            plants.add(c)
        area.append(r)
    return answer(area, plants)


def answer(area, plants):
    tot = 0
    counted = set()
    for i, row in enumerate(area):
        for j, v in enumerate(row):
            sha = f"{i}-{j}"
            if sha in counted:
                continue
            a, c, l = fill_region(area, i, j)
            # print(a, c, l)
            counted = counted.union(c)
            sides = march(area, c, l, v)
            tot += a * sides
    return tot


def fill_region(area, i, j):
    v = area[i][j]
    counts = {f"{i}-{j}"}
    locs = []
    to_vis = [(i, j)]
    adjs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while len(to_vis) > 0:
        cur = to_vis.pop(0)
        locs.append(cur)
        for adj in adjs:
            try:
                new_loc = (cur[0] - adj[0], cur[1] - adj[1])
                if new_loc[0] < 0 or new_loc[1] < 0:
                    raise IndexError
                sha = f"{new_loc[0]}-{new_loc[1]}"
                c = area[new_loc[0]][new_loc[1]]
                if c != v:
                    continue
                else:
                    if sha in counts:
                        continue
                    counts.add(sha)
                    to_vis.append(new_loc)
            except IndexError:
                continue
    return len(counts), counts, locs


def march(area, c, l, v):
    # print(c, l, v)
    xs = list(map(lambda x: x[0], l))
    ys = list(map(lambda x: x[1], l))
    minx = min(xs)
    maxx = max(xs)+1
    miny = min(ys)
    maxy = max(ys)+1

    sides = 0
    # top down
    for i in range(minx, maxx):
        cur = area[i][miny:maxy]
        if i > 0:
            prev = area[i - 1][miny:maxy]
        else:
            prev = ["."] * (maxy - miny)
        on_side = False
        for j in range(len(cur)):
            if (cur[j] == v and f"{i}-{miny + j}" in c) and prev[j] != v and not on_side:
                sides += 1
                on_side = True
            else:
                if cur[j] == v and prev[j] != v:
                    continue
                on_side = False
            # print(cur, prev, on_side, sides)
    # print('U', v, sides)

    # bottom up
    for i in range(maxx - 1, minx - 1, -1):
        cur = area[i][miny:maxy]
        if i < len(area) - 1:
            prev = area[i + 1][miny:maxy]
        else:
            prev = ["."] * (maxy - miny)
        on_side = False
        for j in range(len(cur)):
            if (cur[j] == v and f"{i}-{miny + j}" in c) and prev[j] != v and not on_side:
                sides += 1
                on_side = True
            else:
                if cur[j] == v and prev[j] != v:
                    continue
                on_side = False
            # print(cur, prev, on_side, sides)
    # print('D', v, sides)

    # left to right
    for i in range(miny, maxy):
        sub = area[minx:maxx]
        cur = [s[i] for s in sub]
        if i > 0:
            prev = [s[i-1] for s in sub]
        else:
            prev = ["."] * (maxx - minx)
        on_side = False
        for j in range(len(cur)):
            if (cur[j] == v and f"{minx + j}-{i}" in c) and prev[j] != v and not on_side:
                sides += 1
                on_side = True
            else:
                if cur[j] == v and prev[j] != v:
                    continue
                on_side = False
            # print(cur, prev, on_side, sides)
    # print('L', v, sides)

    # right to left
    for i in range(maxy - 1, miny - 1, -1):
        sub = area[minx:maxx]
        cur = [s[i] for s in sub]
        if i < len(area[0]) - 1:
            prev = [s[i+1] for s in sub]
        else:
            prev = ["."] * (maxx - minx)
        on_side = False
        for j in range(len(cur)):
            if (cur[j] == v and f"{minx + j}-{i}" in c) and prev[j] != v and not on_side:
                sides += 1
                on_side = True
            else:
                if cur[j] == v and prev[j] != v:
                    continue
                on_side = False
            # print(cur, prev, on_side, sides)
    # print('R', v, sides)

    # print(v, sides)
    return sides


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

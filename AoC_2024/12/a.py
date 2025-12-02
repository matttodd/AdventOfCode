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
            a, p, c = fill_region(area, i, j)
            print(a, p, c)
            counted = counted.union(c)
            tot += a * p
    return tot


def fill_region(area, i, j):
    p = 0
    v = area[i][j]
    counts = {f"{i}-{j}"}
    to_vis = [(i, j)]
    adjs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while len(to_vis) > 0:
        cur = to_vis.pop(0)
        for adj in adjs:
            try:
                new_loc = (cur[0] - adj[0], cur[1] - adj[1])
                if new_loc[0] < 0 or new_loc[1] < 0:
                    raise IndexError
                sha = f"{new_loc[0]}-{new_loc[1]}"
                c = area[new_loc[0]][new_loc[1]]
                if c != v:
                    p += 1
                    continue
                else:
                    if sha in counts:
                        continue
                    counts.add(sha)
                    to_vis.append(new_loc)
            except IndexError:
                p += 1
                continue
    return len(counts), p, counts





with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

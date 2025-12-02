
def solve(lines):
    min_loc_seed = -1
    min_loc = 9999999
    seeds = list(map(int, lines.pop(0).split(":")[1].split()))
    dicts = []
    while len(lines) > 0:
        cur = lines.pop(0)
        if "map" in cur:
            dicts.append([])
        elif len(cur) > 1:
            dicts[-1].append(list(map(int, cur.split())))

    for conversion in dicts:
        print(seeds)
        for ind, seed in enumerate(seeds):
            is_in_range = False
            for r in conversion:
                if r[1] <= seed < r[1] + r[2] and not is_in_range:
                    print(r, seed)
                    is_in_range = True
                    diff = seed - r[1]
                    seeds[ind] = r[0] + diff

    return min(seeds)

    # return dicts


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

import sys
sys.setrecursionlimit(20000)

def solve(lines):
    seeds = list(map(int, lines.pop(0).split(":")[1].split()))
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i+1]))
    # seed_ranges = seed_ranges[:3]
    dicts = []
    while len(lines) > 0:
        cur = lines.pop(0)
        if "map" in cur:
            dicts.append([])
        elif len(cur) > 1:
            dicts[-1].append(list(map(int, cur.split())))
    anses = []

    for thing in seed_ranges:
        working_range = [thing]
        for conversion in dicts:
            temp_ranges = []
            # shrink = seed_ranges
            for r in conversion:
                # print(seed_ranges)
                temp_shrink = []
                for i in range(len(working_range)):
                    rng = working_range.pop(0)
                    dest_start = r[0]
                    src_start = r[1]
                    conv_range = r[2]
                    seed_start = rng[0]
                    seed_range = rng[1]
                    # print(r, rng)
                    # Entire seed belongs to this conversion
                    if src_start <= seed_start and src_start + conv_range >= seed_start + seed_range:
                        # print("this is outside the seed range")
                        seed_diff = seed_start - src_start
                        # print(seed_diff)
                        # print((dest_start + seed_diff, seed_range))
                        temp_ranges.append((dest_start + seed_diff, seed_range))
                    # This conversion bisects this seed range
                    elif seed_start <= src_start and src_start + conv_range <= seed_start + seed_range:
                        # print("this is in the middle")
                        seed_diff = src_start - seed_start
                        temp_ranges.append((dest_start, conv_range))
                        temp_shrink.append((seed_start, src_start - 1))
                        temp_shrink.append((src_start + conv_range + 1, seed_range - conv_range - seed_diff))
                    # This conversion takes the front portion of this seed range
                    elif src_start < seed_start and src_start + conv_range >= seed_start and src_start + conv_range < seed_start + seed_range:
                        # print("this is at the start")
                        seed_diff = seed_start - src_start
                        temp_ranges.append((dest_start + seed_diff, conv_range - seed_diff))
                        temp_shrink.append((seed_start + conv_range - seed_diff, seed_range - (conv_range - seed_diff)))
                    # This conversion takes the back portion of this seed range
                    elif src_start > seed_start and src_start <= seed_start + seed_range and src_start + conv_range > seed_start + seed_range:
                        # print("this is at the end")
                        seed_diff = src_start - seed_start
                        temp_ranges.append((dest_start, seed_range - seed_diff))
                        temp_shrink.append((seed_start, seed_diff))
                    else:
                        # print("this is disjoint from the seed range")
                        temp_shrink.append((seed_start, seed_range))
                    # print(temp_shrink)
                working_range.extend(temp_shrink)
                print(len(working_range))
            working_range.extend(temp_ranges)
            print(len(working_range))
            # break
        anses.append(min(map(lambda x: x[0], working_range)))
        print(anses)

    return min(anses)


def solve2(lines):
    seeds = list(map(int, lines.pop(0).split(":")[1].split()))
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i+1]))

    dicts = []
    while len(lines) > 0:
        cur = lines.pop(0)
        if "map" in cur:
            dicts.append([])
        elif len(cur) > 1:
            dicts[-1].append(list(map(int, cur.split())))

    ans = []
    # print(dicts)
    # seed_ranges = [seed_ranges[2]]
    for seed_rng in seed_ranges:
        ans.append(run_range(seed_rng, dicts))
        print(ans)
    return min(ans)


cache = set()


def run_range(rng, dicts, depth=0):
    # print(rng, depth)
    if depth == 7:
        # print(rng)
        return rng[0]
    rnd = dicts[depth]
    for ind, r in enumerate(rnd):
        if (rng, (depth, ind)) in cache:
            return 999999999999
        else:
            cache.add((rng, (depth, ind)))
        dest_start = r[0]
        src_start = r[1]
        conv_range = r[2]
        seed_start = rng[0]
        seed_range = rng[1]
        # print(r, rng)
        if src_start <= seed_start and src_start + conv_range >= seed_start + seed_range:
            # print("this is outside the seed range")
            seed_diff = seed_start - src_start
            # print(seed_diff)
            # print((dest_start + seed_diff, seed_range))
            return run_range((dest_start + seed_diff, seed_range), dicts, depth + 1)
        # This conversion bisects this seed range
        elif seed_start <= src_start and src_start + conv_range <= seed_start + seed_range:
            # print("this is in the middle")
            seed_diff = src_start - seed_start
            # print((dest_start, conv_range))
            # print((seed_start, src_start - seed_start))
            # print((src_start + conv_range, seed_range - conv_range - seed_diff))
            pt1 = run_range((dest_start, conv_range), dicts, depth + 1)
            pt2 = run_range((seed_start, src_start - seed_start), dicts, depth)
            pt3 = run_range((src_start + conv_range, seed_range - conv_range - seed_diff), dicts, depth)
            return min(pt1, pt2, pt3)
        # This conversion takes the front portion of this seed range
        elif src_start < seed_start and src_start + conv_range > seed_start and src_start + conv_range < seed_start + seed_range:
            # print("this is at the start")
            seed_diff = seed_start - src_start
            # print((dest_start + seed_diff, conv_range - seed_diff))
            # print((seed_start + conv_range - seed_diff, seed_range - (conv_range - seed_diff)))
            pt1 = run_range((dest_start + seed_diff, conv_range - seed_diff), dicts, depth + 1)
            pt2 = run_range((seed_start + conv_range - seed_diff, seed_range - (conv_range - seed_diff)), dicts, depth)
            return min(pt1, pt2)
        # This conversion takes the back portion of this seed range
        elif src_start > seed_start and src_start < seed_start + seed_range and src_start + conv_range > seed_start + seed_range:
            # print("this is at the end")
            seed_diff = src_start - seed_start
            # print(r, rng, seed_diff)
            # print((dest_start, seed_range - seed_diff))
            # print((seed_start, seed_diff))
            pt1 = run_range((dest_start, seed_range - seed_diff), dicts, depth + 1)
            pt2 = run_range((seed_start, seed_diff), dicts, depth)
            return min(pt1, pt2)
        # else:
            # print("this is disjoint from the seed range")
    return run_range(rng, dicts, depth + 1)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve2(lines))

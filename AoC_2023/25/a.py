import sys
sys.setrecursionlimit(10000)
from itertools import combinations
from collections import defaultdict


def solve(lines):
    comps = defaultdict(list)
    links = []
    beg = None
    for line in lines:
        start, ends = line.strip().split(':')
        if beg is None:
            beg = start
        ends = ends.split()
        for end in ends:
            links.append((start, end))
            comps[start].append(end)
            comps[end].append(start)
    # print(comps)
    return node_merging(comps, [])


def node_merging(comps, merged):
    for source in comps.keys():
        for node, edges in comps.items():
            if source == node or any(source in merge and node in merge for merge in merged):
                continue
            paths = count_paths(comps, merged, source, node, set())
            print(merged)
            print(paths)
            if paths > 3:
                m1 = None
                for merge in merged:
                    if source in merge:
                        m1 = merge
                        break
                m2 = None
                for merge in merged:
                    if node in merge:
                        m2 = merge
                        break
                if m1 is not None and m2 is not None:
                    print(merged)
                    new = m1.union(m2)
                    merged.remove(m1)
                    merged.remove(m2)
                    merged.append(new)
                    print(merged)
                elif m1 is not None:
                    merged[merged.index(m1)].add(node)
                elif m2 is not None:
                    merged[merged.index(m2)].add(source)
                else:
                    merged.append({source, node})
                return node_merging(comps, merged)
    print(comps, merged)
    return len(merged[0]) * len(merged[1])


def count_paths(comps, merged, source, end, been):
    # print(source, end, been)
    if source == end:
        return 1
    edges = []
    for merge in merged:
        if source in merge:
            for n in merge:
                edges.extend(comps[n])
                # for group_edge in comps[n]:
                #     if group_edge not in merge:
                #         edges.append(group_edge)
            break
    if len(edges) == 0:
        edges = comps[source]
    edges = list(set(edges))
    edges = list(filter(lambda x: (source, x) not in been and (x, source) not in been, edges))
    # print(list(edges))
    for edge in edges:
        been.add((source, edge))
    recur = 0
    # print(list(edges))
    for edge in edges:
        # print(merged, edge, end, been)
        recur += count_paths(comps, merged, edge, end, been)
    return recur


def partition(comps, links, beg):
    combos = combinations(links, 3)
    total = len(comps)
    tot_combos = len(list(combos))
    start = beg
    last = 0
    for ind, combo in enumerate(combos):
        if ind // tot_combos != last:
            last = ind // tot_combos
            print(f"{last}% finished")
        combo = set(combo)
        count = bfs(comps, start, combo)
        if count != total:
            print(combo, count, total)
            return count * (total - count)
    return 0


def bfs(comps, start, combo):
    q = [start]
    seen = set()
    while q:
        cur = q.pop(0)
        seen.add(cur)
        connections = comps[cur]
        for conn in connections:
            if conn not in seen and ((cur, conn) not in combo and (conn, cur) not in combo):
                q.append(conn)
    return len(seen)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

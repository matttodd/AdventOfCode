from collections import defaultdict
from copy import deepcopy
from itertools import combinations
import ast


def main():
    print(solve())


def solve():
    LIMIT = 26
    graph = {}
    rates = {}
    while True:
        try:
            inp = input()
            graph = ast.literal_eval(inp)
            inp = input()
            rates = ast.literal_eval(inp)
            # nodes = list(graph.keys())

        except EOFError:
            maxes = find_max(graph, rates, 'AA', LIMIT)
            return find_best_combo(maxes)


def find_best_combo(finals):
    final = 0
    for i in range(len(finals)):
        for j in range(i):
            if len(finals[i][1].intersection(finals[j][1])) == 1:
                if finals[i][0] + finals[j][0] > final:
                    print(finals[i][0] + finals[j][0])
                final = max(final, finals[i][0] + finals[j][0])
    return final


def find_max(graph, rates, start, limit):
    queue = [(start, limit, 0, {start})]
    final = []
    while queue:
        curr = queue.pop(0)
        neighbors = graph[curr[0]]
        any_processed = False
        for neighbor, weight in neighbors.items():
            if neighbor in curr[3] or curr[1] - weight <= 0:
                continue
            else:
                any_processed = True
                new_seen = curr[3].copy()
                new_seen.add(neighbor)
                next_time = curr[1] - weight - 1
                queue.append((neighbor, next_time, curr[2] + (rates[neighbor] * next_time), new_seen))
        if not any_processed:
            final.append((curr[2], curr[3]))
    final.sort(key=lambda x: x[0], reverse=True)
    return final


main()

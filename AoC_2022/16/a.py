from collections import defaultdict
from copy import deepcopy
from itertools import combinations
import ast


def main():
    print(solve())


def solve():
    total = 0
    LIMIT = 30
    graph = {}
    rates = {}
    nodes = []
    # queue = []
    while True:
        try:
            inp = input().split()
            # graph = ast.literal_eval(inp)
            # inp = input()
            # rates = ast.literal_eval(inp)
            # nodes = list(graph.keys())
            name = inp[1]
            nodes.append(name)
            rate = int(inp[4][5:-1])
            neighbors = inp[9:]
            neighbors = list(map(lambda x: {x.replace(",", ""): 1}, neighbors))
            neighbors = {k: v for d in neighbors for k, v in d.items()}
            graph[name] = neighbors
            rates[name] = rate

        except EOFError:
            # print(rates)
            graph = total_distance_graph(graph, nodes, rates, 'AA')
            # print(graph)
            return find_max(graph, rates, 'AA')
            # step (loc, time, total, seen)
            # return


def find_max(graph, rates, start):
    queue = [(start, 30, 0, [start])]
    final = 0
    while queue:
        curr = queue.pop()
        # if curr[2] > 1700:
        #     print(curr)
        neighbors = graph[curr[0]]
        # print(neighbors)
        for neighbor, weight in neighbors.items():
            if neighbor in curr[3]:
                continue
            elif curr[1] - weight <= 0:
                # print(curr)
                final = max(final, curr[2])
                # if len(curr[3]) == 8 and 'YO' in curr[3] and 'IN' in curr[3] and 'HM' in curr[3] and 'LR' in curr[3]:
                #     print(curr[2], curr[1], curr[3])
                # print(final)
            else:
                new_seen = curr[3].copy()
                new_seen.append(neighbor)
                next_time = curr[1] - weight - 1
                queue.insert(0, (neighbor, next_time, curr[2] + (rates[neighbor] * next_time), new_seen))
        final = max(final, curr[2])
        # if len(curr[3]) == 8 and 'YO' in curr[3] and 'IN' in curr[3] and 'HM' in curr[3] and 'LR' in curr[3]:
        #     print(curr[2], curr[1], curr[3])
    return final


def optimal_usage(location, time_remaining, total_flow, open_valves, graph, rates, OG):
    if time_remaining >= 28:
        # print(graph)
        print(location, time_remaining, total_flow, open_valves, graph)
    possible_states = []
    if time_remaining <= 0:
        return total_flow
    for neighbor, weight in graph[location].items():
        # if neighbor not in open_valves:
        possible_states.append((neighbor,
                                time_remaining - weight,
                                total_flow,
                                open_valves,
                                graph))
    if location not in open_valves:
        temp_valves = open_valves.copy()
        temp_valves.append(location)
        edited_graph = remove_from_graph(graph, location)
        possible_states.append((location,
                                time_remaining - 1,
                                total_flow + (rates[location] * (time_remaining - 1)),
                                temp_valves,
                                edited_graph))
    if len(possible_states) > 0:
        # print(possible_states)
        max_val = max(map(lambda x: optimal_usage(x[0], x[1], x[2], x[3], x[4], rates, False), possible_states))
        # print(max_val)
        return max_val
    else:
        return total_flow


def remove_from_graph(graph, location):
    new_graph = deepcopy(graph)
    nodes_to_update = graph[location] # {AA: 1, BB: 2, CC: 3}
    # new_graph.pop(location)
    # print(nodes_to_update)
    for node, weight in nodes_to_update.items():
        replacement_nodes = {n: weight + w for n, w in nodes_to_update.items() if n != node}
        # print(replacement_nodes)
        # return
        for node2, weight2 in replacement_nodes.items():
            if location in new_graph[node]:
                new_graph[node].pop(location)
            if node2 in new_graph[node] and weight2 > new_graph[node][node2]:
                continue
            new_graph[node][node2] = weight2
        # new_graph[node] = (node, weight + location)
    # print(new_graph)
    return new_graph


def total_distance_graph(graph, nodes, rates, start):
    combos = combinations(nodes, 2)
    new_g = defaultdict(dict)
    for combo in combos:
        new_g[combo[0]][combo[1]] = min_path(graph, combo[0], combo[1])
        new_g[combo[1]][combo[0]] = min_path(graph, combo[0], combo[1])
    to_remove = [k for k, v in rates.items() if v == 0]
    to_remove.remove(start)
    for node, weights in new_g.items():
        for node2 in to_remove:
            if node2 in weights:
                weights.pop(node2)
    for node in to_remove:
        new_g.pop(node)
    print(new_g)
    return new_g


def min_path(graph, start, stop):
    queue = [(start, 0)]
    while queue:
        curr = queue.pop()
        location = curr[0]
        for neighbor in graph[location]:
            if neighbor == stop:
                return curr[1] + 1
            queue.insert(0, (neighbor, curr[1] + 1))


main()

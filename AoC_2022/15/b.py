from collections import defaultdict

def main():
    print(solve())


def solve():
    MAX_DEP = 4000000
    locators = []
    beacons = set()
    all_elligible = defaultdict(lambda: 0)
    while True:
        try:
            inp = input().split()
            lx = int(inp[2][2:-1])
            ly = int(inp[3][2:-1])
            bx = int(inp[8][2:-1])
            by = int(inp[9][2:])
            locators.append(((lx, ly), (bx, by)))
            beacons.add((bx, by))
        except EOFError:
            # for i in range(MAX_DEP + 1):
            #     TARGET = i
            is_first = True
            for pair in locators:
                locator = pair[0]
                beacon = pair[1]
                dist_from_beacon = abs(locator[0] - beacon[0]) + abs(locator[1] - beacon[1]) + 1
                elligible = [(locator[0] + x, locator[1] + (x - dist_from_beacon)) for x in range(dist_from_beacon)]
                elligible.extend([(locator[0] - x, locator[1] - (x - dist_from_beacon)) for x in range(dist_from_beacon)])
                elligible.extend([(locator[0] + (x - dist_from_beacon), locator[1] + x) for x in range(dist_from_beacon)])
                elligible.extend([(locator[0] - (x - dist_from_beacon), locator[1] - x) for x in range(dist_from_beacon)])
                elligible = list(filter(lambda x: 0 <= x[0] <= MAX_DEP and 0 <= x[1] <= MAX_DEP, elligible))
                # if locator == (8, 7):
                #     print(elligible)
                #     print(len(elligible))

                for item in elligible:
                    all_elligible[item] += 1

            possible = list(filter(lambda x: x[1] >= 4, all_elligible.items()))
            possible = list(map(lambda x: x[0], possible))
            finals = []
            for poss in possible:
                worked = True
                for pair in locators:
                    locator = pair[0]
                    beacon = pair[1]
                    # if poss == (8, 17):
                    #     print(dist(poss, locator), dist(locator, beacon))
                    if dist(poss, locator) <= dist(locator, beacon):
                        worked = False
                        break
                if worked:
                    finals.append(poss)
            # print(len(possible))

            return finals


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])



main()

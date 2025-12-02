def main():
    print(solve())


def solve():
    locators = []
    beacons = set()
    xvals = set()
    while True:
        try:
            TARGET = 2000000
            inp = input().split()
            lx = int(inp[2][2:-1])
            ly = int(inp[3][2:-1])
            bx = int(inp[8][2:-1])
            by = int(inp[9][2:])
            locators.append(((lx, ly), (bx, by)))
            beacons.add((bx, by))
        except EOFError:
            for pair in locators:
                locator = pair[0]
                beacon = pair[1]
                dist_from_beacon = abs(locator[0] - beacon[0]) + abs(locator[1] - beacon[1])
                dist_from_target = abs(TARGET - locator[1])
                to_traverse = dist_from_beacon - dist_from_target
                if dist_from_target > 0 and to_traverse > 0:
                    # print(locator, beacon, dist_from_beacon, dist_from_target, to_traverse)
                    vals_to_add = [i for i in range(locator[0] - to_traverse, locator[0] + to_traverse)]
                    # print(vals_to_add)
                    for val in vals_to_add:
                        xvals.add(val)
            # print(xvals)
            return len(xvals)




main()

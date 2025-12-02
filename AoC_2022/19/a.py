from itertools import product


def main():
    print(solve())


def solve():
    total = 0
    blueprints = []
    max_ore = []
    max_clay = []
    max_obs = []
    while True:
        try:
            inp = input().split()
            ore_bot = (int(inp[6]), 0, 0)
            clay_bot = (int(inp[12]), 0, 0)
            ob_bot = (int(inp[18]), int(inp[21]), 0)
            geo_bot = (int(inp[27]), 0, int(inp[30]))
            blueprints.append((ore_bot, clay_bot, ob_bot, geo_bot))
            max_ore.append(max(int(inp[6]), int(inp[12]), int(inp[18]), int(inp[27])))
            max_clay.append(int(inp[21]))
            max_obs.append(int(inp[30]))
        except EOFError:
            for ind, bp in enumerate(blueprints):
                geode, orbot, cbot, obbot, gbot = geodes(bp, 1, 0, 0, 0, 0, 0, 0, 0, 24, max_ore[ind], max_clay[ind], max_obs[ind])
                print(geode, orbot, cbot, obbot, gbot)
                total += (ind + 1) * geode
            return total


def geodes(bp, orbot, cbot, obbot, gbot, ore, clay, obs, geos, t, max_ore, max_clay, max_obs):
    # if orbot == 1 and cbot == 4 and obbot == 2 and gbot == 2:
    #     print(orbot, cbot, obbot, gbot, ore, clay, obs, geos, t)
    possible = []
    if t == 0:
        return geos, orbot, cbot, obbot, gbot
    if obs >= bp[3][2] and ore >= bp[3][0]:
        possible.append(geodes(bp, orbot, cbot, obbot, gbot + 1, ore - bp[3][0] + orbot, clay + cbot, obs - bp[3][2] + obbot, geos + gbot, t - 1, max_ore, max_clay, max_obs))
    elif clay >= bp[2][1] and ore >= bp[2][0] and obbot < max_obs:
        possible.append(geodes(bp, orbot, cbot, obbot + 1, gbot, ore - bp[2][0] + orbot, clay - bp[2][1] + cbot, obs + obbot, geos + gbot, t - 1, max_ore, max_clay, max_obs))
    elif ore >= bp[1][0] and cbot < max_clay:
        possible.append(geodes(bp, orbot, cbot + 1, obbot, gbot, ore - bp[1][0] + orbot, clay + cbot, obs + obbot, geos + gbot, t - 1, max_ore, max_clay, max_obs))
    if ore >= bp[0][0] and orbot < max_ore:
        possible.append(geodes(bp, orbot + 1, cbot, obbot, gbot, ore - bp[0][0] + orbot, clay + cbot, obs + obbot, geos + gbot, t - 1, max_ore, max_clay, max_obs))
    possible.append(geodes(bp, orbot, cbot, obbot, gbot, ore + orbot, clay + cbot, obs + obbot, geos + gbot, t - 1, max_ore, max_clay, max_obs))
    return max(possible)


main()

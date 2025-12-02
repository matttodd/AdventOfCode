import sys

sys.setrecursionlimit(100000)


def main():
    print(solve())


def solve():
    walls = set()
    storms = []
    start = None
    end = None
    r = 0
    while True:
        try:
            inp = list(input())
            for i in range(len(inp)):
                if inp.count('#') > 2:
                    if start is None:
                        start = (inp.index('.'), r)
                    else:
                        end = (inp.index('.'), r)
                if inp[i] == '#':
                    walls.add((i, r))
                elif inp[i] == '<':
                    storms.append(('L', i, r))
                elif inp[i] == '>':
                    storms.append(('R', i, r))
                elif inp[i] == '^':
                    storms.append(('U', i, r))
                elif inp[i] == 'v':
                    storms.append(('D', i, r))
            r += 1
        except EOFError:
            mnx = min(walls, key=lambda x: x[0])[0]
            mny = min(walls, key=lambda x: x[1])[1]
            mxx = max(walls, key=lambda x: x[0])[0]
            mxy = max(walls, key=lambda x: x[1])[1]
            print(mnx, mny, mxx, mxy)
            return turns_to_exit(start, storms, walls, 0, end, mnx, mny, mxx, mxy)


def turns_to_exit(curr, blizz, walls, time, end, mnx, mny, mxx, mxy):
    queue = [(curr, time)]
    cache_time = 0
    pos_set = set()
    blizz = advance_blizz(blizz, walls, mnx, mny, mxx, mxy)
    while queue:
        curr = queue.pop(0)
        # print(curr)
        if curr[0] == end:
            return curr[1]
        if curr[1] != cache_time:
            print(curr[1])
            blizz = advance_blizz(blizz, walls, mnx, mny, mxx, mxy)
            cache_time = curr[1]
        eligibles = [(curr[0][0] - 1, curr[0][1]),
                    (curr[0][0], curr[0][1] - 1), (curr[0][0], curr[0][1]), (curr[0][0], curr[0][1] + 1),
                    (curr[0][0] + 1, curr[0][1])]
        blizz_set = set([(b[1], b[2]) for b in blizz])
        for eligible in eligibles:
            if eligible not in walls and eligible not in blizz_set and eligible[1] > -1:
                pos_set.add((eligible, curr[1] + 1))
        if len(queue) == 0:
            queue.extend(list(pos_set))
            pos_set = set()


def advance_blizz(blizz, walls, mnx, mny, mxx, mxy):
    new_blizz = []
    for bliz in blizz:
        if bliz[0] == 'U':
            if bliz[2] - 1 == mny:
                b = (bliz[0], bliz[1], mxy - 1)
            else:
                b = (bliz[0], bliz[1], bliz[2] - 1)
            new_blizz.append(b)
        elif bliz[0] == 'D':
            if bliz[2] + 1 == mxy:
                b = (bliz[0], bliz[1], mny + 1)
            else:
                b = (bliz[0], bliz[1], bliz[2] + 1)
            new_blizz.append(b)
        elif bliz[0] == 'L':
            if bliz[1] - 1 == mnx:
                b = (bliz[0], mxx - 1, bliz[2])
            else:
                b = (bliz[0], bliz[1] - 1, bliz[2])
            new_blizz.append(b)
        elif bliz[0] == 'R':
            if bliz[1] + 1 == mxx:
                b = (bliz[0], mnx + 1, bliz[2])
            else:
                b = (bliz[0], bliz[1] + 1, bliz[2])
            new_blizz.append(b)

    # print(blizz)
    # print(new_blizz)
    return new_blizz


main()

import sys

sys.setrecursionlimit(100000)


def main():
    print(solve())


def solve():
    # locs = set()
    elves = []
    r = 0
    while True:
        try:
            inp = list(input())
            for i in range(len(inp)):
                if inp[i] == '#':
                    # locs.add((i, r))
                    elves.append((i, r))
            r += 1
        except EOFError:
            return anything_moved(elves)
            # mnx, mny, mxx, mxy = find_min_max(final)
            # draw(final, mnx, mny, mxx, mxy)
            # return ((mxx - mnx + 1) * (mxy - mny + 1)) - len(elves)


def find_min_max(elves):
    mnx = min(elves, key=lambda x: x.loc[0]).loc[0]
    mny = min(elves, key=lambda x: x.loc[1]).loc[1]
    mxx = max(elves, key=lambda x: x.loc[0]).loc[0]
    mxy = max(elves, key=lambda x: x.loc[1]).loc[1]
    return mnx, mny, mxx, mxy


def draw(elves, mnx, mny, mxx, mxy):
    board = [['.' for _ in range(mxx - mnx + 1)] for _ in range(mxy - mny + 1)]
    for elf in elves:
        board[elf.loc[1] - mny][elf.loc[0] - mnx] = '#'
    str_board = "\n".join(list(map(lambda x: "".join(x), board)))
    print(str_board)


def anything_moved(elves):
    i = 1
    while True:
        # if i <= 20:
        print(f"Round {i}")
            # mnx, mny, mxx, mxy = find_min_max(elves)
            # draw(elves, mnx, mny, mxx, mxy)
        anything_move = False
        locs = set(elves)
        new_elves = []
        for elf in elves:
            new_elf = get_next_loc(elf, locs, i)
            anything_move = anything_move or new_elf != elf
            new_elves.append(new_elf)
        for ind, elf in enumerate(new_elves):
            locs_to_check = new_elves.copy()
            locs_to_check.remove(elf)
            locs_to_check = set(locs_to_check)
            if elf not in locs_to_check:
                elves[ind] = elf
        if not anything_move:
            return i
        i += 1


def get_next_loc(loc, elves, round):
    # print(round, dir_list(round))
    d_list = dir_list(round)
    if (loc[0] - 1, loc[1] - 1) not in elves and \
            (loc[0] - 1, loc[1]) not in elves and \
            (loc[0] - 1, loc[1] + 1) not in elves and \
            (loc[0], loc[1] - 1) not in elves and \
            (loc[0], loc[1] + 1) not in elves and \
            (loc[0] + 1, loc[1] - 1) not in elves and \
            (loc[0] + 1, loc[1]) not in elves and \
            (loc[0] + 1, loc[1] + 1) not in elves:
        return loc
    for i in range(len(dir_list(round))):
        if d_list[i] == 'N':
            if (loc[0] - 1, loc[1] - 1) not in elves and \
                    (loc[0], loc[1] - 1) not in elves and \
                    (loc[0] + 1, loc[1] - 1) not in elves:
                return loc[0], loc[1] - 1
        if d_list[i] == 'S':
            if (loc[0] - 1, loc[1] + 1) not in elves and \
                    (loc[0], loc[1] + 1) not in elves and \
                    (loc[0] + 1, loc[1] + 1) not in elves:
                return loc[0], loc[1] + 1
        if d_list[i] == 'W':
            if (loc[0] - 1, loc[1] - 1) not in elves and \
                    (loc[0] - 1, loc[1]) not in elves and \
                    (loc[0] - 1, loc[1] + 1) not in elves:
                return loc[0] - 1, loc[1]
        if d_list[i] == 'E':
            if (loc[0] + 1, loc[1] - 1) not in elves and \
                    (loc[0] + 1, loc[1]) not in elves and \
                    (loc[0] + 1, loc[1] + 1) not in elves:
                return loc[0] + 1, loc[1]
    return loc


def dir_list(i):
    orig = ['N', 'S', 'W', 'E']
    offset = (i - 1) % len(orig)
    return orig[offset:] + orig[:offset]


main()

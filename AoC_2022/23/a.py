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
                    elves.append(Elf((i, r)))
            r += 1
        except EOFError:
            final = final_locs(elves, 10)
            mnx, mny, mxx, mxy = find_min_max(final)
            draw(final, mnx, mny, mxx, mxy)
            return ((mxx - mnx + 1) * (mxy - mny + 1)) - len(elves)


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


def final_locs(elves, iterations):
    for i in range(iterations):
        # print(f"Round {i}")
        # mnx, mny, mxx, mxy = find_min_max(elves)
        # draw(elves, mnx, mny, mxx, mxy)
        locs = set([x.loc for x in elves])
        new_elves = []
        for elf in elves:
            new_elf = elf.get_next_loc(locs, i)
            new_elves.append(new_elf)
        for ind, elf in enumerate(new_elves):
            locs_to_check = new_elves.copy()
            locs_to_check.remove(elf)
            locs_to_check = set(map(lambda x: x.loc, locs_to_check))
            if elf.loc not in locs_to_check:
                elves[ind] = elf
            else:
                elves[ind] = Elf(elves[ind].loc)
    return elves


class Elf:
    def __init__(self, loc):
        self.loc = loc

    def __repr__(self):
        return str(self.loc)

    def dir_list(self, i):
        orig = ['N', 'S', 'W', 'E']
        offset = i % len(orig)
        return orig[offset:] + orig[:offset]

    def get_next_loc(self, elves, round):
        # print(round, self.dir_list(round))
        if (self.loc[0] - 1, self.loc[1] - 1) not in elves and \
                (self.loc[0] - 1, self.loc[1]) not in elves and \
                (self.loc[0] - 1, self.loc[1] + 1) not in elves and \
                (self.loc[0], self.loc[1] - 1) not in elves and \
                (self.loc[0], self.loc[1] + 1) not in elves and \
                (self.loc[0] + 1, self.loc[1] - 1) not in elves and \
                (self.loc[0] + 1, self.loc[1]) not in elves and \
                (self.loc[0] + 1, self.loc[1] + 1) not in elves:
            return self
        for i in range(len(self.dir_list(round))):
            if self.dir_list(round)[i] == 'N':
                if (self.loc[0] - 1, self.loc[1] - 1) not in elves and \
                        (self.loc[0], self.loc[1] - 1) not in elves and \
                        (self.loc[0] + 1, self.loc[1] - 1) not in elves:
                    return Elf((self.loc[0], self.loc[1] - 1))
            if self.dir_list(round)[i] == 'S':
                if (self.loc[0] - 1, self.loc[1] + 1) not in elves and \
                        (self.loc[0], self.loc[1] + 1) not in elves and \
                        (self.loc[0] + 1, self.loc[1] + 1) not in elves:
                    return Elf((self.loc[0], self.loc[1] + 1))
            if self.dir_list(round)[i] == 'W':
                if (self.loc[0] - 1, self.loc[1] - 1) not in elves and \
                        (self.loc[0] - 1, self.loc[1]) not in elves and \
                        (self.loc[0] - 1, self.loc[1] + 1) not in elves:
                    return Elf((self.loc[0] - 1, self.loc[1]))
            if self.dir_list(round)[i] == 'E':
                if (self.loc[0] + 1, self.loc[1] - 1) not in elves and \
                        (self.loc[0] + 1, self.loc[1]) not in elves and \
                        (self.loc[0] + 1, self.loc[1] + 1) not in elves:
                    return Elf((self.loc[0] + 1, self.loc[1]))
        return self


main()

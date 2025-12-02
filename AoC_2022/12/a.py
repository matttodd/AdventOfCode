def main():
    print(solve())


def solve():
    elev = []
    bfs = []
    last_print = 0
    seen = set()
    while True:
        try:
            inp = list(input())
        except EOFError:
            start = None
            end = None
            elev.append(['|' for _ in range(len(elev[0]) + 2)])
            # print(elev)
            for i in range(len(elev)):
                for j in range(len(elev[i])):
                    if elev[i][j] == 'S':
                        elev[i][j] = 'a'
                        start = (i, j, 0)
                    elif elev[i][j] == 'E':
                        elev[i][j] = 'z'
                        end = (i, j)
            bfs.insert(0, start)
            seen.add((start[0], start[1]))
            while len(bfs) > 0:
                curr = bfs.pop()
                # print(curr)
                # if curr[2] != last_print:
                #     last_print = curr[2]
                #     print(curr[2])
                #     print(len(seen), len(bfs))
                if curr[0] == end[0] and curr[1] == end[1]:
                    return curr[2]
                curr_elev = elev[curr[0]][curr[1]]
                n_elev = elev[curr[0]][curr[1] - 1]
                if ord(n_elev) <= ord(curr_elev) + 1 and (curr[0], curr[1] - 1) not in seen:
                    seen.add((curr[0], curr[1] - 1))
                    bfs.insert(0, (curr[0], curr[1] - 1, curr[2] + 1))
                s_elev = elev[curr[0]][curr[1] + 1]
                if ord(s_elev) <= ord(curr_elev) + 1 and (curr[0], curr[1] + 1) not in seen:
                    seen.add((curr[0], curr[1] + 1))
                    bfs.insert(0, (curr[0], curr[1] + 1, curr[2] + 1))
                e_elev = elev[curr[0] - 1][curr[1]]
                if ord(e_elev) <= ord(curr_elev) + 1 and (curr[0] - 1, curr[1]) not in seen:
                    seen.add((curr[0] - 1, curr[1]))
                    bfs.insert(0, (curr[0] - 1, curr[1], curr[2] + 1))
                w_elev = elev[curr[0] + 1][curr[1]]
                if ord(w_elev) <= ord(curr_elev) + 1 and (curr[0] + 1, curr[1]) not in seen:
                    seen.add((curr[0] + 1, curr[1]))
                    bfs.insert(0, (curr[0] + 1, curr[1], curr[2] + 1))
            return

        if len(elev) == 0:
            elev.append(['|' for _ in range(len(inp) + 2)])
        inp.insert(0, '|')
        inp.append('|')
        elev.append(inp)


main()

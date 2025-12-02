def main():
    print(solve())


def solve():
    strengths = []
    pixels = ["." for _ in range(240)]
    cur_cycle = 0
    reg = 1
    while True:
        try:
            inp = input().split()
        except EOFError:
            # ans = [strengths[i-1] for i in range(20, len(strengths), 40)]
            # print(ans)
            # print(strengths)
            lists = [print("".join(pixels[40*i:40*(i+1)])) for i in range(6)]

            return
        if len(inp) == 1:
            cur_cycle += 1
            strengths.append(reg * cur_cycle)
            if abs((reg + 1) - (cur_cycle % 40)) <= 1:
                pixels[cur_cycle-1] = "#"
        else:
            cur_cycle += 1
            strengths.append(reg * cur_cycle)
            if abs((reg + 1) - (cur_cycle % 40)) <= 1:
                pixels[cur_cycle-1] = "#"
            cur_cycle += 1
            strengths.append(reg * cur_cycle)
            if abs((reg + 1) - (cur_cycle % 40)) <= 1:
                pixels[cur_cycle-1] = "#"
            reg += int(inp[1])


main()

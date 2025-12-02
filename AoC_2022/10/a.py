def main():
    print(solve())


def solve():
    strengths = []
    cur_cycle = 0
    reg = 1
    while True:
        try:
            inp = input().split()
        except EOFError:
            ans = [strengths[i-1] for i in range(20, len(strengths), 40)]
            # print(ans)
            # print(strengths)
            return sum(ans)
        if len(inp) == 1:
            cur_cycle += 1
            strengths.append(reg * cur_cycle)
        else:
            cur_cycle += 1
            strengths.append(reg * cur_cycle)
            cur_cycle += 1
            strengths.append(reg * cur_cycle)
            reg += int(inp[1])


main()

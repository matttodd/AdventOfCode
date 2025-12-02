
def main():
    print(solve())


def solve():
    stacks = [["Q", "S", "W", "C", "Z", "V", "F", "T"],
              ["Q", "R", "B"],
              ["B", "Z", "T", "Q", "P", "M", "S"],
              ["D", "V", "F", "R", "Q", "H"],
              ["J", "G", "L", "D", "B", "S", "T", "P"],
              ["W", "R", "T", "Z"],
              ["H", "Q", "M", "N", "S", "F", "R", "J"],
              ["R", "N", "F", "H", "W"],
              ["J", "Z", "T", "Q", "P", "R", "B"]]
    count = 0
    while True:
        count += 1
        try:
            inp = input().split()
            num = int(inp[1])
            s1 = int(inp[3])
            s2 = int(inp[5])
        except EOFError:
            return "".join(list(map(lambda x: x[-1], stacks)))
        if count < 5:
            print(stacks[s1-1])
            print(stacks[s2-1])
        temp = stacks[s1-1][-num:]
        temp.reverse()
        if count < 5:
            print(temp)
        stacks[s2-1].extend(temp)
        stacks[s1-1] = stacks[s1-1][:-num]
        if count < 5:
            print(stacks[s1-1])
            print(stacks[s2-1])


main()

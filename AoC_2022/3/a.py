
def main():
    print(solve())


def solve():
    total = 0
    lines = 0
    count = 0
    while True:
        try:
            inp = input()
            lines += 1
        except EOFError:
            print(lines)
            print(count)
            return total
        tracking = set()
        for val in inp[:len(inp) // 2]:
            tracking.add(val)
        for val in inp[len(inp) // 2:]:
            if val in tracking:
                unicode = ord(val)
                print(val, unicode)
                if unicode <= 90:
                    total += unicode - 38
                    count += 1
                    print(unicode - 38)
                else:
                    total += unicode - 96
                    count += 1
                    print(unicode - 96)
                break


main()

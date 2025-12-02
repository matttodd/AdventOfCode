
def main():
    print(solve())


def solve():
    mx = 0
    curr = 0
    while True:
        try:
            next = input()
        except EOFError:
            return mx
        if next == "":
            mx = mx if mx > curr else curr
            curr = 0
        else:
            curr += int(next)


main()

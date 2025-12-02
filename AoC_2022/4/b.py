
def main():
    print(solve())


def solve():
    total = 0
    while True:
        try:
            r1, r2 = input().split(",")
        except EOFError:
            return total
        b1, b2 = map(int, r1.split("-"))
        b3, b4 = map(int, r2.split("-"))
        if (b3 <= b2 and b4 >= b1) or (b2 <= b3 and b1 >= b4):
            print(b1, b2, b3, b4)
            total += 1


main()

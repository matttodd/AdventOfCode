
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
        print(b1, b2, b3, b4)
        if (b1 >= b3 and b2 <= b4) or (b3 >= b1 and b4 <= b2):
            total += 1


main()

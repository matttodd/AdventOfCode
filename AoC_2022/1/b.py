
def main():
    print(solve())


def solve():
    top3 = [0, 0, 0]
    curr = 0
    while True:
        try:
            next = input()
        except EOFError:
            return sum(top3)
        if next == "":
            mn = min(top3)
            ind = top3.index(mn)
            if curr > mn:
                top3[ind] = curr
            curr = 0
        else:
            curr += int(next)


main()


def main():
    print(solve())


def solve():
    ind = 14
    while True:
        try:
            inp = input()
        except EOFError:
            return ind
        curr = inp[ind-14:ind]
        print(curr)
        while len(set(curr)) != 14:
            ind += 1
            curr = inp[ind-14:ind]


main()

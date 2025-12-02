
def main():
    print(solve())


def solve():
    ind = 4
    while True:
        try:
            inp = input()
        except EOFError:
            return ind
        curr = inp[ind-4:ind]
        print(curr)
        while len(set(curr)) != 4:
            ind += 1
            curr = inp[ind-4:ind]


main()

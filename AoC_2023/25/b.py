import sys

sys.setrecursionlimit(100000)


def main():
    print(solve())


def solve():
    total = 0
    snafus = []
    while True:
        try:
            inp = input()
            snafus.append(inp)
        except EOFError:
            return sum(map(lambda x: snafu_to_ten(x), snafus))


def snafu_to_ten(snafu):
    tot = len(snafu)
    total = 0
    for ind, cha in enumerate(snafu):
        val = 0
        place_val = 5**(tot-ind-1)
        if cha == '=':
            val = -2 * place_val
        if cha == '-':
            val = -1 * place_val
        if cha == '1':
            val = place_val
        if cha == '2':
            val = 2 * place_val
        total += val
    return total


def ten_to_snafu(ten):


main()

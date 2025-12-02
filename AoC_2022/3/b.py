from collections import defaultdict


def main():
    print(solve())


def solve():
    total = 0
    while True:
        try:
            inp1 = set(list(input()))
            inp2 = set(list(input()))
            inp3 = set(list(input()))
        except EOFError:
            return total
        tracking = defaultdict(lambda: 0)
        for val in inp1:
            tracking[val] += 1
        for val in inp2:
            tracking[val] += 1
        for val in inp3:
            tracking[val] += 1
        for key, val in tracking.items():
            if val == 3:
                unicode = ord(key)
                if unicode <= 90:
                    total += unicode - 38
                else:
                    total += unicode - 96


main()

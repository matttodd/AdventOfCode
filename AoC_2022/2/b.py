
def main():
    print(solve())


def solve():
    total = 0
    while True:
        try:
            them, you = list(input().split())
        except EOFError:
            return total
        if them == "A" and you == "X":
            total += 3
        elif them == "B" and you == "X":
            total += 1
        elif them == "C" and you == "X":
            total += 2
        if them == "A" and you == "Y":
            total += 4
        elif them == "B" and you == "Y":
            total += 5
        elif them == "C" and you == "Y":
            total += 6
        if them == "A" and you == "Z":
            total += 8
        elif them == "B" and you == "Z":
            total += 9
        elif them == "C" and you == "Z":
            total += 7


main()

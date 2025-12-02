
def main():
    print(solve())


def solve():
    ct = 0
    while True:
        try:
            next = input()
        except EOFError:
            return ct
        num = ""
        for i in next:
            if i.isdigit():
                num += i
                break
        for i in reversed(next):
            if i.isdigit():
                num += i
                # print(num)
                break
        ct += int(num)



main()

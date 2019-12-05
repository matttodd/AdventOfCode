def solve(data):
    sumation = 0
    for num in data:
        sumation += ((num // 3) - 2)
    print(sumation)

def main():
    data = []
    while(True):
        num = input()
        if num is not "":
            data.append(int(num))
        else:
            break

    solve(data)

if __name__ == "__main__":
    main()
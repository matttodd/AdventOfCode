def solve(data):
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        elif data[i] == 99:
            print(data)
            return
        else:
            print("broken")
            return


def main():
    data = input().split(",")
    data = [int(x) for x in data]
    solve(data)

if __name__ == "__main__":
    main()
def solve(data):
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        elif data[i] == 99:
            # print(data)
            return data[0]
        else:
            # print("broken")
            return


def main():
    data = input().split(",")
    data = [int(x) for x in data]
    for i in range(99):
        for j in range(99):
            testdata = data.copy()
            testdata[1] = i
            testdata[2] = j
            if solve(testdata) == 19690720:
                print(100 * i + j)
                break
    print("done")

if __name__ == "__main__":
    main()
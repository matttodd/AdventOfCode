def solve(data):
    sumation = 0
    for num in data:
        sumation += fuel_val(num)
    print(sumation)

def fuel_val(fuel):
    temp = ((fuel // 3) - 2)
    if temp > 0:
        return temp + fuel_val(temp)
    else:
        return 0

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
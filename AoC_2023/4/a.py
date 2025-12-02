
def solve(lines):
    total = 0
    for line in lines:
        _, data = line.split(":")
        winning, yours = data.split("|")
        winning = winning.split()
        yours = yours.split()
        win_set = set(winning)
        winnings = 0
        # print(winning, yours)
        for num in yours:
            if num in win_set:
                winnings += 1
        print(winnings)
        if winnings > 0:
            total += 2**(winnings-1)

    return total


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

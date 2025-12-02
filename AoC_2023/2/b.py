
def solve(lines):
    total = 0
    for line in lines:
        game, stats = line.split(":")
        checks = stats.split(";")
        min_r = 0
        min_g = 0
        min_b = 0
        for check in checks:
            colors = check.split(",")
            for color in colors:
                num, c_word = color.split()
                num = int(num)
                if c_word == "red":
                    min_r = max(num, min_r)
                if c_word == "green":
                    min_g = max(num, min_g)
                if c_word == "blue":
                    min_b = max(num, min_b)
        total += (min_r * min_g * min_b)

    return total


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

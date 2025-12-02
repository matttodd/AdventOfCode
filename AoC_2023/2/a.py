
def solve(lines):
    total = 0
    r_tot = 12
    g_tot = 13
    b_tot = 14
    for line in lines:
        game, stats = line.split(":")
        round = int(game.split()[1])
        checks = stats.split(";")
        failed = False
        for check in checks:
            colors = check.split(",")
            for color in colors:
                num, c_word = color.split()
                num = int(num)
                if c_word == "red" and num > r_tot:
                    failed = True
                if c_word == "green" and num > g_tot:
                    failed = True
                if c_word == "blue" and num > b_tot:
                    failed = True
        if not failed:
            total += round

    return total


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))


def solve(lines):
    tot = 1
    times = list(map(int, lines[0].split(":")[1].split()))
    distances = list(map(int, lines[1].split(":")[1].split()))
    for t, d in zip(times, distances):
        print(t,d)
        winners = 0
        for i in range(t):
            print(i, t - i, i * (t - i))
            if i * (t - i) > d:
                winners += 1
        print(winners)
        tot *= winners

    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

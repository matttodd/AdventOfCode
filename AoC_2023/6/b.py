
def solve(lines):
    tot = 0
    times = lines[0].split(":")[1].split()
    time = int("".join(times))
    distances = lines[1].split(":")[1].split()
    distance = int("".join(distances))
    print(time, distance)
    for t, d in zip([time], [distance]):
        # print(t,d)
        winners = 0
        for i in range(t):
            print(i, t - i, i * (t - i))
            if i * (t - i) > d:
                winners += 1
        # print(winners)
        tot += winners

    return tot


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

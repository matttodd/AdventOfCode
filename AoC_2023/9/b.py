
def solve(lines):
    tot = 0
    for line in lines:
        start = list(map(int, line.strip().split()))
        tot += recur(start)

    return tot


def recur(l):
    print(l)
    has_non_zero = False
    for val in l:
        if val != 0:
            has_non_zero = True
    if not has_non_zero:
        return 0
    new_l = []
    for i in range(1, len(l)):
        new_l.append(l[i] - l[i-1])
    return l[0] - recur(new_l)


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))
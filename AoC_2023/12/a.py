from functools import reduce


def solve(lines):
    tot = 0
    for line in lines:
        arr, runs = line.strip().split()
        runs = list(map(int, runs.split(',')))
        tot += possibilities(arr, runs)
        # print(is_valid(arr, runs))
    return tot


def possibilities(arr, runs):
    gen = [arr]
    count = 0
    while "?" in gen[0]:
        cur = gen.pop(0)
        i = cur.index("?")
        temp = cur
        cur = cur[:i] + "." + cur[i + 1:]
        temp = temp[:i] + "#" + temp[i + 1:]
        gen.append(cur)
        gen.append(temp)

    for g in gen:
        if is_valid(g, runs):
            count += 1
    return count


def is_valid(arr, runs):
    cur = 0
    cnt = 0
    for char in arr:
        if char == "#":
            if cur >= len(runs):
                return False
            cnt += 1
        else:
            if cnt == 0:
                continue
            if runs[cur] != cnt:
                return False
            cnt = 0
            cur += 1
    if cur == len(runs):
        return True
    if runs[cur] == cnt and cur == len(runs) - 1:
        return True
    else:
        return False


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

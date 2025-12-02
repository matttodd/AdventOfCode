from functools import reduce


def solve(lines):
    tot = 0
    for line in lines:
        arr, runs = line.strip().split()
        big_arr = ""
        runs = list(map(int, runs.split(',')))
        big_runs = []
        for i in range(5):
            big_arr += arr
            big_arr += '?'
            big_runs.extend(runs)
        big_arr = big_arr[:-1]
        ans = possibilitiesa(big_arr, big_runs, {}, 0, 0, 0)
        print(big_arr, big_runs, ans)
        tot += ans
        # print(is_valid(arr, runs))
    return tot


def possibilitiesa(arr, runs, cache, arr_i, runs_i, prog):
    # gen = [(0, 0, 0)]
    # count = 0
    max_ar = len(arr)
    max_runs = len(runs)
    # while gen:
    # arr_i, runs_i, prog = gen.pop(-1)
    if (arr_i, runs_i, prog) in cache:
        return cache[(arr_i, runs_i, prog)]
    if arr_i >= max_ar and runs_i >= max_runs:
        cache[(arr_i, runs_i, prog)] = 1
        return 1
    elif arr_i >= max_ar and runs_i == max_runs - 1:
        outcome = 1 if prog == runs[runs_i] else 0
        cache[(arr_i, runs_i, prog)] = outcome
        return outcome
    elif arr_i < max_ar and runs_i >= max_runs:
        if arr[arr_i] in [".", "?"]:
            outcome = possibilitiesa(arr, runs, cache, arr_i + 1, runs_i, prog)
            cache[(arr_i, runs_i, prog)] = outcome
            return outcome
    elif arr_i < max_ar and runs_i < max_runs:
        cur_val = arr[arr_i]
        cur_run = runs[runs_i] - prog
        if cur_val == "." and prog == 0:
            outcome = possibilitiesa(arr, runs, cache, arr_i + 1, runs_i, prog)
            cache[(arr_i, runs_i, prog)] = outcome
            return outcome
        elif cur_val == '.':
            if cur_run != 0:
                cache[(arr_i, runs_i, prog)] = 0
                return 0
            else:
                outcome = possibilitiesa(arr, runs, cache, arr_i + 1, runs_i + 1, 0)
                cache[(arr_i, runs_i, prog)] = outcome
                return outcome
        elif cur_val == "#":
            if cur_run == 0:
                cache[(arr_i, runs_i, prog)] = 0
                return 0
            else:
                outcome = possibilitiesa(arr, runs, cache, arr_i + 1, runs_i, prog + 1)
                cache[(arr_i, runs_i, prog)] = outcome
                return outcome
        else:
            # remaining = reduce(lambda x, y: x + y + 1, runs[runs_i:]) - prog
            # if remaining > max_ar - arr_i:
            #     cache[(arr_i, runs_i, prog)] = 0
            #     return 0
            if cur_run == 0:
                outcome = possibilitiesa(arr, runs, cache, arr_i + 1, runs_i + 1, 0)
                cache[(arr_i, runs_i, prog)] = outcome
                return outcome
            if prog != 0:
                outcome = possibilitiesa(arr, runs, cache, arr_i + 1, runs_i, prog + 1)
                cache[(arr_i, runs_i, prog)] = outcome
                return outcome
            else:
                outcome1 = possibilitiesa(arr, runs, cache, arr_i + 1, runs_i, prog)
                outcome2 = possibilitiesa(arr, runs, cache, arr_i + 1, runs_i, prog + 1)
                cache[(arr_i, runs_i, prog)] = outcome1 + outcome2
                return outcome1 + outcome2
    cache[(arr_i, runs_i, prog)] = 0
    return 0


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

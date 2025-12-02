import sys
import math

sys.setrecursionlimit(100000)


def main():
    print(solve())


def solve():
    snafus = []
    while True:
        try:
            inp = input()
            snafus.append(inp)
        except EOFError:
            base_ten = sum(map(lambda x: snafu_to_ten(x), snafus))
            print(base_ten)
            return ten_to_snafu(base_ten)
            # return ten_to_snafu(20)


def snafu_to_ten(snafu):
    tot = len(snafu)
    total = 0
    for ind, cha in enumerate(snafu):
        val = 0
        place_val = 5**(tot-ind-1)
        if cha == '=':
            val = -2 * place_val
        if cha == '-':
            val = -1 * place_val
        if cha == '1':
            val = place_val
        if cha == '2':
            val = 2 * place_val
        total += val
    return total


def ten_to_snafu(ten):
    count = 0
    running = ["0" for _ in range(math.ceil(math.log(ten)))]
    i = 1
    while abs(((5**i) // 2) + 1) < abs(ten):
        i += 1
    i = i-1
    first = ((5**i) // 2) + 1
    if ten > 0:
        ten -= 5**i
        next = 1
        if ten >= first:
            ten -= 5**i
            next = 2
    else:
        ten += 5**i
        next = -1
        if ten <= first:
            ten += 5**i
            next = -2
    if next == 2:
        running[-i-1] = '2'
    if next == 1:
        running[-i-1] = '1'
    for j in range(i-1, -1, -1):
        # print(running, ten, j)
        per_unit = 5**j
        val = (ten + (5**j // 2)) // per_unit
        ten -= per_unit * val
        if val == 2:
            running[-j-1] = '2'
        if val == 1:
            running[-j-1] = '1'
        if val == 0:
            running[-j-1] = '0'
        if val == -1:
            running[-j-1] = '-'
        if val == -2:
            running[-j-1] = '='
    while running[0] == '0':
        running = running[1:]
    return "".join(running)


# def ten_to_snafu(ten):
#     total = "0"
#     if ten == 0:
#         return '0'
#     while ten != 0:
#         # print(ten, total)
#         total = snafu_add_one(total)
#         ten -= 1
#
#     return total
#
#
# def snafu_add_one(snafu):
#     if snafu == '':
#         return '1'
#     for i in range(1, len(snafu)+1):
#         if snafu[-i] == '=':
#             # snafu[-i] = '-'
#             snafu = snafu[:-i] + '-' + (snafu[-i+1:] if i > 1 else '')
#             break
#         if snafu[-i] == '-':
#             # snafu[-i] = '0'
#             snafu = snafu[:-i] + '0' + (snafu[-i+1:] if i > 1 else '')
#             break
#         if snafu[-i] == '0':
#             # snafu[-i] = '1'
#             snafu = snafu[:-i] + '1' + (snafu[-i+1:] if i > 1 else '')
#             break
#         if snafu[-i] == '1':
#             # snafu[-i] = '2'
#             snafu = snafu[:-i] + '2' + (snafu[-i+1:] if i > 1 else '')
#             break
#         if snafu[-i] == '2':
#             return snafu_add_one(snafu[:-i]) + '=' + (snafu[-i+1:] if i > 1 else '')
#     return snafu


main()

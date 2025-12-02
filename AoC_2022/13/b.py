import ast
from functools import cmp_to_key


def main():
    print(solve())


def solve():
    worked = []
    left = []
    right = []
    while True:
        left_pair = ast.literal_eval(input())
        right_pair = ast.literal_eval(input())
        try:
            input()
        except EOFError:
            left.append(left_pair)
            right.append(right_pair)
            ind = 0
            left.extend(right)
            std = sorted(left, key=cmp_to_key(right_order))
            return (std.index([[2]]) + 1) * (std.index([[6]]) + 1)

        left.append(left_pair)
        right.append(right_pair)


def right_order(l, r):
    print(l, r)
    if type(l) == int:
        if type(r) == int:
            if l < r:
                return -1
            elif l > r:
                return 1
            else:
                return None
        else:
            return right_order([l], r)
    else:
        if type(r) == int:
            return right_order(l, [r])
        else:
            if len(l) == 0 and len(r) != 0:
                return -1
            elif len(l) != 0 and len(r) == 0:
                return 1
            elif len(l) == len(r) == 0:
                return None
            else:
                if right_order(l[0], r[0]) is None:
                    return right_order(l[1:], r[1:])
                else:
                    return right_order(l[0], r[0])


main()

import ast


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
            ind = 0
            for l, r in zip(left, right):
                ind += 1
                if right_order(l, r):
                    print(str(ind) + "WORKED")
                    worked.append(ind)
            print(worked)
            return sum(worked)

        left.append(left_pair)
        right.append(right_pair)


def right_order(l, r):
    # print(l, r)
    if type(l) == int:
        if type(r) == int:
            return l < r if l != r else None
        else:
            return right_order([l], r)
    else:
        if type(r) == int:
            return right_order(l, [r])
        else:
            if len(l) == 0 and len(r) != 0:
                return True
            elif len(l) != 0 and len(r) == 0:
                return False
            elif len(l) == len(r) == 0:
                return None
            else:
                if right_order(l[0], r[0]) is None:
                    return right_order(l[1:], r[1:])
                else:
                    return right_order(l[0], r[0])

main()

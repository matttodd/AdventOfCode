import sys
sys.setrecursionlimit(100000)

def main():
    print(solve())


def solve():
    li = []
    key = 811589153
    while True:
        try:
            inp = int(input())
            li.append(inp)
        except EOFError:
            leng = len(li)
            inds = list(range(leng))
            li = list(map(lambda x: x * key, li))
            # print(li)
            final = wrap(li, inds, leng)
            # print(final)
            for i in range(9):
                final = wrap(final, inds, leng)
                # print(final)
            zero = final.index(0)
            return final[(1000 + zero) % leng] + final[(2000 + zero) % leng] + final[(3000 + zero) % leng]


def wrap(li, inds, leng):
    # print(len(li), len(set(li)))
    for i in range(leng):
        tracking = inds.index(i) # 0 index in li which has the i'th value from the original
        # print(li)
        # print(inds)
        li, inds = swap(li, inds, leng, tracking, li[tracking])
    return li


def swap(li, inds, leng, tracking, x):
    if x == 0:
        return li, inds
    if abs(x) > leng:
        if x < 0:
            x = -(abs(x) % (leng - 1))
        else:
            x = x % (leng - 1)
    if x < 0:
        # shift left
        if tracking == 0:
            t1 = li[tracking]
            t2 = inds[tracking]
            li[tracking] = li[-1]
            inds[tracking] = inds[-1]
            li[-1] = t1
            inds[-1] = t2
            new_tracking = leng - 1
            new_x = x + 1
        else:
            t1 = li[tracking]
            t2 = inds[tracking]
            li[tracking] = li[tracking - 1]
            inds[tracking] = inds[tracking - 1]
            li[tracking - 1] = t1
            inds[tracking - 1] = t2
            new_tracking = tracking - 1
            new_x = x + 1
        return swap(li, inds, leng, new_tracking, new_x)
    if x > 0:
        # shift right
        if tracking == leng - 1:
            t1 = li[tracking]
            t2 = inds[tracking]
            li[tracking] = li[0]
            inds[tracking] = inds[0]
            li[0] = t1
            inds[0] = t2
            new_tracking = 0
            new_x = x - 1
        else:
            t1 = li[tracking]
            t2 = inds[tracking]
            li[tracking] = li[tracking + 1]
            inds[tracking] = inds[tracking + 1]
            li[tracking + 1] = t1
            inds[tracking + 1] = t2
            new_tracking = tracking + 1
            new_x = x - 1
        return swap(li, inds, leng, new_tracking, new_x)


main()

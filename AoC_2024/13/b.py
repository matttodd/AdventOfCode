from functools import reduce
from math import isclose
import numpy as np


def solve(lines):
    tot = 0
    claws = []
    claw = []
    l = 0
    while lines:
        cur = lines.pop(0)
        cur = cur.strip()
        if cur == "":
            l = 0
            claws.append(claw)
            claw = []
            continue
        if l < 2:
            _, _, x, y = cur.split()
            x = int(x[2:-1])
            y = int(y[2:])
        else:
            _, x, y = cur.split()
            x = int(x[2:-1])
            y = int(y[2:])
            # x += 10000000000000
            # y += 10000000000000
        claw.append((x, y))
        l += 1
    claws.append(claw)
    print(len(claws))
    x = 0
    for c in claws:
        q = answer3(c)
        if q != 0:
            continue
        z = answer3([c[0], c[1], (c[2][0] + 10000000000000, c[2][1] + 10000000000000)])
        if z != 0:
            x += 1
        tot += z
    print(x)
    return tot


def answer(claw):
    ax, ay = claw[0]
    bx, by = claw[1]
    dx, dy = claw[2]
    i = 0
    good = None
    cost = None
    while ax * i <= dx:
        j = 0
        while (bx * j) + (ax * i) <= dx and (by * j) + (ay * i) <= dy:
            if (bx * j) + (ax * i) == dx and (by * j) + (ay * i) == dy:
                if cost is not None:
                    cost = min(cost, (i * 3) + j)
                    good = (i, j)
                else:
                    cost = (i * 3) + j
                    good = (i, j)
            j += 1
        i += 1
    # print(cost, good)
    return good, 0 if cost is None else good, cost


def answer3(claw):
    a, b = claw[0]
    d, e = claw[1]
    c, f = claw[2]

    A = np.array([[a, d], [b, e]])
    B = np.array([c, f])
    # other_ans = answer(claw)
    try:
        X = np.linalg.solve(A, B)
        i = X[0]
        j = X[1]
        # print(i, j)
        # print(other_ans) # 151691881603924
        if isclose(i, round(i), abs_tol=1e-9) and isclose(j, round(j), abs_tol=1e-9) and\
                i >= 0 and j >= 0:
            # if other_ans[0] != (int(i), int(j)):
            #     print("diff", other_ans[0], (int(i), int(j)))
            return (round(i) * 3) + round(j)
        else:#if other_ans[0] != None:
            # print("far or neg", other_ans[0], (int(i), int(j)))
            return 0
    except np.linalg.LinAlgError:
        # if other_ans[0] != None:
            # print("err", other_ans[0])
        return 0


def answer2(claw):
    ax, ay = claw[0]
    bx, by = claw[1]
    dx, dy = claw[2]
    dfx = ax - bx # +
    dfy = ay - by # -
    # overshoot as cheaply as possible
    i = imin = 0
    imax = min((dx // ax) + 1, (dy // ay) + 1)
    jmin = 0
    j = jmax = min((dx // bx) + 1, (dy // by) + 1)
    if ax / bx == ay / by:
        print("UH OH", claw)

    while (((bx * j) + (ax * i)) != dx) or (((by * j) + (ay * i)) != dy):
        prev_i = i
        prev_j = j
        cx = (bx * j) + (ax * i)
        cy = (by * j) + (ay * i)
        diffx = dx - cx
        diffy = dy - cy
        # print(diffx, diffy)
        if (diffx < 0 and diffy < 0) or (abs(diffx) > dx * 1000) or (abs(diffy) > dy * 1000):
            print(0)
            return 0
        if diffx > diffy:
            more_a = max(1, (diffx // ax))
            less_b = min(j, (((more_a * ay)-diffy) // by))
            i += more_a
            j -= less_b
        elif diffy > diffx:
            more_a = max(1, (diffy // ay))
            less_b = min(j, (((more_a * ax)-diffx) // bx))
            i += more_a
            j -= less_b
        else:
            print(0)
            return 0

        cx = (bx * j) + (ax * i)
        cy = (by * j) + (ay * i)
        diffx = dx - cx
        diffy = dy - cy
        print(diffx, diffy, more_a, less_b, i, j)
        if prev_i == i and prev_j == j:
            print(0)
            return 0

    print((i * 3) + j)
    return (i * 3) + j


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

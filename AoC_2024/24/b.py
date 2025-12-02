import sys
sys.setrecursionlimit(10000)
from collections import defaultdict
from functools import reduce

COUNT = 45
BOUND = 2**COUNT-1
HALF = 2**(COUNT//2)-1


def solve(lines):
    vals = {}
    board = []
    for i in range(len(lines)):
        line = lines.pop(0).strip()
        if line == "":
            break
        l, n = line.split()
        vals[l[:-1]] = int(n)
    for i in range(len(lines)):
        line = lines.pop(0).strip()
        x, op, y, _, out = line.split()
        board.append((x, y, op, out))
    return answer(vals, board)


def get_with(x, y, op, board):
    for b in board:
        if x in b and y in b and op in b:
            return b[3]
    # print(x, y, op)


def answer(vals, board):
    swaps = [('z16', 'hmk'), ('z20', 'fhp'), ('rvf', 'tpc'), ('z33', 'fcd')]
    for swap in swaps:
        for i, b in enumerate(board):
            if b[3] == swap[0]:
                temp = board.pop(i)
                board.insert(i, (temp[0], temp[1], temp[2], swap[1]))
            if b[3] == swap[1]:
                temp = board.pop(i)
                board.insert(i, (temp[0], temp[1], temp[2], swap[0]))

    did_carry = None
    for i in range(1, COUNT+1):
        # kxpp = "x" + str(i-2).zfill(2)
        # kypp = "y" + str(i-2).zfill(2)
        # kzpp = "z" + str(i-2).zfill(2)
        kxp = "x" + str(i-1).zfill(2)
        kyp = "y" + str(i-1).zfill(2)
        kzp = "z" + str(i-1).zfill(2)
        kx = "x" + str(i).zfill(2)
        ky = "y" + str(i).zfill(2)
        kz = "z" + str(i).zfill(2)
        cur = get_with(kx, ky, 'XOR', board)
        rem = get_with(kxp, kyp, 'AND', board)
        p_xor = get_with(kxp, kyp, 'XOR', board)
        carrying_through = get_with(p_xor, did_carry, 'AND', board)
        will_carry = get_with(carrying_through, rem, 'OR', board) if did_carry is not None else rem
        final = get_with(will_carry, cur, 'XOR', board)
        did_carry = will_carry
        print(i, cur, rem, p_xor, carrying_through, will_carry, final)


    # x = 15
    # y = 15
    # xbin = str(bin(x))[2:].zfill(COUNT)
    # ybin = str(bin(y))[2:].zfill(COUNT)

    # new_vals = populate(x, y, vals.copy())
    # fin = simulate(new_vals, board.copy())
    # finbin = str(bin(fin))[2:].zfill(COUNT)
    # print(fin, finbin, xbin, ybin)


    dps = depends(board)
    print(dps['z00'], dps['z01'], dps['z02'], dps['z03'])
    # print(vals, board)
    # probs = problem_bits(vals, board)
    # min_prob = min(probs, key=probs.get)
    # print(probs, len(probs), min_prob, probs[min_prob], dps[min_prob])
    # new_dps = defaultdict(set)
    # for m in range(COUNT):
    #     k = str(m).zfill(2)
    #     for b in board:
    #         if k in b[0] or k in b[1] or k in b[3]:
    #             new_dps[k].add(b)
    # print(new_dps)

    # ors = []
    # ands = []
    # xors = []
    # for b in board:
    #     if 'OR' in b and ('z' in b[3] or 'x' in b[0] or 'y' in b[1]):
    #         ors.append(b)
    #     if 'AND' in b and ('z' in b[3]):
    #         ands.append(b)
    #     if 'XOR' in b and 'z' not in b[3] and 'x' not in b[0] and 'x' not in b[1]:
    #         xors.append(b)
    # print('ORS', ors)
    # print('ANDS', ands)
    # print('XORS', xors)

    # for i in range(COUNT): # z16
    #     kx = "x" + str(i).zfill(2)
    #     ky = "y" + str(i).zfill(2)
    #     kz = "z" + str(i).zfill(2)
    #     for b in board: # rsq qkj, spt cpf, qkp tkj, fnv jhb, gvh mch, wjq dsw
    #         if kx in b and ky in b and kz in b:
    #             print("xy", b)
            # if kz in b:
            #     print("z", b)
    #     k = "z" + str(COUNT - i - 1).zfill(2)
    #     print(k, probs[k])
    # print(dps["z16"])
    # for k, v in dps.items():
    #     print(k, len(v))
    # items = list(probs.items())
    # items.sort(key=lambda x: x[1], reverse=True)
    # print(items)
    # z00 <-> z20
    all = map(lambda x: list(x), swaps)
    all = list(reduce(lambda x, y: x + y, all))
    all.sort()
    return ','.join(all)


def problem_bits(vals, board):
    probs = defaultdict(lambda: 0)
    v = vals.copy()
    b = board.copy()
    for i in range(COUNT+1):
        for j in range(COUNT+1):
            x = 2**i-1
            y = 2**j-1
            xbin = str(bin(x))[2:].zfill(COUNT)
            ybin = str(bin(y))[2:].zfill(COUNT)
            # print(xbin, ybin)
            v = populate(x, y, v)
            fin = simulate(v.copy(), b.copy())
            finbin = str(bin(fin))[2:].zfill(COUNT)
            res = x & y
            resbin = str(bin(res))[2:].zfill(COUNT)
            for k in range(COUNT):
                if finbin[k] != resbin[k]:
                    probs["z" + str(COUNT - k - 1).zfill(2)] += 1
    return probs


def depends(board):
    deps = defaultdict(set)
    zdeps = defaultdict(set)
    zs = []
    for b in board:
        x, y, op, out = b
        deps[out].add(x)
        deps[out].add(y)
        if out[0] == 'z':
            zdeps[out].add(x)
            zdeps[out].add(y)
            zs.append(out)

    def add_to(zdps, dps, z, t):
        if t != z:
            zdps[z].add(t)
        for i in dps[t]:
            add_to(zdps, dps, z, i)
    for z in zs:
        add_to(zdeps, deps, z, z)
    return zdeps


def populate(x, y, vals):
    xbin = str(bin(x))[2:].zfill(COUNT)
    ybin = str(bin(y))[2:].zfill(COUNT)
    for i in range(COUNT):
        kx = "x" + str(i).zfill(2)
        ky = "y" + str(i).zfill(2)
        vals[kx] = int(xbin[COUNT-1-i])
        vals[ky] = int(ybin[COUNT-1-i])
    return vals


def simulate(vals, og_board):
    # print(vals, board)
    board = og_board.copy()
    zs = []
    while len(board) != 0:
        x, y, op, out = board.pop(0)
        if x in vals and y in vals:
            if op == 'AND':
                vals[out] = vals[x] & vals[y]
            elif op == 'OR':
                vals[out] = vals[x] | vals[y]
            elif op == 'XOR':
                vals[out] = vals[x] ^ vals[y]
            if out[0] == 'z':
                zs.append((int(out[1:]), vals[out]))
        else:
            board.append((x, y, op, out))
    zs.sort()
    zs.reverse()
    nums = map(lambda x: str(x[1]), zs)
    n = "".join(nums)
    n = int(n, 2)
    return n


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

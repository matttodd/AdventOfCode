import sys
# sys.setrecursionlimit(10000)

def solve(lines):
    pgm = list(map(int, lines[4].strip().split()[1].split(",")))
    return answer(pgm)


def answer(pgm):
    goal = pgm.copy()
    goal.reverse()
    lb = 1
    ub = 8
    i = 0
    for res in goal:
        i+=1
        # print(res, lb, ub)
        for oga in range(lb, ub):
            # print(oga)
            rega = oga
            regb = 0
            regc = 0
            pointer = 0
            my_res = []
            g = pgm[len(pgm)-i:]
            while True:
                try:
                    code = pgm[pointer]
                    operand = pgm[pointer+1]
                    rega, regb, regc, pointer, out = instr(rega, regb, regc, code, operand, pointer)
                    # print(rega, regb, regc, code, operand, out)
                    if out is not None:
                        my_res.append(out)
                        if my_res != g[:len(my_res)]:
                            break
                except IndexError:
                    break
            if my_res == g:
                # print(my_res, g)
                if len(g) == len(pgm):
                    return oga
                lb = (oga * 8)
                ub = (oga * 9)
                break


def instr(rega, regb, regc, code, operand, pointer):
    c = pointer
    out = None
    if code == 0:
        rega = rega // (2**combo(rega, regb, regc, operand)) # to A
    elif code == 1:
        regb = regb ^ operand # in B
    elif code == 2:
        regb = combo(rega, regb, regc, operand) % 8 # in B
    elif code == 3:
        if rega != 0:
            pointer = operand
    elif code == 4:
        regb = regb ^ regc # in B
    elif code == 5:
        out = combo(rega, regb, regc, operand) % 8 # out
    elif code == 6:
        regb = rega // (2**combo(rega, regb, regc, operand)) # to B
    elif code == 7:
        regc = rega // (2**combo(rega, regb, regc, operand)) # to C
    if c == pointer:
        pointer += 2
    return rega, regb, regc, pointer, out


def combo(rega, regb, regc, operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return rega
    elif operand == 5:
        return regb
    elif operand == 6:
        return regc
    else:
        return None

with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

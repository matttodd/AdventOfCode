import sys
# sys.setrecursionlimit(10000)

def solve(lines):
    rega = int(lines[0].strip().split()[-1])
    regb = int(lines[1].strip().split()[-1])
    regc = int(lines[2].strip().split()[-1])
    pgm = list(map(int, lines[4].strip().split()[1].split(",")))
    # print(pgm)
    return answer(rega, regb, regc, pgm)


def answer(rega, regb, regc, pgm):
    tot = []
    pointer = 0
    while True:
        try:
            code = pgm[pointer]
            operand = pgm[pointer+1]
            rega, regb, regc, pointer, out = instr(rega, regb, regc, code, operand, pointer)
            print(rega, regb, regc, code, operand, pointer, out, tot)
            if out is not None:
                tot.append(out)
        except IndexError:
            break
    return ",".join(map(str, tot))


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

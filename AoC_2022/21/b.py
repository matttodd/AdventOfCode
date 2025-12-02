import sys
sys.setrecursionlimit(100000)


def main():
    print(solve())


def solve():
    ops = {}
    resolved = {}
    needs_humn = set()
    while True:
        try:
            inp = input().split()
            if len(inp) == 2:
                ops[inp[0][:-1]] = int(inp[1])
                resolved[inp[0][:-1]] = int(inp[1])
            else:
                ops[inp[0][:-1]] = (inp[1], inp[2], inp[3])
        except EOFError:
            # m1, _, m2 = ops['root']
            populate_needs_humn('root', needs_humn, ops)
            eval_monkey('root', ops, resolved, needs_humn)
            # print(needs_humn)
            # print(resolved)
            return eval_inverse('root', resolved, 0)


def eval_inverse(monkey, resolved, target):
    print(monkey, resolved[monkey], target)
    if monkey == 'humn':
        return target
    m1, op, m2 = resolved[monkey]
    if type(m1) == str:
        if op == "+":
            target = target - m2
        elif op == "-":
            target = target + m2
        elif op == "/":
            target = target * m2
        elif op == "*":
            target = target / m2
        else:
            target = m2
        return eval_inverse(m1, resolved, target)
    else:
        if op == "+":
            target = target - m1
        elif op == "-":
            target = -(target - m1)
        elif op == "/":
            target = target * m1
        elif op == "*":
            target = target / m1
        else:
            target = m1
        return eval_inverse(m2, resolved, target)


def populate_needs_humn(monkey, needs_humn, ops):
    if type(ops[monkey]) == int:
        return
    m1, op, m2 = ops[monkey]
    populate_needs_humn(m1, needs_humn, ops)
    populate_needs_humn(m2, needs_humn, ops)
    if m1 == 'humn' or m2 == 'humn' or m1 in needs_humn or m2 in needs_humn:
        needs_humn.add(monkey)


def eval_monkey(monkey, ops, resolved, needs_humn):
    if monkey == 'humn':
        return None
    if monkey in resolved:
        return resolved[monkey]
    m1, operation, m2 = ops[monkey]
    val1 = eval_monkey(m1, ops, resolved, needs_humn)
    val2 = eval_monkey(m2, ops, resolved, needs_humn)
    # print(m1,val1,m2,val2)
    if val1 is None:
        resolved[monkey] = (m1, operation, val2)
        return
    else:
        resolved[m1] = val1
    if val2 is None:
        resolved[monkey] = (val1, operation, m2)
        return
    else:
        resolved[m2] = val2
    if operation == "+":
        return val1 + val2
    elif operation == "-":
        return val1 - val2
    elif operation == "/":
        return val1 // val2
    elif operation == "*":
        return val1 * val2


main()

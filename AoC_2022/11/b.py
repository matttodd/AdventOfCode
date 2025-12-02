def main():
    print(solve())


def solve():
    ans = 0
    monkeys = []
    operations = []
    tests = []
    t = []
    f = []
    while True:
        inp1 = input().split()[1][:-1]
        inp2 = input().split()[2:]
        inp3op, inp3mag = input().split()[4:]
        inp4 = int(input().split()[3])
        inp5 = int(input().split()[5])
        inp6 = int(input().split()[5])
        items = map(lambda x: int(x.removesuffix(',')), inp2)
        monkeys.append(list(items))
        operations.append((inp3op, inp3mag))
        tests.append(inp4)
        t.append(inp5)
        f.append(inp6)
        try:
            input()
        except EOFError:
            print(monkeys)
            print(operations)
            print(tests)
            print(t)
            print(f)
            rounds = 10000
            inspections = [0 for _ in range(len(monkeys))]
            tot = 1
            for test in tests:
                tot *= test
            for rnd in range(rounds):
                print(rnd)
                for ind, monkey in enumerate(monkeys):
                    for item in monkey:
                        op = operations[ind][0]
                        val = operations[ind][1]
                        if op == "+":
                            if val == 'old':
                                item += item
                            else:
                                item += int(val)
                        elif op == "*":
                            if val == 'old':
                                item *= item
                            else:
                                item *= int(val)
                        # item = item // 3
                        inspections[ind] += 1
                        item %= tot
                        # item += tests[ind]
                        if item % tests[ind] == 0:
                            monkeys[t[ind]].append(item)
                        else:
                            monkeys[f[ind]].append(item)
                    monkeys[ind] = []

            inspections.sort()
            return inspections[-1] * inspections[-2]


main()

from functools import reduce


def solve(lines):
    # for i, line in enumerate(lines):
    stones = list(map(int, lines[0].strip().split()))
    blinks = 25

    return answer(stones, blinks)


def answer(stones, blinks):
    for i in range(blinks):
        stones = blink(stones)
    return len(stones)


def blink(stones):
    n = []
    for stone in stones:
        if stone == 0:
            n.append(1)
        elif len(str(stone)) % 2 == 0:
            s1 = int(str(stone)[:len(str(stone))//2])
            s2 = int(str(stone)[len(str(stone)) // 2:])
            n.append(s1)
            n.append(s2)
        else:
            n.append(stone * 2024)
    return n




with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

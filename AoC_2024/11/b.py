from functools import reduce


def solve(lines):
    # for i, line in enumerate(lines):
    stones = list(map(int, lines[0].strip().split()))
    blinks = 75

    return answer(stones, blinks)


def answer(stones, blinks):
    cache = {}
    cache2 = {}
    tot = 0
    for stone in stones:
        tot += blink(stone, blinks, cache, cache2)
    # print(cache, cache2)
    # for stone in stones:
    #     tot +=
    return tot


def blink(stone, blinks, cache, cache2):
    n = []
    tot = 0
    if str(stone) + "-" + str(blinks) in cache2:
        return cache2[str(stone) + "-" + str(blinks)]
    if blinks == 0:
        return 1
    # if stone in cache:
    #     n = cache[stone]
    # else:
    if stone == 0:
        n.append(1)
    elif len(str(stone)) % 2 == 0:
        s1 = int(str(stone)[:len(str(stone))//2])
        s2 = int(str(stone)[len(str(stone))//2:])
        n.append(s1)
        n.append(s2)
    else:
        n.append(stone * 2024)
    cache[stone] = n
    for s in n:
        tot += blink(s, blinks - 1, cache, cache2)
    cache2[str(stone) + "-" + str(blinks)] = tot
    return tot




with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

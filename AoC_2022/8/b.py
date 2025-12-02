from itertools import permutations

def main():
    print(solve())


def solve():
    trees = []
    locations = set()
    max_score = 0
    while True:
        try:
            inp = input()
        except EOFError:
            print(trees)
            for i in range(len(trees)):
                for j in range(len(trees[i])):
                    print(i, j)
                    curr = trees[i][j]
                    val = 1
                    print(val)
                    running = 0
                    for k in range(i+1, len(trees)):
                        running += 1
                        if trees[k][j] >= curr:
                            break
                    val *= running
                    print(val)
                    running = 0
                    for k in range(j+1, len(trees[0])):
                        running += 1
                        if trees[i][k] >= curr:
                            break
                    val *= running
                    print(val)
                    running = 0
                    for k in range(i-1, -1, -1):
                        running += 1
                        if trees[k][j] >= curr:
                            break
                    val *= running
                    print(val)
                    running = 0
                    for k in range(j-1, -1, -1):
                        running += 1
                        if trees[i][k] >= curr:
                            break
                    val *= running
                    print(val)
                    if val > max_score:
                        max_score = val
            return max_score
        trees.append(list(map(int, list(inp))))


main()

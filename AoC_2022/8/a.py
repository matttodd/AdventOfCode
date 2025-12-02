def main():
    print(solve())


def solve():
    trees = []
    locations = set()
    count = 0
    while True:
        try:
            inp = input()
        except EOFError:
            print(trees)
            for row in range(len(trees)):
                last_tallest = -1
                for col in range(len(trees[row])):
                    if trees[row][col] > last_tallest:
                        locations.add((row, col))
                        last_tallest = trees[row][col]
                last_tallest = -1
                for col in range(len(trees[row]) - 1, -1, -1):
                    if trees[row][col] > last_tallest:
                        locations.add((row, col))
                        last_tallest = trees[row][col]
            for col in range(len(trees[0])):
                last_tallest = -1
                for row in range(len(trees)):
                    if trees[row][col] > last_tallest:
                        locations.add((row, col))
                        last_tallest = trees[row][col]
                last_tallest = -1
                for row in range(len(trees) - 1, -1, -1):
                    if trees[row][col] > last_tallest:
                        locations.add((row, col))
                        last_tallest = trees[row][col]

            return len(locations)
        trees.append(list(map(int, list(inp))))


main()

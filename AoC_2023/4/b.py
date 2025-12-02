
def solve(lines):
    tot = 0
    games = []
    for line in lines:
        _, data = line.split(":")
        winning, yours = data.split("|")
        winning = winning.split()
        yours = yours.split()
        win_set = set(winning)
        games.append((win_set, yours))
    for i in range(len(lines)):
        tot += play_scratcher(i, games)
    return tot

cache = {}

def play_scratcher(i, games):
    # print(i+1)
    if i in cache:
        return cache[i]
    winners = 0
    new_cards = 1
    game = games[i]
    for num in game[1]:
        if num in game[0]:
            winners += 1
    # print(list(range(i+1, i + winners+1)))
    for j in range(i+1, i + winners+1):
        new_cards += play_scratcher(j, games)
    cache[i] = new_cards
    return new_cards



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

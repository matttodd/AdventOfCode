
def solve(lines):
    tot = 0
    hands = []
    for line in lines:
        hand, bet = line.split()
        hands.append((hand, int(bet)))

    sorted_hands = sorted(hands, key=lambda x: num_for_hand(x))

    for i, hand in enumerate(sorted_hands):
        tot += (1+i) * hand[1]

    print(sorted_hands)

    return tot


card_rank = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9,
             "9": 8, "8": 7, "7": 6, "6": 5, "5": 4,
             "4": 3, "3": 2, "2": 1}


def num_for_hand(hand):
    hand = hand[0]
    val = 0
    if is_five(hand):
        val += 10**17
    elif is_four(hand):
        val += 10**16
    elif is_full(hand):
        val += 10**15
    elif is_three(hand):
        val += 10**14
    elif is_two_p(hand):
        val += 10**13
    elif is_one_p(hand):
        val += 10**12
    else:
        val += 0

    for ind, c in enumerate(hand):
        val += card_rank[c] * (10**(10 - 2 * ind))

    return val



def is_five(hand):
    first = hand[0]
    for c in hand:
        if c != first:
            return False
    return True


def is_four(hand):
    for c in hand:
        if hand.count(c) == 4:
            return True
    return False


def is_full(hand):
    cards = list(set(hand))
    if len(cards) != 2:
        return False
    if hand.count(cards[0]) != 2 and hand.count(cards[0]) != 3:
        return False
    return True


def is_three(hand):
    for c in hand:
        if hand.count(c) == 3:
            return True
    return False


def is_two_p(hand):
    ps = 0
    cards = list(set(hand))
    if len(cards) != 3:
        return False
    for c in cards:
        if hand.count(c) == 2:
            ps += 1
    return ps == 2


def is_one_p(hand):
    ps = 0
    cards = list(set(hand))
    if len(cards) != 4:
        return False
    for c in cards:
        if hand.count(c) == 2:
            ps += 1
    return ps == 1



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

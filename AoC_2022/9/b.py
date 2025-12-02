def main():
    print(solve())


def solve():
    bod = [(0, 0) for _ in range(10)]
    locations = set()
    while True:
        try:
            direction, mag = input().split()
            mag = int(mag)
        except EOFError:
            return len(locations)
        for i in range(mag):
            # temp_head1 = bod[-1]
            # print(to_string(bod))
            if direction == "R":
                bod[-1] = (bod[-1][0] + 1, bod[-1][1])
            elif direction == "L":
                bod[-1] = (bod[-1][0] - 1, bod[-1][1])
            elif direction == "U":
                bod[-1] = (bod[-1][0], bod[-1][1] + 1)
            elif direction == "D":
                bod[-1] = (bod[-1][0], bod[-1][1] - 1)
            # tail = new_tail(bod[-1], tail, temp_head)
            for j in range(len(bod) - 2, -1, -1):
                # temp_head2 = bod[j]
                # print(bod[j+1], bod[j])
                bod[j] = new_tail(bod[j+1], bod[j])
                # temp_head1 = temp_head2
            locations.add(bod[0])


def to_string(bod):
    board = [["." for i in range(27)] for j in range(27)]
    for ind, b in enumerate(bod):
        board[b[1]+11][b[0]+11] = str(ind)

    # print(board)
    # minx = min(map(lambda x: x[0], bod))
    # maxx = max(map(lambda x: x[0], bod))
    # miny = min(map(lambda x: x[1], bod))
    # maxy = max(map(lambda x: x[1], bod))
    # out = ["".join(["." for _ in range(maxx - minx + 1)]) for _ in range(maxy - miny + 1)]
    return "\n".join(map(lambda x: "".join(x), board)) + '\n'


def new_tail(head, tail):
    if head[0] - tail[0] > 1:
        if head[1] > tail[1]:
            return tail[0] + 1, tail[1] + 1
        elif head[1] < tail[1]:
            return tail[0] + 1, tail[1] - 1
        return tail[0] + 1, tail[1]
    if tail[0] - head[0] > 1:
        if head[1] > tail[1]:
            return tail[0] - 1, tail[1] + 1
        elif head[1] < tail[1]:
            return tail[0] - 1, tail[1] - 1
        return tail[0] - 1, tail[1]
    if head[1] - tail[1] > 1:
        if head[0] > tail[0]:
            return tail[0] + 1, tail[1] + 1
        elif head[0] < tail[0]:
            return tail[0] - 1, tail[1] + 1
        return tail[0], tail[1] + 1
    if tail[1] - head[1] > 1:
        if head[0] > tail[0]:
            return tail[0] + 1, tail[1] - 1
        elif head[0] < tail[0]:
            return tail[0] - 1, tail[1] - 1
        return tail[0], tail[1] - 1
    return tail


main()

def main():
    print(solve())


def solve():
    head = (0, 0)
    tail = (0, 0)
    locations = set()
    while True:
        try:
            direction, mag = input().split()
            mag = int(mag)
        except EOFError:
            return len(locations)
        for i in range(mag):
            temp_head = head
            if direction == "R":
                head = (head[0] + 1, head[1])
            elif direction == "L":
                head = (head[0] - 1, head[1])
            elif direction == "U":
                head = (head[0], head[1] + 1)
            elif direction == "D":
                head = (head[0], head[1] - 1)
            tail = new_tail(head, tail, temp_head)
            locations.add(tail)


def new_tail(head, tail, oldhead):
    if abs(head[0] - tail[0]) > 1:
        return oldhead
    elif abs(head[1] - tail[1]) > 1:
        return oldhead
    return tail

main()

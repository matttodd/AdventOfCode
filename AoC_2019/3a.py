def enum(wire):
    points = []
    x = 0
    y = 0
    for command in wire:
        direction = command[0]
        num = int(command[1:])
        if direction == 'R':
            points.extend([(new_x + x, y) for new_x in range(1, num+1)])
            x += num
            pass
        if direction == 'L':
            points.extend([(x - new_x, y) for new_x in range(1, num+1)])
            x -= num
            pass
        if direction == 'U':
            points.extend([(x, new_y + y) for new_y in range(1, num+1)])
            y += num
        if direction == 'D':
            points.extend([(x, y - new_y) for new_y in range(1, num+1)])
            y -= num
    return points


def main():
    wire1 = input().split(",")
    wire2 = input().split(",")
    coords1 = enum(wire1)
    print(len(coords1))
    coords2 = enum(wire2)
    print(len(coords2))
    common = []
    for coord in coords1:
        if coord in coords2:
            common.append(coord)
    print(len(common))
    ans = min(list(map(lambda x: abs(x[0]) + abs(x[1]), common)))
    print(ans)

if __name__ == "__main__":
    main()
from functools import reduce


def solve(lines):
    tot = 0
    board = []
    moves = []
    walls = set()
    boxes = []
    loc = None
    for i in range(len(lines)):
        line = lines.pop(0).strip()
        if line == "":
            break
        board.append(list(line))
        for j in range(len(line)):
            if line[j] == "#":
                walls.add((i, j))
            if line[j] == "@":
                loc = (i, j)
            if line[j] == "O":
                boxes.append((i, j))
    for i in range(len(lines)):
        line = lines.pop(0).strip()
        moves.extend(list(line))
    # print(board, walls, boxes, loc, moves)
    return answer(board, walls, boxes, loc, moves)


def answer(board, walls, boxes, loc, moves):
    for move in moves:
        boxes, loc = do_move(board, walls, boxes, loc, move, False)
    tot = 0
    # print(loc, boxes)
    for box in boxes:
        tot += (100 * box[0]) + box[1]
    return tot


def do_move(board, walls, boxes, loc, move, isbox):
    # if not isbox:
    # print(loc, move, isbox)
    # print(boxes)
    d = None
    if move == '^':
        d = (-1, 0)
    elif move == 'v':
        d = (1, 0)
    elif move == '<':
        d = (0, -1)
    elif move == '>':
        d = (0, 1)

    des = (loc[0] + d[0], loc[1] + d[1])
    # dest = board[des[0]][des[1]]
    if des in walls:
        return boxes, loc
    if des in boxes:
        # temp_remove = des
        # boxes.remove(temp_remove)
        boxes, moved = do_move(board, walls, boxes, des, move, True)
        # print(loc, des, moved)
        if moved != des:
            if isbox:
                # print(f"MOVED BOX {des}")
                boxes.remove(loc)
                boxes.append(des)
                loc = des
            else:
                loc = des
        # else:
            # print(f"COULDNT MOVED BOX {des}")
    else:
        if isbox:
            boxes.remove(loc)
            boxes.append(des)
            loc = des
        else:
            loc = des
    return boxes, loc



with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

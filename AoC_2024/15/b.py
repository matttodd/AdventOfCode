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
        new_line = ""
        if line == "":
            break
        for j, c in enumerate(line):
            if line[j] == "#":
                new_line += "##"
                walls.add((i, 2*j))
                walls.add((i, (2*j)+1))
            if line[j] == "@":
                new_line += "@."
                loc = (i, 2*j)
            if line[j] == "O":
                new_line += "[]"
                boxes.append((i, 2*j))
            if line[j] == '.':
                new_line += ".."
        board.append(list(new_line))
    for i in range(len(lines)):
        line = lines.pop(0).strip()
        moves.extend(list(line))
    # print(board, walls, boxes, loc, moves)
    return answer(board, walls, boxes, loc, moves)


def answer(board, walls, boxes, loc, moves):
    p_board(board, walls, boxes, loc)
    for i, move in enumerate(moves):
        boxes, loc = do_move(board, walls, boxes, loc, move, False)
        # if i < 700:
        #     print(i, move, boxes)
        #     p_board(board, walls, boxes, loc)
    tot = 0
    print(loc, boxes)
    p_board(board, walls, boxes, loc)
    for box in boxes:
        tot += (100 * box[0]) + box[1]
    return tot


def p_board(board, walls, boxes, loc):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) in walls:
                board[i][j] = '#'
            elif (i, j) in boxes:
                board[i][j] = '['
                # board[i][j + 1] = ']'
            elif (i, j) == loc:
                board[i][j] = '@'
            else:
                board[i][j] = ' '
    print("\n".join(list(map(lambda x: "".join(x), board))))


def do_move(board, walls, boxes, loc, move, isbox):
    og_box = boxes.copy()
    temp = None
    if isbox:
        temp = loc
        boxes.remove(temp)
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
    # if loc[1] == 2 or loc[1] == 3 or loc[1] == 4:
    # print(loc, move, isbox, des)
    # print(boxes)
    # p_board(board, walls, boxes, loc)
    # dest = board[des[0]][des[1]]
    if des in walls or ((des[0], des[1]+1) in walls and isbox):
        # if temp:
        #     boxes.append(temp)
        return og_box, loc
    if des in boxes or ((des[0], des[1]+1) in boxes and isbox) or ((des[0], des[1]-1) in boxes):
        moves = 0
        if (des[0], des[1]-1) in boxes:
            moves += 1
            pushed = (des[0], des[1]-1)
            boxes, moved = do_move(board, walls, boxes, pushed, move, True)
            # print(loc, des, moved)
            if moved != pushed:
                moves -= 1
        if des in boxes or ((des[0], des[1]+1) in boxes and isbox):
            moves += 1
            pushed = des if des in boxes else (des[0], des[1]+1)
            boxes, moved = do_move(board, walls, boxes, pushed, move, True)
            # print(loc, des, moved)
            if moved != pushed:
                moves -= 1
        if moves == 0:
            if isbox:
                temp = None
                boxes.append(des)
            # print(f"ALL MOVES MADE {boxes}")
            loc = des
        else:
            # temp = None
            # print(f"ALL MOVES NOT MADE {og_box, loc}")
            return og_box, loc#boxes = og_box
    else:
        if isbox:
            temp = None
            boxes.append(des)
        loc = des
    if temp is not None:
        boxes.append(temp)
    return boxes, loc


with open('input_a.txt', 'r') as f:
    lines = f.readlines()
    print(solve(lines))

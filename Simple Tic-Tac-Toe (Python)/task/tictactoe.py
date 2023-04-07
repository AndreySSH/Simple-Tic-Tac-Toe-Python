def print_field():
    g = field
    print(f'''\
---------
| {g[0]} {g[1]} {g[2]} |
| {g[3]} {g[4]} {g[5]} |
| {g[6]} {g[7]} {g[8]} |
---------\
    ''')


def check_situation():
    cols = [field[3 * i:3 * i + 3] for i in range(3)]
    rows = [field[i:i + 7:3] for i in range(3)]
    diags = [field[0:9:4], field[2:7:2]]

    variants = cols + rows + diags

    num_x = 0
    num_o = 0
    num_blanks = 0

    for step in field:
        if step == 'X':
            num_x += 1
        elif step == 'O':
            num_o += 1
        else:
            num_blanks += 1
    XxX = ['X', 'X', 'X']
    OoO = ['O', 'O', 'O']
    if (XxX in variants) and not (OoO in variants):
        return 'X wins'
    elif (OoO in variants) and not (XxX in variants):
        return 'O wins'
    elif abs(num_x - num_o) > 1 or (XxX in variants) and (OoO in variants):
        return 'Impossible'
    elif num_blanks == 0:
        return 'Draw'
    else:
        return 'Not finished'


def get_move() -> int:
    while True:
        move_str = input('> ')
        coords = []
        for move in move_str.split():
            try:
                coord = int(move)
            except ValueError:
                print('You should enter numbers!')
                break
            else:
                if 1 <= coord <= 3:
                    coords.append(coord - 1)
                else:
                    print('Coordinates should be from 1 to 3!')
                    break
        if len(coords) == 2:
            return coords[0] * 3 + coords[1]


def update_field(move: int) -> bool:
    global field
    if field[move] != ' ':
        print('This cell is occupied! Choose another one!')
        return False
    else:
        field[move] = player
        return True


def update_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


if __name__ == '__main__':

    player = 'X'
    field = [' ' for i in range(9)]

    print_field()

    while True:
        while True:
            current_move = get_move()
            if update_field(current_move):
                print_field()
                break
        status = check_situation()
        # print(f'Status: {status}')
        if status == 'X wins' or status == 'O wins' or status == 'Draw':
            print(status)
            break
        else:
            update_player()

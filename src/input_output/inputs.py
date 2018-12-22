import sys
from src.obtain_values.obtain_values import obtain_pos_value
from src.conf.settings import messages, letters
from src.checks.checks import check_in_board


def format_input(input_str):
    if input_str.lower() == 'exit\n':
        exit()
    if len(input_str) == 2:
        if input_str[0].lower() in letters:
            position = input_str
        else:
            return 0
    elif len(input_str) == 3:
        if input_str[0].lower() in letters:
            position = input_str.split(' ')
        else:
            return 0
    else:
        return 0
    return position


def choose_piece(turn, board, def_pos=False):
    print(messages['CHOOSE_PIECE'].format(turn))
    if not def_pos:
        position = str(sys.stdin.readline()).replace('\n', '')
    else:
        position = def_pos
    position = format_input(position)
    if not position:
        return 0
    in_board = check_in_board(position, board)
    pos = obtain_pos_value(position, board)
    if in_board and pos[1] == turn:
        return position
    else:
        if not in_board:
            print(messages['WRONG_MOVEMENT'])
            return 0
        if pos[1] != turn:
            print(messages['WRONG_PIECE'])
            return 0


def choose_move(board, def_pos=False):
    print(messages['CHOOSE_MOVE'])
    if not def_pos:
        position2 = str(sys.stdin.readline()).replace('\n', '')
    else:
        position2 = def_pos
    position2 = format_input(position2)
    if not position2:
        return 0
    in_board = check_in_board(position2, board)
    if not in_board:
        if not in_board:
            print(messages['WRONG_MOVEMENT'])
            return 0
    else:
        return position2

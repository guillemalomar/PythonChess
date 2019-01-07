import os
import sys
from src.obtain_values.obtain_values import obtain_pos_value, assign_pos_value
from src.conf.settings import messages, letters


def format_input(input_str):
    if input_str.lower() == 'exit':
        try:
            os.remove('logs/movements.log')
        except FileNotFoundError:
            pass
        os.remove('logs/current.log')
        exit()
    elif input_str.lower() == 'save':
        os.rename('logs/current.log', 'logs/movements.log')
        exit()
    if len(input_str) == 2:
        if input_str[0].lower() in letters:
            position = input_str
        else:
            return 0
    elif len(input_str) == 3:
        if input_str[1] == ' ':
            if input_str[0].lower() in letters:
                position = input_str.split(' ')
            else:
                return 0
        else:
            position = [input_str[0], input_str[1:]]
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
    pos = obtain_pos_value(position, board)
    if pos and pos[1] == turn:
        return position
    else:
        print(messages['WRONG_PIECE'])
        return 0


def choose_move(def_pos=False):
    print(messages['CHOOSE_MOVE'])
    if not def_pos:
        position2 = str(sys.stdin.readline()).replace('\n', '')
    else:
        position2 = def_pos
    position2 = format_input(position2)
    if not position2:
        return 0
    return position2


def promote(position, value, board):
    correct_piece = False
    piece = ''
    while not correct_piece:
        print(messages['PROMOTE_PAWN'])
        piece = str(sys.stdin.readline()).replace('\n', '')
        correct_piece, piece = check_promotable(piece)
    assign_pos_value(position, piece + value[1], board)


def check_promotable(piece):
    promotions = {1: 'Q', 2: 'H', 3: 'T', 4: 'B'}
    if int(piece) not in range(1, 5):
        return False, piece
    return True, promotions[int(piece)]

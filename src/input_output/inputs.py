import sys
from src.obtain_values.obtain_values import obtain_pos_value
from src.input_output.outputs import format_input
from src.conf.settings import messages
from src.checks.checks import check_in_board


def choose_piece(turn, board):
    print(messages['CHOOSE_PIECE'].format(turn))
    position = str(sys.stdin.readline())
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


def choose_move(board):
    print(messages['CHOOSE_MOVE'])
    position2 = str(sys.stdin.readline())
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

from src.obtain_values.obtain_values import obtain_v_coord, obtain_pos_value
from src.conf.settings import messages


def move_piece(position, position2, board):
    if board[obtain_v_coord(position2[0])][int(position2[1])-1][0].lower() == 'k':
        print(messages['PLAYER_WIN'].format(obtain_pos_value(position, board)[1]))
        exit()
    board[obtain_v_coord(position2[0])][int(position2[1])-1] = ''.join(obtain_pos_value(position, board))
    board[obtain_v_coord(position[0])][int(position[1])-1] = '  '
    return board

import logging
from src.obtain_values.obtain_values import obtain_v_coord, obtain_pos_value
from src.conf.settings import messages


def move_piece(position, position2, board):
    curr_pos_val = obtain_pos_value(position, board)
    if board[obtain_v_coord(position2[0])][int(position2[1])-1][0].lower() == 'k':
        print(messages['PLAYER_WIN'].format(curr_pos_val[1]))
        exit()
    board[obtain_v_coord(position2[0])][int(position2[1])-1] = ''.join(curr_pos_val)
    board[obtain_v_coord(position[0])][int(position[1])-1] = '  '
    logging.getLogger('log1').warning('{} {}'.format(position, position2))
    logging.getLogger('log2').warning('Player {} has moved {} from {} to {}'.format(curr_pos_val[1],
                                                                                  curr_pos_val[0],
                                                                                  position,
                                                                                  position2))
    return board

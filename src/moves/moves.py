import logging
from src.obtain_values.obtain_values import obtain_pos_value, assign_pos_value
from src.conf.settings import messages
from src.moves.deaths import add_death
from src.input_output.outputs import print_table
from src.input_output.inputs import promote
from src.checks.checks import check_if_check
from src.input_output.timer import black_timer, white_timer


def move_piece(position, position2, board):
    curr_pos_val = obtain_pos_value(position, board)
    targ_pos_val = obtain_pos_value(position2, board)

    turn = curr_pos_val[1]

    assign_pos_value(position2, ''.join(curr_pos_val), board)
    assign_pos_value(position, '  ', board)

    if targ_pos_val != '  ':
        add_death(targ_pos_val)
        assign_pos_value(position2, ''.join(curr_pos_val) + 'k', board)

    logging.getLogger('log1').warning('{} {}'.format(position, position2))
    logging.getLogger('log2').warning('Player {} has moved {} from {} to {}'.format(curr_pos_val[1],
                                                                                    curr_pos_val[0],
                                                                                    position,
                                                                                    position2))
    if targ_pos_val[0].lower() == 'k':
        print_table(board)
        print(messages['PLAYER_WIN'].format(curr_pos_val[1]))
        exit()
    if curr_pos_val[0].lower() == 'p' and \
       ((position2[0] == 0 and curr_pos_val[1].lower() == 'w') or
        (position2[0] == len(board)-1 and curr_pos_val[1].lower() == 'b')):
        promote(position2, curr_pos_val, board)

    check_if_check(board, curr_pos_val[1])

    if turn == 'W':
        white_timer.pause_time()
        black_timer.start_time()
    else:
        black_timer.pause_time()
        white_timer.start_time()

    return board

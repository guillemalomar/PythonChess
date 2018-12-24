import argparse
import itertools
import logging
from src.checks.checks import check_correct_move
from src.conf.settings import size_x, size_y
from src.conf.board_init import board_init
from src.conf.logger import setup_logger
from src.input_output.inputs import choose_move, choose_piece
from src.input_output.outputs import print_table, clean_screen, start_print
from src.moves.moves import move_piece


turn_iter = itertools.cycle('WB')

formatter = logging.Formatter('%(message)s')
current_logger = setup_logger('log1', "src/logs/current.log", with_formatter=formatter)
super_logger = setup_logger('log2', "src/logs/all.log")


def main_function(coord_x_or, coord_y_or, turn, cont_file=''):
    if cont_file != '':
        file = open(cont_file, 'r')
    else:
        file = ''
    board = board_init(coord_x_or, coord_y_or)
    print_table(board)
    while True:
        if cont_file != '':
            try:
                line = next(file)
                turn_move = line.replace('\n', '')
            except StopIteration:
                turn_move = False
                cont_file = ''
        else:
            turn_move = False
        position = 0
        correct_move = 0
        target = 0
        while not correct_move:
            while not position:
                if turn_move:
                    position = choose_piece(turn, board, turn_move.split()[0])
                else:
                    position = choose_piece(turn, board)

            if turn_move:
                target = choose_move(board, turn_move.split()[1])
            else:
                target = choose_move(board)
            if target:
                correct_move = check_correct_move(position, target, board)
            else:
                position = 0
        board = move_piece(position, target, board)
        print_table(board)
        turn = next(turn_iter)


if __name__ == "__main__":

    # Arguments are taken from command line

    parser = argparse.ArgumentParser(description='Python Chess',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--sizex', action="store", dest="size_x",
                        help="Horizontal size of the chess board",
                        default=size_x, type=int)
    parser.add_argument('--sizey', action="store", dest="size_y",
                        help="Vertical size of the chess board",
                        default=size_y, type=int)
    parser.add_argument('-c', action="store_true", help="If you want to continue a game stored in src/logs/movements.log")
    args = parser.parse_args()
    size_x = args.size_x
    size_y = args.size_y

    initial_turn = next(turn_iter)

    clean_screen()

    start_print()

    if args.c:
        main_function(size_x, size_y, turn=initial_turn, cont_file='movements.log')
    else:
        main_function(size_x, size_y, turn=initial_turn)  # TESTING
        # main_function(size_x, size_y, turn=initial_turn, cont_file='movements.log')

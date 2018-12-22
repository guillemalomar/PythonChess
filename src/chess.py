import argparse
import itertools
from src.conf.settings import size_x, size_y
from src.conf.board_init import board_init
from src.input_output.outputs import print_table, clean_screen
from src.input_output.inputs import choose_move, choose_piece
from src.moves.moves import move_piece
from src.checks.checks import check_correct_move


turn_iter = itertools.cycle('WB')


def main_function(coord_x_or, coord_y_or, turn):

    board = board_init(coord_x_or, coord_y_or)
    print_table(board)
    while True:
        position = 0
        target = 0
        while not target:
            while not position:
                position = choose_piece(turn, board)
            target = choose_move(position, board, turn)
            if target:
                if check_correct_move(position, target, board):
                    move_piece(position, target, board)
            position = 0
        print_table(board)
        turn = next(turn_iter)


if __name__ == "__main__":
    clean_screen()

    # Arguments are taken from command line

    parser = argparse.ArgumentParser(description='Reddit Crawler Client',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--sizex', action="store", dest="size_x",
                        help="Horizontal size of the chess board",
                        default=size_x, type=int)
    parser.add_argument('--sizey', action="store", dest="size_y",
                        help="Vertical size of the chess board",
                        default=size_y, type=int)
    args = parser.parse_args()
    size_x = args.size_x
    size_y = args.size_y
    initial_turn = next(turn_iter)

    print("Chess app")
    main_function(size_x, size_y, turn=initial_turn)

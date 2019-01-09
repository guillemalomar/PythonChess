import argparse
import logging
from tkinter import Tk
from src.conf.settings import size_x, size_y
from src.board import Board
from src.conf.logger import setup_logger
from src.game_execution import GameExecution


formatter = logging.Formatter('%(message)s')
current_logger = setup_logger('log1', "logs/current.log", with_formatter=formatter)
super_logger = setup_logger('log2', "logs/all.log")


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
    parser.add_argument('-c', action="store_true",
                        help="If you want to continue a game stored in src/logs/movements.log")
    args = parser.parse_args()
    size_x = args.size_x
    size_y = args.size_y

    root = Tk()
    app = GameExecution()
    board = Board(size_x, size_y)
    app.show_board(board)
    root.mainloop()

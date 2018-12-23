from src.conf.settings import board_delimiter, letters, pieces
from termcolor import colored
from src.moves.deaths import black_deaths, white_deaths


def clean_screen():
    """
    Method called to do a 'clear', just for application visualization purposes
    :return:
    """
    print(chr(27) + "[2J")


def print_table(board):

    print(" ------------------------- ")
    print('|     ' + ' '.join([str(i+1) for i in range(len(board[0]))]) + '     |')
    print('|   ' + board_delimiter * ((2*len(board[0]))+3) + '   | {}'.format('Killed by B:' + ' '.join(white_deaths) if len(white_deaths) else ''))
    for i in range(len(board)):
        line = '| ' + letters[i].upper() + ' ' + board_delimiter + ' '
        values = ''
        for j in range(len(board[0])):
            values += (colored(board[i][j][0], 'white') if board[i][j][1] == 'B' else colored(board[i][j][0], 'grey')) + ' '
        print(line + values + board_delimiter + ' ' + letters[i].upper() + ' |')
    print('|   ' + board_delimiter * ((2*len(board[0]))+3) + '   | {}'.format('Killed by W:' + ' '.join(black_deaths) if len(black_deaths) else ''))
    print('|     ' + ' '.join([str(i+1) for i in range(len(board[0]))]) + '     |')
    print(" ------------------------- ")


def print_legend():
    print(colored('--- Legend ---'), 'blue')
    for p_letter, p_name in pieces.items():
        print(colored(p_letter + ': ' + p_name, 'blue'))

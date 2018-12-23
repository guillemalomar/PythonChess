from src.conf.settings import board_delimiter, letters, pieces
from termcolor import colored


def clean_screen():
    """
    Method called to do a 'clear', just for application visualization purposes
    :return:
    """
    print(chr(27) + "[2J")


def print_table(board):

    print(" ------------------------- ")
    print('|     ' + ' '.join([str(i+1) for i in range(len(board[0]))]) + '     |')
    print('|   ' + board_delimiter * ((2*len(board[0]))+3) + '   |')
    for i in range(len(board)):
        line = '| ' + letters[i].upper() + ' ' + board_delimiter + ' '
        values = ''
        for j in range(len(board[0])):
            values += board[i][j][0] + ' '
        if i > len(board) / 2:
            print(line + colored(values, 'grey') + board_delimiter + ' ' + letters[i].upper() + ' |')
        else:
            print(line + colored(values, 'white') + board_delimiter + ' ' + letters[i].upper() + ' |')
    print('|   ' + board_delimiter * ((2*len(board[0]))+3) + '   |')
    print('|     ' + ' '.join([str(i+1) for i in range(len(board[0]))]) + '     |')
    print(" ------------------------- ")


def print_legend():
    print(colored('--- Legend ---'), 'blue')
    for p_letter, p_name in pieces.items():
        print(colored(p_letter + ': ' + p_name, 'blue'))

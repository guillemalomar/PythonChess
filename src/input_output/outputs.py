from src.conf.settings import board_delimiter, letters


def clean_screen():
    """
    Method called to do a 'clear', just for application visualization purposes
    :return:
    """
    print(chr(27) + "[2J")


def print_table(board):

    print(" ----------------------------------")
    print('|      ' + '  '.join([str(i+1) for i in range(len(board[0]))]) + '      |')
    print('|    ' + board_delimiter * ((3*len(board[0]))+3) + '   |')
    for i in range(len(board)):
        line = '|  ' + letters[i].upper() + ' ' + board_delimiter + ' '
        for j in range(len(board[0])):
            line += board[i][j] + ' '
        print(line + board_delimiter + ' ' + letters[i].upper() + ' |')
    print('|    ' + board_delimiter * ((3*len(board[0]))+3) + '   |')
    print('|      ' + '  '.join([str(i+1) for i in range(len(board[0]))]) + '      |')
    print(" ----------------------------------")


def format_input(input_str):
    if input_str.lower()[0:4] == 'exit':
        exit()
    if len(input_str) == 3:
        position = input_str
    elif len(input_str) == 4:
        position = input_str.split(' ')
    else:
        return 0
    return position

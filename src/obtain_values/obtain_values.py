from src.conf.settings import letters


def obtain_pos_value(position, board):
    return board[obtain_v_coord(position[0])][int(position[1])-1]


def obtain_v_coord(letter_coordinate):
    return letters.index(letter_coordinate.lower())

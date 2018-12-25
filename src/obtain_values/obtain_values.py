from src.conf.settings import letters


def obtain_pos_value(position, board):
    try:
        position = board[obtain_v_coord(position[0])][int(position[1])-1]
        return position
    except IndexError:
        return False


def assign_pos_value(position, value, board):
    board[obtain_v_coord(position[0])][int(position[1]) - 1] = value
    return board


def obtain_v_coord(letter_coordinate):
    try:
        return letters.index(letter_coordinate.lower())
    except ValueError:
        return False
    except AttributeError:
        return False

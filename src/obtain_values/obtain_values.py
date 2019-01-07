
def obtain_pos_value(position, board):
    try:
        position = board[int(position[0])][int(position[1])]
        return position
    except IndexError:
        return False


def assign_pos_value(position, value, board):
    board[int(position[0])][int(position[1])] = value
    return board

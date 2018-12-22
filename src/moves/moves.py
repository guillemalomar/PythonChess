from src.obtain_values.obtain_values import obtain_v_coord, obtain_pos_value


def move_piece(position, position2, board):
    board[obtain_v_coord(position2[0])][int(position2[1])-1] = ''.join(obtain_pos_value(position, board))
    board[obtain_v_coord(position[0])][int(position[1])-1] = '  '

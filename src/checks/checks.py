from src.obtain_values.obtain_values import obtain_pos_value, assign_pos_value
from src.conf.settings import messages
from src.conf.movements import movements


def check_correct_move(position, position2, board, show_output=False):
    piece_type = obtain_pos_value(position, board)[0].lower()
    try:
        piece_movements = movements[piece_type]
    except KeyError:
        return 0
    if piece_type != 'p':
        for piece_movement in piece_movements:
            if piece_type == 'h' or piece_type == 'k':
                if int(position2[0]) == int(position[0]) + piece_movement[0]\
                        and int(position2[1]) == int(position[1]) + piece_movement[1]:
                    if obtain_pos_value(position2, board)[1] == position[1]:
                        if show_output:
                            print(messages['OWN_ATTACK'])
                        return 0
                    return 1
            else:
                for n in range(1, 15):
                    if int(position2[0]) == int(position[0]) + (piece_movement[0]*n)\
                            and int(position2[1]) == int(position[1]) + (piece_movement[1]*n):
                        incorrect_movement = False
                        for j in range(n-1, 0, -1):
                            if board[int(position[0]) +
                                     (piece_movement[0]*j)][int(position[1]) + (piece_movement[1]*j) - 1] != '  ':
                                incorrect_movement = True
                        if not incorrect_movement:
                            if obtain_pos_value(position2, board)[1] == position[1]:
                                if show_output:
                                    print(messages['OWN_ATTACK'])
                                return 0
                            return 1
    else:
        if obtain_pos_value(position2, board) != '  ':
            piece_movements = movements['p_attack']
            print('attacking')
        if (int(position[0]) == len(board) - 2 and obtain_pos_value(position, board)[1] == 'W') or \
           (int(position[0]) == 1 and obtain_pos_value(position, board)[1] == 'B'):
            piece_movements = movements['p_first_move']
            print('advancing')
        for piece_movement in piece_movements:
            if obtain_pos_value(position, board)[1] == 'W':
                if int(position2[0]) == int(position[0]) - piece_movement[0]\
                        and int(position2[1]) == int(position[1]) - piece_movement[1]:
                    if obtain_pos_value(position2, board)[1] == position[1]:
                        if show_output:
                            print(messages['OWN_ATTACK'])
                        return 0
                    return 1
            else:
                if int(position2[0]) == int(position[0]) + piece_movement[0]\
                        and int(position2[1]) == int(position[1]) + piece_movement[1]:
                    if obtain_pos_value(position2, board)[1] == position[1]:
                        if show_output:
                            print(messages['OWN_ATTACK'])
                        return 0
                    return 1
    if show_output:
        print(messages['WRONG_MOVEMENT'])
    return 0


def check_if_check(board, turn):
    king = find_king(board, obtain_other_turn(turn))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][1].upper() == turn.upper():
                if check_correct_move((i, j), king, board):
                    assign_pos_value((i, j), obtain_pos_value((i, j), board)[0:2] + 'c', board)


def find_king(board, turn):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'K' + turn.upper():
                return i, j


def obtain_other_turn(turn):
    if turn.lower() == 'w':
        return 'b'
    else:
        return 'w'

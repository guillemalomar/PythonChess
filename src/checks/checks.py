from src.obtain_values.obtain_values import obtain_pos_value, obtain_v_coord
from src.conf.settings import messages
from src.game_rules.movements import movements


def check_in_board(position, board):
    if int(position[1]) - 1 in range(0, len(board[0])) and obtain_v_coord(position[0]) in range(0, len(board)):
        return True
    else:
        return False


def check_correct_move(position, position2, board):
    piece_type = obtain_pos_value(position, board)[0].lower()
    piece_movements = movements[piece_type]
    if piece_type != 'p':
        for piece_movement in piece_movements:
            if piece_type == 'h' or piece_type == 'k':
                if int(obtain_v_coord(position2[0])) == int(obtain_v_coord(position[0])) + piece_movement[0]\
                        and int(position2[1]) == int(position[1]) + piece_movement[1]:
                    if obtain_pos_value(position2, board)[1] == position[1]:
                        print(messages['OWN_ATTACK'])
                        return 0
                    return 1
            else:
                for n in range(1, 15):
                    if int(obtain_v_coord(position2[0])) == int(obtain_v_coord(position[0])) + (piece_movement[0]*n)\
                            and int(position2[1]) == int(position[1]) + (piece_movement[1]*n):
                        incorrect_movement = False
                        for j in range(n-1, 0, -1):
                            if board[int(obtain_v_coord(position[0])) + (piece_movement[0]*j)][int(position[1]) + (piece_movement[1]*j) - 1] != '  ':
                                incorrect_movement = True
                        if not incorrect_movement:
                            if obtain_pos_value(position2, board)[1] == position[1]:
                                print(messages['OWN_ATTACK'])
                                return 0
                            return 1
    else:
        if obtain_pos_value(position2, board) != '  ':
            piece_movements = movements['p_attack']
        for piece_movement in piece_movements:
            if position[1] == 'W':
                if int(obtain_v_coord(position2[0])) == int(obtain_v_coord(position[0])) - piece_movement[0]\
                        and int(position2[1]) == int(position[1]) - piece_movement[1]:
                    if obtain_pos_value(position2, board)[1] == position[1]:
                        print(messages['OWN_ATTACK'])
                        return 0
                    return 1
            else:
                if obtain_v_coord(position2[0]) == int(obtain_v_coord(position[0])) + piece_movement[0]\
                        and int(position2[1]) == int(position[1]) + piece_movement[1]:
                    if obtain_pos_value(position2, board)[1] == position[1]:
                        print(messages['OWN_ATTACK'])
                        return 0
                    return 1
    print(messages['WRONG_MOVEMENT'])
    return 0

import logging
import sys
from src.game_execution.deaths import add_death
from tkinter.ttk import Button, Style
from src.conf.settings import board_delimiter, letters, messages
from src.conf.movements import movements
from src.game_execution.deaths import black_deaths, white_deaths
from termcolor import colored
from src.timer.timer import black_timer, white_timer


class Board:
    def __init__(self, coordinates_x, coordinates_y):
        self.positions = [['  ' for _ in range(coordinates_x)] for _ in range(coordinates_y)]

        #              V  H
        self.positions[0][0] = 'TB'
        self.positions[0][1] = 'HB'
        self.positions[0][2] = 'BB'
        self.positions[0][3] = 'QB'
        self.positions[0][4] = 'KB'
        self.positions[0][5] = 'BB'
        self.positions[0][6] = 'HB'
        self.positions[0][7] = 'TB'

        self.positions[coordinates_y-1][0] = 'TW'
        self.positions[coordinates_y-1][1] = 'HW'
        self.positions[coordinates_y-1][2] = 'BW'
        self.positions[coordinates_y-1][3] = 'QW'
        self.positions[coordinates_y-1][4] = 'KW'
        self.positions[coordinates_y-1][5] = 'BW'
        self.positions[coordinates_y-1][6] = 'HW'
        self.positions[coordinates_y-1][7] = 'TW'

        for i in range(coordinates_x):
            self.positions[1][i] = 'PB'
            self.positions[coordinates_y-2][i] = 'PW'

    def obtain_pos_value(self, position):
        try:
            position = self.positions[int(position[0])][int(position[1])]
            return position
        except IndexError:
            return False

    def assign_pos_value(self, position, value):
        self.positions[int(position[0])][int(position[1])] = value

    def show_board(self, app):

        button_style = Style()
        button_style.configure("B.TLabel", background='black')
        button_style.configure("W.TLabel", background='white')

        param = ''
        for ind1, x in enumerate(self.positions):
            for ind2, y in enumerate(x):
                if (ind1 + ind2) % 2 == 1:
                    color = 'B'
                    try:
                        param = eval('app.' + y.lower() + 'b')
                    except AttributeError:
                        pass
                else:
                    color = 'W'
                    try:
                        param = eval('app.' + y.lower() + 'w')
                    except AttributeError:
                        pass
                if y.lower() != '  ':
                    piece_button = Button(app,
                                          style=color+".TLabel",
                                          command=lambda v=(ind1, ind2): app.button_pressed(v, self),
                                          image=param)
                else:
                    piece_button = Button(app,
                                          style=color+".TLabel",
                                          command=lambda v=(ind1, ind2): app.button_pressed(v, self))

                piece_button.place(x=(80*ind2) + 25, y=(80*ind1)+25, width=74, height=74)
        app.pack()

    def print_board(self):

        print(' ' + ('-' * (2 * len(self.positions[0]) + 9)))
        print('|     ' + ' '.join([str(i + 1) for i in range(len(self.positions[0]))]) + '     |')
        print('|   ' + board_delimiter * ((2 * len(self.positions[0])) + 3) + '   | {}'.format(
            'Killed by B:' + ' '.join(white_deaths) if len(white_deaths) else ''))
        for i in range(len(self.positions)):
            line = '| ' + letters[i].upper() + ' ' + board_delimiter + ' '
            values = ''
            for j in range(len(self.positions[0])):
                value = self.positions[i][j]
                if len(value) >= 3:
                    if self.positions[i][j][2] == 'c':
                        values += colored(self.positions[i][j][0], 'yellow')
                    elif self.positions[i][j][2] == 'k':
                        values += colored(self.positions[i][j][0], 'red')
                    self.positions[i][j] = value[0:2]
                elif self.positions[i][j][1] == 'B':
                    values += colored(self.positions[i][j][0], 'magenta')
                elif self.positions[i][j][1] == 'W':
                    values += colored(self.positions[i][j][0], 'white')
                else:
                    values += ' '
                values += ' '
            print(line + values + board_delimiter + ' ' + letters[i].upper() + ' |')
        print('|   ' + board_delimiter * ((2 * len(self.positions[0])) + 3) + '   | {}'.format(
            'Killed by W:' + ' '.join(black_deaths) if len(black_deaths) else ''))
        print('|     ' + ' '.join([str(i + 1) for i in range(len(self.positions[0]))]) + '     |')
        print(' ' + ('-' * (2 * len(self.positions[0]) + 9)))
        white_timer.print_timer()
        black_timer.print_timer()

    def move_piece(self, position, position2):
        curr_pos_val = self.obtain_pos_value(position)
        targ_pos_val = self.obtain_pos_value(position2)

        turn = curr_pos_val[1]

        self.assign_pos_value(position2, ''.join(curr_pos_val))
        self.assign_pos_value(position, '  ')

        if targ_pos_val != '  ':
            add_death(targ_pos_val)
            self.assign_pos_value(position2, ''.join(curr_pos_val) + 'k')

        logging.getLogger('log1').warning('{} {}'.format(position, position2))
        logging.getLogger('log2').warning('Player {} has moved {} from {} to {}'.format(curr_pos_val[1],
                                                                                        curr_pos_val[0],
                                                                                        position,
                                                                                        position2))
        if targ_pos_val[0].lower() == 'k':
            self.print_board()
            print(messages['PLAYER_WIN'].format(curr_pos_val[1]))
            exit()
        if curr_pos_val[0].lower() == 'p' and \
                ((position2[0] == 0 and curr_pos_val[1].lower() == 'w') or
                 (position2[0] == len(self.positions) - 1 and curr_pos_val[1].lower() == 'b')):
            self.promote(position2, curr_pos_val)

        self.check_if_check(curr_pos_val[1])

        if turn == 'W':
            white_timer.pause_time()
            black_timer.start_time()
        else:
            black_timer.pause_time()
            white_timer.start_time()

    def promote(self, position, value):
        correct_piece = False
        piece = ''
        while not correct_piece:
            print(messages['PROMOTE_PAWN'])
            piece = str(sys.stdin.readline()).replace('\n', '')
            correct_piece, piece = self.check_promotable(piece)
        self.assign_pos_value(position, piece + value[1])

    @staticmethod
    def check_promotable(piece):
        promotions = {1: 'Q', 2: 'H', 3: 'T', 4: 'B'}
        if int(piece) not in range(1, 5):
            return False, piece
        return True, promotions[int(piece)]

    def check_all_free_ways(self, piece_movements, position, position2, show_output=False, attack_range=15):
        for piece_movement in piece_movements:
            if self.check_free_way(piece_movement, position, position2, attack_range, show_output):
                return 1
        return 0

    def check_free_way(self, piece_movement, position, position2, attack_range, show_output=False):
        incorrect_movement = False
        for n in range(1, attack_range+1):
            if position2[0] == position[0] + (piece_movement[0] * n) and \
               position2[1] == position[1] + (piece_movement[1] * n):
                for j in range(n - 1, 0, -1):
                    if self.obtain_pos_value((position[0] + (piece_movement[0] * j),
                                              position[1] + (piece_movement[1] * j))) != '  ':
                        incorrect_movement = True
                if not incorrect_movement:
                    if self.obtain_pos_value(position2)[1] == self.obtain_pos_value(position)[1]:
                        if show_output:
                            print(messages['OWN_ATTACK'])
                        return 0
                    return 1
        return 0

    def check_correct_move(self, position, position2, show_output=False):
        piece_type = self.obtain_pos_value(position)[0].lower()
        if piece_type != 'p':
            try:
                piece_movements = movements[piece_type]
            except KeyError:
                return 0
            if piece_type == 'h' or piece_type == 'k':
                return self.check_all_free_ways(piece_movements, position, position2, True, 1)
            else:
                return self.check_all_free_ways(piece_movements, position, position2, True)
        else:
            value_in_pos = self.obtain_pos_value(position)
            value_in_tgt = self.obtain_pos_value(position2)
            if value_in_pos[1] == 'W':
                piece_movements = movements['p_w']
            else:
                piece_movements = movements['p_b']
            if value_in_tgt != '  ':
                if value_in_pos[1] == 'W':
                    piece_movements.extend(movements['p_attack_w'])
                else:
                    piece_movements.extend(movements['p_attack_b'])
            if self.is_first_pawn_movement(position):
                if value_in_pos[1] == 'W':
                    piece_movements.extend(movements['p_first_move_w'])
                else:
                    piece_movements.extend(movements['p_first_move_b'])

            for piece_movement in piece_movements:
                if self.check_free_way(piece_movement, position, position2, 1, True):
                    if value_in_tgt[1] == value_in_pos[1]:
                        if show_output:
                            print(messages['OWN_ATTACK'])
                        return 0
                    return 1
        if show_output:
            print(messages['WRONG_MOVEMENT'])
        return 0

    def is_first_pawn_movement(self, position):
        return (position[0] == len(self.positions) - 2 and self.obtain_pos_value(position)[1] == 'W') or \
               (position[0] == 1 and self.obtain_pos_value(position)[1] == 'B')

    def check_if_check(self, turn):
        king = self.find_king(self.obtain_other_turn(turn))
        for i in range(len(self.positions)):
            for j in range(len(self.positions[0])):
                if self.positions[i][j][1].upper() == turn.upper():
                    if self.check_correct_move((i, j), king):
                        self.assign_pos_value((i, j), self.obtain_pos_value((i, j))[0:2] + 'c')

    def find_king(self, turn):
        for i in range(len(self.positions)):
            for j in range(len(self.positions[0])):
                if self.positions[i][j] == 'K' + turn.upper():
                    return i, j

    @staticmethod
    def obtain_other_turn(turn):
        if turn.lower() == 'w':
            return 'b'
        else:
            return 'w'

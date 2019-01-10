import logging
import sys
from src.conf.settings import board_delimiter, letters, messages
from src.conf.movements import movements
from termcolor import colored
from src.timer import black_timer, white_timer


class Board:
    def __init__(self, coordinates_x, coordinates_y):
        """
        This method initializes a board, with a size specified in its parameters.
        It also creates the lists to store the killed pieces for each player.
        :param coordinates_x: (int) desired width of the board.
        :param coordinates_y: (int) desired depth of the board.
        """
        self.squares = [['     ' for _ in range(coordinates_x)] for _ in range(coordinates_y)]

        #            V  H
        self.squares[0][0] = 'TB   '
        self.squares[0][1] = 'HB   '
        self.squares[0][2] = 'BB   '
        self.squares[0][3] = 'QB   '
        self.squares[0][4] = 'KB   '
        self.squares[0][5] = 'BB   '
        self.squares[0][6] = 'HB   '
        self.squares[0][7] = 'TB   '

        self.squares[coordinates_y - 1][0] = 'TW   '
        self.squares[coordinates_y - 1][1] = 'HW   '
        self.squares[coordinates_y - 1][2] = 'BW   '
        self.squares[coordinates_y - 1][3] = 'QW   '
        self.squares[coordinates_y - 1][4] = 'KW   '
        self.squares[coordinates_y - 1][5] = 'BW   '
        self.squares[coordinates_y - 1][6] = 'HW   '
        self.squares[coordinates_y - 1][7] = 'TW   '

        for i in range(coordinates_x):
            self.squares[1][i] = 'PB   '
            self.squares[coordinates_y - 2][i] = 'PW   '

        self.black_deaths = []
        self.white_deaths = []

    def get_pos_val(self, pos):
        """
        Given a position, this method returns the piece that can be found in
        that position (or empty). If the coordinates do not exist in the
        board, it returns a False.
        :param pos: (tuple) Coordinates x and j of the desired position.
        :return: (str) The found value if it exists, otherwise a False.
        """
        try:
            return self.squares[int(pos[0])][int(pos[1])]
        except IndexError:
            return False

    def put_pos_val(self, pos, val):
        """
        This method assigns a given value to a given board position.
        :param pos: (tuple) Coordinates x and j of the desired position.
        :param val: (str) Value to assign to the given position.
        """
        self.squares[int(pos[0])][int(pos[1])] = val

    def print_board_in_terminal(self):
        """
        This method was used before having a GUI. Now it's used mainly
        to develop.
        It prints the current state of the board in the terminal.
        """
        print(' ' + ('-' * (2 * len(self.squares[0]) + 9)))
        print('|     ' + ' '.join([str(i + 1) for i in range(len(self.squares[0]))]) + '     |')
        print('|   ' + board_delimiter * ((2 * len(self.squares[0])) + 3) + '   | {}'.format(
            'Killed by B:' + ' '.join(self.white_deaths) if len(self.white_deaths) else ''))
        for i in range(len(self.squares)):
            line = '| ' + letters[i].upper() + ' ' + board_delimiter + ' '
            values = ''
            for j in range(len(self.squares[0])):
                value = self.squares[i][j]
                if value[2] == 'k' or value[3] == 'c' or value[4] == 'l':
                    if value[2] == 'k':
                        values += colored(self.squares[i][j][0], 'red')
                    elif value[3] == 'c':
                        values += colored(self.squares[i][j][0], 'yellow')
                    else:
                        values += colored(self.squares[i][j][0], 'green')
                elif self.squares[i][j][1] == 'B':
                    values += colored(self.squares[i][j][0], 'magenta')
                elif self.squares[i][j][1] == 'W':
                    values += colored(self.squares[i][j][0], 'white')
                else:
                    values += ' '
                values += ' '
            print(line + values + board_delimiter + ' ' + letters[i].upper() + ' |')
        print('|   ' + board_delimiter * ((2 * len(self.squares[0])) + 3) + '   | {}'.format(
            'Killed by W:' + ' '.join(self.black_deaths) if len(self.black_deaths) else ''))
        print('|     ' + ' '.join([str(i + 1) for i in range(len(self.squares[0]))]) + '     |')
        print(' ' + ('-' * (2 * len(self.squares[0]) + 9)))
        white_timer.print_timer()
        black_timer.print_timer()

    def move_piece(self, pos, pos2):
        """
        This method moves a piece from one square of the board to another one
        :param pos: (tuple) Source of the piece.
        :param pos2: (tuple) Target of the piece.
        """
        pos_val = self.get_pos_val(pos)
        targ_val = self.get_pos_val(pos2)

        turn = pos_val[1]

        self.put_pos_val(pos2, ''.join(pos_val))
        self.put_pos_val(pos, '     ')

        if targ_val[0:4] != '    ':
            self.add_death(targ_val[0:2])
            new_val = list(pos_val)
            new_val[2] = 'k'
            self.put_pos_val(pos2, "".join(new_val))

        logging.getLogger('log1').warning(
            '{} {}'.format(pos, pos2))
        logging.getLogger('log2').warning(
            messages['MOVE_DONE'].format(pos_val[1], pos_val[0], pos, pos2))
        if targ_val[0].lower() == 'k':
            self.print_board_in_terminal()
            print(messages['PLAYER_WIN'].format(pos_val[1]))
            exit()

        if pos_val[0].lower() == 'p' and \
                ((pos2[0] == 0 and
                  pos_val[1].lower() == 'w') or
                 (pos2[0] == len(self.squares) - 1 and
                  pos_val[1].lower() == 'b')):
            self.promote(pos2, pos_val)

        self.check_if_check(pos_val[1])

        if turn == 'W':
            white_timer.pause_time()
            black_timer.start_time()
        else:
            black_timer.pause_time()
            white_timer.start_time()

    def promote(self, position, value):
        """
        This method asks for the player to decide which piece wants
        the pawn to promote to, and doesn't stop asking until a
        correct piece has been given.
        :param position: (tuple) The position where the piece will
            be promoted.
        :param value: (str) The current value of the piece before
            getting promoted.
        """
        correct_piece = False
        piece = ''
        while not correct_piece:
            print(messages['PROMOTE_PAWN'])
            piece = str(sys.stdin.readline()).replace('\n', '')
            correct_piece, piece = self.check_promotable(piece)
        self.put_pos_val(position, piece + value[1:])

    @staticmethod
    def check_promotable(piece):
        """
        This method checks if the given piece number is correct and returns
        the piece name (otherwise returns False and the number.)
        :param piece: (int) The number given by the user.
        """
        promotions = {1: 'Q', 2: 'H', 3: 'T', 4: 'B'}
        if int(piece) not in range(1, 5):
            return False, piece
        return True, promotions[int(piece)]

    def check_free_ways(self, movs, pos, pos2, att_rng=15, show=False):
        """
        This method checks all the possible directions of a piece to see
        if a given movement is possible without having any obstacle on
        the way.
        :param movs: (list of tuples). Possible directions of the piece.
        :param pos: (tuple) Source of the piece.
        :param pos2: (tuple) Target of the piece.
        :param att_rng: (int) The attack range of the piece.
        :param show: (bool) If this method has to print the results.
        :return: (bool) If the movement is possible.
        """
        for mov in movs:
            if self.check_free_way(mov, pos, pos2, att_rng, show):
                return 1
        return 0

    def check_free_way(self, mov, pos, pos2, att_rng, show=False):
        """
        This method checks all the possible directions of a piece to see
        if a given movement is possible without having any obstacle on
        the way.
        :param mov: (tuples). A possible direction of the piece.
        :param pos: (tuple) Source of the piece.
        :param pos2: (tuple) Target of the piece.
        :param att_rng: (int) The attack range of the piece.
        :param show: (bool) If this method has to print the results.
        :return: (bool) If the movement is possible.
        """
        incorrect_movement = False
        for n in range(1, att_rng + 1):
            if pos2[0] == pos[0] + (mov[0] * n) and \
               pos2[1] == pos[1] + (mov[1] * n):
                for j in range(n - 1, 0, -1):
                    if self.get_pos_val((pos[0] + (mov[0] * j),
                                         pos[1] + (mov[1] * j))) != '     ':
                        incorrect_movement = True
                if mov in [[2, 0], [-2, 0]]:
                    if self.get_pos_val((pos[0] + (mov[0] / 2),
                                         pos[1])) != '     ':
                        incorrect_movement = True
                if not incorrect_movement:
                    if self.get_pos_val(pos2)[1] == \
                       self.get_pos_val(pos)[1]:
                        if show:
                            print(messages['OWN_ATTACK'])
                        return 0
                    return 1
        return 0

    def check_correct_move(self, pos, pos2, show=False):
        """
        This method checks if a move is possible.
        :param pos: (tuple) Source of the piece.
        :param pos2: (tuple) Target of the piece.
        :param show: (bool) If the results have to be printed.
        :return: (bool) If the move is correct.
        """
        piece_type = self.get_pos_val(pos)[0].lower()
        if piece_type != 'p':
            try:
                movs = movements[piece_type]
            except KeyError:
                return 0
            if piece_type == 'h' or piece_type == 'k':
                return self.check_free_ways(movs, pos, pos2, 1, True)
            else:
                return self.check_free_ways(movs, pos, pos2, 15, True)
        else:
            value_in_pos = self.get_pos_val(pos)
            value_in_tgt = self.get_pos_val(pos2)
            if value_in_pos[1] == 'W':
                movs = list(movements['p_w'])
            else:
                movs = list(movements['p_b'])
            if value_in_tgt != '    ':
                if value_in_pos[1] == 'W':
                    movs.extend(movements['p_attack_w'])
                else:
                    movs.extend(movements['p_attack_b'])
            if self.is_first_pawn_movement(pos):
                if value_in_pos[1] == 'W':
                    movs.extend(movements['p_first_move_w'])
                else:
                    movs.extend(movements['p_first_move_b'])

            for mov in movs:
                if self.check_free_way(mov, pos, pos2, 1, True):
                    if value_in_tgt[1] == value_in_pos[1]:
                        if show:
                            print(messages['OWN_ATTACK'])
                        return 0
                    return 1
        if show:
            print(messages['WRONG_MOVEMENT'])
        return 0

    def is_first_pawn_movement(self, pos):
        """
        This method checks if its the first movement of the given pawn.
        :param pos: (tuple) Position of the pawn.
        :return: (bool) True if the pawn is in its original position,
            false otherwise.
        """
        return (pos[0] == 1 and
                self.get_pos_val(pos)[1] == 'B') or \
               (pos[0] == len(self.squares) - 2 and
                self.get_pos_val(pos)[1] == 'W')

    def check_if_check(self, turn):
        """
        This method checks if in the current state of the board, there is
        any piece checking the opponents king. If there is, it updates its
        state to be shown differently to the user.
        :param turn: (str) the current turn.
        """
        king = self.find_king(self.obtain_other_turn(turn))
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                value = self.get_pos_val((i, j))
                if value[1].upper() == turn.upper():
                    if self.check_correct_move((i, j), king):
                        new_val = list(value)
                        new_val[3] = 'c'
                        self.put_pos_val((i, j), "".join(new_val))

    def find_king(self, turn):
        """
        This method searches for the king of a given color, and returns
        its position.
        :param turn: (str) The color of the wanted king.
        :return: (tuple) The position of the king.
        """
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                if self.squares[i][j][0:2] == 'K' + turn.upper():
                    return i, j

    @staticmethod
    def obtain_other_turn(turn):
        """
        This method returns the opposite turn given a turn.
        :param turn: (str) The given turn.
        :return: (str) The opposite to the given turn.
        """
        if turn.lower() == 'w':
            return 'b'
        else:
            return 'w'

    def add_death(self, piece):
        """
        This method adds a piece to its list of deaths.
        :param piece: (str) the name of the piece.
        """
        if piece[1] == 'B':
            self.black_deaths.append(piece[0])
        else:
            self.white_deaths.append(piece[0])

    def check_movements(self, pos):
        piece_type = self.get_pos_val(pos)[0].lower()
        value = self.get_pos_val(pos)
        if piece_type != 'p':
            try:
                moves = movements[piece_type]
            except KeyError:
                return 0
            if piece_type == 'h' or piece_type == 'k':
                mov_range = 2
            else:
                mov_range = 15
            for mov in moves:
                for i in range(1, mov_range):
                    new_pos = (pos[0] + (mov[0] * i),
                               pos[1] + (mov[1] * i))
                    if new_pos[0] in range(0, 8) and new_pos[1] in range(0, 8):
                        new_val = self.get_pos_val(new_pos)
                        if new_val[1] != value[1] or new_val[0:4] == '    ':
                            new_val = list(new_val)
                            new_val[4] = 'l'
                            self.put_pos_val(new_pos, "".join(new_val))
                            if "".join(new_val)[0:4] != '    ':
                                break
                        else:
                            break
                    else:
                        break
        else:
            if value[1] == 'W':
                moves = list(movements['p_w'])
                for m in movements['p_attack_w']:
                    poss_att = (pos[0] + m[0],
                                pos[1] + m[1])
                    if poss_att[0] in range(0, 8) and poss_att[1] in range(0, 8):
                        if self.get_pos_val(poss_att)[1].lower() == 'b':
                            moves.append(m)
            else:
                moves = list(movements['p_b'])
                for m in movements['p_attack_b']:
                    poss_att = (pos[0] + m[0],
                                pos[1] + m[1])
                    if poss_att[0] in range(0, 8) and poss_att[1] in range(0, 8):
                        if self.get_pos_val(poss_att)[1].lower() == 'w':
                            moves.append(m)
            if self.is_first_pawn_movement(pos):
                if value[1] == 'W':
                    moves.extend(movements['p_first_move_w'])
                else:
                    moves.extend(movements['p_first_move_b'])
            print(moves)
            for mov in moves:
                new_pos = (pos[0] + mov[0],
                           pos[1] + mov[1])
                if new_pos[0] in range(0, 8) and new_pos[1] in range(0, 8):
                    new_val = self.get_pos_val(new_pos)
                    if new_val[1] != value[1] or new_val[0:4] == '    ':
                        new_val = list(new_val)
                        new_val[4] = 'l'
                        self.put_pos_val(new_pos, "".join(new_val))

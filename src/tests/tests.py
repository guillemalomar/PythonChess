import unittest
from src.obtain_values.obtain_values import obtain_pos_value, obtain_v_coord
from src.conf.board_init import board_init
from src.moves.moves import move_piece
from src.input_output.inputs import choose_piece, choose_move
from src.checks.checks import check_in_board, check_correct_move


class ObtainValuesTests(unittest.TestCase):

    board = board_init(8, 8)

    def test_obtainpos(self):
        position = obtain_pos_value('a1', self.board)
        self.assertEqual(position, 'TB')

        position = obtain_pos_value('c1', self.board)
        self.assertEqual(position, '  ')

        position = obtain_pos_value('x1', self.board)
        self.assertEqual(position, False)

    def test_obtainvcoord(self):
        position = obtain_v_coord('a')
        self.assertEqual(position, 0)

        position = obtain_v_coord('c')
        self.assertEqual(position, 2)

        position = obtain_v_coord(1)
        self.assertEqual(position, False)


class MovesTests(unittest.TestCase):

    board = board_init(8, 8)

    def test_movepiece(self):
        board = move_piece('b2', 'b3', self.board)
        self.assertEqual(obtain_pos_value('b2', board), '  ')
        self.assertEqual(obtain_pos_value('b3', board), 'PB')


class InputOutputTests(unittest.TestCase):

    board = board_init(8, 8)

    def test_input_piece(self):
        position = choose_piece('W', self.board, 'g1')
        self.assertEqual(position, 'g1')

    def test_input_piece_wrong(self):
        position = choose_piece('W', self.board, '01')
        self.assertEqual(position, 0)

    def test_input_piece_wrong2(self):
        position = choose_piece('W', self.board, '0112')
        self.assertEqual(position, 0)

    def test_input_move(self):
        target = choose_move(self.board, 'g1')
        self.assertEqual(target, 'g1')

    def test_input_move_wrong(self):
        target = choose_move(self.board, 'g0')
        self.assertEqual(target, 0)


class BoardInitTests(unittest.TestCase):

    def test_boardinit(self):
        board = board_init(8, 8)
        self.assertEqual(board[0][0], 'TB')

    def test_boardinit2(self):
        board = board_init(8, 8)
        self.assertEqual(board[7][0], 'TW')

    def test_boardinit3(self):
        board = board_init(8, 10)
        self.assertFalse(board[7][0] == 'TW')

    def test_boardinit4(self):
        board = board_init(8, 10)
        self.assertEqual(board[9][0], 'TW')


class CheckTests(unittest.TestCase):

    board = board_init(8, 8)

    def test_in_board(self):
        self.assertTrue(check_in_board('a1', self.board))
        self.assertFalse(check_in_board('a0', self.board))

    def test_correct_move(self):
        self.assertTrue(check_correct_move('b2', 'c2', self.board))
        self.assertFalse(check_correct_move('b2', 'c3', self.board))
        self.assertFalse(check_correct_move('b2', 'b2', self.board))

import unittest
from src.board.board import Board


class ObtainValuesTests(unittest.TestCase):

    board = Board(8, 8)

    def test_obtainpos(self):
        position = self.board.obtain_pos_value((0, 0))
        self.assertEqual(position, 'TB')

        position = self.board.obtain_pos_value((2, 0))
        self.assertEqual(position, '  ')

        position = self.board.obtain_pos_value((10, 1))
        self.assertEqual(position, False)


class MovesTests(unittest.TestCase):

    board = Board(8, 8)

    def test_movepiece(self):
        self.board.move_piece((1, 1), (2, 1))
        self.assertEqual(self.board.obtain_pos_value((1, 1)), '  ')
        self.assertEqual(self.board.obtain_pos_value((1, 2)), 'PB')


class BoardInitTests(unittest.TestCase):

    def test_boardinit(self):
        board = Board(8, 8)
        self.assertEqual(board.positions[0][0], 'TB')

    def test_boardinit2(self):
        board = Board(8, 8)
        self.assertEqual(board.positions[7][0], 'TW')

    def test_boardinit3(self):
        board = Board(8, 10)
        self.assertFalse(board.positions[7][0] == 'TW')

    def test_boardinit4(self):
        board = Board(8, 10)
        self.assertEqual(board.positions[9][0], 'TW')


class CheckTests(unittest.TestCase):

    board = Board(8, 8)

    def test_correct_move(self):
        self.assertTrue(self.board.check_correct_move((1, 1), (2, 1)))
        self.assertFalse(self.board.check_correct_move((1, 1), (2, 2)))
        self.assertFalse(self.board.check_correct_move((1, 1), (1, 1)))

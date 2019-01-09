import random
import unittest
from src.board import Board


class ObtainValuesTests(unittest.TestCase):

    def test_obtainpos(self):

        board = Board(8, 8)
        position = board.obtain_pos_value((0, 0))
        self.assertEqual(position, 'TB  ')

        position = board.obtain_pos_value((2, 0))
        self.assertEqual(position, '    ')

        position = board.obtain_pos_value((10, 1))
        self.assertEqual(position, False)

    def test_find_king(self):
        board = Board(8, 8)
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        board.assign_pos_value((0, 4), '    ')
        board.assign_pos_value((i, j), 'KB  ')
        self.assertEqual(board.find_king('B'), (i, j))
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        board.assign_pos_value((7, 4), '    ')
        board.assign_pos_value((i, j), 'KW  ')
        self.assertEqual(board.find_king('W'), (i, j))


class MovesTests(unittest.TestCase):

    board = Board(8, 8)

    def test_movepiece(self):
        self.board.move_piece((1, 1), (2, 1))
        self.assertEqual(self.board.obtain_pos_value((1, 1)), '    ')
        self.assertEqual(self.board.obtain_pos_value((1, 2)), 'PB  ')


class BoardInitTests(unittest.TestCase):

    def test_boardinit(self):
        board = Board(8, 8)
        self.assertEqual(board.positions[0][0], 'TB  ')

    def test_boardinit2(self):
        board = Board(8, 8)
        self.assertEqual(board.positions[7][0], 'TW  ')

    def test_boardinit3(self):
        board = Board(8, 10)
        self.assertFalse(board.positions[7][0] == 'TW  ')

    def test_boardinit4(self):
        board = Board(8, 10)
        self.assertEqual(board.positions[9][0], 'TW  ')


class CheckTests(unittest.TestCase):

    def test_correct_move(self):
        board = Board(8, 8)
        self.assertTrue(board.check_correct_move((1, 1), (2, 1)))
        self.assertFalse(board.check_correct_move((1, 1), (2, 2)))
        self.assertFalse(board.check_correct_move((1, 1), (1, 1)))

    def test_check_if_check(self):
        board = Board(8, 8)
        board.assign_pos_value((0, 3), 'QW  ')
        board.check_if_check('W')
        self.assertEqual(board.obtain_pos_value((0, 3)), 'QW c')

    def test_check_is_pawn_first_movement(self):
        board = Board(8, 8)
        self.assertEqual(board.is_first_pawn_movement((1, 1)), True)

        board.assign_pos_value((2, 1), 'PB  ')
        self.assertEqual(board.is_first_pawn_movement((2, 1)), False)
        
    def test_check_free_way(self):
        board = Board(8, 8)
        self.assertTrue(board.check_free_way([2, 0], (1, 0), (3, 0), 1))

        board = Board(8, 8)
        board.assign_pos_value((2, 0), 'QW  ')
        board.print_board_in_terminal()
        self.assertFalse(board.check_free_way([2, 0], (1, 0), (3, 0), 1))

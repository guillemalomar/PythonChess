import random
import unittest
from src.board import Board


class ObtainValuesTests(unittest.TestCase):

    def setUp(self):
        self.board = Board(8, 8)

    def test_obtainpos(self):

        position = self.board.get_pos_val((0, 0))
        self.assertEqual(position, 'TB  ')

        position = self.board.get_pos_val((2, 0))
        self.assertEqual(position, '    ')

        position = self.board.get_pos_val((10, 1))
        self.assertEqual(position, False)

    def test_find_king(self):
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        self.board.put_pos_val((0, 4), '    ')
        self.board.put_pos_val((i, j), 'KB  ')
        self.assertEqual(self.board.find_king('B'), (i, j))
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        self.board.put_pos_val((7, 4), '    ')
        self.board.put_pos_val((i, j), 'KW  ')
        self.assertEqual(self.board.find_king('W'), (i, j))


class MovesTests(unittest.TestCase):

    def setUp(self):
        self.board = Board(8, 8)

    def test_movepiece(self):
        self.board.move_piece((1, 1), (2, 1))
        self.assertEqual(self.board.get_pos_val((1, 1)), '    ')
        self.assertEqual(self.board.get_pos_val((1, 2)), 'PB  ')


class BoardInitTests(unittest.TestCase):

    def setUp(self):
        self.board = Board(8, 8)

    def test_boardinit(self):
        self.assertEqual(self.board.squares[0][0], 'TB  ')

    def test_boardinit2(self):
        self.assertEqual(self.board.squares[7][0], 'TW  ')

    def test_boardinit3(self):
        board = Board(8, 10)
        self.assertFalse(board.squares[7][0] == 'TW  ')

    def test_boardinit4(self):
        board = Board(8, 10)
        self.assertEquals(board.squares[9][0], 'TW  ')


class CheckTests(unittest.TestCase):

    def setUp(self):
        self.board = Board(8, 8)

    def test_correct_move(self):
        self.assertTrue(self.board.check_correct_move((1, 1), (2, 1)))
        self.assertFalse(self.board.check_correct_move((1, 1), (2, 2)))
        self.assertFalse(self.board.check_correct_move((1, 1), (1, 1)))

    def test_check_if_check(self):
        self.board.put_pos_val((0, 3), 'QW  ')
        self.board.check_if_check('W')
        self.assertEqual(self.board.get_pos_val((0, 3)), 'QW c')

    def test_check_if_killer(self):
        self.board.put_pos_val((0, 2), 'QW  ')
        self.board.move_piece((0, 2), (0, 1))
        self.assertEqual(self.board.get_pos_val((0, 1)), 'QWk ')

    def test_check_add_death(self):
        self.board.put_pos_val((0, 2), 'QW  ')
        self.board.move_piece((0, 2), (0, 1))
        self.assertTrue('H' in self.board.black_deaths)

    def test_obtain_other_turn(self):
        self.assertEquals(self.board.obtain_other_turn('W'), 'b')
        self.assertEquals(self.board.obtain_other_turn('B'), 'w')

    def test_check_is_pawn_first_movement(self):
        self.assertEqual(self.board.is_first_pawn_movement((1, 1)), True)

        self.board.put_pos_val((2, 1), 'PB  ')
        self.assertEqual(self.board.is_first_pawn_movement((2, 1)), False)
        
    def test_check_free_way(self):
        self.assertTrue(self.board.check_free_way([2, 0], (1, 0), (3, 0), 1))

        self.board.put_pos_val((2, 0), 'QW  ')
        self.assertFalse(self.board.check_free_way([2, 0], (1, 0), (3, 0), 1))

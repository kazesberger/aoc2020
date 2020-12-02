import unittest
import second
from timeit import timeit


class TestFirst(unittest.TestCase):

    def test_is_valid(self):
        self.assertTrue(second.is_valid('asdfa', (1, 2, 'a')))
        self.assertFalse(second.is_valid('asdfaa', (1, 2, 'a')))
        self.assertTrue(second.is_valid('asdfaa', (1, 4, 'a')))
        self.assertFalse(second.is_valid('asdfaa', (1, 4, 'b')))

    def test_is_valid_p2(self):
        self.assertTrue(second.is_valid_p2('abcde', (1, 3, 'a')))
        self.assertFalse(second.is_valid_p2('cdefg', (1, 3, 'b')))
        self.assertFalse(second.is_valid_p2('ccccccccc', (2, 9, 'c')))

    def test_parse_line(self):
        self.assertEqual(second.parse_line('15-16 l: klfbblslvjclmlnqklvg'), ('klfbblslvjclmlnqklvg', (15, 16, 'l')))

    def test_part1_test_input(self):
        self.assertEqual(second.solve_part1(second.get_puzzle_input(test=True)), 2)

    def test_part2_test_input(self):
        self.assertEqual(second.solve_part2(second.get_puzzle_input(test=True)), 1)


if __name__ == '__main__':
    unittest.main()

import unittest
import third


class TestFirst(unittest.TestCase):

    def test_part1_test_input(self):
        self.assertEqual(third.solve_part1(third.get_puzzle_input(test=True)), 7)

    def test_part2_test_input(self):
        self.assertEqual(third.solve_part1(third.get_puzzle_input(test=True), 1), 2)
        self.assertEqual(third.solve_part1(third.get_puzzle_input(test=True), 5), 3)
        self.assertEqual(third.solve_part1(third.get_puzzle_input(test=True), 7), 4)
        self.assertEqual(third.solve_part1(third.get_puzzle_input(test=True), shift_right=1, shift_down=2), 2)


if __name__ == '__main__':
    unittest.main()

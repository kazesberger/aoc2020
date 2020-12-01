import unittest
import first
from timeit import timeit

test_input = [1721, 979, 366, 299, 675, 1456]
test_solution1 = 514579
solution1 = 870331


def get_puzzle_input():
    with open('input.txt', 'r') as f:
        return list(map(int, f))


class TestFirst(unittest.TestCase):
    def test_get_tuples(self):
        expected_result = {(299, 366),
                           (299, 675),
                           (299, 979),
                           (299, 1456),
                           (299, 1721),
                           (366, 299),
                           (366, 675),
                           (366, 979),
                           (366, 1456),
                           (366, 1721),
                           (675, 299),
                           (675, 366),
                           (675, 979),
                           (675, 1456),
                           (675, 1721),
                           (979, 299),
                           (979, 366),
                           (979, 675),
                           (979, 1456),
                           (979, 1721),
                           (1456, 299),
                           (1456, 366),
                           (1456, 675),
                           (1456, 979),
                           (1456, 1721),
                           (1721, 299),
                           (1721, 366),
                           (1721, 675),
                           (1721, 979),
                           (1721, 1456)}

        actual = set(first.get_tuples(test_input))
        # print(actual)
        self.assertEqual(actual, set(expected_result))

    def test_part1_solution1(self):
        self.assertEqual(solution1, first.solution1(get_puzzle_input()))

    def test_part1_solution2(self):
        self.assertEqual(solution1, first.solution2(get_puzzle_input()))

    def test_print_benchmarks(self):
        import first
        puzzle_input = get_puzzle_input()
        print(f'solution1: result={first.solution1(puzzle_input)} time={timeit("first.solution1(puzzle_input)", globals=locals(), number=100)}')
        print(f'solution2: result={first.solution2(puzzle_input)} time={timeit("first.solution2(puzzle_input)", globals=locals(), number=100)}')
        print(f'solve_part2: result={first.solve_part2(puzzle_input)} time={timeit("first.solution2(puzzle_input)", globals=locals(), number=100)}')

    def test_part2_test_input(self):
        self.assertEqual(first.solve_part2(test_input), 241861950)

if __name__ == '__main__':
    unittest.main()

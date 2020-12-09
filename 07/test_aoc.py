import unittest
import aoc


class TestFirst(unittest.TestCase):

    def test_parse_rule(self):
        light_red_rule = ['light', 'red', '1', 'bright', 'white', '2', 'muted', 'yellow']
        self.assertEqual(aoc.get_bag_contents({}, light_red_rule[2:]), {'bright white': 1, 'muted yellow': 2})


if __name__ == '__main__':
    unittest.main()

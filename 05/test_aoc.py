import unittest
import aoc


class TestFirst(unittest.TestCase):

    # FBFBBFF RLR
    # 0101100 101
    # 44      5

    def test_get_seat_id(self):
        self.assertEquals(aoc.get_seat_id('FBFBBFFRLR'), 357)

if __name__ == '__main__':
    unittest.main()

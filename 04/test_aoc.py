import unittest
import aoc


class TestFirst(unittest.TestCase):

    def test_validate_hgt(self):
        self.assertTrue(aoc.validate_height('60in'))
        self.assertTrue(aoc.validate_height('190cm'))
        self.assertFalse(aoc.validate_height('190in'))
        self.assertFalse(aoc.validate_height('190'))

    def test_validate_ecl(self):
        self.assertTrue(aoc.validate_eye_color('brn'))
        self.assertFalse(aoc.validate_eye_color('wat'))


    def test_validate_haircolor(self):
        self.assertTrue(aoc.validate_hair_color('#123abc'))
        self.assertFalse(aoc.validate_hair_color('#123abz'))
        self.assertFalse(aoc.validate_hair_color('#123'))
        self.assertFalse(aoc.validate_hair_color('#1234567'))

    def test_validate_pid(self):
        self.assertTrue(aoc.validate_passport_id('0123456789'))
        self.assertTrue(aoc.validate_passport_id('000000001'))


if __name__ == '__main__':
    unittest.main()

import unittest
from main import find_choc_pairs

class TestFindChocPairs(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(find_choc_pairs([4, 3, -5, 5, -3, -4]), [(3, -3), (4, -4), (5, -5)])

    def test_case_2(self):
        self.assertEqual(find_choc_pairs([3, 2, -3, -2]), [(2, -2), (3, -3)])

    def test_case_3(self):
        self.assertEqual(find_choc_pairs([5, -5, 100]), [(5, -5)])

    def test_case_4(self):
        self.assertEqual(find_choc_pairs([1]), [])

    def test_case_5(self):
        self.assertEqual(find_choc_pairs([1, -1]), [(1, -1)])

    def test_case_6(self):
        self.assertEqual(find_choc_pairs([2, 3, 4]), [])

    def test_case_7(self):
        self.assertEqual(find_choc_pairs([-100, 100, -50, 40, 10]), [(100, -100)])

    def test_case_8(self):
        pairs = [(val, -val) for val in range(1, 100001)]
        self.assertEqual(find_choc_pairs(list(range(-100000, 100001))), pairs)

if __name__ == '__main__':
    unittest.main()
import os
import sys
import unittest

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import get_longest_subarray

class TestGetLongestSubarray(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(get_longest_subarray([1, 2, 3, 4, 5], 5), [2, 3])

    def test_2(self):
        self.assertListEqual(get_longest_subarray([1, 2, 3, 7], 6), [1, 2, 3])

    def test_3(self):
        self.assertListEqual(get_longest_subarray([10, 2, 7, 1, 3, 4, 10], 10), [2, 7, 1])

    def test_4(self):
        self.assertListEqual(get_longest_subarray([1, 2, 3, 4, 5], 15), [1, 2, 3, 4, 5])

    def test_5(self):
        self.assertListEqual(get_longest_subarray([1, 1000, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1], 10), [1, 1, 1, 2, 1, 1, 1, 1, 1])

    def test_6(self):
        self.assertListEqual(get_longest_subarray([1000, 2000, 3000, 4000, 5000], 7000), [3000, 4000])

    def test_7(self):
        self.assertListEqual(get_longest_subarray([1, 3, 3, 3, 1, 4, 4, 1], 7), [1, 3, 3])

    def test_8(self):
        self.assertListEqual(get_longest_subarray([5, 1, 1, 5, 1, 1, 1], 5), [5])

    def test_9(self):
        self.assertListEqual(get_longest_subarray([1]*500000, 500), [1]*500)

if __name__ == "__main__":
    unittest.main()
import unittest
from main import maximum_sum

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(maximum_sum([1, 9, -1, -2, 7, 3, -1, 2, 4, -6], 5), (16, 1))

    def test2(self):
        self.assertEqual(maximum_sum([-2, -3, 4, -1, -2, 1, 5, -3], 5), (7, 2))

    def test3(self):
        self.assertEqual(maximum_sum([-2, -5, 6, -2, -3, 1, 5, -6], 2), (6, 5))

    def test4(self):
        self.assertEqual(maximum_sum([1, 2, 3, 4, 5, -6], 1), (5, 4))

    def test5(self):
        self.assertEqual(maximum_sum([1], 1), (1, 0))

    def test6(self):
        self.assertEqual(maximum_sum([1, -1, 1, -1, 1, -1, 1, -1], 2), (0, 0))

    def test7(self):
        self.assertEqual(maximum_sum([100, 200, 300, 400], 2), (700, 2))

    def test8(self):
        large_array = [i for i in range(1, 100001)]
        k = 50000
        expected_sum = sum(range(50001, 100001))  # Sum of integers from 50001 to 100000
        self.assertEqual(maximum_sum(large_array, k), (expected_sum, 50000))


if __name__ == '__main__':
    unittest.main()
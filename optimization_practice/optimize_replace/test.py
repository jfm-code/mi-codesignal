import unittest
from main import optimizedReplace


class SolutionTests(unittest.TestCase):
    
    def test_example(self):
        A = [10, 20, 30, 40, 50]
        B = [7, 5, 1, 2, 4]
        expected_output = [20, 50, 40, 30, 20]
        self.assertEqual(optimizedReplace(A, B), expected_output)

    def test1(self):
        A = [1]
        B = [1]
        expected_output = [1]
        self.assertEqual(optimizedReplace(A, B), expected_output)

    def test2(self):
        A = [-3, -2, -1]
        B = [-1, -2, -4]
        expected_output = [-2, -3, -2]
        self.assertEqual(optimizedReplace(A, B), expected_output)

    def test3(self):
        A = [2, 0, 3]
        B = [5, 10, 7]
        expected_output = [3, 3, 2]
        self.assertEqual(optimizedReplace(A, B), expected_output)

    def test4(self):
        A = [-1000, 1000, 800, 0, 550]
        B = [-800, 801, 0, -550, 1000]
        expected_output = [0, 550, 0, -1000, 1000]
        self.assertEqual(optimizedReplace(A, B), expected_output)

    def test5(self):
        A = [5, 8, 0, 12, -17]
        B = [9, 2, 4, -100, 8]
        expected_output = [-17, 0, 8, 8, 5]
        self.assertEqual(optimizedReplace(A, B), expected_output)

    def test6(self):
        A = [-1, 3, 7, 0, 2]
        B = [4, 5, 7, 10, 1]
        expected_output = [3, -1, 3, 7, -1]
        self.assertEqual(optimizedReplace(A, B), expected_output)

    def test7(self):
        A = list(range(1, 100001))
        B = [i * i for i in range(100000, 0, -1)]
        expected_output = list(range(2, 100001)) + [99999]
        self.assertEqual(optimizedReplace(A, B), expected_output)


if __name__ == '__main__':
    unittest.main()
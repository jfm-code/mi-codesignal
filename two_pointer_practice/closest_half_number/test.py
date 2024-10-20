import unittest
from main import solution

class TestSolution(unittest.TestCase):
    
    def test1(self):
        X = [4, 12, 3, 9, 6, 1, 5, 8, 37, 25, 100]
        Y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 112, 113, 114, 115, 116]
        expected = [70, 40, 20, 100, 100, 100, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.assertEqual(solution(X,Y), expected)

    def test2(self):
        X = [1, 5, 3, 4, 2]
        Y = [1, 2, 3, 4, 5]
        expected = [1, 1, 1, 5, 5]
        self.assertEqual(solution(X,Y), expected)

    def test3(self):
        X = [10, 24, 30, 40, 50]
        Y = [18, 19, 20, 21, 22]
        expected = [18, 18, 18, 18, 18]
        self.assertEqual(solution(X,Y), expected)

    def test4(self):
        X = [91, 85, 75, 60, 120, 150, 125]
        Y = [24, 48, 150, 210, 76, 98, 45, 97, 77, 107]
        expected = [210, 210, 150, 24, 210, 210, 210, 210, 210, 210]
        self.assertEqual(solution(X,Y), expected)

    def test5(self):
        X = [1, 2, 3, 4, 5]
        Y = [6, 7, 8, 9, 10]
        expected = [8, 8, 9, 9, 10]
        self.assertEqual(solution(X,Y), expected)

    def test6(self):
        X = [100, 200, 130, 170, 160, 180]
        Y = [1000, 2000, 500, 3000, 1500, 3500]
        expected = [2000, 2000, 2000, 2000, 2000, 2000]
        self.assertEqual(solution(X,Y), expected)

    def test7(self):
        X = [24, 43, 77, 89, 23, 456, 778, 123, 55, 33]
        Y = [140, 230, 340, 450, 250, 289, 49, 364, 221, 145, 340, 456, 445, 456, 567]
        expected = [340, 364, 364, 364, 364, 364, 140, 364, 364, 340, 364, 364, 364, 364, 364]
        self.assertEqual(solution(X,Y), expected)

    def test8(self):
        X = list(range(1, 50001))  # Simple sequence from 1 to 50000
        Y = list(range(50000, 100000))  # Simple sequence from 50000 to 99999

        # Generate the expected result
        expected = []
        for y in Y:
            closest_half_index = y // 2 - 1
            expected.append(Y[closest_half_index])

        result = solution(X, Y)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
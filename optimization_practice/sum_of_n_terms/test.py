import unittest
from main import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(1, 5), 15)

    def test2(self):
        self.assertEqual(solution(5, 1), 15)

    def test3(self):
        self.assertEqual(solution(1, 1), 1)

    def test4(self):
        self.assertEqual(solution(500, 500), 500)

    def test5(self):
        self.assertEqual(solution(1, 500), 125250)

    def test6(self):
        self.assertEqual(solution(123, 321), 44178)

    def test7(self):
        self.assertEqual(solution(1, 1000000000), 500000000500000000)

if __name__ == '__main__':
    unittest.main()
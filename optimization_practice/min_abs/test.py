import unittest
from main import solution


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), 1)

    def test2(self):
        self.assertEqual(solution([1]), 0)
        
    def test3(self):
        self.assertEqual(solution([3, 1]), 2)
        
    def test4(self):
        self.assertEqual(solution([-1, 0, 1]), 1)
        
    def test5(self):
        self.assertEqual(solution([-100]), 0)
        
    def test6(self):
        self.assertEqual(solution([1, 10, 36, 60]), 9)
        
    def test7(self):
        self.assertEqual(solution([-10, -1, 0, 1, 15]), 1)
        
    def test8(self):
        self.assertEqual(solution([69, -98, 34, 21, -19]), 13)
        
    def test9(self):
        self.assertEqual(solution([0, 0]), 0)

    def test10(self):
        self.assertEqual(solution(list(range(1000000))), 1)


if __name__ == '__main__':
    unittest.main()
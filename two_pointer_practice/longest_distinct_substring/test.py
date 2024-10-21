import os
import sys
import unittest

# these lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("acaabcc", 2), 4)

    def test2(self):
        self.assertEqual(solution("aaaaaaa", 1), 7)

    def test3(self):
        self.assertEqual(solution("abcabcabcabc", 3), 12)

    def test4(self):
        self.assertEqual(solution("abcabcabcabc", 2), 2)

    def test5(self):
        self.assertEqual(solution("AaAaAa", 1), 1)

    def test6(self):
        self.assertEqual(solution("1234567890", 10), 10)

    def test7(self):
        self.assertEqual(solution("", 1), 0)

    def test8(self):
        self.assertEqual(solution("abcabcabcabc", 4), 12)

    def test9(self):
        self.assertEqual(solution("1"*50000 + "2"*50000, 2), 100000)

if __name__ == '__main__':
    unittest.main()
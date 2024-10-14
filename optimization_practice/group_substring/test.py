import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import string_partition


class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(string_partition("abacbc"), [6])

    def test2(self):
        self.assertEqual(string_partition("a"), [1])

    def test3(self):
        self.assertEqual(string_partition("abc"), [1, 1, 1])

    def test4(self):
        self.assertEqual(string_partition("aaabbbccc"), [3, 3, 3])
        
    def test5(self):
        self.assertEqual(string_partition("zabacbcz"), [8])
        
    def test6(self):
        self.assertEqual(string_partition("abcabcabc"), [9])
        
    def test7(self):
        self.assertEqual(string_partition("abacdcd"), [3, 4])
        
    def test8(self):
        self.assertEqual(string_partition("feepplkpadaasdr"), [1, 2, 5, 6, 1])

    def test9(self):
        self.assertEqual(string_partition("a" * 1000000), [1000000])

if __name__ == '__main__':
    unittest.main()
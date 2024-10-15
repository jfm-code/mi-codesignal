import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from main import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertDictEqual(solution(['dog', 'cat', 'bird', 'cat', 'dog', 'elephant', 'dog']), {'dog': 2, 'cat': 2})

    def test2(self):
        self.assertDictEqual(solution(['rain', 'rain', 'go', 'away']), {'rain': 1})

    def test3(self):
        self.assertDictEqual(solution(['foo', 'bar', 'foo', 'bar', 'foo']), {'foo': 2, 'bar': 2})

    def test4(self):
        self.assertDictEqual(solution(['a', 'b', 'c', 'a', 'b', 'c', 'a']), {'a': 3, 'b': 3, 'c': 3})

    def test5(self):
        self.assertDictEqual(solution(['apple', 'banana', 'carrot', 'apple', 'eggplant', 'banana', 'apple']), {'banana': 4, 'apple': 3})

    def test6(self):
        self.assertDictEqual(solution(['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'x', 'y']), {'x': 2, 'y': 2, 'z': 3})

    def test7(self):
        self.assertDictEqual(solution(['python', 'java', 'csharp', 'javascript', 'python', 'java', 'python']), {'python': 2, 'java': 4})

    def test8(self):
        self.assertDictEqual(solution(['python', 'python', 'python', 'python', 'python']), {'python': 1})

    def test9(self):
        word_list = ["word"] * (10**5 - 1)
        word_list.append("anotherword")
        expected_output = {"word": 1}
        self.assertDictEqual(solution(word_list), expected_output)

if __name__ == '__main__':
    unittest.main()
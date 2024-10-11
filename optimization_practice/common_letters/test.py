import unittest
from main import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("hello", ['h', 'a', 'e', 'i', 'o', 'u']), ['e', 'h', 'o'])

    def test2(self):
        self.assertEqual(solution("world", ['w', 'o', 'r', 'l', 'd']), ['d', 'l', 'o', 'r', 'w'])

    def test3(self):
        self.assertEqual(solution("python", ['a', 'b', 'c']), [])

    def test4(self):
        self.assertEqual(solution('a'*500, ['a', 'b', 'c']), ['a'])

    def test5(self):
        self.assertEqual(solution('', ['a', 'b', 'c']), [])

    def test6(self):
        self.assertEqual(solution('abcdefghij'*100000, 'a'*999990+'dkaablpp'), ['a', 'b', 'd'])


if __name__ == '__main__':
    unittest.main()
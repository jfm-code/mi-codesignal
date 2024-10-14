import unittest
from main import solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(solution("Hello, world!"), ('l', 2))

    def test_case_2(self):
        self.assertEqual(solution("Life is like a box of chocolates"), ('i', 3))

    def test_case_3(self):
        self.assertEqual(solution("1... 2... 3... Go!"), ('.', 3))

    def test_case_4(self):
        self.assertEqual(solution("A quick brown fox jumps over the lazy dog."), ('o', 4))

    def test_case_5(self):
        self.assertEqual(solution("Python is fun!"), ('n', 2))

    def test_case_6(self):
        self.assertEqual(solution("To be, or not to be: that is the question."), ('o', 5))

    def test_case_7(self):
        self.assertEqual(solution("Winners never quit and quitters never win."), ('i', 4))

    def test_case_8(self):
        self.assertEqual(solution("May the force be with you."), ('e', 3))

    def test_case_9(self):
        self.assertEqual(solution("In the end, it's not the years in your life that count. It's the life in your years."), ('t', 6))

    def test_case_10(self):
        self.assertEqual(solution("Whether you think you can or you think you can’t, you’re right."), ('t', 4))

if __name__ == "__main__":
    unittest.main()
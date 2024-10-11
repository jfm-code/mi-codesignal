import unittest
from main import solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        input1 = ["mars", "jupiter", "venus", "earth"]
        input2 = ["earth", "mars", "neptune"]
        expected_output = [True, False, False, True]
        self.assertEqual(solution(input1, input2), expected_output)

    def test_case_2(self):
        input1 = ["venus"]
        input2 = ["venus"]
        expected_output = [True]
        self.assertEqual(solution(input1, input2), expected_output)

    def test_case_3(self):
        input1 = ["earth", "mars"]
        input2 = ["mars", "earth"]
        expected_output = [True, True]
        self.assertEqual(solution(input1, input2), expected_output)

    def test_case_4(self):
        input1 = ["jupiter", "saturn", "neptune"]
        input2 = ["neptune"]
        expected_output = [False, False, True]
        self.assertEqual(solution(input1, input2), expected_output)

    def test_case_5(self):
        input1 = ["mars"]
        input2 = []
        expected_output = [False]
        self.assertEqual(solution(input1, input2), expected_output)

    def test_case_6(self):
        input1 = ["jupiter", "jupiter"]
        input2 = ["jupiter"]
        expected_output = [True, True]
        self.assertEqual(solution(input1, input2), expected_output)

    def test_case_7(self):
        input1 = ["mars", "venus", "earth", "neptune", "saturn"]
        input2 = ["mars", "jupiter", "saturn"]
        expected_output = [True, False, False, False, True]
        self.assertEqual(solution(input1, input2), expected_output)

    def test_case_8(self):
        input1 = ["b", "c", "cac", "h", "d", "dj", "baba", "ab", "ba", "ab"] * 100000
        input2 = ["a", "b", "e", "h", "j", "p"] * 100000 + ["bab", "cac"] * 200000
        expected_output = [True, False, True, True, False, False, False, False, False, False] * 100000
        self.assertEqual(solution(input1, input2), expected_output)

if __name__ == "__main__":
    unittest.main()
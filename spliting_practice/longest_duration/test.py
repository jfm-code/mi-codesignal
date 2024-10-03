import unittest
from main import solution

class SolutionTest(unittest.TestCase):
    def test_case1(self):
        logs = "1 borrow 09:00, 2 borrow 10:00, 1 return 12:00, 3 borrow 13:00, 2 return 15:00, 3 return 16:00"
        self.assertEqual(solution(logs), [(2, '05:00')])

    def test_case2(self):
        logs = "1 borrow 09:00, 2 borrow 10:00, 1 return 16:00, 3 borrow 13:00, 2 return 15:00, 3 return 16:00"
        self.assertEqual(solution(logs), [(1, '07:00')])

    def test_case3(self):
        logs = "1 borrow 05:00, 1 return 18:00, 2 borrow 08:00, 2 return 17:00"
        self.assertEqual(solution(logs), [(1, '13:00')])

    def test_case4(self):
        logs = "1 borrow 06:00, 2 borrow 07:00, 3 borrow 08:00, 1 return 12:00, 2 return 13:00, 3 return 14:00"
        self.assertEqual(solution(logs), [(1, '06:00'), (2, '06:00'), (3, '06:00')])

    def test_case5(self):
        logs = "1 borrow 09:00, 1 return 09:01, 2 borrow 09:02, 2 return 09:03"
        self.assertEqual(solution(logs), [(1, '00:01'), (2, '00:01')])

    def test_case6(self):
        logs = "1 borrow 12:00, 1 return 18:00, 2 borrow 06:00, 2 return 12:00, 3 borrow 00:00, 3 return 06:00"
        self.assertEqual(solution(logs), [(1, '06:00'), (2, '06:00'), (3, '06:00')])

    def test_case7(self):
        logs = "1 borrow 01:00, 1 return 04:00, 2 borrow 02:00, 2 return 05:00"
        self.assertEqual(solution(logs), [(1, '03:00'), (2, '03:00')])

    def test_case8(self):
        logs = "1 borrow 01:00, 1 return 02:00, 2 borrow 03:00, 2 return 05:00, 1 borrow 06:00, 1 return 10:00"
        self.assertEqual(solution(logs), [(1, '05:00')])

if __name__ == "__main__":
    unittest.main()
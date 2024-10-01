import unittest
from main import analyze_competition

class TestAnalyzeCompetition(unittest.TestCase):

    def test_1(self):
        log_string = "1 fail 09:00, 1 solve 10:00 50, 2 solve 11:00 60, 3 solve 12:00 70, 2 fail 13:00, 3 fail 14:00"
        expected = [(3, 70, 1, 1), (2, 60, 1, 1), (1, 50, 1, 1)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_2(self):
        log_string = "1 solve 10:00 70, 2 solve 11:00 60, 3 solve 12:00 50, 2 fail 13:00, 2 solve 14:00 70"
        expected = [(2, 130, 2, 1), (1, 70, 1, 0), (3, 50, 1, 0)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_3(self):
        log_string = "1 solve 10:00 70, 1 fail 11:00, 3 solve 12:00 80, 2 fail 13:00, 3 fail 14:00"
        expected = [(3, 80, 1, 1), (1, 70, 1, 1)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_4(self):
        log_string = "3 solve 10:00 70, 2 solve 11:00 80, 1 solve 12:00 90, 2 solve 13:00 100, 3 fail 14:00"
        expected = [(2, 180, 2, 0), (1, 90, 1, 0), (3, 70, 1, 1)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_5(self):
        log_string = "1 solve 10:00 60, 1 fail 11:00, 2 solve 12:00 70, 3 fail 13:00, 2 fail 14:00, 3 solve 15:00 80"
        expected = [(3, 80, 1, 1), (2, 70, 1, 1), (1, 60, 1, 1)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_6(self):
        log_string = "2 solve 09:00 50, 2 fail 10:00, 1 solve 11:00 60, 1 fail 12:00, 3 solve 13:00 70"
        expected = [(3, 70, 1, 0), (1, 60, 1, 1), (2, 50, 1, 1)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_7(self):
        log_string = "2 fail 09:00, 1 solve 10:00 50, 3 solve 11:00 60, 1 fail 12:00, 3 fail 13:00, 2 solve 14:00 70"
        expected = [(2, 70, 1, 1), (3, 60, 1, 1), (1, 50, 1, 1)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_8(self):
        log_string = "2 fail 09:00, 3 solve 10:00 50, 2 solve 11:00 60, 1 fail 12:00, 3 fail 13:00, 3 solve 14:00 70"
        expected = [(3, 120, 2, 1), (2, 60, 1, 1)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_9(self):
        log_string = "1 fail 09:00, 2 solve 10:00 50, 3 solve 11:00 70, 1 fail 12:00, 2 solve 13:00 60, 1 solve 14:00 80"
        expected = [(2, 110, 2, 0), (1, 80, 1, 2), (3, 70, 1, 0)]
        self.assertEqual(analyze_competition(log_string), expected)

    def test_10(self):
        log_string = "1 fail 09:00, 2 fail 10:00, 3 solve 11:00 50"
        expected = [(3, 50, 1, 0)]
        self.assertEqual(analyze_competition(log_string), expected)


if __name__ == '__main__':
    unittest.main()
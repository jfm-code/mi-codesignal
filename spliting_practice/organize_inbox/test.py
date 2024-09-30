import unittest
from main import organize_inbox

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        email_str = "JohnDoe@gmail.com, Subject1, 09:00; JaneDoe@gmail.com, Subject2, 10:00; JohnDoe@gmail.com, Subject3, 12:00; Bot@gmail.com, Subject4, 08:00; Bot@gmail.com, Subject5, 09:00"
        expected_result = [('Bot@gmail.com', 2), ('JohnDoe@gmail.com', 2), ('JaneDoe@gmail.com', 1)]
        self.assertEqual(organize_inbox(email_str), expected_result)
        
    def test_case_2(self):
        email_str = "Bot1@gmail.com, Subject1, 09:00; Bot2@gmail.com, Subject2, 10:00; Bot3@gmail.com, Subject3, 12:00; Bot4@gmail.com, Subject4, 13:00"
        expected_result = [('Bot1@gmail.com', 1), ('Bot2@gmail.com', 1), ('Bot3@gmail.com', 1), ('Bot4@gmail.com', 1)]
        self.assertEqual(organize_inbox(email_str), expected_result)

    def test_case_3(self):
        email_str = "Testemail@gmail.com, Subject1, 09:00"
        expected_result = [('Testemail@gmail.com', 1)]
        self.assertEqual(organize_inbox(email_str), expected_result)

    def test_case_4(self):
        email_str = "a@gmail.com, Subject1, 09:00; a@gmail.com, Subject2, 09:00; b@gmail.com, Subject1, 09:00; b@gmail.com, Subject2, 09:00; c@gmail.com, Subject1, 09:00"
        expected_result = [('a@gmail.com', 2), ('b@gmail.com', 2), ('c@gmail.com', 1)]
        self.assertEqual(organize_inbox(email_str), expected_result)

    def test_case_5(self):
        email_str = "JohnDoe@gmail.com, Subject1, 09:00; JaneDoe@gmail.com, Subject2, 10:00; JohnDoe@gmail.com, Subject3, 12:00; Bot@gmail.com, Subject4, 08:00"
        expected_result = [('JohnDoe@gmail.com', 2), ('Bot@gmail.com', 1), ('JaneDoe@gmail.com', 1)]
        self.assertEqual(organize_inbox(email_str), expected_result)

    def test_case_6(self):
        email_str = "a@gmail.com, Subject1, 12:00; b@gmail.com, Subject2, 13:00; a@gmail.com, Subject3, 14:00; a@gmail.com, Subject4, 08:00; b@gmail.com, Subject5, 09:00"
        expected_result = [('a@gmail.com', 3), ('b@gmail.com', 2)]
        self.assertEqual(organize_inbox(email_str), expected_result)


if __name__ == "__main__":
    unittest.main()
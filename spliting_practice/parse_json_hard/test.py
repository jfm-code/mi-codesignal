import unittest
from main import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution('001,Age=25,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n002,Age=30,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com', '001', 'Email', 'johndoe@gmail.com'), 
        [{'001': {'Age': '25', 'Name': 'John', 'Address': {'Street': 'Main St', 'City': 'NY', 'Zip': '10001'}, 'Email': 'johndoe@gmail.com'}}, {'002': {'Age': '30', 'Name': 'Jane', 'Address': {'Street': '2nd St', 'City': 'LA', 'Zip': '90001'}, 'Email': 'jane@hotmail.com'}}])
    def test2(self):
        self.assertEqual(solution('001,Age=25,Name=John,Email=john@gmail.com', '001', 'Age', '30'), [{'001': {'Age': '30', 'Name': 'John', 'Email': 'john@gmail.com'}}])
    def test3(self):
        self.assertEqual(solution('001,Score=80,Subject=(Maths=85;English=75;History=90),Email=john@gmail.com', '001', 'Score', '85'), [{'001': {'Score': '85', 'Subject': {'Maths': '85', 'English': '75', 'History': '90'}, 'Email': 'john@gmail.com'}}])
    def test4(self):
        self.assertEqual(solution('001,Name=John,Email=john@gmail.com\n002,Name=Jane,Email=jane@hotmail.com\n003,Name=Bob,Email=bob@gmail.com', '003', 'Email', 'bob@yahoo.com'), 
        [{'001': {'Name': 'John', 'Email': 'john@gmail.com'}}, {'002': {'Name': 'Jane', 'Email': 'jane@hotmail.com'}}, {'003': {'Name': 'Bob', 'Email': 'bob@yahoo.com'}}])
    def test5(self):
        self.assertEqual(solution('001,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n002,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com', '002', 'Address', '(Street=3rd Ave;City=SF;Zip=94101)'), 
        [{'001': {'Name': 'John', 'Address': {'Street': 'Main St', 'City': 'NY', 'Zip': '10001'}, 'Email': 'john@gmail.com'}}, {'002': {'Name': 'Jane', 'Address': {'Street': '3rd Ave', 'City': 'SF', 'Zip': '94101'}, 'Email': 'jane@hotmail.com'}}])
    def test6(self):
        self.assertEqual(solution('001,Name=John,Email=john@gmail.com', '001', 'Name', 'Johnny'), [{'001': {'Name': 'Johnny', 'Email': 'john@gmail.com'}}])

if __name__ == '__main__':
    unittest.main()
import unittest
from main import find_influencer

class SolutionTests(unittest.TestCase):
    def test01(self):
        self.assertEqual(find_influencer([(100, 200), (200, 300), (100, 300), (100, 400), (400, 500), (500, 600), (200, 600)]), 100)
        
    def test02(self):
        self.assertEqual(find_influencer([(500, 1000), (500, 100), (100, 300), (100, 200), (200, 600), (600, 1000)]), 100)
        
    def test03(self):
        self.assertEqual(find_influencer([(1, 2), (2, 3), (3, 4), (4, 5)]), 3)
        
    def test04(self):
        self.assertEqual(find_influencer([(200, 100), (200, 300), (200, 400), (200, 500)]), 100)
        
    def test05(self):
        self.assertEqual(find_influencer([(1, 2)]), 1)
        
    def test06(self):
        self.assertEqual(find_influencer([(1, 2), (1, 3), (1, 4), (2, 5), (3, 6), (4, 7)]), 1)
        
    def test07(self):
        self.assertEqual(find_influencer([(1, 2), (2, 1)]), 1)
        
    def test08(self):
        self.assertEqual(find_influencer([(1, 2), (2, 3), (3, 1)]), 1)
        
    def test09(self):
        self.assertEqual(find_influencer([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]), 1)
    
    def test10(self):
        connections = [(i, i + 1) for i in range(1, 1001)]
        self.assertEqual(find_influencer(connections), 3)
        

if __name__ == "__main__":
    unittest.main()
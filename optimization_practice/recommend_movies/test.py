import unittest

from main import recommend_movies

class TestSolution(unittest.TestCase):
    def test_1(self):
        user_history = [1, 2, 3, 4, 5]
        popular_movies = [1, 2, 3, 6, 7, 8, 9, 10]
        unpopular_movies = [4, 5, 11]
        expected = [6, 7, 8, 9, 10]
        self.assertEqual(recommend_movies(user_history, popular_movies, unpopular_movies), expected)

    def test_2(self):
        user_history = [10, 20, 30, 40, 50]
        popular_movies = [50, 100, 200, 300, 400, 500]
        unpopular_movies = [30, 40, 500]
        expected = [100, 200, 300, 400]
        self.assertEqual(recommend_movies(user_history, popular_movies, unpopular_movies), expected)

    def test_3(self):
        user_history = []
        popular_movies = [1, 2, 3, 4, 5]
        unpopular_movies = []
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(recommend_movies(user_history, popular_movies, unpopular_movies), expected)

    def test_4(self):
        user_history = [1, 2, 3, 4, 5]
        popular_movies = []
        unpopular_movies = []
        expected = []
        self.assertEqual(recommend_movies(user_history, popular_movies, unpopular_movies), expected)

    def test_5(self):
        user_history = [1, 2, 3, 4, 5]
        popular_movies = [1, 2, 3, 4, 5]
        unpopular_movies = [1, 2, 3, 4, 5]
        expected = []
        self.assertEqual(recommend_movies(user_history, popular_movies, unpopular_movies), expected)
    
    def test_6(self):
        user_history = []
        popular_movies = []
        unpopular_movies = []
        expected = []
        self.assertEqual(recommend_movies(user_history, popular_movies, unpopular_movies), expected)

    def test_7(self):
        user_history = list(range(1, 750001))
        popular_movies = list(range(250000, 1000001))
        unpopular_movies = list(range(1, 1000001))
        expected = []
        self.assertEqual(recommend_movies(user_history, popular_movies, unpopular_movies), expected)

if __name__ == '__main__':
    unittest.main()
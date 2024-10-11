# The result array should contain the IDs of the popular movies that the user has not yet watched, 
# and which are not included in the unpopular_movies array

def recommend_movies(user_history, popular_movies, unpopular_movies):
    user_history = set(user_history)
    popular_movies = set(popular_movies)
    unpopular_movies = set(unpopular_movies)
    result_set = popular_movies - user_history - unpopular_movies
    return sorted(list(result_set))
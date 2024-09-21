import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=b3b8578bcc815b94b4b172469ef4baca&language=en-US")
    data = response.json()
    return 'https://image.tmdb.org/t/p/original' + data["poster_path"]
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distance = similarity[movie_index]
    recommend_movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_list = []
    recommend_movies_poster = []
    for i in recommend_movies_list:
        movies_id = i[0]
        print(movies_id)
        recommend_list.append(movies.iloc[movies_id].original_title)
        recommend_movies_poster.append(fetch_poster(movies_id))
    return recommend_list, recommend_movies_poster


movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

recommend("Avatar")
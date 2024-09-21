import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    try:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=b3b8578bcc815b94b4b172469ef4baca&language=en-US")
        data = response.json()
        return 'https://image.tmdb.org/t/p/original' + data["poster_path"]
    except Exception as e:
        print(e)
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distance = similarity[movie_index]
    recommend_movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_list = []
    recommend_movies_poster = []
    for i in recommend_movies_list:
        movies_id = movies.iloc[i[0]].id
        recommend_list.append(movies.iloc[i[0]].original_title)
        recommend_movies_poster.append(fetch_poster(movies_id))
    return recommend_list, recommend_movies_poster


movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")
option = st.selectbox(
    "How would you like to be contacted?",
    movies['original_title'].values,
)

st.write("You selected:", option)

if st.button("Recommended"):
    names, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)  # Creating 5 columns

    columns = [col1, col2, col3, col4, col5]  # List of columns

    for i in range(5):
        with columns[i]:
            st.text(names[i])
            st.image(posters[i])




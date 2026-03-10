import streamlit as st
import pickle
import pandas as pd
import requests
import gzip

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=9dc40d868e1fc535896b642ddbc990f9&language=en-US"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return ""

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return ""

    except requests.exceptions.RequestException:
        return ""

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(gzip.open('similarity.pkl.gz','rb'))
movies=pd.DataFrame(movies_dict)

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'select movie to see',
    movies['title'].values
)  

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0])

    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1])

    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2])

    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3])

    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4])
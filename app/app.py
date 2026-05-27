import streamlit as st 

st.title("Movie Recommendation System")

from src.recommender import recommend
from src.recommender import movies

#select a movie from the dropdown (a movie you have watched)

selected_movie=st.selectbox("select a movie", movies['title'].values)

if st.button("Recommend"):
    recommendations=recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)

        
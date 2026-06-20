import streamlit as st 
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
st.title("Movie Recommendation System")

from src.recommender import recommend
from src.recommender import movies

#select a movie from the dropdown (a movie you have watched)

selected_movie=st.selectbox("select a movie", movies['title'].values)

if st.button("Recommend"):
    recommendation_movie,recommended_posters=recommend(selected_movie)

    cols=st.columns(5)

    for col,movie,poster in zip(cols,recommendation_movie,recommended_posters):
        col.write(movie)

        if poster:
            col.image(poster)


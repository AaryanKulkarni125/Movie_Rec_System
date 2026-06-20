import pickle
import requests

movies=pickle.load(open("model/movies.pkl",'rb'))
similarity=pickle.load(open("model/similarity.pkl",'rb'))



def recommend(movie):

    if movie not in movies['title'].values:
        return ['Movie not found '], []

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies=[]
    recommended_posters=[]

    for i in movies_list[1:6]:

        mov_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_posters.append(fetch_poster(mov_id))
        

       

    return recommended_movies,recommended_posters

def fetch_poster(movie_id):

    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c3c41f21e49ae0967eae973bf5460954"
    )

    if response.status_code != 200:
        return None

    data = response.json()

    poster_path = data['poster_path']

    if poster_path is None:
        return None

    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path
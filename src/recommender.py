import pickle

movies=pickle.load(open("model/movies.pkl",'rb'))
similarity=pickle.load(open("model/similarity.pkl",'rb'))
vectors=pickle.load(open("model/vectors.pkl",'rb'))
cv=pickle.load(open("model/vocab.pkl",'rb'))


def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in movies_list[1:6]:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations
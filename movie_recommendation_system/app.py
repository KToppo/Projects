import streamlit as st
import pickle
import pandas as pd
import requests


headers = {
    "User-Agent": "Mozilla/5.0",
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTE1MTdlZDNiZDJkODNjYWZlMTFhYjg4ZDZhMzYxOCIsIm5iZiI6MTc1Mjc2NjYzMi40ODUsInN1YiI6IjY4NzkxOGE4NGVmNTM1MDFiNjNkYjZiMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YPFCMiqy2MwuJSQCFRM8kGxeqN9El2C4Fo1qtW7BP48"
}
API_KEY = 'a11517ed3bd2d83cafe11ab88d6a3618'


movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))



def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US",headers=headers)
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommended_movies = []
    recommended_movies_poster = []
    count = 1
    found = 1
    while count <= 5:
        movie_id = movies.iloc[distances[found][0]]
        try:
            recommended_movies_poster.append(fetch_poster(movie_id=movie_id.movie_id))
            recommended_movies.append(movie_id.title)
            count += 1
        except:
            continue
        found += 1
        if found == 25:
            break
    return recommended_movies, recommended_movies_poster


def main():
    st.title('Movie Recommender System')

    selected_movie_name = st.selectbox(
        "Select the movie you like",
        movies['title'],
    )

    if st.button("Recommend"):
        names, posters = recommend(selected_movie_name)
        
        if names != []:
            cols = st.columns(len(names))
            for col, name, poster in zip(cols, names, posters):
                with col:
                    st.text(name)
                    st.image(poster)

        else:
            st.text('Surver error')

if __name__ == '__main__':
    main()
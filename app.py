import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=30ecc73b655558a3cb60f43c77ad5a3a&language=en-US"
    data = requests.get(url).json()

    if 'poster_path' in data and data['poster_path']:
        poster_path = data['poster_path']
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    else:
        full_path = "https://via.placeholder.com/500x750?text=No+Image+Available"

    return full_path


def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_ids = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_ids.append(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].original_title)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_ids


#Streamlit App
st.header('Movie Recommender System')

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

st.markdown("""
    <style>
    .movie-container {
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .movie-container:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
        border-color: #ff6f61;
    }
    </style>
    """, unsafe_allow_html=True)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_ids = recommend(selected_movie)

    col1, col2 = st.columns(2)

    for i in range(0, len(recommended_movie_names)):
        movie_link = f"https://www.themoviedb.org/movie/{recommended_movie_ids[i]}"  # Link to TMDB page
        movie_html = f"""
            <div class="movie-container">
                <h5>{recommended_movie_names[i]}</h5>
                <a href="{movie_link}" target="_blank">
                    <img src="{recommended_movie_posters[i]}" width="100%">
                </a>
            </div>
        """
        if i % 2 == 0:
            with col1:
                st.markdown(movie_html, unsafe_allow_html=True)
        else:
            with col2:
                st.markdown(movie_html, unsafe_allow_html=True)

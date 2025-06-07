import pickle
import streamlit as st
import pandas as pd
import requests
import os

# Load data
try:
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Required data files (movies.pkl and similarity.pkl) are missing. Please ensure they are present in the repository.")
    st.stop()

# TMDB API key
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# Function to get poster from TMDB
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/300x450?text=Poster+Not+Found"

# Cache the recommendation function
@st.cache_data
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return [], []
    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_names = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_names.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_names, recommended_posters

# -------------------- UI ------------------------

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #e74c3c;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #c0392b;
        }
        .recommend-box {
            margin-top: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎬 Movie Recommender System")
st.markdown("Get personalized movie recommendations based on your favorite film.")

movie_list = movies['title'].values
selected_movie = st.selectbox("🔍 Choose a movie you like:", movie_list)

if st.button('🎯 Recommend'):
    with st.spinner('Finding the perfect movies for you...'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        if not recommended_movie_names:
            st.error("Sorry, movie not found.")
        else:
            st.markdown("---")
            st.subheader("📽️ Top 5 Recommendations")
            cols = st.columns(5)
            for i in range(5):
                with cols[i]:
                    st.image(recommended_movie_posters[i], use_container_width=True)
                    st.markdown(f"<div style='text-align:center; font-weight:bold;'>{recommended_movie_names[i]}</div>", unsafe_allow_html=True)

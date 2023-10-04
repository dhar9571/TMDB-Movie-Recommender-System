import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Load the movies DataFrame
movies = pickle.load(open('movies.pkl', 'rb'))

# Load the similarity data
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(name, num_recommendations=10):
    index = movies[movies['title'] == name].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:num_recommendations+1]

    recommended = []
    recommended_movies_posters = []
    for item in movies_list:
        movie_id = movies.iloc[item[0]]['movie_id']
        recommended.append(movies.iloc[item[0]]['title'])
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended, recommended_movies_posters

st.title('Movie Recommender System')

# Get a list of movie titles
movies_list = movies['title'].tolist()

# Create a selection box for movie selection
movie_name = st.selectbox('Select a movie you like', movies_list)

# Style for the "Recommend" button (green with black text)
button_style = """
    <style>
    div.stButton > button:first-child {
        background-color: green !important;
        color: black !important;
    }
    </style>
"""

# Display the button with the custom style
st.markdown(button_style, unsafe_allow_html=True)

if st.button('Recommend'):
    names, posters = recommend(movie_name, num_recommendations=10)
    st.write("Top 10 Recommendations:")

    # Display the selected movie poster
    st.markdown(
        f'<h2 style="text-align:center;">{movie_name}</h2>'
        f'<div style="display: flex; justify-content: center; margin-bottom: 20px;">'
        f'<img src="{fetch_poster(movies[movies["title"] == movie_name].iloc[0]["movie_id"])}" alt="{movie_name}" style="width: 200px;">'
        f'</div>',
        unsafe_allow_html=True
    )

    # Use HTML/CSS to display posters and recommendations horizontally with space
    poster_html = '<div style="display: flex; flex-direction: row; overflow-x: auto;">'
    for recommendation, poster_url in zip(names, posters):
        poster_html += f'<div style="margin-right: 20px;">'
        poster_html += f'<img src="{poster_url}" alt="{recommendation}" style="width: 200px;">'
        poster_html += f'<p>{recommendation}</p>'
        poster_html += f'</div>'
    poster_html += '</div>'

    st.write(poster_html, unsafe_allow_html=True)
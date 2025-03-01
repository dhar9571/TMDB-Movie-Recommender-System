import pandas as pd
import numpy as np 
import joblib 
import pickle 
import gzip
import requests
from utility.params_utils import ParamsUtils


class PrepareData:
    
    def __init__(self):
        self.settings = ParamsUtils.get_configuration("config.yaml")

        # Load the object with decompression
        with gzip.open(self.settings['paths']['movies_obj'], 'rb') as file:
            self.movies = joblib.load(file)

        with gzip.open(self.settings['paths']['credits_obj'], 'rb') as file1:
            self.similarity = joblib.load(file1)
    
    def recommend(self, name, num_recommendations=10):
        index = self.movies[self.movies['title'] == name].index[0]
        distances = self.similarity[index]
        movies_list = sorted(list(enumerate(self.similarity[index])), reverse=True, key=lambda x: x[1])[1:num_recommendations+1]

        recommended = []
        recommended_movies_posters = []
        for item in movies_list:
            movie_id = self.movies.iloc[item[0]]['movie_id']
            recommended.append(self.movies.iloc[item[0]]['title'])
            recommended_movies_posters.append(self.fetch_poster(movie_id))

        return recommended, recommended_movies_posters
    
    
    def fetch_poster(self, movie_id):
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8')
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
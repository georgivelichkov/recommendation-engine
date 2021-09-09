import json
import urllib.parse

import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_shows(title):
    df2 = pd.read_csv('data/tmdb.csv')

    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df2['soup'])

    cosine_similarity(count_matrix, count_matrix)

    df2 = df2.reset_index()
    indices = pd.Series(df2.index, index=df2['title'])
    all_titles = [df2['title'][i] for i in range(len(df2['title']))]

    if title not in all_titles:
        return {"result": "No title found!!"}

    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    sim_scores = list(enumerate(cosine_sim[indices[title]]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return_df = pd.DataFrame(columns=['title', 'year', 'homepage', 'image_url'])
    return_df['title'] = df2['title'].iloc[movie_indices]
    return_df['year'] = df2['release_date'].iloc[movie_indices]
    return_df['homepage'] = df2['homepage'].iloc[movie_indices]
    return_df['image_url'] = get_poster(df2['title'].iloc[movie_indices])

    return return_df


def get_poster(movie_names_df):
    movie_images = []
    for movie_name in movie_names_df:
        response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=d324b54d&t=" + movie_name)
        data = response.json()
        movie_images.append(data['Poster'])

    return movie_images

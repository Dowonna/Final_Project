import pandas as pd
import scipy.sparse as spa

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_data():
        netflix_tmdb_data = pd.read_csv('dataset/netflix_tmdb.csv')
        netflix_tmdb_data['title'] = netflix_tmdb_data['title'].str.lower()
        
        return netflix_tmdb_data

# 영화 배우('cast') 컬럼과 장르('genres') 컬럼을 제외한 나머지를 'combine'이라는 컬럼명으로 병합함
def combine_data(data):
        movie_recommendation = data.drop(columns=['id', 'type', 'title', 'director', 'overview', 'vote_average', 'vote_count'])
        movie_recommendation['combine'] = movie_recommendation[movie_recommendation.columns[0:2]].apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)
        
        movie_recommendation = movie_recommendation.drop(columns=['cast', 'genres'])
        
        return movie_recommendation

# sklean의 'TfidfVectorizer'와 'CountVectorizer' Library 사용
def transform_data(data_combine, data_overview):
        cnt = CountVectorizer(stop_words='english')
        cnt_mtx = cnt.fit_transform(data_combine['combine'])

        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_mtx = tfidf.fit_transform(data_overview['overview'])

        combine_sparse = spa.hstack([cnt_mtx, tfidf_mtx], format='csr')
        cosine_sim = cosine_similarity(combine_sparse, combine_sparse)
        
        return cosine_sim

def recommendate_movies(title, data, combine, transform):
        indices = pd.Series(data.index, index=data['title'])
        index = indices[title]

        similarity_scores = list(enumerate(transform[index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        similarity_scores = similarity_scores[1:11]  # 입력받은 영화와 유사한 Top10 영화를 추출함

        movie_indices = [i[0] for i in similarity_scores]

        movie_id = data['id'].iloc[movie_indices]
        movie_title = data['title'].iloc[movie_indices]
        movie_genres = data['genres'].iloc[movie_indices]

        recommendate_data = pd.DataFrame(columns=['Id', 'Movie_Name', 'Genres'])

        recommendate_data['Id'] = movie_id
        recommendate_data['Movie_Name'] = movie_title
        recommendate_data['Genres'] = movie_genres

        return recommendate_data

def movies_result(movie_name):
        movie_name = movie_name.lower()
        find_movie = get_data()
        combine_result = combine_data(find_movie)
        transform_result = transform_data(combine_result, find_movie)

        if movie_name not in find_movie['title'].unique():
                return 'This Movie does not exist in the DataBase.'
        else:
                recommendations = recommendate_movies(movie_name, find_movie, combine_result, transform_result)
                return recommendations.to_dict('records')
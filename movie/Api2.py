import requests
import json
from pprint import pprint


#以下Api取得用のコード
class TMDB:
    def __init__(self):
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5YTY3MTcwMTA2NTk4ZjgyZjU3NWNkYmM1ZGQxZTM2YSIsInN1YiI6IjY2NjdkMWQ1NTM3YmVkMWE4N2E2YTk5ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.AamXVqqdHzy-HYdk7Hjsz0qU7Oc_UzjbRp_ayVLVmyI"
        self.headers_ = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json;charset=utf-8'}        
        self.base_url_ = 'https://api.themoviedb.org/3/'
        self.img_base_url_ = 'https://image.tmdb.org/t/p/w500'

    def _json_by_get_request(self, url, params={}):
        res = requests.get(url, headers=self.headers_, params=params)
        return json.loads(res.text)   

    def search_movies(self, query):
        params = {'query': query, 'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}search/movie'
        return self._json_by_get_request(url, params)                    

    def get_movie(self, movie_id):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}'
        return self._json_by_get_request(url, params)

    def get_movie_account_states(self, movie_id):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/account_states'
        return self._json_by_get_request(url, params)    

    def get_movie_alternative_titles(self, movie_id, country=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/alternative_titles'
        return self._json_by_get_request(url, params)    

    def get_movie_changes(self, movie_id, start_date=None, end_date=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}'
        return self._json_by_get_request(url, params)    

    def get_movie_credits(self, movie_id):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/credits'
        return self._json_by_get_request(url, params)   

    def get_movie_external_ids(self, movie_id):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/external_ids'
        return self._json_by_get_request(url, params)

    def get_movie_images(self, movie_id, language=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/images'
        return self._json_by_get_request(url, params)        

    def get_movie_keywords(self, movie_id):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/keywords'
        return self._json_by_get_request(url, params)    

    def get_movie_release_dates(self, movie_id):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/release_dates'
        return self._json_by_get_request(url, params)

    def get_movie_videos(self, movie_id, language=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/videos'
        return self._json_by_get_request(url, params)

    def get_movie_translations(self, movie_id):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/translations'
        return self._json_by_get_request(url, params)

    def get_movie_recommendations(self, movie_id, language=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/recommendations'
        return self._json_by_get_request(url, params)

    def get_similar_movies(self, movie_id, language=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/similar'
        return self._json_by_get_request(url, params)

    def get_movie_reviews(self, movie_id, language=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/reviews'
        return self._json_by_get_request(url, params)

    def get_movie_lists(self, movie_id, language=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/{movie_id}/lists'
        return self._json_by_get_request(url, params)

    def get_latest_movies(self, language=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/latest'
        return self._json_by_get_request(url, params)

    def get_now_playing_movies(self, language=None, region=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/now_playing'
        return self._json_by_get_request(url, params)

    def get_popular_movies(self, language=None, region=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/popular'
        return self._json_by_get_request(url, params)

    def get_top_rated_movies(self, language=None, region=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/top_rated'
        return self._json_by_get_request(url, params)

    def get_upcoming_movies(self, language=None, region=None):
        params = {'language': 'ja-JP', 'region': 'JP'}
        url = f'{self.base_url_}movie/upcoming'
        return self._json_by_get_request(url, params)


def gety(movie_name):
   api = TMDB() 
   res = api.search_movies(movie_name)
   reslist = []
   for a in res["results"]:
     reslist.append({"title":str(a["title"]),"overview":str(a["overview"]),"imagepath":"https://image.tmdb.org/t/p/w500" + str(a["poster_path"])})
   return reslist


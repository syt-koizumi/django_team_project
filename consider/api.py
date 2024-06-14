import requests
import json

#Api取得用のクラス 
class TMDB:
    def __init__(self):
        #Apiキー　各自で変更して使用してもよいかも
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5YTY3MTcwMTA2NTk4ZjgyZjU3NWNkYmM1ZGQxZTM2YSIsInN1YiI6IjY2NjdkMWQ1NTM3YmVkMWE4N2E2YTk5ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.AamXVqqdHzy-HYdk7Hjsz0qU7Oc_UzjbRp_ayVLVmyI"
        self.headers_ = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json;charset=utf-8'}        
        self.base_url_ = 'https://api.themoviedb.org/3/'
        self.img_base_url_ = 'https://image.tmdb.org/t/p/w500'

    def _json_by_get_request(self, url, params={}):
        res = requests.get(url, headers=self.headers_, params=params)
        return json.loads(res.text)   

    def search_movies(self, query):
        params = {'query': query}
        url = f'{self.base_url_}search/movie'
        return self._json_by_get_request(url, params)    

def MylistApi(movie_name):
   api = TMDB()
   res = api.search_movies(movie_name)
   return str(res["results"][0]["overview"]),"https://image.tmdb.org/t/p/w500"+ str(res["results"][0]["poster_path"])
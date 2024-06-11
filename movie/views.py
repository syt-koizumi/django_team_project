

from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import FormView
from django.shortcuts import render
from .forms import MovieSearchForm
from django.shortcuts import redirect
from .Api import  TMDB
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
#検索結果の一覧を表示するTemplateView

class MovieSearchResultView(ListView):
    template_name = 'movie/movie_search_result.html'
    

   


#検索画面の作成を行う
class MovieSearchView(FormView):
    template_name = 'movie/movie_search.html'
    form_class = MovieSearchForm
    
    #ここでApiを呼び出す
    def form_valid(self, form):
        # フォームのデータを取得して、次のビューに渡す
        movie_name = form.cleaned_data['movie_name']
        data = GetMovieApi(movie_name)
        return render(self.request, 'movie/movie_search_result.html',{"movie_name":data})
    
def GetMovieApi(movie_name):
    api = TMDB() # tokenは発行された文字列を代入
    res = api.search_movies(movie_name)
    return str(res['results'])
    
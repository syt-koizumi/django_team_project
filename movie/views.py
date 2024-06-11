

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.shortcuts import render
from .forms import MovieSearchForm
from django.shortcuts import redirect
from .Api import  TMDB
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
#検索結果の一覧を表示するTemplateView
class MovieSearchResultView(TemplateView,ModelFormMixin):
    template_name = "movie/movie_search_result.html"
   



#検索画面の作成を行う
class MovieSearchView(FormView):
    template_name = 'movie/movie_search.html'
    form_class = MovieSearchForm
    
    #ここでApiを呼び出す
    def form_valid(self, form):
        # フォームのデータを取得して、次のビューに渡す
        movie_name = form.cleaned_data['movie_name']
        resultdata = GetMovieApi(movie_name)
        
        return redirect('movie:search_result', movie_name=movie_name, resultdata=resultdata)
        # 成功後のURLにデータを渡す
        self.success_url = reverse_lazy('movie:search_result', kwargs={'movie_name': movie_name, 'resultdata': resultdata})
        return super().form_valid(form)
    
    
def GetMovieApi(movie_name):
    api = TMDB() # tokenは発行された文字列を代入
    res = api.search_movies(movie_name)
    res['results']
    return "aaa"
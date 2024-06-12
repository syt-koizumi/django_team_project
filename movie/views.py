

from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView, FormView
from django.views.generic import FormView
from django.shortcuts import render
from .forms import MovieSearchForm
from django.shortcuts import redirect
from .Api import gety
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from .models import MyMovieModel

#映画の詳細を表示する
class MovieDetailView(TemplateView):
    template_name = 'movie/movie_detail.html'
    

#検索画面の作成を行う
class MovieSearchView(FormView):
    template_name = 'movie/movie_search.html'
    form_class = MovieSearchForm
    
    #ここでApiを呼び出す
    def form_valid(self, form):
        movie_name = form.cleaned_data['movie_name'] #変数movie_nameにuserの入力した値を代入
        objectlist = gety(movie_name) #これを使って、APIを呼び出す関数を実行
        return render(self.request,'movie/movie_search_result.html',{"objects":objectlist})
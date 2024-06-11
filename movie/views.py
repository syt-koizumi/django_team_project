

from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import FormView
from django.shortcuts import render
from .forms import MovieSearchForm
from django.shortcuts import redirect
from .Api import gety
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
        movie_name = form.cleaned_data['movie_name']
        objectlist = gety(movie_name)
        return render(self.request,'movie/movie_search_result.html',{"objects":objectlist})
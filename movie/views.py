from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView, FormView,View
from django.views.generic import FormView
from django.shortcuts import render
from .forms import MovieSearchForm,MyMovieForm
from django.shortcuts import redirect
from .Api import gety,MylistApi
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from .models import MyMovieModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404

#映画の詳細を表示する
class MovieDetailView(LoginRequiredMixin,TemplateView):
    template_name = 'movie/movie_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        overview1 , imagepath1 = MylistApi(context["movie_name"])
        context.update({"overview": overview1})
        context.update({"imagepath": imagepath1})
        results = MyMovieModel.objects.filter(name = context["movie_name"],createUser= self.request.user)
        if results.exists():
          context.update({"mylist":"t"})
        else:
          context.update({"mylist":"f"})
        return context


#検索画面用のビュー
class MovieSearchView(FormView):
    template_name = 'movie/movie_search.html'
    form_class = MovieSearchForm
    
    #ここでApiを呼び出す
    def form_valid(self, form):
        movie_name = form.cleaned_data['movie_name'] #変数movie_nameにuserの入力した値を代入
        objectlist = gety(movie_name) #これを使って、APIを呼び出す関数を実行
        return render(self.request,'movie/movie_search_result.html',{"objects":objectlist})


#mylistに追加ボタンを押したときの処理
def AddMyList(request, name):
    overview1 , imagepath1 = MylistApi(name)#ここでapiをたたいて取得
    MyMovieModel.objects.create(name=name, overview=overview1, imagepath = imagepath1).createUser.set([request.user])#新しいモデルを作成
    return redirect('mypage:mylist')#検索画面に遷移する


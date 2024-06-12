from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from movie.models import MyMovieModel
from django.views.generic import TemplateView,ListView,CreateView, FormView

    
class MylistView(LoginRequiredMixin,ListView):
    template_name = 'mypage/mylist.html'
    model = MyMovieModel
    def get_queryset(self):
        # 現在のログイン中のユーザーに関連する MyMovieModel オブジェクトを返します。
        return MyMovieModel.objects.filter(createUser=self.request.user)
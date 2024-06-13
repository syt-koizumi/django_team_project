from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView
from movie.models import MyMovieModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.http import Http404
    
    
class MylistView(LoginRequiredMixin, TemplateView):
    template_name = 'mypage/mylist.html'

    def get(self, request):

        MyMovieModel_data = MyMovieModel.objects.filter(createUser=self.request.user)
        context = {
            'MyMovieModel_data': MyMovieModel_data
        }
        return render(request, 'mypage/mylist.html', context)
    
    
class DeleteView(LoginRequiredMixin, DeleteView):
    model = MyMovieModel
    template_name = 'mypage/delete.html'
    success_url = reverse_lazy('mypage:mylist')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # ログインユーザーのオブジェクトのみを返す
        return queryset.filter(createUser=self.request.user, id=self.kwargs['pk'])

    def get_object(self, queryset=None):
        # 削除するオブジェクトを取得する
        obj = super().get_object(queryset)
        if obj is None:
            # オブジェクトが存在しない場合は404エラーを返す
            raise Http404("オブジェクトが見つかりません")
        return obj
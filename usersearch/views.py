from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from accounts.models import CustomUser
from .forms import UserSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


# ユーザー検索用のビュー
class UserSearchView(TemplateView):
    template_name = "usersearch/userlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserSearchForm()
        return context

from django.views.generic import ListView
from .forms import UserSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from accounts.models import CustomUser
# 検索結果表示用のビュー
class UserSearchResultView(ListView):
    model = CustomUser
    template_name = "usersearch/userlist_result.html"
    context_object_name = "objects"

    def get_queryset(self):
        query = self.request.GET.get('user_name', '')
        if query:
            object_list = CustomUser.objects.filter(Q(username__icontains=query))  # 'username'フィールドを検索
        else:
            object_list = CustomUser.objects.none()  # クエリがない場合は空のクエリセットを返す
        return object_list

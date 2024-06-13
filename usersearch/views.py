from django.shortcuts import render
from django.views.generic import TemplateView, FormView,ListView
from accounts.models import CustomUser
from .forms import UserSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin

#ユーザ検索用のビュー
class UserSearchView(TemplateView):
    model = CustomUser
    template_name = "usersearch/userlist.html"
    form_class = UserSearchForm


    #ここでユーザを呼び出す
   # def form_valid(self, request,**kwargs):
    #    context = super().form_valid(**kwargs)
     #   CustomUser_data = CustomUser.objects.filter(name = context["user_name"])
      #  context = {
       #     'CustomUser_data': CustomUser_data
       # }
       # return render(request, 'usersearch/userlist_result.html', context)

class UserSearchResultView(ListView):
    model = CustomUser
    template_name = "usersearch/userlist_result.html"
    context_object_name = "objects"

    

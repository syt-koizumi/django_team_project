from django.shortcuts import render
from django.views.generic import TemplateView
    

    
class MylistView(TemplateView):
    template_name = 'mypage/mylist.html'

from django.shortcuts import render
from django.views.generic import TemplateView

class TopPageView(TemplateView):
    template_name = "toppage/toppage.html"

# Create your views here.




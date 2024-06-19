from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView, FormView,View
from django.urls import reverse_lazy


class TopicTop(TemplateView):
     template_name = "topic/topic.html"
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView, FormView,View
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from . import consider
from .api import MylistApi
from movie.models import MyMovieModel
class ConsiderView(TemplateView):
    template_name = "consider/consider.html"
    
class ConsiderResultView(TemplateView):
    template_name = "consider/consider_result.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result_list = []
        
        for a in range(1,6,1):#consider.htmlの質問数によってこの数字は変更する
            result_list.append(self.request.GET.get("q"+ str(a)))
        movie_name = consider.getConsiderMovieName(result_list)
        overview1,imagepath1 = MylistApi(movie_name)
        context.update({"movie_name": movie_name})
        context.update({"overview": overview1})
        context.update({"imagepath": imagepath1})
        results = MyMovieModel.objects.filter(name = context["movie_name"],createUser= self.request.user)
        if results.exists():
          context.update({"mylist":"t"})
        else:
          context.update({"mylist":"f"})
        return context
    
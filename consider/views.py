from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView, FormView,View
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404

class ConsiderView(TemplateView):
    template_name = "consider/consider.html"
    
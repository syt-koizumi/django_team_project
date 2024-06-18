from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import send_user
from django.urls import reverse_lazy

class create_mail(ListView):
    model = send_user
    template_name = 'mail/create_mail.html'
    context_object_name = 'title'
    ordering = ['-dtcreated']  #日付で逆順に並べ替える

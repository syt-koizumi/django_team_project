from django.shortcuts import render
from django.views.generic import ListView
from .models import send_user

class create_mail(ListView):
    template_name = 'mail/create_mail.html'
    model = send_user

